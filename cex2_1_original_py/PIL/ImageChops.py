# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: PIL\ImageChops.pyc
# Compiled at: 2010-05-15 16:50:38
import Image

def constant(image, value):
    """Fill a channel with a given grey level"""
    return Image.new('L', image.size, value)


def duplicate(image):
    """Create a copy of a channel"""
    return image.copy()


def invert(image):
    """Invert a channel"""
    image.load()
    return image._new(image.im.chop_invert())


def lighter(image1, image2):
    """Select the lighter pixels from each image"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_lighter(image2.im))


def darker(image1, image2):
    """Select the darker pixels from each image"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_darker(image2.im))


def difference(image1, image2):
    """Subtract one image from another"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_difference(image2.im))


def multiply(image1, image2):
    """Superimpose two positive images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_multiply(image2.im))


def screen(image1, image2):
    """Superimpose two negative images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_screen(image2.im))


def add(image1, image2, scale=1.0, offset=0):
    """Add two images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_add(image2.im, scale, offset))


def subtract(image1, image2, scale=1.0, offset=0):
    """Subtract two images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_subtract(image2.im, scale, offset))


def add_modulo(image1, image2):
    """Add two images without clipping"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_add_modulo(image2.im))


def subtract_modulo(image1, image2):
    """Subtract two images without clipping"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_subtract_modulo(image2.im))


def logical_and(image1, image2):
    """Logical and between two images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_and(image2.im))


def logical_or(image1, image2):
    """Logical or between two images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_or(image2.im))


def logical_xor(image1, image2):
    """Logical xor between two images"""
    image1.load()
    image2.load()
    return image1._new(image1.im.chop_xor(image2.im))


def blend(image1, image2, alpha):
    """Blend two images using a constant transparency weight"""
    return Image.blend(image1, image2, alpha)


def composite(image1, image2, mask):
    """Create composite image by blending images using a transparency mask"""
    return Image.composite(image1, image2, mask)


def offset(image, xoffset, yoffset=None):
    """Offset image in horizontal and/or vertical direction"""
    if yoffset is None:
        yoffset = xoffset
    image.load()
    return image._new(image.im.offset(xoffset, yoffset))