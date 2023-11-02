# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: wx\lib\imageutils.pyc
# Compiled at: 2011-07-15 22:30:42
import wx

def grayOut(anImage):
    """
    Convert the given image (in place) to a grayed-out
    version, appropriate for a 'disabled' appearance.
    """
    factor = 0.7
    if anImage.HasMask():
        maskColor = (
         anImage.GetMaskRed(), anImage.GetMaskGreen(), anImage.GetMaskBlue())
    else:
        maskColor = None
    if anImage.HasAlpha():
        alpha = anImage.GetAlphaData()
    else:
        alpha = None
    data = map(ord, list(anImage.GetData()))
    for i in range(0, len(data), 3):
        pixel = (data[i], data[i + 1], data[i + 2])
        pixel = makeGray(pixel, factor, maskColor)
        for x in range(3):
            data[i + x] = pixel[x]

    anImage.SetData(('').join(map(chr, data)))
    if alpha:
        anImage.SetAlphaData(alpha)
    return


def makeGray((r, g, b), factor, maskColor):
    """
    Make a pixel grayed-out. If the pixel
    matches the maskColor, it won't be
    changed.
    """
    if (
     r, g, b) != maskColor:
        return map((lambda x: int((230 - x) * factor) + x), (r, g, b))
    else:
        return (
         r, g, b)


def stepColour(c, step):
    """
    stepColour is a utility function that simply darkens or lightens a
    color, based on the specified step value.  A step of 0 is
    completely black and a step of 200 is totally white, and 100
    results in the same color as was passed in.
    """

    def _blendColour(fg, bg, dstep):
        result = bg + dstep * (fg - bg)
        if result < 0:
            result = 0
        if result > 255:
            result = 255
        return result

    if step == 100:
        return c
    r = c.Red()
    g = c.Green()
    b = c.Blue()
    step = min(step, 200)
    step = max(step, 0)
    dstep = (step - 100.0) / 100.0
    if step > 100:
        bg = 255.0
        dstep = 1.0 - dstep
    else:
        bg = 0.0
        dstep = 1.0 + dstep
    r = _blendColour(r, bg, dstep)
    g = _blendColour(g, bg, dstep)
    b = _blendColour(b, bg, dstep)
    return wx.Colour(int(r), int(g), int(b))