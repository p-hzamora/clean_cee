# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\lib\colors.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = "Defines standard colour-handling classes and colour names.\n\nWe define standard classes to hold colours in two models:  RGB and CMYK.\nThese can be constructed from several popular formats.  We also include\n\n- pre-built colour objects for the HTML standard colours\n\n- pre-built colours used in ReportLab's branding\n\n- various conversion and construction functions\n\nThese tests are here because doctest cannot find them otherwise.\n>>> toColor('rgb(128,0,0)')==toColor('rgb(50%,0%,0%)')\nTrue\n>>> toColor('rgb(50%,0%,0%)')!=Color(0.5,0,0,1)\nTrue\n>>> toColor('hsl(0,100%,50%)')==toColor('rgb(255,0,0)')\nTrue\n>>> toColor('hsl(-120,100%,50%)')==toColor('rgb(0,0,255)')\nTrue\n>>> toColor('hsl(120,100%,50%)')==toColor('rgb(0,255,0)')\nTrue\n>>> toColor('rgba( 255,0,0,0.5)')==Color(1,0,0,0.5)\nTrue\n>>> toColor('cmyk(1,0,0,0 )')==CMYKColor(1,0,0,0)\nTrue\n>>> toColor('pcmyk( 100 , 0 , 0 , 0 )')==PCMYKColor(100,0,0,0)\nTrue\n>>> toColor('cmyka(1,0,0,0,0.5)')==CMYKColor(1,0,0,0,alpha=0.5)\nTrue\n>>> toColor('pcmyka(100,0,0,0,0.5)')==PCMYKColor(100,0,0,0,alpha=0.5)\nTrue\n>>> toColor('pcmyka(100,0,0,0)')\nTraceback (most recent call last):\n    ....\nValueError: css color 'pcmyka(100,0,0,0)' has wrong number of components\n"
import math, re
from reportlab.lib.utils import fp_str

class Color:
    """This class is used to represent color.  Components red, green, blue
    are in the range 0 (dark) to 1 (full intensity)."""

    def __init__(self, red=0, green=0, blue=0, alpha=1):
        """Initialize with red, green, blue in range [0-1]."""
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __repr__(self):
        return 'Color(%s)' % fp_str(*(self.red, self.green, self.blue, self.alpha)).replace(' ', ',')

    def __hash__(self):
        return hash((self.red, self.green, self.blue, self.alpha))

    def __cmp__(self, other):
        """simple comparison by component; cmyk != color ever
        >>> cmp(Color(0,0,0),None)
        -1
        >>> cmp(Color(0,0,0),black)
        0
        >>> cmp(Color(0,0,0),CMYKColor(0,0,0,1)),Color(0,0,0).rgba()==CMYKColor(0,0,0,1).rgba()
        (-1, True)
        """
        if isinstance(other, CMYKColor) or not isinstance(other, Color):
            return -1
        try:
            return cmp((self.red, self.green, self.blue, self.alpha), (
             other.red, other.green, other.blue, other.alpha))
        except:
            return -1

        return 0

    def rgb(self):
        """Returns a three-tuple of components"""
        return (
         self.red, self.green, self.blue)

    def rgba(self):
        """Returns a four-tuple of components"""
        return (
         self.red, self.green, self.blue, self.alpha)

    def bitmap_rgb(self):
        return tuple(map((lambda x: int(x * 255) & 255), self.rgb()))

    def bitmap_rgba(self):
        return tuple(map((lambda x: int(x * 255) & 255), self.rgba()))

    def hexval(self):
        return '0x%02x%02x%02x' % self.bitmap_rgb()

    def hexvala(self):
        return '0x%02x%02x%02x%02x' % self.bitmap_rgba()

    def int_rgb(self):
        v = self.bitmap_rgb()
        return v[0] << 16 | v[1] << 8 | v[2]

    def int_rgba(self):
        v = self.bitmap_rgba()
        return int((v[0] << 24 | v[1] << 16 | v[2] << 8 | v[3]) & 16777215)

    _cKwds = ('red green blue alpha').split()

    def cKwds(self):
        for k in self._cKwds:
            yield (
             k, getattr(self, k))

    cKwds = property(cKwds)

    def clone(self, **kwds):
        """copy then change values in kwds"""
        D = dict([ kv for kv in self.cKwds ])
        D.update(kwds)
        return self.__class__(**D)

    def _lookupName(self, D={}):
        if not D:
            for n, v in getAllNamedColors().iteritems():
                if not isinstance(v, CMYKColor):
                    t = (
                     v.red, v.green, v.blue)
                    if t in D:
                        n = n + '/' + D[t]
                    D[t] = n

        t = (
         self.red, self.green, self.blue)
        return t in D and D[t] or None

    @property
    def normalizedAlpha(self):
        return self.alpha


