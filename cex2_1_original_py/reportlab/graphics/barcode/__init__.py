# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\barcode\__init__.pyc
# Compiled at: 2013-04-03 12:01:28
__version__ = '0.9'
__doc__ = 'Popular barcodes available as reusable widgets'

def getCodes():
    """Returns a dict mapping code names to widgets"""
    from widgets import BarcodeI2of5, BarcodeCode128, BarcodeStandard93, BarcodeExtended93, BarcodeStandard39, BarcodeExtended39, BarcodeMSI, BarcodeCodabar, BarcodeCode11, BarcodeFIM, BarcodePOSTNET, BarcodeUSPS_4State
    from eanbc import Ean13BarcodeWidget, Ean8BarcodeWidget, UPCA
    from qr import QrCodeWidget
    codes = {}
    for widget in (
     BarcodeI2of5,
     BarcodeCode128,
     BarcodeStandard93,
     BarcodeExtended93,
     BarcodeStandard39,
     BarcodeExtended39,
     BarcodeMSI,
     BarcodeCodabar,
     BarcodeCode11,
     BarcodeFIM,
     BarcodePOSTNET,
     BarcodeUSPS_4State,
     Ean13BarcodeWidget,
     Ean8BarcodeWidget,
     UPCA,
     QrCodeWidget):
        codeName = widget.codeName
        codes[codeName] = widget

    return codes


def getCodeNames():
    """Returns sorted list of supported bar code names"""
    return sorted(getCodes().keys())


def createBarcodeDrawing(codeName, **options):
    """This creates and returns a drawing with a barcode.
    """
    from reportlab.graphics.shapes import Drawing, Group
    codes = getCodes()
    bcc = codes[codeName]
    width = options.pop('width', None)
    height = options.pop('height', None)
    isoScale = options.pop('isoScale', 0)
    kw = {}
    for k, v in options.iteritems():
        if k.startswith('_') or k in bcc._attrMap:
            kw[k] = v

    bc = bcc(**kw)
    if hasattr(bc, 'validate'):
        bc.validate()
        if not bc.valid:
            raise ValueError("Illegal barcode with value '%s' in code '%s'" % (options.get('value', None), codeName))
    x1, y1, x2, y2 = bc.getBounds()
    w = float(x2 - x1)
    h = float(y2 - y1)
    sx = width not in ('auto', None)
    sy = height not in ('auto', None)
    if sx or sy:
        sx = sx and width / w or 1.0
        sy = sy and height / h or 1.0
        if isoScale:
            if sx < 1.0 and sy < 1.0:
                sx = sy = max(sx, sy)
            else:
                sx = sy = min(sx, sy)
        w *= sx
        h *= sy
    else:
        sx = sy = 1
    d = Drawing(width=w, height=h, transform=[sx, 0, 0, sy, -sx * x1, -sy * y1])
    d.add(bc, '_bc')
    return d


def createBarcodeImageInMemory(codeName, **options):
    """This creates and returns barcode as an image in memory.
    Takes same arguments as createBarcodeDrawing and also an
    optional format keyword which can be anything acceptable
    to Drawing.asString eg gif, pdf, tiff, py ......
    """
    format = options.pop('format', 'png')
    d = createBarcodeDrawing(codeName, **options)
    return d.asString(format)