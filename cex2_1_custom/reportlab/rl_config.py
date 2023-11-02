# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: reportlab\rl_config.pyc
# Compiled at: 2013-03-27 15:37:42
__version__ = ' $Id$ '
__doc__ = 'Configuration file.  You may edit this if you wish.'
allowTableBoundsErrors = 1
shapeChecking = 1
defaultEncoding = 'WinAnsiEncoding'
defaultGraphicsFontName = 'Times-Roman'
pageCompression = 1
useA85 = 1
defaultPageSize = 'A4'
defaultImageCaching = 0
ZLIB_WARNINGS = 1
warnOnMissingFontGlyphs = 0
verbose = 0
showBoundary = 0
emptyTableAction = 'error'
invariant = 0
eps_preview_transparent = None
eps_preview = 1
eps_ttf_embed = 1
eps_ttf_embed_uid = 0
overlapAttachedSpace = 1
longTableOptimize = 1
autoConvertEncoding = 0
_FUZZ = 1e-06
wrapA85 = 0
fsEncodings = ('utf8', 'cp1252', 'cp430')
odbc_driver = 'odbc'
platypus_link_underline = 0
canvas_basefontname = 'Helvetica'
allowShortTableRows = 1
imageReaderFlags = 0
paraFontSizeHeightOffset = 1
canvas_baseColor = None
ignoreContainerActions = 1
ttfAsciiReadable = 1
T1SearchPath = ('c:/Program Files/Adobe/Acrobat 9.0/Resource/Font', 'c:/Program Files/Adobe/Acrobat 8.0/Resource/Font',
                'c:/Program Files/Adobe/Acrobat 7.0/Resource/Font', 'c:/Program Files/Adobe/Acrobat 6.0/Resource/Font',
                'c:/Program Files/Adobe/Acrobat 5.0/Resource/Font', 'c:/Program Files/Adobe/Acrobat 4.0/Resource/Font',
                '%(disk)s/Applications/Python %(sys_version)s/reportlab/fonts', '/usr/lib/Acrobat9/Resource/Font',
                '/usr/lib/Acrobat8/Resource/Font', '/usr/lib/Acrobat7/Resource/Font',
                '/usr/lib/Acrobat6/Resource/Font', '/usr/lib/Acrobat5/Resource/Font',
                '/usr/lib/Acrobat4/Resource/Font', '/usr/local/Acrobat9/Resource/Font',
                '/usr/local/Acrobat8/Resource/Font', '/usr/local/Acrobat7/Resource/Font',
                '/usr/local/Acrobat6/Resource/Font', '/usr/local/Acrobat5/Resource/Font',
                '/usr/local/Acrobat4/Resource/Font', '%(REPORTLAB_DIR)s/fonts', '%(REPORTLAB_DIR)s/../fonts',
                '%(REPORTLAB_DIR)s/../../fonts', '%(HOME)s/fonts')
TTFSearchPath = ('c:/winnt/fonts', 'c:/windows/fonts', '/usr/lib/X11/fonts/TrueType/',
                 '/usr/share/fonts/truetype', '%(REPORTLAB_DIR)s/fonts', '%(REPORTLAB_DIR)s/../fonts',
                 '%(REPORTLAB_DIR)s/../../fonts', '%(HOME)s/fonts', '~/Library/Fonts',
                 '/Library/Fonts', '/Network/Library/Fonts', '/System/Library/Fonts')
