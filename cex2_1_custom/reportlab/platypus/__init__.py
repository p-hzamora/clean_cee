# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\platypus\__init__.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Page Layout and Typography Using Scripts" - higher-level framework for flowing documents'
from reportlab.platypus.flowables import Flowable, Image, Macro, PageBreak, Preformatted, Spacer, XBox, CondPageBreak, KeepTogether, TraceInfo, FailOnWrap, FailOnDraw, PTOContainer, KeepInFrame, ParagraphAndImage, ImageAndFlowables, ListFlowable, ListItem
from reportlab.platypus.paragraph import Paragraph, cleanBlockQuotedText, ParaLines
from reportlab.platypus.paraparser import ParaFrag
from reportlab.platypus.tables import Table, TableStyle, CellStyle, LongTable
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import BaseDocTemplate, NextPageTemplate, PageTemplate, ActionFlowable, SimpleDocTemplate, FrameBreak, PageBegin, Indenter, NotAtTopPageBreak
from xpreformatted import XPreformatted