class CMYKColor(Color):
    """This represents colors using the CMYK (cyan, magenta, yellow, black)
    model commonly used in professional printing.  This is implemented
    as a derived class so that renderers which only know about RGB "see it"
    as an RGB color through its 'red','green' and 'blue' attributes, according
    to an approximate function.

    The RGB approximation is worked out when the object in constructed, so
    the color attributes should not be changed afterwards.

    Extra attributes may be attached to the class to support specific ink models,
    and renderers may look for these."""
    _scale = 1.0

    def __init__(self, cyan=0, magenta=0, yellow=0, black=0, spotName=None, density=1, knockout=None, alpha=1):
        """
        Initialize with four colors in range [0-1]. the optional
        spotName, density & knockout may be of use to specific renderers.
        spotName is intended for use as an identifier to the renderer not client programs.
        density is used to modify the overall amount of ink.
        knockout is a renderer dependent option that determines whether the applied colour
        knocksout (removes) existing colour; None means use the global default.
        """
        self.cyan = cyan
        self.magenta = magenta
        self.yellow = yellow
        self.black = black
        self.spotName = spotName
        self.density = max(min(density, 1), 0)
        self.knockout = knockout
        self.alpha = alpha
        self.red, self.green, self.blue = cmyk2rgb((cyan, magenta, yellow, black))
        if density < 1:
            r, g, b = self.red, self.green, self.blue
            r = density * (r - 1) + 1
            g = density * (g - 1) + 1
            b = density * (b - 1) + 1
            self.red, self.green, self.blue = r, g, b

    def __repr__(self):
        return '%s(%s%s%s%s%s)' % (self.__class__.__name__,
         fp_str(self.cyan, self.magenta, self.yellow, self.black).replace(' ', ','),
         self.spotName and ',spotName=' + repr(self.spotName) or '',
         self.density != 1 and ',density=' + fp_str(self.density) or '',
         self.knockout is not None and ',knockout=%d' % self.knockout or '',
         self.alpha is not None and ',alpha=%s' % self.alpha or '')

    def fader(self, n, reverse=False):
        """return n colors based on density fade
        *NB* note this dosen't reach density zero"""
        scale = self._scale
        dd = scale / float(n)
        L = [ self.clone(density=scale - i * dd) for i in xrange(n) ]
        if reverse:
            L.reverse()
        return L

    def __hash__(self):
        return hash((self.cyan, self.magenta, self.yellow, self.black, self.density, self.spotName, self.alpha))

    def __cmp__(self, other):
        """obvious way to compare colours
        Comparing across the two color models is of limited use.
        >>> cmp(CMYKColor(0,0,0,1),None)
        -1
        >>> cmp(CMYKColor(0,0,0,1),_CMYK_black)
        0
        >>> cmp(PCMYKColor(0,0,0,100),_CMYK_black)
        0
        >>> cmp(CMYKColor(0,0,0,1),Color(0,0,1)),Color(0,0,0).rgba()==CMYKColor(0,0,0,1).rgba()
        (-1, True)
        """
        if not isinstance(other, CMYKColor):
            return -1
        try:
            return cmp((
             self.cyan, self.magenta, self.yellow, self.black, self.density, self.alpha, self.spotName), (
             other.cyan, other.magenta, other.yellow, other.black, other.density, other.alpha, other.spotName))
        except:
            return -1

        return 0

    def cmyk(self):
        """Returns a tuple of four color components - syntactic sugar"""
        return (
         self.cyan, self.magenta, self.yellow, self.black)

    def cmyka(self):
        """Returns a tuple of five color components - syntactic sugar"""
        return (
         self.cyan, self.magenta, self.yellow, self.black, self.alpha)

    def _density_str(self):
        return fp_str(self.density)

    _cKwds = ('cyan magenta yellow black density alpha spotName knockout').split()

    def _lookupName(self, D={}):
        if not D:
            for n, v in getAllNamedColors().iteritems():
                if isinstance(v, CMYKColor):
                    t = (
                     v.cyan, v.magenta, v.yellow, v.black)
                    if t in D:
                        n = n + '/' + D[t]
                    D[t] = n

        t = (
         self.cyan, self.magenta, self.yellow, self.black)
        return t in D and D[t] or None

    @property
    def normalizedAlpha(self):
        return self.alpha * self._scale