CMapSearchPath = ('/usr/lib/Acrobat9/Resource/CMap', '/usr/lib/Acrobat8/Resource/CMap',
                  '/usr/lib/Acrobat7/Resource/CMap', '/usr/lib/Acrobat6/Resource/CMap',
                  '/usr/lib/Acrobat5/Resource/CMap', '/usr/lib/Acrobat4/Resource/CMap',
                  '/usr/local/Acrobat9/Resource/CMap', '/usr/local/Acrobat8/Resource/CMap',
                  '/usr/local/Acrobat7/Resource/CMap', '/usr/local/Acrobat6/Resource/CMap',
                  '/usr/local/Acrobat5/Resource/CMap', '/usr/local/Acrobat4/Resource/CMap',
                  'C:\\Program Files\\Adobe\\Acrobat\\Resource\\CMap', 'C:\\Program Files\\Adobe\\Acrobat 9.0\\Resource\\CMap',
                  'C:\\Program Files\\Adobe\\Acrobat 8.0\\Resource\\CMap', 'C:\\Program Files\\Adobe\\Acrobat 7.0\\Resource\\CMap',
                  'C:\\Program Files\\Adobe\\Acrobat 6.0\\Resource\\CMap', 'C:\\Program Files\\Adobe\\Acrobat 5.0\\Resource\\CMap',
                  'C:\\Program Files\\Adobe\\Acrobat 4.0\\Resource\\CMap', '%(REPORTLAB_DIR)s/fonts/CMap',
                  '%(REPORTLAB_DIR)s/../fonts/CMap', '%(REPORTLAB_DIR)s/../../fonts/CMap',
                  '%(HOME)s/fonts/CMap')
try:
    from ....................................................................local_rl_config import *
except:
    pass

_SAVED = {}
sys_version = None

def _setOpt(name, value, conv=None):
    """set a module level value from environ/default"""
    from os import environ
    ename = 'RL_' + name
    if ename in environ:
        value = environ[ename]
    if conv:
        value = conv(value)
    globals()[name] = value


def _startUp():
    """This function allows easy resetting to the global defaults
    If the environment contains 'RL_xxx' then we use the value
    else we use the given default"""
    global _unset_
    global sys_version
    V = ('T1SearchPath\nCMapSearchPath\nTTFSearchPath\nallowTableBoundsErrors\nshapeChecking\ndefaultEncoding \ndefaultGraphicsFontName\npageCompression \ndefaultPageSize \ndefaultImageCaching \nZLIB_WARNINGS \nwarnOnMissingFontGlyphs \nverbose \nshowBoundary \nemptyTableAction\ninvariant\neps_preview_transparent\neps_preview\neps_ttf_embed\neps_ttf_embed_uid\noverlapAttachedSpace\nlongTableOptimize \nautoConvertEncoding  \n_FUZZ\nwrapA85\nfsEncodings\nodbc_driver\nplatypus_link_underline\ncanvas_basefontname\nallowShortTableRows\nimageReaderFlags\nparaFontSizeHeightOffset\ncanvas_baseColor\nignoreContainerActions\nttfAsciiReadable').split()
    import os, sys
    sys_version = sys.version.split()[0]
    from reportlab.lib import pagesizes
    from reportlab.lib.utils import rl_isdir
    if _SAVED == {}:
        _unset_ = getattr(sys, '_rl_config__unset_', None)
        if _unset_ is None:

            class _unset_:
                pass

            sys._rl_config__unset_ = _unset_ = _unset_()
        for k in V:
            _SAVED[k] = globals()[k]

    import reportlab
    D = {'REPORTLAB_DIR': os.path.abspath(os.path.dirname(reportlab.__file__)), 'HOME': os.environ.get('HOME', os.getcwd()), 
       'disk': os.getcwd().split(':')[0], 
       'sys_version': sys_version}
    for name in ('T1SearchPath', 'TTFSearchPath', 'CMapSearchPath'):
        P = []
        for p in _SAVED[name]:
            d = (p % D).replace('/', os.sep)
            if rl_isdir(d):
                P.append(d)

        _setOpt(name, P)

    for k in V[3:]:
        v = _SAVED[k]
        if isinstance(v, (int, float)):
            conv = type(v)
        elif k == 'defaultPageSize':
            conv = lambda v, M=pagesizes: getattr(M, v)
        else:
            conv = None
        _setOpt(k, v, conv)

    return


_registered_resets = []

def register_reset(func):
    _registered_resets[:] = [ x for x in _registered_resets if x() ]
    L = [ x for x in _registered_resets if x() is func ]
    if L:
        return
    from weakref import ref
    _registered_resets.append(ref(func))


def _reset():
    _startUp()
    for f in _registered_resets[:]:
        c = f()
        if c:
            c()
        else:
            _registered_resets.remove(f)


_startUp()