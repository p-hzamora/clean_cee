# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\graphics\renderPS.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Render drawing objects in Postscript'
import string, types
from reportlab.pdfbase.pdfmetrics import getFont, stringWidth, unicode2T1
from reportlab.lib.utils import fp_str, getStringIO
from reportlab.lib.colors import black
from reportlab.graphics.renderbase import Renderer, StateTracker, getStateDelta, renderScaledDrawing
from reportlab.graphics.shapes import STATE_DEFAULTS
import math
from types import StringType
from operator import getitem
from reportlab import rl_config
_ESCAPEDICT = {}
for c in xrange(256):
    if c < 32 or c >= 127:
        _ESCAPEDICT[chr(c)] = '\\%03o' % c
    elif c in (ord('\\'), ord('('), ord(')')):
        _ESCAPEDICT[chr(c)] = '\\' + chr(c)
    else:
        _ESCAPEDICT[chr(c)] = chr(c)
    del c

def _escape_and_limit(s):
    R = []
    aR = R.append
    n = 0
    for c in s:
        c = _ESCAPEDICT[c]
        aR(c)
        n += len(c)
        if n >= 200:
            n = 0
            aR('\\\n')

    return ('').join(R)


PS_WinAnsiEncoding = '       \n/RE { %def       \n  findfont begin     \n  currentdict dup length dict begin  \n { %forall   \n   1 index /FID ne { def } { pop pop } ifelse    \n } forall    \n /FontName exch def dup length 0 ne { %if    \n   /Encoding Encoding 256 array copy def     \n   0 exch { %forall      \n     dup type /nametype eq { %ifelse     \n       Encoding 2 index 2 index put      \n       pop 1 add     \n     }{ %else    \n       exch pop      \n     } ifelse    \n   } forall      \n } if pop    \n  currentdict dup end end    \n  /FontName get exch definefont pop  \n} bind def       \n \n/WinAnsiEncoding [       \n  39/quotesingle 96/grave 128/euro 130/quotesinglbase/florin/quotedblbase    \n  /ellipsis/dagger/daggerdbl/circumflex/perthousand  \n  /Scaron/guilsinglleft/OE 145/quoteleft/quoteright  \n  /quotedblleft/quotedblright/bullet/endash/emdash       \n  /tilde/trademark/scaron/guilsinglright/oe/dotlessi     \n  159/Ydieresis 164/currency 166/brokenbar 168/dieresis/copyright    \n  /ordfeminine 172/logicalnot 174/registered/macron/ring     \n  177/plusminus/twosuperior/threesuperior/acute/mu       \n  183/periodcentered/cedilla/onesuperior/ordmasculine    \n  188/onequarter/onehalf/threequarters 192/Agrave/Aacute     \n  /Acircumflex/Atilde/Adieresis/Aring/AE/Ccedilla    \n  /Egrave/Eacute/Ecircumflex/Edieresis/Igrave/Iacute     \n  /Icircumflex/Idieresis/Eth/Ntilde/Ograve/Oacute    \n  /Ocircumflex/Otilde/Odieresis/multiply/Oslash  \n  /Ugrave/Uacute/Ucircumflex/Udieresis/Yacute/Thorn  \n  /germandbls/agrave/aacute/acircumflex/atilde/adieresis     \n  /aring/ae/ccedilla/egrave/eacute/ecircumflex       \n  /edieresis/igrave/iacute/icircumflex/idieresis     \n  /eth/ntilde/ograve/oacute/ocircumflex/otilde       \n  /odieresis/divide/oslash/ugrave/uacute/ucircumflex     \n  /udieresis/yacute/thorn/ydieresis  \n] def    \n'