class PCMYKColor(CMYKColor):
    """100 based CMYKColor with density and a spotName; just like Rimas uses"""
    _scale = 100.0

    def __init__(self, cyan, magenta, yellow, black, density=100, spotName=None, knockout=None, alpha=100):
        CMYKColor.__init__(self, cyan / 100.0, magenta / 100.0, yellow / 100.0, black / 100.0, spotName, density / 100.0, knockout=knockout, alpha=alpha / 100.0)

    def __repr__(self):
        return '%s(%s%s%s%s%s)' % (self.__class__.__name__,
         fp_str(self.cyan * 100, self.magenta * 100, self.yellow * 100, self.black * 100).replace(' ', ','),
         self.spotName and ',spotName=' + repr(self.spotName) or '',
         self.density != 1 and ',density=' + fp_str(self.density * 100) or '',
         self.knockout is not None and ',knockout=%d' % self.knockout or '',
         self.alpha is not None and ',alpha=%s' % fp_str(self.alpha * 100) or '')

    def cKwds(self):
        K = self._cKwds
        S = K[:6]
        for k in self._cKwds:
            v = getattr(self, k)
            if k in S:
                v *= 100
            yield (
             k, v)

    cKwds = property(cKwds)


class CMYKColorSep(CMYKColor):
    """special case color for making separating pdfs"""
    _scale = 1.0

    def __init__(self, cyan=0, magenta=0, yellow=0, black=0, spotName=None, density=1, alpha=1):
        CMYKColor.__init__(self, cyan, magenta, yellow, black, spotName, density, knockout=None, alpha=alpha)
        return

    _cKwds = ('cyan magenta yellow black density alpha spotName').split()


class PCMYKColorSep(PCMYKColor, CMYKColorSep):
    """special case color for making separating pdfs"""
    _scale = 100.0

    def __init__(self, cyan=0, magenta=0, yellow=0, black=0, spotName=None, density=100, alpha=100):
        PCMYKColor.__init__(self, cyan, magenta, yellow, black, density, spotName, knockout=None, alpha=alpha)
        return

    _cKwds = ('cyan magenta yellow black density alpha spotName').split()


def cmyk2rgb(cmyk, density=1):
    """Convert from a CMYK color tuple to an RGB color tuple"""
    c, m, y, k = cmyk
    r = 1.0 - min(1.0, c + k)
    g = 1.0 - min(1.0, m + k)
    b = 1.0 - min(1.0, y + k)
    return (r, g, b)


def rgb2cmyk(r, g, b):
    """one way to get cmyk from rgb"""
    c = 1 - r
    m = 1 - g
    y = 1 - b
    k = min(c, m, y)
    c = min(1, max(0, c - k))
    m = min(1, max(0, m - k))
    y = min(1, max(0, y - k))
    k = min(1, max(0, k))
    return (c, m, y, k)


def color2bw(colorRGB):
    """Transform an RGB color to a black and white equivalent."""
    col = colorRGB
    r, g, b, a = (col.red, col.green, col.blue, col.alpha)
    n = (r + g + b) / 3.0
    bwColorRGB = Color(n, n, n, a)
    return bwColorRGB


def HexColor(val, htmlOnly=False, hasAlpha=False):
    """This function converts a hex string, or an actual integer number,
    into the corresponding color.  E.g., in "#AABBCC" or 0xAABBCC,
    AA is the red, BB is the green, and CC is the blue (00-FF).

    An alpha value can also be given in the form #AABBCCDD or 0xAABBCCDD where
    DD is the alpha value if hasAlpha is True.

    For completeness I assume that #aabbcc or 0xaabbcc are hex numbers
    otherwise a pure integer is converted as decimal rgb.  If htmlOnly is true,
    only the #aabbcc form is allowed.

    >>> HexColor('#ffffff')
    Color(1,1,1,1)
    >>> HexColor('#FFFFFF')
    Color(1,1,1,1)
    >>> HexColor('0xffffff')
    Color(1,1,1,1)
    >>> HexColor('16777215')
    Color(1,1,1,1)

    An '0x' or '#' prefix is required for hex (as opposed to decimal):

    >>> HexColor('ffffff')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'ffffff'

    >>> HexColor('#FFFFFF', htmlOnly=True)
    Color(1,1,1,1)
    >>> HexColor('0xffffff', htmlOnly=True)
    Traceback (most recent call last):
    ValueError: not a hex string
    >>> HexColor('16777215', htmlOnly=True)
    Traceback (most recent call last):
    ValueError: not a hex string

    """
    if isinstance(val, basestring):
        b = 10
        if val[:1] == '#':
            val = val[1:]
            b = 16
            if len(val) == 8:
                alpha = True
        else:
            if htmlOnly:
                raise ValueError('not a hex string')
            if val[:2].lower() == '0x':
                b = 16
                val = val[2:]
                if len(val) == 8:
                    alpha = True
        val = int(val, b)
    if hasAlpha:
        return Color((val >> 24 & 255) / 255.0, (val >> 16 & 255) / 255.0, (val >> 8 & 255) / 255.0, (val & 255) / 255.0)
    return Color((val >> 16 & 255) / 255.0, (val >> 8 & 255) / 255.0, (val & 255) / 255.0)


