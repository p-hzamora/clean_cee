# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ImageDraw2.pyc
# Compiled at: 2010-05-15 16:50:38
import Image, ImageColor, ImageDraw, ImageFont, ImagePath

class Pen:

    def __init__(self, color, width=1, opacity=255):
        self.color = ImageColor.getrgb(color)
        self.width = width


class Brush:

    def __init__(self, color, opacity=255):
        self.color = ImageColor.getrgb(color)


class Font:

    def __init__(self, color, file, size=12):
        self.color = ImageColor.getrgb(color)
        self.font = ImageFont.truetype(file, size)


class Draw:

    def __init__(self, image, size=None, color=None):
        if not hasattr(image, 'im'):
            image = Image.new(image, size, color)
        self.draw = ImageDraw.Draw(image)
        self.image = image
        self.transform = None
        return

    def flush(self):
        return self.image

    def render(self, op, xy, pen, brush=None):
        outline = fill = None
        width = 1
        if isinstance(pen, Pen):
            outline = pen.color
            width = pen.width
        elif isinstance(brush, Pen):
            outline = brush.color
            width = brush.width
        if isinstance(brush, Brush):
            fill = brush.color
        elif isinstance(pen, Brush):
            fill = pen.color
        if self.transform:
            xy = ImagePath.Path(xy)
            xy.transform(self.transform)
        if op == 'line':
            self.draw.line(xy, fill=outline, width=width)
        else:
            getattr(self.draw, op)(xy, fill=fill, outline=outline)
        return

    def settransform(self, (xoffset, yoffset)):
        self.transform = (
         1, 0, xoffset, 0, 1, yoffset)

    def arc(self, xy, start, end, *options):
        self.render('arc', xy, start, end, *options)

    def chord(self, xy, start, end, *options):
        self.render('chord', xy, start, end, *options)

    def ellipse(self, xy, *options):
        self.render('ellipse', xy, *options)

    def line(self, xy, *options):
        self.render('line', xy, *options)

    def pieslice(self, xy, start, end, *options):
        self.render('pieslice', xy, start, end, *options)

    def polygon(self, xy, *options):
        self.render('polygon', xy, *options)

    def rectangle(self, xy, *options):
        self.render('rectangle', xy, *options)

    def symbol(self, xy, symbol, *options):
        raise NotImplementedError('not in this version')

    def text(self, xy, text, font):
        if self.transform:
            xy = ImagePath.Path(xy)
            xy.transform(self.transform)
        self.draw.text(xy, text, font=font.font, fill=font.color)

    def textsize(self, text, font):
        return self.draw.textsize(text, font=font.font)