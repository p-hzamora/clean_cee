# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\barcode\test.pyc
# Compiled at: 2013-04-03 12:01:28
import os, sys, time
from reportlab.graphics.barcode.common import *
from reportlab.graphics.barcode.code39 import *
from reportlab.graphics.barcode.code93 import *
from reportlab.graphics.barcode.code128 import *
from reportlab.graphics.barcode.usps import *
from reportlab.graphics.barcode.usps4s import USPS_4State
from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Preformatted, PageBreak
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.frames import Frame
from reportlab.platypus.flowables import XBox, KeepTogether
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing, createBarcodeImageInMemory

def run():
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    story = []
    story.append(Paragraph('I2of5', styleN))
    story.append(I2of5(1234, barWidth=inch * 0.02, checksum=0))
    story.append(Paragraph('MSI', styleN))
    story.append(MSI(1234))
    story.append(Paragraph('Codabar', styleN))
    story.append(Codabar('A012345B', barWidth=inch * 0.02))
    story.append(Paragraph('Code 11', styleN))
    story.append(Code11('01234545634563'))
    story.append(Paragraph('Code 39', styleN))
    story.append(Standard39('A012345B%R'))
    story.append(Paragraph('Extended Code 39', styleN))
    story.append(Extended39('A012345B}'))
    story.append(Paragraph('Code93', styleN))
    story.append(Standard93('CODE 93'))
    story.append(Paragraph('Extended Code93', styleN))
    story.append(Extended93('L@@K! Code 93 :-)'))
    story.append(Paragraph('Code 128', styleN))
    c = Code128('AB-12345678')
    story.append(c)
    story.append(Paragraph('USPS FIM', styleN))
    story.append(FIM('A'))
    story.append(Paragraph('USPS POSTNET', styleN))
    story.append(POSTNET('78247-1043'))
    story.append(Paragraph('USPS 4 State', styleN))
    story.append(USPS_4State('01234567094987654321', '01234567891'))
    from reportlab.graphics.barcode import createBarcodeDrawing
    story.append(Paragraph('EAN13', styleN))
    bcd = createBarcodeDrawing('EAN13', value='123456789012')
    story.append(bcd)
    story.append(Paragraph('EAN8', styleN))
    bcd = createBarcodeDrawing('EAN8', value='1234567')
    story.append(bcd)
    story.append(Paragraph('UPCA', styleN))
    bcd = createBarcodeDrawing('UPCA', value='03600029145')
    story.append(bcd)
    story.append(Paragraph('USPS_4State', styleN))
    bcd = createBarcodeDrawing('USPS_4State', value='01234567094987654321', routing='01234567891')
    story.append(bcd)
    story.append(Paragraph('Label Size', styleN))
    story.append(XBox((2.0 + 5.0 / 8.0) * inch, 1 * inch, '1x2-5/8"'))
    story.append(Paragraph('Label Size', styleN))
    story.append(XBox(1.75 * inch, 0.5 * inch, '1/2x1-3/4"'))
    c = Canvas('out.pdf')
    f = Frame(inch, inch, 6 * inch, 9 * inch, showBoundary=1)
    f.addFromList(story, c)
    c.save()
    print 'saved out.pdf'


