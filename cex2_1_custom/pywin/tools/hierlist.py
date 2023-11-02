# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\tools\hierlist.pyc
# Compiled at: 2012-04-30 19:46:46
import sys, win32ui, win32con, win32api
from win32api import RGB
from pywin.mfc import object, window, docview, dialog
import commctrl

def GetItemText(item):
    if type(item) == type(()) or type(item) == type([]):
        use = item[0]
    else:
        use = item
    if type(use) == type(''):
        return use
    else:
        return repr(item)


class HierDialog(dialog.Dialog):

    def __init__(self, title, hierList, bitmapID=win32ui.IDB_HIERFOLDERS, dlgID=win32ui.IDD_TREE, dll=None, childListBoxID=win32ui.IDC_LIST1):
        dialog.Dialog.__init__(self, dlgID, dll)
        self.hierList = hierList
        self.dlgID = dlgID
        self.title = title

    def OnInitDialog(self):
        self.SetWindowText(self.title)
        self.hierList.HierInit(self)
        return dialog.Dialog.OnInitDialog(self)


class HierList(object.Object):

    def __init__(self, root, bitmapID=win32ui.IDB_HIERFOLDERS, listBoxId=None, bitmapMask=None):
        self.listControl = None
        self.bitmapID = bitmapID
        self.root = root
        self.listBoxId = listBoxId
        self.itemHandleMap = {}
        self.filledItemHandlesMap = {}
        self.bitmapMask = bitmapMask
        return

    def __getattr__(self, attr):
        try:
            return getattr(self.listControl, attr)
        except AttributeError:
            return object.Object.__getattr__(self, attr)

    def ItemFromHandle(self, handle):
        return self.itemHandleMap[handle]

    def SetStyle(self, newStyle):
        hwnd = self.listControl.GetSafeHwnd()
        style = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)
        win32api.SetWindowLong(hwnd, win32con.GWL_STYLE, style | newStyle)

    def HierInit(self, parent, listControl=None):
        if self.bitmapMask is None:
            bitmapMask = RGB(0, 0, 255)
        else:
            bitmapMask = self.bitmapMask
        self.imageList = win32ui.CreateImageList(self.bitmapID, 16, 0, bitmapMask)
        if listControl is None:
            if self.listBoxId is None:
                self.listBoxId = win32ui.IDC_LIST1
            self.listControl = parent.GetDlgItem(self.listBoxId)
        else:
            self.listControl = listControl
            lbid = listControl.GetDlgCtrlID()
            assert self.listBoxId is None or self.listBoxId == lbid, 'An invalid listbox control ID has been specified (specified as %s, but exists as %s)' % (self.listBoxId, lbid)
            self.listBoxId = lbid
        self.listControl.SetImageList(self.imageList, commctrl.LVSIL_NORMAL)
        if sys.version_info[0] < 3:
            parent.HookNotify(self.OnTreeItemExpanding, commctrl.TVN_ITEMEXPANDINGA)
            parent.HookNotify(self.OnTreeItemSelChanged, commctrl.TVN_SELCHANGEDA)
        else:
            parent.HookNotify(self.OnTreeItemExpanding, commctrl.TVN_ITEMEXPANDINGW)
            parent.HookNotify(self.OnTreeItemSelChanged, commctrl.TVN_SELCHANGEDW)
        parent.HookNotify(self.OnTreeItemDoubleClick, commctrl.NM_DBLCLK)
        self.notify_parent = parent
        if self.root:
            self.AcceptRoot(self.root)
        return

    def DeleteAllItems(self):
        self.listControl.DeleteAllItems()
        self.root = None
        self.itemHandleMap = {}
        self.filledItemHandlesMap = {}
        return

    def HierTerm(self):
        parent = self.notify_parent
        if sys.version_info[0] < 3:
            parent.HookNotify(None, commctrl.TVN_ITEMEXPANDINGA)
            parent.HookNotify(None, commctrl.TVN_SELCHANGEDA)
        else:
            parent.HookNotify(None, commctrl.TVN_ITEMEXPANDINGW)
            parent.HookNotify(None, commctrl.TVN_SELCHANGEDW)
        parent.HookNotify(None, commctrl.NM_DBLCLK)
        self.DeleteAllItems()
        self.listControl = None
        self.notify_parent = None
        return

    def OnTreeItemDoubleClick(self, info, extra):
        hwndFrom, idFrom, code = info
        if idFrom != self.listBoxId:
            return None
        else:
            item = self.itemHandleMap[self.listControl.GetSelectedItem()]
            self.TakeDefaultAction(item)
            return 1

    def OnTreeItemExpanding(self, info, extra):
        hwndFrom, idFrom, code = info
        if idFrom != self.listBoxId:
            return
        else:
            action, itemOld, itemNew, pt = extra
            itemHandle = itemNew[0]
            if itemHandle not in self.filledItemHandlesMap:
                item = self.itemHandleMap[itemHandle]
                self.AddSubList(itemHandle, self.GetSubList(item))
                self.filledItemHandlesMap[itemHandle] = None
            return 0

    def OnTreeItemSelChanged(self, info, extra):
        hwndFrom, idFrom, code = info
        if idFrom != self.listBoxId:
            return None
        else:
            action, itemOld, itemNew, pt = extra
            itemHandle = itemNew[0]
            item = self.itemHandleMap[itemHandle]
            self.PerformItemSelected(item)
            return 1

    def AddSubList(self, parentHandle, subItems):
        for item in subItems:
            self.AddItem(parentHandle, item)

    def AddItem(self, parentHandle, item, hInsertAfter=commctrl.TVI_LAST):
        text = self.GetText(item)
        if self.IsExpandable(item):
            cItems = 1
        else:
            cItems = 0
        bitmapCol = self.GetBitmapColumn(item)
        bitmapSel = self.GetSelectedBitmapColumn(item)
        if bitmapSel is None:
            bitmapSel = bitmapCol
        hitem = self.listControl.InsertItem(parentHandle, hInsertAfter, (None, None, None, text, bitmapCol, bitmapSel, cItems, 0))
        self.itemHandleMap[hitem] = item
        return hitem

    def _GetChildHandles(self, handle):
        ret = []
        try:
            handle = self.listControl.GetChildItem(handle)
            while 1:
                ret.append(handle)
                handle = self.listControl.GetNextItem(handle, commctrl.TVGN_NEXT)

        except win32ui.error:
            pass

        return ret

    def ItemFromHandle(self, handle):
        return self.itemHandleMap[handle]

    def Refresh(self, hparent=None):
        if hparent is None:
            hparent = commctrl.TVI_ROOT
        if hparent not in self.filledItemHandlesMap:
            return
        else:
            root_item = self.itemHandleMap[hparent]
            old_handles = self._GetChildHandles(hparent)
            old_items = list(map(self.ItemFromHandle, old_handles))
            new_items = self.GetSubList(root_item)
            inew = 0
            hAfter = commctrl.TVI_FIRST
            for iold in range(len(old_items)):
                inewlook = inew
                matched = 0
                while inewlook < len(new_items):
                    if old_items[iold] == new_items[inewlook]:
                        matched = 1
                        break
                    inewlook = inewlook + 1

                if matched:
                    for i in range(inew, inewlook):
                        hAfter = self.AddItem(hparent, new_items[i], hAfter)

                    inew = inewlook + 1
                    hold = old_handles[iold]
                    if hold in self.filledItemHandlesMap:
                        self.Refresh(hold)
                else:
                    hdelete = old_handles[iold]
                    for hchild in self._GetChildHandles(hdelete):
                        del self.itemHandleMap[hchild]
                        if hchild in self.filledItemHandlesMap:
                            del self.filledItemHandlesMap[hchild]

                    self.listControl.DeleteItem(hdelete)
                hAfter = old_handles[iold]

            for newItem in new_items[inew:]:
                self.AddItem(hparent, newItem)

            return

    def AcceptRoot(self, root):
        self.listControl.DeleteAllItems()
        self.itemHandleMap = {commctrl.TVI_ROOT: root}
        self.filledItemHandlesMap = {commctrl.TVI_ROOT: root}
        subItems = self.GetSubList(root)
        self.AddSubList(0, subItems)

    def GetBitmapColumn(self, item):
        if self.IsExpandable(item):
            return 0
        else:
            return 4

    def GetSelectedBitmapColumn(self, item):
        return

    def GetSelectedBitmapColumn(self, item):
        return 0

    def CheckChangedChildren(self):
        return self.listControl.CheckChangedChildren()

    def GetText(self, item):
        return GetItemText(item)

    def PerformItemSelected(self, item):
        try:
            win32ui.SetStatusText('Selected ' + self.GetText(item))
        except win32ui.error:
            pass

    def TakeDefaultAction(self, item):
        win32ui.MessageBox('Got item ' + self.GetText(item))