def linearlyInterpolatedColor(c0, c1, x0, x1, x):
    """
    Linearly interpolates colors. Can handle RGB, CMYK and PCMYK
    colors - give ValueError if colours aren't the same.
    Doesn't currently handle 'Spot Color Interpolation'.
    """
    if c0.__class__ != c1.__class__:
        raise ValueError("Color classes must be the same for interpolation!\nGot %r and %r'" % (c0, c1))
    if x1 < x0:
        x0, x1, c0, c1 = (
         x1, x0, c1, c0)
    if x < x0 - 1e-08 or x > x1 + 1e-08:
        raise ValueError, "Can't interpolate: x=%f is not between %f and %f!" % (x, x0, x1)
    if x <= x0:
        return c0
    if x >= x1:
        return c1
    cname = c0.__class__.__name__
    dx = float(x1 - x0)
    x = x - x0
    if cname == 'Color':
        r = c0.red + x * (c1.red - c0.red) / dx
        g = c0.green + x * (c1.green - c0.green) / dx
        b = c0.blue + x * (c1.blue - c0.blue) / dx
        a = c0.alpha + x * (c1.alpha - c0.alpha) / dx
        return Color(r, g, b, alpha=a)
    if cname == 'CMYKColor':
        if cmykDistance(c0, c1) < 1e-08:
            assert c0.spotName == c1.spotName, 'Identical cmyk, but different spotName'
            c = c0.cyan
            m = c0.magenta
            y = c0.yellow
            k = c0.black
            d = c0.density + x * (c1.density - c0.density) / dx
            a = c0.alpha + x * (c1.alpha - c0.alpha) / dx
            return CMYKColor(c, m, y, k, density=d, spotName=c0.spotName, alpha=a)
        else:
            if cmykDistance(c0, _CMYK_white) < 1e-08:
                c = c1.cyan
                m = c1.magenta
                y = c1.yellow
                k = c1.black
                d = x * c1.density / dx
                a = x * c1.alpha / dx
                return CMYKColor(c, m, y, k, density=d, spotName=c1.spotName, alpha=a)
            if cmykDistance(c1, _CMYK_white) < 1e-08:
                c = c0.cyan
                m = c0.magenta
                y = c0.yellow
                k = c0.black
                d = x * c0.density / dx
                d = c0.density * (1 - x / dx)
                a = c0.alpha * (1 - x / dx)
                return PCMYKColor(c, m, y, k, density=d, spotName=c0.spotName, alpha=a)
            c = c0.cyan + x * (c1.cyan - c0.cyan) / dx
            m = c0.magenta + x * (c1.magenta - c0.magenta) / dx
            y = c0.yellow + x * (c1.yellow - c0.yellow) / dx
            k = c0.black + x * (c1.black - c0.black) / dx
            d = c0.density + x * (c1.density - c0.density) / dx
            a = c0.alpha + x * (c1.alpha - c0.alpha) / dx
            return CMYKColor(c, m, y, k, density=d, alpha=a)

    elif cname == 'PCMYKColor':
        if cmykDistance(c0, c1) < 1e-08:
            assert c0.spotName == c1.spotName, 'Identical cmyk, but different spotName'
            c = c0.cyan
            m = c0.magenta
            y = c0.yellow
            k = c0.black
            d = c0.density + x * (c1.density - c0.density) / dx
            a = c0.alpha + x * (c1.alpha - c0.alpha) / dx
            return PCMYKColor(c * 100, m * 100, y * 100, k * 100, density=d * 100, spotName=c0.spotName, alpha=100 * a)
        else:
            if cmykDistance(c0, _CMYK_white) < 1e-08:
                c = c1.cyan
                m = c1.magenta
                y = c1.yellow
                k = c1.black
                d = x * c1.density / dx
                a = x * c1.alpha / dx
                return PCMYKColor(c * 100, m * 100, y * 100, k * 100, density=d * 100, spotName=c1.spotName, alpha=a * 100)
            if cmykDistance(c1, _CMYK_white) < 1e-08:
                c = c0.cyan
                m = c0.magenta
                y = c0.yellow
                k = c0.black
                d = x * c0.density / dx
                d = c0.density * (1 - x / dx)
                a = c0.alpha * (1 - x / dx)
                return PCMYKColor(c * 100, m * 100, y * 100, k * 100, density=d * 100, spotName=c0.spotName, alpha=a * 100)
            c = c0.cyan + x * (c1.cyan - c0.cyan) / dx
            m = c0.magenta + x * (c1.magenta - c0.magenta) / dx
            y = c0.yellow + x * (c1.yellow - c0.yellow) / dx
            k = c0.black + x * (c1.black - c0.black) / dx
            d = c0.density + x * (c1.density - c0.density) / dx
            a = c0.alpha + x * (c1.alpha - c0.alpha) / dx
            return PCMYKColor(c * 100, m * 100, y * 100, k * 100, density=d * 100, alpha=a * 100)

    else:
        raise ValueError, "Can't interpolate: Unknown color class %s!" % cname


