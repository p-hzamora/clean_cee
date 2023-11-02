# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\pdfgen\pdfimages.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = '\nImage functionality sliced out of canvas.py for generalization\n'
import os, string
from types import StringType
import reportlab
from reportlab import rl_config
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase import pdfdoc
from reportlab.lib.utils import fp_str, getStringIO
from reportlab.lib.utils import import_zlib, haveImages
from reportlab.lib.boxstuff import aspectRatioFix

class PDFImage:
    """Wrapper around different "image sources".  You can make images
    from a PIL Image object, a filename (in which case it uses PIL),
    an image we previously cached (optimisation, hardly used these
    days) or a JPEG (which PDF supports natively)."""

    def __init__(self, image, x, y, width=None, height=None, caching=0):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.filename = None
        self.imageCaching = caching
        self.colorSpace = 'DeviceRGB'
        self.bitsPerComponent = 8
        self.filters = []
        self.source = None
        self.getImageData()
        return

    def jpg_imagedata(self):
        fp = open(self.image, 'rb')
        try:
            result = self._jpg_imagedata(fp)
        finally:
            fp.close()

        return result

    def _jpg_imagedata(self, imageFile):
        info = pdfutils.readJPEGInfo(imageFile)
        self.source = 'JPEG'
        imgwidth, imgheight = info[0], info[1]
        if info[2] == 1:
            colorSpace = 'DeviceGray'
        elif info[2] == 3:
            colorSpace = 'DeviceRGB'
        else:
            colorSpace = 'DeviceCMYK'
        imageFile.seek(0)
        imagedata = []
        imagedata.append('BI /W %d /H %d /BPC 8 /CS /%s /F [%s/DCT] ID' % (imgwidth, imgheight, colorSpace, rl_config.useA85 and '/A85 ' or ''))
        data = imageFile.read()
        if rl_config.useA85:
            data = pdfutils._AsciiBase85Encode(data)
        pdfutils._chunker(data, imagedata)
        imagedata.append('EI')
        return (imagedata, imgwidth, imgheight)

    def cache_imagedata(self):
        image = self.image
        if not pdfutils.cachedImageExists(image):
            zlib = import_zlib()
            if not zlib:
                return
            if not haveImages:
                return
            pdfutils.cacheImageFile(image)
        cachedname = os.path.splitext(image)[0] + (rl_config.useA85 and '.a85' or '.bin')
        imagedata = open(cachedname, 'rb').readlines()
        imagedata = map(string.strip, imagedata)
        return imagedata

    def PIL_imagedata(self):
        image = self.image
        if image.format == 'JPEG':
            fp = image.fp
            fp.seek(0)
            return self._jpg_imagedata(fp)
        self.source = 'PIL'
        zlib = import_zlib()
        if not zlib:
            return
        if image.mode == 'CMYK':
            myimage = image
            colorSpace = 'DeviceCMYK'
            bpp = 4
        else:
            myimage = image.convert('RGB')
            colorSpace = 'RGB'
            bpp = 3
        imgwidth, imgheight = myimage.size
        imagedata = [
         'BI /W %d /H %d /BPC 8 /CS /%s /F [%s/Fl] ID' % (imgwidth, imgheight, colorSpace, rl_config.useA85 and '/A85 ' or '')]
        raw = myimage.tostring()
        assert len(raw) == imgwidth * imgheight * bpp, 'Wrong amount of data for image'
        data = zlib.compress(raw)
        if rl_config.useA85:
            data = pdfutils._AsciiBase85Encode(data)
        pdfutils._chunker(data, imagedata)
        imagedata.append('EI')
        return (imagedata, imgwidth, imgheight)

    def non_jpg_imagedata(self, image):
        if not self.imageCaching:
            imagedata = pdfutils.cacheImageFile(image, returnInMemory=1)
        else:
            imagedata = self.cache_imagedata()
        words = string.split(imagedata[1])
        imgwidth = string.atoi(words[1])
        imgheight = string.atoi(words[3])
        return (imagedata, imgwidth, imgheight)

    def getImageData(self, preserveAspectRatio=False):
        """Gets data, height, width - whatever type of image"""
        image = self.image
        if type(image) == StringType:
            self.filename = image
            if os.path.splitext(image)[1] in ('.jpg', '.JPG', '.jpeg', '.JPEG'):
                try:
                    imagedata, imgwidth, imgheight = self.jpg_imagedata()
                except:
                    imagedata, imgwidth, imgheight = self.non_jpg_imagedata(image)

            else:
                imagedata, imgwidth, imgheight = self.non_jpg_imagedata(image)
        else:
            import sys
            if sys.platform[0:4] == 'java':
                imagedata, imgwidth, imgheight = self.JAVA_imagedata()
            else:
                imagedata, imgwidth, imgheight = self.PIL_imagedata()
        self.imageData = imagedata
        self.imgwidth = imgwidth
        self.imgheight = imgheight
        self.width = self.width or imgwidth
        self.height = self.height or imgheight

    def drawInlineImage(self, canvas, preserveAspectRatio=False, anchor='sw'):
        """Draw an Image into the specified rectangle.  If width and
        height are omitted, they are calculated from the image size.
        Also allow file names as well as images.  This allows a
        caching mechanism"""
        width = self.width
        height = self.height
        if width < 1e-06 or height < 1e-06:
            return False
        x, y, self.width, self.height, scaled = aspectRatioFix(preserveAspectRatio, anchor, self.x, self.y, width, height, self.imgwidth, self.imgheight)
        if not canvas.bottomup:
            y = y + height
        canvas._code.append('q %s 0 0 %s cm' % (fp_str(self.width), fp_str(self.height, x, y)))
        for line in self.imageData:
            canvas._code.append(line)

        canvas._code.append('Q')
        return True

    def format(self, document):
        """Allow it to be used within pdfdoc framework.  This only
        defines how it is stored, not how it is drawn later."""
        dict = pdfdoc.PDFDictionary()
        dict['Type'] = '/XObject'
        dict['Subtype'] = '/Image'
        dict['Width'] = self.width
        dict['Height'] = self.height
        dict['BitsPerComponent'] = 8
        dict['ColorSpace'] = pdfdoc.PDFName(self.colorSpace)
        content = string.join(self.imageData[3:-1], '\n') + '\n'
        strm = pdfdoc.PDFStream(dictionary=dict, content=content)
        return strm.format(document)


if __name__ == '__main__':
    srcfile = os.path.join(os.path.dirname(reportlab.__file__), 'test', 'pythonpowered.gif')
    assert os.path.isfile(srcfile), 'image not found'
    pdfdoc.LongFormat = 1
    img = PDFImage(srcfile, 100, 100)
    import pprint
    doc = pdfdoc.PDFDocument()
    print 'source=', img.source
    print img.format(doc)