class HierListWithItems(HierList):

    def __init__(self, root, bitmapID=win32ui.IDB_HIERFOLDERS, listBoxID=None, bitmapMask=None):
        HierList.__init__(self, root, bitmapID, listBoxID, bitmapMask)

    def DelegateCall(self, fn):
        return fn()

    def GetBitmapColumn(self, item):
        rc = self.DelegateCall(item.GetBitmapColumn)
        if rc is None:
            rc = HierList.GetBitmapColumn(self, item)
        return rc

    def GetSelectedBitmapColumn(self, item):
        return self.DelegateCall(item.GetSelectedBitmapColumn)

    def IsExpandable(self, item):
        return self.DelegateCall(item.IsExpandable)

    def GetText(self, item):
        return self.DelegateCall(item.GetText)

    def GetSubList(self, item):
        return self.DelegateCall(item.GetSubList)

    def PerformItemSelected(self, item):
        func = getattr(item, 'PerformItemSelected', None)
        if func is None:
            return HierList.PerformItemSelected(self, item)
        else:
            return self.DelegateCall(func)
            return

    def TakeDefaultAction(self, item):
        func = getattr(item, 'TakeDefaultAction', None)
        if func is None:
            return HierList.TakeDefaultAction(self, item)
        else:
            return self.DelegateCall(func)
            return


class HierListItem:

    def __init__(self):
        pass

    def GetText(self):
        pass

    def GetSubList(self):
        pass

    def IsExpandable(self):
        pass

    def GetBitmapColumn(self):
        return

    def GetSelectedBitmapColumn(self):
        return

    def __lt__(self, other):
        return id(self) < id(other)

    def __eq__(self, other):
        return False