def obj_R_G_B(c):
    """attempt to convert an object to (red,green,blue)"""
    if isinstance(c, Color):
        return (c.red, c.green, c.blue)
    if isinstance(c, (tuple, list)):
        if len(c) == 3:
            return tuple(c)
        if len(c) == 4:
            return toColor(c).rgb()
        raise ValueError('obj_R_G_B(%r) bad argument' % c)


transparent = Color(0, 0, 0, alpha=0)
_CMYK_white = CMYKColor(0, 0, 0, 0)
_PCMYK_white = PCMYKColor(0, 0, 0, 0)
_CMYK_black = CMYKColor(0, 0, 0, 1)
_PCMYK_black = PCMYKColor(0, 0, 0, 100)
ReportLabBlueOLD = HexColor(5133960)
ReportLabBlue = HexColor(13183)
ReportLabBluePCMYK = PCMYKColor(100, 65, 0, 30, spotName='Pantone 288U')
ReportLabLightBlue = HexColor(12040659)
ReportLabFidBlue = HexColor(3368652)
ReportLabFidRed = HexColor(13369395)
ReportLabGreen = HexColor(3368448)
ReportLabLightGreen = HexColor(3381555)
aliceblue = HexColor(15792383)
antiquewhite = HexColor(16444375)
aqua = HexColor(65535)
aquamarine = HexColor(8388564)
azure = HexColor(15794175)
beige = HexColor(16119260)
bisque = HexColor(16770244)
black = HexColor(0)
blanchedalmond = HexColor(16772045)
blue = HexColor(255)
blueviolet = HexColor(9055202)
brown = HexColor(10824234)
burlywood = HexColor(14596231)
cadetblue = HexColor(6266528)
chartreuse = HexColor(8388352)
chocolate = HexColor(13789470)
coral = HexColor(16744272)
cornflowerblue = cornflower = HexColor(6591981)
cornsilk = HexColor(16775388)
crimson = HexColor(14423100)
cyan = HexColor(65535)
darkblue = HexColor(139)
darkcyan = HexColor(35723)
darkgoldenrod = HexColor(12092939)
darkgray = HexColor(11119017)
darkgrey = darkgray
darkgreen = HexColor(25600)
darkkhaki = HexColor(12433259)
darkmagenta = HexColor(9109643)
darkolivegreen = HexColor(5597999)
darkorange = HexColor(16747520)
darkorchid = HexColor(10040012)
darkred = HexColor(9109504)
darksalmon = HexColor(15308410)
darkseagreen = HexColor(9419915)
darkslateblue = HexColor(4734347)
darkslategray = HexColor(3100495)
darkslategrey = darkslategray
darkturquoise = HexColor(52945)
darkviolet = HexColor(9699539)
deeppink = HexColor(16716947)
deepskyblue = HexColor(49151)
dimgray = HexColor(6908265)
dimgrey = dimgray
dodgerblue = HexColor(2003199)
firebrick = HexColor(11674146)
floralwhite = HexColor(16775920)
forestgreen = HexColor(2263842)
fuchsia = HexColor(16711935)
gainsboro = HexColor(14474460)
ghostwhite = HexColor(16316671)
gold = HexColor(16766720)
goldenrod = HexColor(14329120)
gray = HexColor(8421504)
grey = gray
green = HexColor(32768)
greenyellow = HexColor(11403055)
honeydew = HexColor(15794160)
hotpink = HexColor(16738740)
indianred = HexColor(13458524)
indigo = HexColor(4915330)
ivory = HexColor(16777200)
khaki = HexColor(15787660)
lavender = HexColor(15132410)
lavenderblush = HexColor(16773365)
lawngreen = HexColor(8190976)
lemonchiffon = HexColor(16775885)
lightblue = HexColor(11393254)
lightcoral = HexColor(15761536)
lightcyan = HexColor(14745599)
lightgoldenrodyellow = HexColor(16448210)
lightgreen = HexColor(9498256)
lightgrey = HexColor(13882323)
lightpink = HexColor(16758465)
lightsalmon = HexColor(16752762)
lightseagreen = HexColor(2142890)
lightskyblue = HexColor(8900346)
lightslategray = HexColor(7833753)
lightslategrey = lightslategray
lightsteelblue = HexColor(11584734)
lightyellow = HexColor(16777184)
lime = HexColor(65280)
limegreen = HexColor(3329330)
linen = HexColor(16445670)
magenta = HexColor(16711935)
maroon = HexColor(8388608)
mediumaquamarine = HexColor(6737322)
mediumblue = HexColor(205)
mediumorchid = HexColor(12211667)
mediumpurple = HexColor(9662683)
mediumseagreen = HexColor(3978097)
mediumslateblue = HexColor(8087790)
mediumspringgreen = HexColor(64154)
mediumturquoise = HexColor(4772300)
mediumvioletred = HexColor(13047173)
midnightblue = HexColor(1644912)
mintcream = HexColor(16121850)
mistyrose = HexColor(16770273)
moccasin = HexColor(16770229)
navajowhite = HexColor(16768685)
navy = HexColor(128)
oldlace = HexColor(16643558)
olive = HexColor(8421376)
olivedrab = HexColor(7048739)
orange = HexColor(16753920)
orangered = HexColor(16729344)
orchid = HexColor(14315734)
palegoldenrod = HexColor(15657130)
palegreen = HexColor(10025880)
paleturquoise = HexColor(11529966)
palevioletred = HexColor(14381203)
papayawhip = HexColor(16773077)
peachpuff = HexColor(16767673)
peru = HexColor(13468991)
pink = HexColor(16761035)
plum = HexColor(14524637)
powderblue = HexColor(11591910)
purple = HexColor(8388736)
red = HexColor(16711680)
rosybrown = HexColor(12357519)
royalblue = HexColor(4286945)
saddlebrown = HexColor(9127187)
salmon = HexColor(16416882)
sandybrown = HexColor(16032864)
seagreen = HexColor(3050327)
seashell = HexColor(16774638)
sienna = HexColor(10506797)
silver = HexColor(12632256)
skyblue = HexColor(8900331)
slateblue = HexColor(6970061)
slategray = HexColor(7372944)
slategrey = slategray
snow = HexColor(16775930)
springgreen = HexColor(65407)
steelblue = HexColor(4620980)
tan = HexColor(13808780)
teal = HexColor(32896)
thistle = HexColor(14204888)
tomato = HexColor(16737095)
turquoise = HexColor(4251856)
violet = HexColor(15631086)
wheat = HexColor(16113331)
white = HexColor(16777215)
whitesmoke = HexColor(16119285)
yellow = HexColor(16776960)
yellowgreen = HexColor(10145074)
fidblue = HexColor(3368652)
fidred = HexColor(13369395)
fidlightblue = HexColor('#d6e0f5')
ColorType = type(black)