def fullTest(fileName='test_full.pdf'):
    """Creates large-ish test document with a variety of parameters"""
    story = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    styleH2 = styles['Heading2']
    story = []
    story.append(Paragraph('ReportLab Barcode Test Suite - full output', styleH))
    story.append(Paragraph('Generated on %s' % time.ctime(time.time()), styleN))
    story.append(Paragraph('', styleN))
    story.append(Paragraph('Repository information for this build:', styleN))
    if os.path.split(os.getcwd())[-1] == 'barcode' and os.path.isdir('.svn'):
        infoLines = os.popen('svn info').read()
        story.append(Preformatted(infoLines, styles['Code']))
    story.append(Paragraph('About this document', styleH2))
    story.append(Paragraph('History and Status', styleH2))
    story.append(Paragraph('\n        This is the test suite and docoumentation for the ReportLab open source barcode API,\n        being re-released as part of the forthcoming ReportLab 2.0 release.\n        ', styleN))
    story.append(Paragraph('\n        Several years ago Ty Sarna contributed a barcode module to the ReportLab community.\n        Several of the codes were used by him in hiw work and to the best of our knowledge\n        this was correct.  These were written as flowable objects and were available in PDFs,\n        but not in our graphics framework.  However, we had no knowledge of barcodes ourselves\n        and did not advertise or extend the package.\n        ', styleN))
    story.append(Paragraph('\n        We "wrapped" the barcodes to be usable within our graphics framework; they are now available\n        as Drawing objects which can be rendered to EPS files or bitmaps.  For the last 2 years this\n        has been available in our Diagra and Report Markup Language products.  However, we did not\n        charge separately and use was on an "as is" basis.\n        ', styleN))
    story.append(Paragraph('\n        A major licensee of our technology has kindly agreed to part-fund proper productisation\n        of this code on an open source basis in Q1 2006.  This has involved addition of EAN codes\n        as well as a proper testing program.  Henceforth we intend to publicise the code more widely,\n        gather feedback, accept contributions of code and treat it as "supported".  \n        ', styleN))
    story.append(Paragraph('\n        This involved making available both downloads and testing resources.  This PDF document\n        is the output of the current test suite.  It contains codes you can scan (if you use a nice sharp\n        laser printer!), and will be extended over coming weeks to include usage examples and notes on\n        each barcode and how widely tested they are.  This is being done through documentation strings in\n        the barcode objects themselves so should always be up to date.\n        ', styleN))
    story.append(Paragraph('Usage examples', styleH2))
    story.append(Paragraph('\n        To be completed\n        ', styleN))
    story.append(Paragraph('The codes', styleH2))
    story.append(Paragraph('\n        Below we show a scannable code from each barcode, with and without human-readable text.\n        These are magnified about 2x from the natural size done by the original author to aid\n        inspection.  This will be expanded to include several test cases per code, and to add\n        explanations of checksums.  Be aware that (a) if you enter numeric codes which are too\n        short they may be prefixed for you (e.g. "123" for an 8-digit code becomes "00000123"),\n        and that the scanned results and readable text will generally include extra checksums\n        at the end.\n        ', styleN))
    codeNames = getCodeNames()
    from reportlab.lib.utils import flatten
    width = [ float(x[8:]) for x in sys.argv if x.startswith('--width=') ]
    height = [ float(x[9:]) for x in sys.argv if x.startswith('--height=') ]
    isoScale = [ int(x[11:]) for x in sys.argv if x.startswith('--isoscale=') ]
    options = {}
    if width:
        options['width'] = width[0]
    if height:
        options['height'] = height[0]
    if isoScale:
        options['isoScale'] = isoScale[0]
    scales = [ x[8:].split(',') for x in sys.argv if x.startswith('--scale=') ]
    scales = map(float, scales and flatten(scales) or [1])
    scales = map(float, scales and flatten(scales) or [1])
    for scale in scales:
        story.append(PageBreak())
        story.append(Paragraph('Scale = %.1f' % scale, styleH2))
        story.append(Spacer(36, 12))
        for codeName in codeNames:
            s = [
             Paragraph('Code: ' + codeName, styleH2)]
            for hr in (0, 1):
                s.append(Spacer(36, 12))
                dr = createBarcodeDrawing(codeName, humanReadable=hr, **options)
                dr.renderScale = scale
                s.append(dr)
                s.append(Spacer(36, 12))

            s.append(Paragraph('Barcode should say: ' + dr._bc.value, styleN))
            story.append(KeepTogether(s))

    SimpleDocTemplate(fileName).build(story)
    print 'created', fileName


if __name__ == '__main__':
    run()
    fullTest()

    def createSample(name, memory):
        f = open(name, 'wb')
        f.write(memory)
        f.close()


    createSample('test_cbcim.png', createBarcodeImageInMemory('EAN13', value='123456789012'))
    createSample('test_cbcim.gif', createBarcodeImageInMemory('EAN8', value='1234567', format='gif'))
    createSample('test_cbcim.pdf', createBarcodeImageInMemory('UPCA', value='03600029145', format='pdf'))
    createSample('test_cbcim.tiff', createBarcodeImageInMemory('USPS_4State', value='01234567094987654321', routing='01234567891', format='tiff'))