class PSCanvas():

    def __init__(self, size=(300, 300), PostScriptLevel=2):
        self.width, self.height = size
        xtraState = []
        self._xtraState_push = xtraState.append
        self._xtraState_pop = xtraState.pop
        self.comments = 0
        self.code = []
        self.code_append = self.code.append
        self._sep = '\n'
        self._strokeColor = self._fillColor = self._lineWidth = self._font = self._fontSize = self._lineCap = self._lineJoin = self._color = None
        self._fontsUsed = []
        self.setFont(STATE_DEFAULTS['fontName'], STATE_DEFAULTS['fontSize'])
        self.setStrokeColor(STATE_DEFAULTS['strokeColor'])
        self.setLineCap(2)
        self.setLineJoin(0)
        self.setLineWidth(1)
        self.PostScriptLevel = PostScriptLevel
        return

    def comment(self, msg):
        if self.comments:
            self.code_append('%' + msg)

    def drawImage(self, image, x1, y1, x2=None, y2=None):
        if self.PostScriptLevel == 1:
            self._drawImageLevel1(image, x1, y1, x2=None, y2=None)
        elif self.PostScriptLevel == 2:
            self._drawImageLevel2(image, x1, y1, x2=None, y2=None)
        else:
            raise ValueError('Unsupported Postscript Level %s' % self.PostScriptLevel)
        return

    def clear(self):
        self.code_append('showpage')

    def _t1_re_encode(self):
        if not self._fontsUsed:
            return
        C = []
        for fontName in self._fontsUsed:
            fontObj = getFont(fontName)
            if not fontObj._dynamicFont and fontObj.encName == 'WinAnsiEncoding':
                C.append('WinAnsiEncoding /%s /%s RE' % (fontName, fontName))

        if C:
            C.insert(0, PS_WinAnsiEncoding)
            self.code.insert(1, string.join(C, self._sep))

    def save(self, f=None):
        if not hasattr(f, 'write'):
            file = open(f, 'wb')
        else:
            file = f
        if self.code[-1] != 'showpage':
            self.clear()
        self.code.insert(0, '%%!PS-Adobe-3.0 EPSF-3.0\n%%%%BoundingBox: 0 0 %d %d\n%%%% Initialization:\n/m {moveto} bind def\n/l {lineto} bind def\n/c {curveto} bind def\n' % (self.width, self.height))
        self._t1_re_encode()
        file.write(string.join(self.code, self._sep))
        if file is not f:
            file.close()
            from reportlab.lib.utils import markfilename
            markfilename(f, creatorcode='XPR3', filetype='EPSF')

    def saveState(self):
        self._xtraState_push((self._fontCodeLoc,))
        self.code_append('gsave')

    def restoreState(self):
        self.code_append('grestore')
        self._fontCodeLoc, = self._xtraState_pop()

    def stringWidth(self, s, font=None, fontSize=None):
        """Return the logical width of the string if it were drawn
        in the current font (defaults to self.font)."""
        font = font or self._font
        fontSize = fontSize or self._fontSize
        return stringWidth(s, font, fontSize)

    def setLineCap(self, v):
        if self._lineCap != v:
            self._lineCap = v
            self.code_append('%d setlinecap' % v)

    def setLineJoin(self, v):
        if self._lineJoin != v:
            self._lineJoin = v
            self.code_append('%d setlinejoin' % v)

    def setDash(self, array=[], phase=0):
        """Two notations.  pass two numbers, or an array and phase"""
        psoperation = 'setdash'
        if isinstance(array, (float, int)):
            self.code_append('[%s %s] 0 %s' % (array, phase, psoperation))
        elif isinstance(array, (tuple, list)):
            assert phase >= 0, 'phase is a length in user space'
            textarray = string.join(map(str, array))
            self.code_append('[%s] %s %s' % (textarray, phase, psoperation))

    def setStrokeColor(self, color):
        self._strokeColor = color
        self.setColor(color)

    def setColor(self, color):
        if self._color != color:
            self._color = color
            if color:
                if hasattr(color, 'cyan'):
                    self.code_append('%s setcmykcolor' % fp_str(color.cyan, color.magenta, color.yellow, color.black))
                else:
                    self.code_append('%s setrgbcolor' % fp_str(color.red, color.green, color.blue))

    def setFillColor(self, color):
        self._fillColor = color
        self.setColor(color)

    def setLineWidth(self, width):
        if width != self._lineWidth:
            self._lineWidth = width
            self.code_append('%s setlinewidth' % width)

    def setFont(self, font, fontSize, leading=None):
        if self._font != font or self._fontSize != fontSize:
            self._fontCodeLoc = len(self.code)
            self._font = font
            self._fontSize = fontSize
            self.code_append('')

    def line(self, x1, y1, x2, y2):
        if self._strokeColor != None:
            self.setColor(self._strokeColor)
            self.code_append('%s m %s l stroke' % (fp_str(x1, y1), fp_str(x2, y2)))
        return

    def _escape(self, s):
        """
        return a copy of string s with special characters in postscript strings
        escaped with backslashes.
        """
        try:
            return _escape_and_limit(s)
        except:
            raise ValueError('cannot escape %s %s' % (s, repr(s)))

    def _issueT1String(self, fontObj, x, y, s):
        fc = fontObj
        code_append = self.code_append
        fontSize = self._fontSize
        fontsUsed = self._fontsUsed
        escape = self._escape
        if not isinstance(s, unicode):
            try:
                s = s.decode('utf8')
            except UnicodeDecodeError as e:
                i, j = e.args[2:4]
                raise UnicodeDecodeError(*(e.args[:4] + ('%s\n%s-->%s<--%s' % (e.args[4], s[i - 10:i], s[i:j], s[j:j + 10]),)))

        for f, t in unicode2T1(s, [fontObj] + fontObj.substitutionFonts):
            if f != fc:
                psName = f.face.name
                code_append('(%s) findfont %s scalefont setfont' % (psName, fp_str(fontSize)))
                if psName not in fontsUsed:
                    fontsUsed.append(psName)
                fc = f
            code_append('%s m (%s) show ' % (fp_str(x, y), escape(t)))
            x += f.stringWidth(t.decode(f.encName), fontSize)

        if fontObj != fc:
            self._font = None
            self.setFont(fontObj.face.name, fontSize)
        return

    def drawString(self, x, y, s, angle=0):
        if self._fillColor != None:
            fontObj = getFont(self._font)
            if not self.code[self._fontCodeLoc]:
                psName = fontObj.face.name
                self.code[self._fontCodeLoc] = '(%s) findfont %s scalefont setfont' % (psName, fp_str(self._fontSize))
                if psName not in self._fontsUsed:
                    self._fontsUsed.append(psName)
            self.setColor(self._fillColor)
            if angle != 0:
                self.code_append('gsave %s translate %s rotate' % (fp_str(x, y), fp_str(angle)))
                x = y = 0
            if fontObj._dynamicFont:
                s = self._escape(s)
                self.code_append('%s m (%s) show ' % (fp_str(x, y), s))
            else:
                self._issueT1String(fontObj, x, y, s)
            if angle != 0:
                self.code_append('grestore')
        return

    def drawCentredString(self, x, y, text, text_anchor='middle'):
        if self._fillColor is not None:
            textLen = stringWidth(text, self._font, self._fontSize)
            if text_anchor == 'end':
                x -= textLen
            elif text_anchor == 'middle':
                x -= textLen / 2.0
            elif text_anchor == 'numeric':
                x -= numericXShift(text_anchor, text, textLen, self._font, self._fontSize)
            self.drawString(x, y, text)
        return

    def drawRightString(self, text, x, y):
        self.drawCentredString(text, x, y, text_anchor='end')

    def drawCurve(self, x1, y1, x2, y2, x3, y3, x4, y4, closed=0):
        codeline = '%s m %s curveto'
        data = (fp_str(x1, y1), fp_str(x2, y2, x3, y3, x4, y4))
        if self._fillColor != None:
            self.setColor(self._fillColor)
            self.code_append(codeline % data + ' eofill')
        if self._strokeColor != None:
            self.setColor(self._strokeColor)
            self.code_append(codeline % data + (closed and ' closepath' or '') + ' stroke')
        return

    def rect(self, x1, y1, x2, y2, stroke=1, fill=1):
        """Draw a rectangle between x1,y1, and x2,y2"""
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        self.polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)), closed=1, stroke=stroke, fill=fill)

    def roundRect(self, x1, y1, x2, y2, rx=8, ry=8):
        """Draw a rounded rectangle between x1,y1, and x2,y2,
        with corners inset as ellipses with x radius rx and y radius ry.
        These should have x1<x2, y1<y2, rx>0, and ry>0."""
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        ellipsePath = 'matrix currentmatrix %s %s translate %s %s scale 0 0 1 %s %s arc setmatrix'
        rr = [
         'newpath']
        a = rr.append
        a(ellipsePath % (x1 + rx, y1 + ry, rx, -ry, 90, 180))
        a(ellipsePath % (x1 + rx, y2 - ry, rx, -ry, 180, 270))
        a(ellipsePath % (x2 - rx, y2 - ry, rx, -ry, 270, 360))
        a(ellipsePath % (x2 - rx, y1 + ry, rx, -ry, 0, 90))
        a('closepath')
        self._fillAndStroke(rr)

    def ellipse(self, x1, y1, x2, y2):
        """Draw an orthogonal ellipse inscribed within the rectangle x1,y1,x2,y2.
        These should have x1<x2 and y1<y2."""
        self.drawArc(x1, y1, x2, y2)

    def circle(self, xc, yc, r):
        self.ellipse(xc - r, yc - r, xc + r, yc + r)

    def drawArc(self, x1, y1, x2, y2, startAng=0, extent=360, fromcenter=0):
        """Draw a partial ellipse inscribed within the rectangle x1,y1,x2,y2,
        starting at startAng degrees and covering extent degrees.   Angles
        start with 0 to the right (+x) and increase counter-clockwise.
        These should have x1<x2 and y1<y2."""
        cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        rx, ry = (x2 - x1) / 2.0, (y2 - y1) / 2.0
        codeline = self._genArcCode(x1, y1, x2, y2, startAng, extent)
        startAngleRadians = math.pi * startAng / 180.0
        extentRadians = math.pi * extent / 180.0
        endAngleRadians = startAngleRadians + extentRadians
        codelineAppended = 0
        if self._fillColor != None:
            self.setColor(self._fillColor)
            self.code_append(codeline)
            codelineAppended = 1
            if self._strokeColor != None:
                self.code_append('gsave')
            self.lineTo(cx, cy)
            self.code_append('eofill')
            if self._strokeColor != None:
                self.code_append('grestore')
        if self._strokeColor != None:
            self.setColor(self._strokeColor)
            startx, starty = cx + rx * math.cos(startAngleRadians), cy + ry * math.sin(startAngleRadians)
            if not codelineAppended:
                self.code_append(codeline)
            if fromcenter:
                self.lineTo(cx, cy)
                self.lineTo(startx, starty)
                self.code_append('closepath')
            self.code_append('stroke')
        return

    def _genArcCode(self, x1, y1, x2, y2, startAng, extent):
        """Calculate the path for an arc inscribed in rectangle defined by (x1,y1),(x2,y2)"""
        xScale = abs((x2 - x1) / 2.0)
        yScale = abs((y2 - y1) / 2.0)
        x, y = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        codeline = 'matrix currentmatrix %s %s translate %s %s scale 0 0 1 %s %s %s setmatrix'
        if extent >= 0:
            arc = 'arc'
        else:
            arc = 'arcn'
        data = (
         x, y, xScale, yScale, startAng, startAng + extent, arc)
        return codeline % data

    def polygon(self, p, closed=0, stroke=1, fill=1):
        assert len(p) >= 2, 'Polygon must have 2 or more points'
        start = p[0]
        p = p[1:]
        poly = []
        a = poly.append
        a('%s m' % fp_str(start))
        for point in p:
            a('%s l' % fp_str(point))

        if closed:
            a('closepath')
        self._fillAndStroke(poly, stroke=stroke, fill=fill)

    def lines(self, lineList, color=None, width=None):
        if self._strokeColor != None:
            self._setColor(self._strokeColor)
            codeline = '%s m %s l stroke'
            for line in lineList:
                self.code_append(codeline % (fp_str(line[0]), fp_str(line[1])))

        return

    def moveTo(self, x, y):
        self.code_append('%s m' % fp_str(x, y))

    def lineTo(self, x, y):
        self.code_append('%s l' % fp_str(x, y))

    def curveTo(self, x1, y1, x2, y2, x3, y3):
        self.code_append('%s c' % fp_str(x1, y1, x2, y2, x3, y3))

    def closePath(self):
        self.code_append('closepath')

    def polyLine(self, p):
        assert len(p) >= 1, 'Polyline must have 1 or more points'
        if self._strokeColor != None:
            self.setColor(self._strokeColor)
            self.moveTo(p[0][0], p[0][1])
            for t in p[1:]:
                self.lineTo(t[0], t[1])

            self.code_append('stroke')
        return

    def drawFigure(self, partList, closed=0):
        figureCode = []
        a = figureCode.append
        first = 1
        for part in partList:
            op = part[0]
            args = list(part[1:])
            if op == figureLine:
                if first:
                    first = 0
                    a('%s m' % fp_str(args[:2]))
                else:
                    a('%s l' % fp_str(args[:2]))
                a('%s l' % fp_str(args[2:]))
            elif op == figureArc:
                first = 0
                x1, y1, x2, y2, startAngle, extent = args[:6]
                a(self._genArcCode(x1, y1, x2, y2, startAngle, extent))
            elif op == figureCurve:
                if first:
                    first = 0
                    a('%s m' % fp_str(args[:2]))
                else:
                    a('%s l' % fp_str(args[:2]))
                a('%s curveto' % fp_str(args[2:]))
            else:
                raise TypeError, 'unknown figure operator: ' + op

        if closed:
            a('closepath')
        self._fillAndStroke(figureCode)

    def _fillAndStroke(self, code, clip=0, fill=1, stroke=1):
        fill = self._fillColor and fill
        stroke = self._strokeColor and stroke
        if fill or stroke or clip:
            self.code.extend(code)
            if fill:
                if stroke or clip:
                    self.code_append('gsave')
                self.setColor(self._fillColor)
                self.code_append('eofill')
                if stroke or clip:
                    self.code_append('grestore')
            if stroke:
                if clip:
                    self.code_append('gsave')
                self.setColor(self._strokeColor)
                self.code_append('stroke')
                if clip:
                    self.code_append('grestore')
            if clip:
                self.code_append('clip')
                self.code_append('newpath')

    def translate(self, x, y):
        self.code_append('%s translate' % fp_str(x, y))

    def scale(self, x, y):
        self.code_append('%s scale' % fp_str(x, y))

    def transform(self, a, b, c, d, e, f):
        self.code_append('[%s] concat' % fp_str(a, b, c, d, e, f))

    def _drawTimeResize(self, w, h):
        """if this is used we're probably in the wrong world"""
        self.width, self.height = w, h

    def _drawImageLevel1(self, image, x1, y1, x2=None, y2=None):
        """drawImage(self,image,x1,y1,x2=None,y2=None) : If x2 and y2 are ommitted, they are
        calculated from image size. (x1,y1) is upper left of image, (x2,y2) is lower right of
        image in piddle coordinates."""
        component_depth = 8
        myimage = image.convert('RGB')
        imgwidth, imgheight = myimage.size
        if not x2:
            x2 = imgwidth + x1
        if not y2:
            y2 = y1 + imgheight
        drawwidth = x2 - x1
        drawheight = y2 - y1
        self.code.extend([
         'gsave',
         '%s %s translate' % (x1, -y1 - drawheight),
         '%s %s scale' % (drawwidth, drawheight),
         '/scanline %d 3 mul string def' % imgwidth])
        self.code.extend([
         '%s %s %s' % (imgwidth, imgheight, component_depth),
         '[%s %s %s %s %s %s]' % (imgwidth, 0, 0, -imgheight, 0, imgheight),
         '{ currentfile scanline readhexstring pop } false 3',
         'colorimage '])
        rawimage = myimage.tostring()
        hex_encoded = self._AsciiHexEncode(rawimage)
        outstream = getStringIO(hex_encoded)
        dataline = outstream.read(78)
        while dataline != '':
            self.code_append(dataline)
            dataline = outstream.read(78)

        self.code_append('% end of image data')
        self.code_append('grestore')

    def _AsciiHexEncode(self, input):
        """Helper function used by images"""
        output = getStringIO()
        for char in input:
            output.write('%02x' % ord(char))

        return output.getvalue()

    def _drawImageLevel2(self, image, x1, y1, x2=None, y2=None):
        """At present we're handling only PIL"""
        if image.mode == 'L':
            imBitsPerComponent = 8
            imNumComponents = 1
            myimage = image
        else:
            if image.mode == '1':
                myimage = image.convert('L')
                imNumComponents = 1
                myimage = image
            else:
                myimage = image.convert('RGB')
                imNumComponents = 3
                imBitsPerComponent = 8
            imwidth, imheight = myimage.size
            if not x2:
                x2 = imwidth + x1
            if not y2:
                y2 = y1 + imheight
            drawwidth = x2 - x1
            drawheight = y2 - y1
            self.code.extend([
             'gsave',
             '%s %s translate' % (x1, -y1 - drawheight),
             '%s %s scale' % (drawwidth, drawheight)])
            if imNumComponents == 3:
                self.code_append('/DeviceRGB setcolorspace')
            elif imNumComponents == 1:
                self.code_append('/DeviceGray setcolorspace')
            self.code_append('\n<<\n/ImageType 1\n/Width %d /Height %d  %% dimensions of source image\n/BitsPerComponent %d' % (imwidth, imheight, imBitsPerComponent))
            if imNumComponents == 1:
                self.code_append('/Decode [0 1]')
            if imNumComponents == 3:
                self.code_append('/Decode [0 1 0 1 0 1]  %% decode color values normally')
            self.code.extend(['/ImageMatrix [%s 0 0 %s 0 %s]' % (imwidth, -imheight, imheight),
             '/DataSource currentfile /ASCIIHexDecode filter',
             '>> % End image dictionary',
             'image'])
            rawimage = myimage.tostring()
            hex_encoded = self._AsciiHexEncode(rawimage)
            outstream = getStringIO(hex_encoded)
            dataline = outstream.read(78)
            while dataline != '':
                self.code_append(dataline)
                dataline = outstream.read(78)

        self.code_append('> % end of image data')
        self.code_append('grestore')


