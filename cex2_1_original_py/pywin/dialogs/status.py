# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\dialogs\status.pyc
# Compiled at: 2011-03-19 11:51:18
from pywin.mfc import dialog
from pywin.mfc.thread import WinThread
import threading, win32ui, win32con, win32api, time

def MakeProgressDlgTemplate(caption, staticText=''):
    style = win32con.DS_MODALFRAME | win32con.WS_POPUP | win32con.WS_VISIBLE | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.DS_SETFONT
    cs = win32con.WS_CHILD | win32con.WS_VISIBLE
    w = 215
    h = 36
    h = 40
    dlg = [
     [
      caption,
      (
       0, 0, w, h),
      style,
      None,
      (8, 'MS Sans Serif')]]
    s = win32con.WS_TABSTOP | cs
    dlg.append([130, staticText, 1000, (7, 7, w - 7, h - 32), cs | win32con.SS_LEFT])
    return dlg


class CStatusProgressDialog(dialog.Dialog):

    def __init__(self, title, msg='', maxticks=100, tickincr=1):
        self.initMsg = msg
        templ = MakeProgressDlgTemplate(title, msg)
        dialog.Dialog.__init__(self, templ)
        self.maxticks = maxticks
        self.tickincr = tickincr
        self.pbar = None
        return

    def OnInitDialog(self):
        rc = dialog.Dialog.OnInitDialog(self)
        self.static = self.GetDlgItem(1000)
        self.pbar = win32ui.CreateProgressCtrl()
        self.pbar.CreateWindow(win32con.WS_CHILD | win32con.WS_VISIBLE, (10, 30, 310,
                                                                         44), self, 1001)
        self.pbar.SetRange(0, self.maxticks)
        self.pbar.SetStep(self.tickincr)
        self.progress = 0
        self.pincr = 5
        return rc

    def Close(self):
        self.EndDialog(0)

    def SetMaxTicks(self, maxticks):
        if self.pbar is not None:
            self.pbar.SetRange(0, maxticks)
        return

    def Tick(self):
        if self.pbar is not None:
            self.pbar.StepIt()
        return

    def SetTitle(self, text):
        self.SetWindowText(text)

    def SetText(self, text):
        self.SetDlgItemText(1000, text)

    def Set(self, pos, max=None):
        if self.pbar is not None:
            self.pbar.SetPos(pos)
            if max is not None:
                self.pbar.SetRange(0, max)
        return


MYWM_SETTITLE = win32con.WM_USER + 10
MYWM_SETMSG = win32con.WM_USER + 11
MYWM_TICK = win32con.WM_USER + 12
MYWM_SETMAXTICKS = win32con.WM_USER + 13
MYWM_SET = win32con.WM_USER + 14

class CThreadedStatusProcessDialog(CStatusProgressDialog):

    def __init__(self, title, msg='', maxticks=100, tickincr=1):
        self.title = title
        self.msg = msg
        self.threadid = win32api.GetCurrentThreadId()
        CStatusProgressDialog.__init__(self, title, msg, maxticks, tickincr)

    def OnInitDialog(self):
        rc = CStatusProgressDialog.OnInitDialog(self)
        self.HookMessage(self.OnTitle, MYWM_SETTITLE)
        self.HookMessage(self.OnMsg, MYWM_SETMSG)
        self.HookMessage(self.OnTick, MYWM_TICK)
        self.HookMessage(self.OnMaxTicks, MYWM_SETMAXTICKS)
        self.HookMessage(self.OnSet, MYWM_SET)
        return rc

    def _Send(self, msg):
        try:
            self.PostMessage(msg)
        except win32ui.error:
            pass

    def OnTitle(self, msg):
        CStatusProgressDialog.SetTitle(self, self.title)

    def OnMsg(self, msg):
        CStatusProgressDialog.SetText(self, self.msg)

    def OnTick(self, msg):
        CStatusProgressDialog.Tick(self)

    def OnMaxTicks(self, msg):
        CStatusProgressDialog.SetMaxTicks(self, self.maxticks)

    def OnSet(self, msg):
        CStatusProgressDialog.Set(self, self.pos, self.max)

    def Close(self):
        assert self.threadid, 'No thread!'
        win32api.PostThreadMessage(self.threadid, win32con.WM_QUIT, 0, 0)

    def SetMaxTicks(self, maxticks):
        self.maxticks = maxticks
        self._Send(MYWM_SETMAXTICKS)

    def SetTitle(self, title):
        self.title = title
        self._Send(MYWM_SETTITLE)

    def SetText(self, text):
        self.msg = text
        self._Send(MYWM_SETMSG)

    def Tick(self):
        self._Send(MYWM_TICK)

    def Set(self, pos, max=None):
        self.pos = pos
        self.max = max
        self._Send(MYWM_SET)


class ProgressThread(WinThread):

    def __init__(self, title, msg='', maxticks=100, tickincr=1):
        self.title = title
        self.msg = msg
        self.maxticks = maxticks
        self.tickincr = tickincr
        self.dialog = None
        WinThread.__init__(self)
        self.createdEvent = threading.Event()
        return

    def InitInstance(self):
        self.dialog = CThreadedStatusProcessDialog(self.title, self.msg, self.maxticks, self.tickincr)
        self.dialog.CreateWindow()
        try:
            self.dialog.SetForegroundWindow()
        except win32ui.error:
            pass

        self.createdEvent.set()
        return WinThread.InitInstance(self)

    def ExitInstance(self):
        return 0


def StatusProgressDialog(title, msg='', maxticks=100, parent=None):
    d = CStatusProgressDialog(title, msg, maxticks)
    d.CreateWindow(parent)
    return d


def ThreadedStatusProgressDialog(title, msg='', maxticks=100):
    t = ProgressThread(title, msg, maxticks)
    t.CreateThread()
    end_time = time.time() + 10
    while time.time() < end_time:
        if t.createdEvent.isSet():
            break
        win32ui.PumpWaitingMessages()
        time.sleep(0.1)

    return t.dialog


def demo():
    d = StatusProgressDialog('A Demo', 'Doing something...')
    import win32api
    for i in range(100):
        if i == 50:
            d.SetText('Getting there...')
        if i == 90:
            d.SetText('Nearly done...')
        win32api.Sleep(20)
        d.Tick()

    d.Close()


def thread_demo():
    d = ThreadedStatusProgressDialog('A threaded demo', 'Doing something')
    import win32api
    for i in range(100):
        if i == 50:
            d.SetText('Getting there...')
        if i == 90:
            d.SetText('Nearly done...')
        win32api.Sleep(20)
        d.Tick()

    d.Close()


if __name__ == '__main__':
    thread_demo()