def colorDistance(col1, col2):
    """Returns a number between 0 and root(3) stating how similar
    two colours are - distance in r,g,b, space.  Only used to find
    names for things."""
    return math.sqrt((col1.red - col2.red) ** 2 + (col1.green - col2.green) ** 2 + (col1.blue - col2.blue) ** 2)


def cmykDistance(col1, col2):
    """Returns a number between 0 and root(4) stating how similar
    two colours are - distance in r,g,b, space.  Only used to find
    names for things."""
    return math.sqrt((col1.cyan - col2.cyan) ** 2 + (col1.magenta - col2.magenta) ** 2 + (col1.yellow - col2.yellow) ** 2 + (col1.black - col2.black) ** 2)


_namedColors = None

def getAllNamedColors():
    global _namedColors
    if _namedColors is not None:
        return _namedColors
    else:
        import colors
        _namedColors = {}
        for name, value in colors.__dict__.items():
            if isinstance(value, Color):
                _namedColors[name] = value

        return _namedColors


def describe(aColor, mode=0):
    """finds nearest colour match to aColor.
    mode=0 print a string desription
    mode=1 return a string description
    mode=2 return (distance, colorName)
    """
    namedColors = getAllNamedColors()
    closest = (10, None, None)
    for name, color in namedColors.items():
        distance = colorDistance(aColor, color)
        if distance < closest[0]:
            closest = (
             distance, name, color)

    if mode <= 1:
        s = 'best match is %s, distance %0.4f' % (closest[1], closest[0])
        if mode == 0:
            print s
        else:
            return s
    else:
        if mode == 2:
            return (closest[1], closest[0])
        raise ValueError, 'Illegal value for mode ' + str(mode)
    return


def hue2rgb(m1, m2, h):
    if h < 0:
        h += 1
    if h > 1:
        h -= 1
    if h * 6 < 1:
        return m1 + (m2 - m1) * h * 6
    if h * 2 < 1:
        return m2
    if h * 3 < 2:
        return m1 + (m2 - m1) * (4 - 6 * h)
    return m1


def hsl2rgb(h, s, l):
    if l <= 0.5:
        m2 = l * (s + 1)
    else:
        m2 = l + s - l * s
    m1 = l * 2 - m2
    return (hue2rgb(m1, m2, h + 1.0 / 3), hue2rgb(m1, m2, h), hue2rgb(m1, m2, h - 1.0 / 3))


import re
_re_css = re.compile('^\\s*(pcmyk|cmyk|rgb|hsl)(a|)\\s*\\(\\s*([^)]*)\\)\\s*$')

