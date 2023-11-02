# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: pywin\mfc\docview.pyc
# Compiled at: 2011-11-05 15:37:34
import win32ui, win32con, object, window

class View(window.Wnd):

    def __init__(self, initobj):
        window.Wnd.__init__(self, initobj)

    def OnInitialUpdate(self):
        pass


class CtrlView(View):

    def __init__(self, doc, wndclass, style=0):
        View.__init__(self, win32ui.CreateCtrlView(doc, wndclass, style))


class EditView(CtrlView):

    def __init__(self, doc):
        View.__init__(self, win32ui.CreateEditView(doc))


class RichEditView(CtrlView):

    def __init__(self, doc):
        View.__init__(self, win32ui.CreateRichEditView(doc))


class ListView(CtrlView):

    def __init__(self, doc):
        View.__init__(self, win32ui.CreateListView(doc))


class TreeView(CtrlView):

    def __init__(self, doc):
        View.__init__(self, win32ui.CreateTreeView(doc))


class ScrollView(View):

    def __init__(self, doc):
        View.__init__(self, win32ui.CreateView(doc))


class FormView(View):

    def __init__(self, doc, id):
        View.__init__(self, win32ui.CreateFormView(doc, id))


class Document(object.CmdTarget):

    def __init__(self, template, docobj=None):
        if docobj is None:
            docobj = template.DoCreateDoc()
        object.CmdTarget.__init__(self, docobj)
        return


class RichEditDoc(object.CmdTarget):

    def __init__(self, template):
        object.CmdTarget.__init__(self, template.DoCreateRichEditDoc())


class CreateContext:
    """A transient base class used as a CreateContext"""

    def __init__(self, template, doc=None):
        self.template = template
        self.doc = doc

    def __del__(self):
        self.close()

    def close(self):
        self.doc = None
        self.template = None
        return


class DocTemplate(object.CmdTarget):

    def __init__(self, resourceId=None, MakeDocument=None, MakeFrame=None, MakeView=None):
        if resourceId is None:
            resourceId = win32ui.IDR_PYTHONTYPE
        object.CmdTarget.__init__(self, self._CreateDocTemplate(resourceId))
        self.MakeDocument = MakeDocument
        self.MakeFrame = MakeFrame
        self.MakeView = MakeView
        self._SetupSharedMenu_()
        return

    def _SetupSharedMenu_(self):
        pass

    def _CreateDocTemplate(self, resourceId):
        return win32ui.CreateDocTemplate(resourceId)

    def __del__(self):
        object.CmdTarget.__del__(self)

    def CreateCreateContext(self, doc=None):
        return CreateContext(self, doc)

    def CreateNewFrame(self, doc):
        makeFrame = self.MakeFrame
        if makeFrame is None:
            makeFrame = window.MDIChildWnd
        wnd = makeFrame()
        context = self.CreateCreateContext(doc)
        wnd.LoadFrame(self.GetResourceID(), -1, None, context)
        return wnd

    def CreateNewDocument(self):
        makeDocument = self.MakeDocument
        if makeDocument is None:
            makeDocument = Document
        return makeDocument(self)

    def CreateView(self, frame, context):
        makeView = self.MakeView
        if makeView is None:
            makeView = EditView
        view = makeView(context.doc)
        view.CreateWindow(frame)
        return


class RichEditDocTemplate(DocTemplate):

    def __init__(self, resourceId=None, MakeDocument=None, MakeFrame=None, MakeView=None):
        if MakeView is None:
            MakeView = RichEditView
        if MakeDocument is None:
            MakeDocument = RichEditDoc
        DocTemplate.__init__(self, resourceId, MakeDocument, MakeFrame, MakeView)
        return

    def _CreateDocTemplate(self, resourceId):
        return win32ui.CreateRichEditDocTemplate(resourceId)


def t():

    class FormTemplate(DocTemplate):

        def CreateView(self, frame, context):
            makeView = self.MakeView
            view = ListView(context.doc)
            view.CreateWindow(frame)

    t = FormTemplate()
    return t.OpenDocumentFile(None)