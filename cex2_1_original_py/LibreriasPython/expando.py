# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: LibreriasPython\expando.pyc
# Compiled at: 2014-06-02 12:13:24
"""
This module contains the `ExpandoTextCtrl` which is a multi-line
text control that will expand its height on the fly to be able to show
all the lines of the content of the control.
"""
import wx, newevent
wxEVT_ETC_LAYOUT_NEEDED = wx.NewEventType()
EVT_ETC_LAYOUT_NEEDED = wx.PyEventBinder(wxEVT_ETC_LAYOUT_NEEDED, 1)

class ExpandoTextCtrl(wx.TextCtrl):
    """
    The ExpandoTextCtrl is a multi-line wx.TextCtrl that will
    adjust its height on the fly as needed to accomodate the number of
    lines needed to display the current content of the control.  It is
    assumed that the width of the control will be a fixed value and
    that only the height will be adjusted automatically.  If the
    control is used in a sizer then the width should be set as part of
    the initial or min size of the control.

    When the control resizes itself it will attempt to also make
    necessary adjustments in the sizer hierarchy it is a member of (if
    any) but if that is not suffiecient then the programmer can catch
    the EVT_ETC_LAYOUT_NEEDED event in the container and make any
    other layout adjustments that may be needed.
    """
    _defaultHeight = -1

    def __init__(self, parent, id=-1, value='', pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name='expando'):
        self.defaultHeight = self._getDefaultHeight(parent)
        w, h = size
        if h == -1:
            h = self.defaultHeight
        style = style | wx.TE_MULTILINE | wx.TE_NO_VSCROLL | wx.TE_RICH2
        wx.TextCtrl.__init__(self, parent, id, value, pos, (w, h), style, validator, name)
        self.extraHeight = self.defaultHeight - self.GetCharHeight()
        self.numLines = 1
        self.maxHeight = -1
        if value:
            wx.CallAfter(self._adjustCtrl)
        self.Bind(wx.EVT_TEXT, self.OnTextChanged)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def SetMaxHeight(self, h):
        """
        Sets the max height that the control will expand to on its
        own, and adjusts it down if needed.
        """
        self.maxHeight = h
        if h != -1 and self.GetSize().height > h:
            self.SetSize((-1, h))

    def GetMaxHeight(self):
        """Sets the max height that the control will expand to on its own"""
        return self.maxHeight

    def SetFont(self, font):
        wx.TextCtrl.SetFont(self, font)
        self.numLines = -1
        self._adjustCtrl()

    def WriteText(self, text):
        wx.TextCtrl.WriteText(self, text)
        self._adjustCtrl()

    def AppendText(self, text):
        self.SetValue(self.GetValue() + text)
        self.SetInsertionPointEnd()

    def OnTextChanged(self, evt):
        self._adjustCtrl()
        evt.Skip()

    def OnSize(self, evt):
        self._adjustCtrl()
        evt.Skip()

    def _adjustCtrl(self):
        numLines = self.GetNumberOfLines()
        if numLines != self.numLines:
            self.numLines = numLines
            charHeight = self.GetCharHeight()
            height = numLines * charHeight + self.extraHeight
            if not (self.maxHeight != -1 and height > self.maxHeight):
                if self.GetContainingSizer() is not None:
                    mw, mh = self.GetMinSize()
                    self.SetMinSize((mw, height))
                    if self.GetParent().GetSizer() is not None:
                        self.GetParent().Layout()
                    else:
                        self.GetContainingSizer().Layout()
                else:
                    self.SetSize((-1, height))
                evt = wx.PyCommandEvent(wxEVT_ETC_LAYOUT_NEEDED, self.GetId())
                evt.SetEventObject(self)
                evt.height = height
                evt.numLines = numLines
                self.GetEventHandler().ProcessEvent(evt)
        return

    def _getDefaultHeight(self, parent):
        if self.__class__._defaultHeight != -1:
            return self.__class__._defaultHeight
        tc = wx.TextCtrl(parent)
        sz = tc.GetSize()
        tc.Destroy()
        self.__class__._defaultHeight = sz.height
        return sz.height

    if 'wxGTK' in wx.PlatformInfo:

        def GetNumberOfLines(self):
            text = self.GetValue()
            width = self.GetSize().width
            dc = wx.ClientDC(self)
            dc.SetFont(self.GetFont())
            count = 0
            for line in text.split('\n'):
                count += 1
                w, h = dc.GetTextExtent(line)
                if w > width:
                    count += self._wrapLine(line, dc, width)

            if not count:
                count = 1
            return count

        def _wrapLine(self, line, dc, width):
            pte = dc.GetPartialTextExtents(line)
            width -= wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X)
            idx = 0
            start = 0
            count = 0
            spc = -1
            while idx < len(pte):
                if line[idx] == ' ':
                    spc = idx
                if pte[idx] - start > width:
                    count += 1
                    if spc != -1:
                        idx = spc + 1
                        spc = -1
                    start = pte[idx]
                else:
                    idx += 1

            return count