class cssParse:

    def pcVal(self, v):
        v = v.strip()
        try:
            c = eval(v[:-1])
            if not isinstance(c, (float, int)):
                raise ValueError
            c = min(100, max(0, c)) / 100.0
        except:
            raise ValueError('bad percentage argument value %r in css color %r' % (v, self.s))

        return c

    def rgbPcVal(self, v):
        return int(self.pcVal(v) * 255 + 0.5) / 255.0

    def rgbVal(self, v):
        v = v.strip()
        try:
            c = eval(v[:])
            if not isinstance(c, int):
                raise ValueError
            return int(min(255, max(0, c))) / 255.0
        except:
            raise ValueError('bad argument value %r in css color %r' % (v, self.s))

    def hueVal(self, v):
        v = v.strip()
        try:
            c = eval(v[:])
            if not isinstance(c, (int, float)):
                raise ValueError
            return (c % 360 + 360) % 360 / 360.0
        except:
            raise ValueError('bad hue argument value %r in css color %r' % (v, self.s))

    def alphaVal(self, v, c=1, n='alpha'):
        try:
            a = eval(v.strip())
            if not isinstance(a, (int, float)):
                raise ValueError
            return min(c, max(0, a))
        except:
            raise ValueError('bad %s argument value %r in css color %r' % (n, v, self.s))

    _n_c = dict(pcmyk=(4, 100, True, False), cmyk=(4, 1, True, False), hsl=(3, 1, False, True), rgb=(3, 1, False, False))

    def __call__(self, s):
        n = _re_css.match(s)
        if not n:
            return
        else:
            self.s = s
            b, c, cmyk, hsl = self._n_c[n.group(1)]
            ha = n.group(2)
            n = n.group(3).split(',')
            if len(n) != b + (ha and 1 or 0):
                raise ValueError('css color %r has wrong number of components' % s)
            if ha:
                n, a = n[:b], self.alphaVal(n[b], c)
            else:
                a = c
            if cmyk:
                C = self.alphaVal(n[0], c, 'cyan')
                M = self.alphaVal(n[1], c, 'magenta')
                Y = self.alphaVal(n[2], c, 'yellow')
                K = self.alphaVal(n[3], c, 'black')
                return (c > 1 and PCMYKColor or CMYKColor)(C, M, Y, K, alpha=a)
            if hsl:
                R, G, B = hsl2rgb(self.hueVal(n[0]), self.pcVal(n[1]), self.pcVal(n[2]))
            else:
                R, G, B = map('%' in n[0] and self.rgbPcVal or self.rgbVal, n)
            return Color(R, G, B, a)


cssParse = cssParse()

class toColor:

    def __init__(self):
        self.extraColorsNS = {}

    def setExtraColorsNameSpace(self, NS):
        self.extraColorsNS = NS

    def __call__(self, arg, default=None):
        """try to map an arbitrary arg to a color instance
        """
        if isinstance(arg, Color):
            return arg
        else:
            assert isinstance(arg, (tuple, list)) and 3 <= len(arg) <= 4, 'Can only convert 3 and 4 sequences to color'
            if not (0 <= min(arg) and max(arg) <= 1):
                raise AssertionError
                return len(arg) == 3 and Color(arg[0], arg[1], arg[2]) or CMYKColor(arg[0], arg[1], arg[2], arg[3])
            if isinstance(arg, basestring):
                C = cssParse(arg)
                if C:
                    return C
                if arg in self.extraColorsNS:
                    return self.extraColorsNS[arg]
                C = getAllNamedColors()
                s = arg.lower()
                if s in C:
                    return C[s]
                try:
                    return toColor(eval(arg))
                except:
                    pass

            try:
                return HexColor(arg)
            except:
                if default is None:
                    raise ValueError('Invalid color value %r' % arg)
                return default

            return


toColor = toColor()

def toColorOrNone(arg, default=None):
    """as above but allows None as a legal value"""
    if arg is None:
        return
    else:
        return toColor(arg, default)
        return


def setColors(**kw):
    UNDEF = []
    progress = 1
    assigned = {}
    while kw and progress:
        progress = 0
        for k, v in kw.items():
            if isinstance(v, (tuple, list)):
                c = map((lambda x, UNDEF=UNDEF: toColor(x, UNDEF)), v)
                if isinstance(v, tuple):
                    c = tuple(c)
                ok = UNDEF not in c
            else:
                c = toColor(v, UNDEF)
                ok = c is not UNDEF
            if ok:
                assigned[k] = c
                del kw[k]
                progress = 1

    if kw:
        raise ValueError("Can't convert\n%s" % str(kw))
    getAllNamedColors()
    for k, c in assigned.items():
        globals()[k] = c
        if isinstance(c, Color):
            _namedColors[k] = c


