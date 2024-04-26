"""
document
===============================================================================
"""
from __future__ import annotations

import logging
import os
import subprocess
import sys
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Optional

import glyphsLib
import wbDefcon
import wx
from fontTools.misc import plistlib
from fontTools.ufoLib import UFOFileStructure, UFOFormatVersion, UFOReader
from fontTools.ufoLib.errors import UFOLibError
from wbBase.document import Document, FileNameFromPath, dbg
from wbDefcon import Font
from wbDefcon.tools.conversion import robofont_guides_to_UFO3, robofont_mark_to_UFO3
from wbFontParts import RFont

# from .dialog.newFontDialog import NewFontDialog
from .dialog.revertFontDialog import RevertFontDialog
from .view.font import UfoFontView
from .view.glyph import UfoGlyphView

if TYPE_CHECKING:
    from wbDefcon import Glyph
    from defcon.tools.notifications import Notification
    from .template import UfoTemplate

log = logging.getLogger(__name__)

if hasattr(subprocess, "STARTUPINFO"):
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
else:
    info = None


# class UFOsaveProgressBar(wx.ProgressDialog):
#     def __init__(self, font:Font, formatVersion=None, structure=None, path=None):
#         tickCount = font.getSaveProgressBarTickCount(formatVersion, structure, path)
#         # print("tickCount", tickCount)
#         wx.ProgressDialog.__init__(
#             self,
#             title="Save UFO",
#             message="",
#             maximum=tickCount,
#             parent=wx.GetApp().TopWindow,
#             style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE,
#         )

#     def __enter__(self):
#         return self

#     def __exit__(self, type, value, trace_back):
#         self.Destroy()

#     def update(self, text="", increment=1):
#         # print(self.Value + increment, text)
#         newVal = min(self.Value + increment, self.Range)
#         self.Update(newVal, text)


class UFOsaveProgress:
    def __init__(self, font:Font, formatVersion=None, structure=None, path=None):
        self.tickCount = font.getSaveProgressBarTickCount(
            formatVersion, structure, path
        )
        self.dlg = None

    def __enter__(self):
        self.dlg = wx.ProgressDialog(
            title="Save UFO",
            message="",
            maximum=self.tickCount,
            parent=wx.GetApp().TopWindow,
            style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE,
        )
        return self.dlg

    def __exit__(self, type, value, trace_back):
        self.dlg.Destroy()
        return True