from ..shapes import *

def draw(drawing, canvas, x=0, y=0, showBoundary=rl_config.showBoundary):
    """As it says"""
    R = _PSRenderer()
    R.draw(renderScaledDrawing(drawing), canvas, x, y, showBoundary=showBoundary)


def _pointsFromList(L):
    """
    given a list of coordinates [x0, y0, x1, y1....]
    produce a list of points [(x0,y0), (y1,y0),....]
    """
    P = []
    a = P.append
    for i in xrange(0, len(L), 2):
        a((L[i], L[i + 1]))

    return P


class _PSRenderer(Renderer):
    """This draws onto a EPS document.  It needs to be a class
    rather than a function, as some EPS-specific state tracking is
    needed outside of the state info in the SVG model."""

    def __init__(self):
        self._tracker = StateTracker()

    def drawNode(self, node):
        """This is the recursive method called for each node
        in the tree"""
        self._canvas.comment('begin node %r' % node)
        color = self._canvas._color
        if not (isinstance(node, Path) and node.isClipPath):
            self._canvas.saveState()
        deltas = getStateDelta(node)
        self._tracker.push(deltas)
        self.applyStateChanges(deltas, {})
        self.drawNodeDispatcher(node)
        rDeltas = self._tracker.pop()
        if not (isinstance(node, Path) and node.isClipPath):
            self._canvas.restoreState()
        self._canvas.comment('end node %r' % node)
        self._canvas._color = color
        for k, v in rDeltas.items():
            if k in self._restores:
                setattr(self._canvas, self._restores[k], v)

    _restores = {'strokeColor': '_strokeColor', 'strokeWidth': '_lineWidth', 'strokeLineCap': '_lineCap', 'strokeLineJoin': '_lineJoin', 
       'fillColor': '_fillColor', 'fontName': '_font', 'fontSize': '_fontSize'}

    def drawRect(self, rect):
        if rect.rx == rect.ry == 0:
            self._canvas.rect(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height)
        else:
            self._canvas.roundRect(rect.x, rect.y, rect.x + rect.width, rect.y + rect.height, rect.rx, rect.ry)

    def drawLine(self, line):
        if self._canvas._strokeColor:
            self._canvas.line(line.x1, line.y1, line.x2, line.y2)

    def drawCircle(self, circle):
        self._canvas.circle(circle.cx, circle.cy, circle.r)

    def drawWedge(self, wedge):
        yradius, radius1, yradius1 = wedge._xtraRadii()
        if (radius1 == 0 or radius1 is None) and (yradius1 == 0 or yradius1 is None):
            startangledegrees = wedge.startangledegrees
            endangledegrees = wedge.endangledegrees
            centerx = wedge.centerx
            centery = wedge.centery
            radius = wedge.radius
            extent = endangledegrees - startangledegrees
            self._canvas.drawArc(centerx - radius, centery - yradius, centerx + radius, centery + yradius, startangledegrees, extent, fromcenter=1)
        else:
            self.drawPolygon(wedge.asPolygon())
        return

    def drawPolyLine(self, p):
        if self._canvas._strokeColor:
            self._canvas.polyLine(_pointsFromList(p.points))

    def drawEllipse(self, ellipse):
        x1 = ellipse.cx - ellipse.rx
        x2 = ellipse.cx + ellipse.rx
        y1 = ellipse.cy - ellipse.ry
        y2 = ellipse.cy + ellipse.ry
        self._canvas.ellipse(x1, y1, x2, y2)

    def drawPolygon(self, p):
        self._canvas.polygon(_pointsFromList(p.points), closed=1)

    def drawString(self, stringObj):
        if self._canvas._fillColor:
            S = self._tracker.getState()
            text_anchor, x, y, text = (S['textAnchor'], stringObj.x, stringObj.y, stringObj.text)
            if text_anchor not in ('start', 'inherited'):
                font, fontSize = S['fontName'], S['fontSize']
                textLen = stringWidth(text, font, fontSize)
                if text_anchor == 'end':
                    x -= textLen
                elif text_anchor == 'middle':
                    x -= textLen / 2
                else:
                    if text_anchor == 'numeric':
                        x -= numericXShift(text_anchor, text, textLen, font, fontSize, encoding='winansi')
                    else:
                        raise ValueError, 'bad value for text_anchor ' + str(text_anchor)
            self._canvas.drawString(x, y, text)

    def drawPath(self, path):
        from reportlab.graphics.shapes import _renderPath
        c = self._canvas
        drawFuncs = (c.moveTo, c.lineTo, c.curveTo, c.closePath)
        isClosed = _renderPath(path, drawFuncs)
        if not isClosed:
            c._fillColor = None
        c._fillAndStroke([], clip=path.isClipPath)
        return

    def applyStateChanges(self, delta, newState):
        """This takes a set of states, and outputs the operators
        needed to set those properties"""
        for key, value in delta.items():
            if key == 'transform':
                self._canvas.transform(value[0], value[1], value[2], value[3], value[4], value[5])
            elif key == 'strokeColor':
                self._canvas.setStrokeColor(value)
            elif key == 'strokeWidth':
                self._canvas.setLineWidth(value)
            elif key == 'strokeLineCap':
                self._canvas.setLineCap(value)
            elif key == 'strokeLineJoin':
                self._canvas.setLineJoin(value)
            elif key == 'strokeDashArray':
                if value:
                    if isinstance(value, (list, tuple)) and len(value) == 2 and isinstance(value[1], (tuple, list)):
                        phase = value[0]
                        value = value[1]
                    else:
                        phase = 0
                    self._canvas.setDash(value, phase)
                else:
                    self._canvas.setDash()
            elif key == 'fillColor':
                self._canvas.setFillColor(value)
            elif key in ('fontSize', 'fontName'):
                fontname = delta.get('fontName', self._canvas._font)
                fontsize = delta.get('fontSize', self._canvas._fontSize)
                self._canvas.setFont(fontname, fontsize)

    def drawImage(self, image):
        from reportlab.lib.utils import ImageReader
        im = ImageReader(image.path)
        x0 = image.x
        y0 = image.y
        x1 = image.width
        if x1 is not None:
            x1 += x0
        y1 = image.height
        if y1 is not None:
            y1 += y0
        self._canvas.drawImage(im._image, x0, y0, x1, y1)
        return


def drawToFile(d, fn, showBoundary=rl_config.showBoundary, **kwd):
    d = renderScaledDrawing(d)
    c = PSCanvas((d.width, d.height))
    draw(d, c, 0, 0, showBoundary=showBoundary)
    c.save(fn)


def drawToString(d, showBoundary=rl_config.showBoundary):
    """Returns a PS as a string in memory, without touching the disk"""
    s = getStringIO()
    drawToFile(d, s, showBoundary=showBoundary)
    return s.getvalue()


def test(outdir='epsout'):
    import os
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    import testshapes
    drawings = []
    for funcname in dir(testshapes):
        if funcname[0:10] == 'getDrawing':
            drawing = eval('testshapes.' + funcname + '()')
            docstring = eval('testshapes.' + funcname + '.__doc__')
            drawings.append((drawing, docstring))

    i = 0
    for d, docstring in drawings:
        filename = outdir + os.sep + 'renderPS_%d.eps' % i
        drawToFile(d, filename)
        print 'saved', filename
        i = i + 1


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        outdir = sys.argv[1]
    else:
        outdir = 'epsout'
    test(outdir)