def Whiter(c, f):
    """given a color combine with white as c*f w*(1-f) 0<=f<=1"""
    c = toColor(c)
    if isinstance(c, CMYKColorSep):
        c = c.clone()
        if isinstance(c, PCMYKColorSep):
            c.__class__ = PCMYKColor
        else:
            c.__class__ = CMYKColor
    if isinstance(c, PCMYKColor):
        w = _PCMYK_white
    elif isinstance(c, CMYKColor):
        w = _CMYK_white
    else:
        w = white
    return linearlyInterpolatedColor(w, c, 0, 1, f)


def Blacker(c, f):
    """given a color combine with black as c*f+b*(1-f) 0<=f<=1"""
    c = toColor(c)
    if isinstance(c, CMYKColorSep):
        c = c.clone()
        if isinstance(c, PCMYKColorSep):
            c.__class__ = PCMYKColor
        else:
            c.__class__ = CMYKColor
    if isinstance(c, PCMYKColor):
        b = _PCMYK_black
    elif isinstance(c, CMYKColor):
        b = _CMYK_black
    else:
        b = black
    return linearlyInterpolatedColor(b, c, 0, 1, f)


def fade(aSpotColor, percentages):
    """Waters down spot colors and returns a list of new ones

    e.g fade(myColor, [100,80,60,40,20]) returns a list of five colors
    """
    out = []
    for percent in percentages:
        frac = percent * 0.01
        newCyan = frac * aSpotColor.cyan
        newMagenta = frac * aSpotColor.magenta
        newYellow = frac * aSpotColor.yellow
        newBlack = frac * aSpotColor.black
        newDensity = frac * aSpotColor.density
        newSpot = CMYKColor(newCyan, newMagenta, newYellow, newBlack, spotName=aSpotColor.spotName, density=newDensity)
        out.append(newSpot)

    return out


def _enforceError(kind, c, tc):
    if isinstance(tc, Color):
        xtra = tc._lookupName()
        xtra = xtra and '(%s)' % xtra or ''
    else:
        xtra = ''
    raise ValueError('Non %s color %r%s' % (kind, c, xtra))


def _enforceSEP(c):
    """pure separating colors only, this makes black a problem"""
    tc = toColor(c)
    if not isinstance(tc, CMYKColorSep):
        _enforceError('separating', c, tc)
    return tc


def _enforceSEP_BLACK(c):
    """separating + blacks only"""
    tc = toColor(c)
    if isinstance(tc, CMYKColorSep) or isinstance(tc, Color):
        if tc.red == tc.blue == tc.green:
            tc = _CMYK_black.clone(density=1 - tc.red)
        elif not (isinstance(tc, CMYKColor) and tc.cyan == tc.magenta == tc.yellow == 0):
            _enforceError('separating or black', c, tc)
    return tc


def _enforceSEP_CMYK(c):
    """separating or cmyk only"""
    tc = toColor(c)
    if isinstance(tc, CMYKColorSep) or isinstance(tc, Color):
        if tc.red == tc.blue == tc.green:
            tc = _CMYK_black.clone(density=1 - tc.red)
        elif not isinstance(tc, CMYKColor):
            _enforceError('separating or CMYK', c, tc)
    return tc


def _enforceCMYK(c):
    """cmyk outputs only (rgb greys converted)"""
    tc = toColor(c)
    if isinstance(tc, CMYKColor) or isinstance(tc, Color):
        if tc.red == tc.blue == tc.green:
            tc = _CMYK_black.clone(black=1 - tc.red, alpha=tc.alpha)
        else:
            _enforceError('CMYK', c, tc)
    elif isinstance(tc, CMYKColorSep):
        tc = tc.clone()
        tc.__class__ = CMYKColor
    return tc


def _enforceRGB(c):
    tc = toColor(c)
    if isinstance(tc, CMYKColor):
        if tc.cyan == tc.magenta == tc.yellow == 0:
            v = 1 - tc.black * tc.density
            tc = Color(v, v, v, alpha=tc.alpha)
        else:
            _enforceError('RGB', c, tc)
    return tc


def _chooseEnforceColorSpace(enforceColorSpace):
    if enforceColorSpace is not None and not callable(enforceColorSpace):
        if isinstance(enforceColorSpace, basestring):
            enforceColorSpace = enforceColorSpace.upper()
        if enforceColorSpace == 'CMYK':
            enforceColorSpace = _enforceCMYK
        else:
            if enforceColorSpace == 'RGB':
                enforceColorSpace = _enforceRGB
            elif enforceColorSpace == 'SEP':
                enforceColorSpace = _enforceSEP
        if enforceColorSpace == 'SEP_BLACK':
            enforceColorSpace = _enforceSEP_BLACK
        else:
            if enforceColorSpace == 'SEP_CMYK':
                enforceColorSpace = _enforceSEP_CMYK
            else:
                raise ValueError('Invalid value for Canvas argument enforceColorSpace=%r' % enforceColorSpace)
    return enforceColorSpace


if __name__ == '__main__':
    import doctest
    doctest.testmod()