class UfoDocument(Document):
    """
    Document implementation for Unified Font Objects
    """

    binaryData = False
    canReload = True

    def __init__(self, template:UfoTemplate):
        super().__init__(template)
        self._rFont = None

    @property
    def font(self) -> Optional[Font]:
        """
        The Font object associated with this document.
        """
        return self._data

    @font.setter
    def font(self, font: Font):
        assert isinstance(font, Font)
        assert self._data is None, "Can not replace font in UfoDoc"
        self._data = font
        self._data.document = self
        # self._rFont = RFont(self._data)

    @font.deleter
    def font(self):
        font = self._data
        if font is None:
            return
        assert isinstance(font, Font)
        del font._doc
        font.endSelfNotificationObservation()
        font.destroyAllRepresentations()
        glyph:Glyph
        for glyph in font:
            glyph.endSelfNotificationObservation()
            glyph.destroyAllRepresentations()
        glyphNames = list(font.keys())
        for name in glyphNames:
            del font[name]
        self._rFont = None
        self._data = None

    @property
    def RFont(self) -> RFont:
        if self._rFont is None and self._data is not None:
            self._rFont = RFont(self._data)
        assert isinstance(self._rFont, RFont)
        return self._rFont

    @property
    def title(self) -> str:
        if self.font is not None:
            if self.font.path:
                name = os.path.basename(self.font.path)
            else:
                name = " ".join(
                    [
                        n
                        for n in (self.font.info.familyName, self.font.info.styleName)
                        if n
                    ]
                )
            return f"Font - {name}"
        else:
            return "No Font"

    @title.setter
    def title(self, title):
        pass
        # raise NotImplementedError

    @property
    def printableName(self) -> str:
        return self.title

    @property
    def modified(self) -> bool:
        """
        True if the document has been saved.
        """
        if self.font is not None:
            return self.font.dirty
        return False

    @modified.setter
    def modified(self, modified):
        _modified = bool(modified)
        if self.font and _modified != self.font.dirty:
            self.font.dirty = _modified
            self.UpdateAllViews(self, ("modify", self, self._modified))

    @property
    def fontView(self) -> Optional[UfoFontView]:
        for view in self.views:
            if isinstance(view, UfoFontView):
                return view
        return None

    # -----------------------------------------------------------------------------
    # internal methods
    # -----------------------------------------------------------------------------

    def beginObservation(self):
        font = self.font
        if font is not None:
            if not font.hasObserver(self, "Font.Changed"):
                font.addObserver(self, "handleNotification", "Font.Changed")
            if not font.info.hasObserver(self, "Info.Changed"):
                font.info.addObserver(self, "handleNotification", "Info.Changed")
            if not font.info.hasObserver(self, "Info.ValueChanged"):
                font.info.addObserver(self, "handleNotification", "Info.ValueChanged")

    def OnNewDocument(self, familyName=None, styleName=None):
        dbg("UfoDocument.OnNewDocument()", indent=1)
        font = Font()
        font.info.unitsPerEm = 1000
        if isinstance(familyName, str):
            font.info.familyName = familyName
        else:
            font.info.familyName = "Untitled"
        if isinstance(styleName, str):
            font.info.styleName = styleName
        font.dirty = False
        self.font = font
        # self.modified = False
        super().OnNewDocument()
        self.beginObservation()
        self.UpdateAllViews(self, ("font loaded", True))
        dbg("UfoDocument.OnNewDocument() - done", indent=0)

    def OnOpenDocument(self, filename: str) -> bool:
        dbg(f'UfoDocument.OnOpenDocument(filename="{filename}")', indent=1)
        result = False
        if self.OnSaveModified():
            if self.typeName == "UFO document":
                from .template import GlyphsTemplate, UfoTemplate, VFBTemplate

                if isinstance(self.template, UfoTemplate):
                    result = self.openUFO(filename)
                elif isinstance(self.template, VFBTemplate):
                    result = self.openVFB(filename)
                elif isinstance(self.template, GlyphsTemplate):
                    result = self.openGlyphs(filename)
                else:
                    wx.LogError("Unknown Template type")
                if result:
                    self.set_modificationDate()
                    self.modified = False
                    self.beginObservation()
                    self.UpdateAllViews(self, ("font loaded", True))
        dbg(f"UfoDocument.OnOpenDocument() -> {result}", indent=0)
        return result

    def openUFO(self, filename: str) -> bool:
        dbg(f'UfoDocument.openUFO(filename="{filename}")', indent=1)
        result = False
        ufoPath = self.getUFOpath(filename)
        if ufoPath:
            try:
                self.font = Font(ufoPath)
                self.font.lib.dirty = False  # why is lib dirty here?
                self.path = ufoPath
                self.saved = True
                result = True
            except UFOLibError:
                result = False
        dbg(f"UfoDocument.openUFO() -> {result}")
        dbg(indent=0)
        return result

    def openVFB(self, filename: str) -> bool:
        dbg(f'UfoDocument.openVFB(filename="{filename}")')
        if os.path.isfile(filename):
            steps = 7
            progress = wx.ProgressDialog(
                title="Import VFB",
                message="",
                maximum=steps,
                parent=self.manager.documentNotebook,
                style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE,
            )
            with TemporaryDirectory() as tempDir:
                progress.Update(0, "Reading VFB file")
                tempUFOpath = os.path.join(tempDir, "temp.ufo")
                log.debug(tempUFOpath)
                arguments = [
                    "vfb2ufo",
                    "-pp",
                    "-s",
                    "-fo",
                    filename,
                    tempUFOpath,
                ]
                process = subprocess.Popen(
                    arguments,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    startupinfo=info,
                )
                outdata, errordata = process.communicate()
                log.debug("vfb2ufo returncode: %s", process.returncode)
                process.terminate()
                if errordata:
                    log.error(errordata.decode())
                    raise Exception("Conversion vfb2ufo failed")
                if outdata:
                    log.info(outdata.decode().strip())
                if not os.path.isdir(tempUFOpath):
                    raise Exception("Temp UFO folder not found")
                progress.Update(2, "Reading converted data")
                # fix groups.plist
                groupsPath = os.path.join(tempUFOpath, "groups.plist")
                if os.path.isfile(groupsPath):
                    with open(groupsPath, "rb") as groupsFile:
                        groups = plistlib.load(groupsFile)
                    for groupName in list(groups.keys()):
                        if groupName.startswith("public.kern"):
                            del groups[groupName]
                    with open(groupsPath, "wb") as groupsFile:
                        plistlib.dump(groups, groupsFile)
                wbDefconFont = Font(tempUFOpath)
                progress.Update(3, "Processing converted data")
                fontPartFont = RFont(wbDefconFont)
                progress.Update(4, "Loading font")
                font:RFont = fontPartFont.copy()
                progress.Update(5, "Closing input file")
                fontPartFont.close()
                fontPartFont = None
                wbDefconFont = None
            progress.Update(6, "Post processing")
            self.font = font.naked()
            robofont_guides_to_UFO3(self.font)
            robofont_mark_to_UFO3(self.font)
            self.font._ufoFormatVersion = UFOFormatVersion.FORMAT_3_0
            self.font._ufoFileStructure = UFOFileStructure.ZIP
            self._rFont = font
            from .template import UfoTemplate

            self._template = self.manager.FindTemplateByType(UfoTemplate)
            progress.Update(7, "Done")
            progress.Destroy()
            self.saved = False
            self._path = ""
            dbg("UfoDocument.openVFB() done")
            return True
        dbg("UfoDocument.openVFB() failed file not found")
        return False

    def openGlyphs(self, filename: str) -> bool:
        dbg(f'UfoDocument.openGlyphs(filename="{filename}")', indent=1)
        result = False
        ufos = glyphsLib.load_to_ufos(filename, ufo_module=wbDefcon)
        if len(ufos) == 1:
            self.font = ufos[0]
            self.font._ufoFormatVersion = UFOFormatVersion.FORMAT_3_0
            self.font._ufoFileStructure = UFOFileStructure.ZIP
            from .template import UfoTemplate

            self._template = self.manager.FindTemplateByType(UfoTemplate)
            self.path = ""
            self.saved = False
            dbg("UfoDocument.openGlyphs() done")
            return True
        dbg(f"UfoDocument.openGlyphs() -> {result}")
        dbg(indent=0)
        return result

    def getUFOpath(self, filename: str) -> str:
        if filename:
            head, tail = os.path.split(filename)
            __, ext = os.path.splitext(tail)
            if ext.upper() in (".UFO", ".UFOZ"):
                return filename
            elif ext.upper() == ".PLIST" and tail in self.validFileNames:
                __, ext = os.path.splitext(head)
                if ext.upper() == ".UFO":
                    return head
        return ""

    def revert(self) -> None:
        if self.path and os.path.exists(self.path):
            font = self.font
            if not self.modificationDateCorrect:
                reader = UFOReader(self.path, validate=font.ufoLibReadValidate)
                layerNames = reader.getLayerNames()
                font._reader = reader
                for layerName in layerNames:
                    if layerName in font.layers:
                        font.layers[layerName]._glyphSet = reader.getGlyphSet(
                            layerName,
                            validateRead=font.layers.ufoLibReadValidate,
                            validateWrite=font.layers.ufoLibWriteValidate,
                        )
            dlg = RevertFontDialog(self.frame, font)
            if dlg.ShowModal() == wx.ID_OK:
                if dlg.checkBox_font_lib.Value:
                    font.reloadLib()
                    font.lib.dirty = False
                if dlg.checkBox_font_info.Value:
                    font.reloadInfo()
                    font.info.dirty = False
                if dlg.checkBox_groups.Value:
                    font.reloadGroups()
                    font.groups.dirty = False
                if dlg.checkBox_kerning.Value:
                    font.reloadKerning()
                    font.kerning.dirty = False
                if dlg.checkBox_features.Value:
                    font.reloadFeatures()
                    font.features.dirty = False
                if dlg.checkBox_images.Value:
                    font.reloadImages(font.images.fileNames)
                if dlg.checkBox_data.Value:
                    font.reloadData(font.data.fileNames)
                log.debug("layerdata: %r", dlg.layerdata)
                font.reloadLayers(dlg.layerdata)
                self.set_modificationDate()
                self.UpdateAllViews(self, ["font loaded"])
                self.saved = True
            dlg.Destroy()

    def OnSaveDocument(self, filename: str) -> bool:
        """
        Takes filename (which must not be empty),
        and calls SaveObject. If SaveObject returns true, the
        document is set to unmodified; otherwise, an error message box is
        displayed.
        """
        dbg(f"UfoDocument.OnSaveDocument(filename={filename})", indent=1)
        if not filename:
            dbg("UfoDocument.OnSaveDocument() no filename return False", indent=0)
            return False
        saved = False
        try:
            saved = self.SaveObject(filename)
        except:
            # for debugging purposes
            import traceback

            traceback.print_exc()
            wx.MessageBox(
                "Could not save '%s'.  %s"
                % (FileNameFromPath(filename), sys.exc_info()[1]),
                "File Error",
                wx.OK | wx.ICON_EXCLAMATION,
                self.frame,
            )
            dbg("UfoDocument.OnSaveDocument() save failed return False", indent=0)
            return False
        if saved:
            self.path = filename
            self.set_modificationDate()
            self.modified = False
            self.saved = True
            dbg("UfoDocument.OnSaveDocument() -> done return True", indent=0)
            wx.LogStatus(f"UfoDocument saved: {self.printableName}")
            return True
        dbg("UfoDocument.OnSaveDocument() -> not saved return False", indent=0)
        return False

    def SaveObject(self, filename: str) -> bool:
        dbg(f"UfoDocument.SaveObject({filename})", indent=1)
        self.font.holdNotifications()
        # with UFOsaveProgressBar(self.font, path=filename) as progress:
        #     self.font.save(filename, progressBar=progress)
        self.font.save(filename)
        self.font.releaseHeldNotifications()
        dbg("UfoDocument.SaveObject() -> done", indent=0)
        return True

    def handleNotification(self, notification:Notification):
        log.debug("UfoDocument.handleNotification %r", notification.name)
        view = self.fontView
        if view:
            if notification.name == "Info.ValueChanged":
                if notification.data["attribute"] in ("familyName", "styleName"):
                    view.frame.title = self.title
                if self.font.info.dirty:
                    self.font.dirty = True
            if notification.name == "Font.Changed":
                view.OnUpdate(self, ("modify", notification.data))

    def showGlyph(
        self, glyphname: str, newPage: bool = False, view: Optional[UfoGlyphView] = None
    ) -> bool:
        dbg(
            f"UfoDocument.showGlyph(glyphname={glyphname}, newPage={newPage}, view={view})"
        )
        font = self.font
        if font and glyphname in font:
            glyph = font[glyphname]
            newView = False
            if not newPage and view is None:
                for v in self.views:
                    if isinstance(v, UfoGlyphView):
                        view = v
                        break
            if not view:
                view = UfoGlyphView()
                if view.OnCreate(self, None):
                    self.AddView(view)
                    newView = True
                else:
                    wx.LogError("Can not create view for %r" % glyph)
                    view.Destroy()
                    return False
            view.glyph = glyph
            view.Activate()
            view.frame.CurrentPage.Refresh()
            if newView:
                canvas = view.frame.canvas
                canvas.zoom = canvas.ClientSize.height / (font.info.unitsPerEm * 1.2)
                bounds = glyph.bounds
                if bounds:
                    x0, y0, x1, y1 = bounds
                    x = (x0 + x1) / 2
                    y = (y0 + y1) / 2
                else:
                    x = y = 500
                wx.LogDebug("UfoDoc.showGlyph.centerCanvasOnScreen(%r, %r)" % (x, y))
                canvas.centerCanvasOnScreen(x, y)
            return True
        wx.LogError("Can not find glyph %r in font %r" % (glyphname, font))
        return False

    def DeleteContents(self) -> None:
        font = self.font
        if font is not None:
            if font.hasObserver(self, "Font.Changed"):
                font.removeObserver(self, "Font.Changed")
            if font.info.hasObserver(self, "Info.Changed"):
                font.info.removeObserver(self, "Info.Changed")
            font.close()
        super().DeleteContents()
