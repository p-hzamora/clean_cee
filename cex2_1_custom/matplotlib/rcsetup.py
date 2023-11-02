# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\rcsetup.pyc
# Compiled at: 2012-11-08 06:38:04
"""
The rcsetup module contains the default values and the validation code for
customization using matplotlib's rc settings.

Each rc setting is assigned a default value and a function used to validate any
attempted changes to that setting. The default values and validation functions
are defined in the rcsetup module, and are used to construct the rcParams global
object which stores the settings and is referenced throughout matplotlib.

These default values should be consistent with the default matplotlibrc file
that actually reflects the values given here. Any additions or deletions to the
parameter set listed here should also be visited to the
:file:`matplotlibrc.template` in matplotlib's root source directory.
"""
from __future__ import print_function
import os, warnings
from matplotlib.fontconfig_pattern import parse_fontconfig_pattern
from matplotlib.colors import is_color_like
interactive_bk = [
 'GTK', 'GTKAgg', 'GTKCairo', 'FltkAgg', 'MacOSX', 
 'QtAgg', 'Qt4Agg', 
 'TkAgg', 'WX', 'WXAgg', 'CocoaAgg', 
 'GTK3Cairo', 'GTK3Agg']
non_interactive_bk = [
 'agg', 'cairo', 'emf', 'gdk', 
 'pdf', 'pgf', 'ps', 'svg', 'template']
all_backends = interactive_bk + non_interactive_bk

class ValidateInStrings:

    def __init__(self, key, valid, ignorecase=False):
        """valid is a list of legal strings"""
        self.key = key
        self.ignorecase = ignorecase

        def func(s):
            if ignorecase:
                return s.lower()
            else:
                return s

        self.valid = dict([ (func(k), k) for k in valid ])

    def __call__(self, s):
        if self.ignorecase:
            s = s.lower()
        if s in self.valid:
            return self.valid[s]
        raise ValueError('Unrecognized %s string "%s": valid strings are %s' % (
         self.key, s, self.valid.values()))


def validate_path_exists(s):
    """If s is a path, return s, else False"""
    if os.path.exists(s):
        return s
    raise RuntimeError('"%s" should be a path but it does not exist' % s)


def validate_bool(b):
    """Convert b to a boolean or raise"""
    if type(b) is str:
        b = b.lower()
    if b in ('t', 'y', 'yes', 'on', 'true', '1', 1, True):
        return True
    if b in ('f', 'n', 'no', 'off', 'false', '0', 0, False):
        return False
    raise ValueError('Could not convert "%s" to boolean' % b)


def validate_bool_maybe_none(b):
    """Convert b to a boolean or raise"""
    if type(b) is str:
        b = b.lower()
    if b == 'none':
        return
    else:
        if b in ('t', 'y', 'yes', 'on', 'true', '1', 1, True):
            return True
        if b in ('f', 'n', 'no', 'off', 'false', '0', 0, False):
            return False
        raise ValueError('Could not convert "%s" to boolean' % b)
        return


def validate_float(s):
    """convert s to float or raise"""
    try:
        return float(s)
    except ValueError:
        raise ValueError('Could not convert "%s" to float' % s)


def validate_int(s):
    """convert s to int or raise"""
    try:
        return int(s)
    except ValueError:
        raise ValueError('Could not convert "%s" to int' % s)


def validate_fonttype(s):
    """confirm that this is a Postscript of PDF font type that we know how to convert to"""
    fonttypes = {'type3': 3, 'truetype': 42}
    try:
        fonttype = validate_int(s)
    except ValueError:
        if s.lower() in fonttypes.iterkeys():
            return fonttypes[s.lower()]
        raise ValueError('Supported Postscript/PDF font types are %s' % fonttypes.keys())
    else:
        if fonttype not in fonttypes.itervalues():
            raise ValueError('Supported Postscript/PDF font types are %s' % fonttypes.values())
        return fonttype


_validate_standard_backends = ValidateInStrings('backend', all_backends, ignorecase=True)

def validate_backend(s):
    if s.startswith('module://'):
        return s
    else:
        return _validate_standard_backends(s)


validate_qt4 = ValidateInStrings('backend.qt4', ['PyQt4', 'PySide'])

def validate_toolbar(s):
    validator = ValidateInStrings('toolbar', [
     'None', 'classic', 'toolbar2'], ignorecase=True)
    s = validator(s)
    if s.lower == 'classic':
        warnings.warn("'classic' Navigation Toolbar is deprecated in v1.2.x and will be removed in v1.3")
    return s


def validate_maskedarray(v):
    try:
        if v == 'obsolete':
            return v
    except ValueError:
        pass

    warnings.warn('rcParams key "maskedarray" is obsolete and has no effect;\n please delete it from your matplotlibrc file')


class validate_nseq_float:

    def __init__(self, n):
        self.n = n

    def __call__(self, s):
        """return a seq of n floats or raise"""
        if type(s) is str:
            ss = s.split(',')
            if len(ss) != self.n:
                raise ValueError('You must supply exactly %d comma separated values' % self.n)
            try:
                return [ float(val) for val in ss ]
            except ValueError:
                raise ValueError('Could not convert all entries to floats')

        else:
            assert type(s) in (list, tuple)
            if len(s) != self.n:
                raise ValueError('You must supply exactly %d values' % self.n)
            return [ float(val) for val in s ]


class validate_nseq_int:

    def __init__(self, n):
        self.n = n

    def __call__(self, s):
        """return a seq of n ints or raise"""
        if type(s) is str:
            ss = s.split(',')
            if len(ss) != self.n:
                raise ValueError('You must supply exactly %d comma separated values' % self.n)
            try:
                return [ int(val) for val in ss ]
            except ValueError:
                raise ValueError('Could not convert all entries to ints')

        else:
            assert type(s) in (list, tuple)
            if len(s) != self.n:
                raise ValueError('You must supply exactly %d values' % self.n)
            return [ int(val) for val in s ]


def validate_color(s):
    """return a valid color arg"""
    try:
        if s.lower() == 'none':
            return 'None'
    except AttributeError:
        pass

    if is_color_like(s):
        return s
    stmp = '#' + s
    if is_color_like(stmp):
        return stmp
    colorarg = s
    msg = ''
    if s.find(',') >= 0:
        stmp = ('').join([ c for c in s if c.isdigit() or c == '.' or c == ',' ])
        vals = stmp.split(',')
        if len(vals) != 3:
            msg = '\nColor tuples must be length 3'
        else:
            try:
                colorarg = [ float(val) for val in vals ]
            except ValueError:
                msg = '\nCould not convert all entries to floats'

    if not msg and is_color_like(colorarg):
        return colorarg
    raise ValueError('%s does not look like a color arg%s' % (s, msg))


def validate_colorlist(s):
    """return a list of colorspecs"""
    if type(s) is str:
        return [ validate_color(c.strip()) for c in s.split(',') ]
    else:
        assert type(s) in [list, tuple]
        return [ validate_color(c) for c in s ]


def validate_stringlist(s):
    """return a list"""
    if type(s) is str:
        return [ v.strip() for v in s.split(',') ]
    else:
        assert type(s) in [list, tuple]
        return [ str(v) for v in s ]


validate_orientation = ValidateInStrings('orientation', [
 'landscape', 'portrait'])

def validate_aspect(s):
    if s in ('auto', 'equal'):
        return s
    try:
        return float(s)
    except ValueError:
        raise ValueError('not a valid aspect specification')


def validate_fontsize(s):
    if type(s) is str:
        s = s.lower()
    if s in ('xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large',
             'smaller', 'larger'):
        return s
    try:
        return float(s)
    except ValueError:
        raise ValueError('not a valid font size')


def validate_font_properties(s):
    parse_fontconfig_pattern(s)
    return s


validate_fontset = ValidateInStrings('fontset', ['cm', 'stix', 'stixsans', 'custom'])
validate_mathtext_default = ValidateInStrings('default', ('rm cal it tt sf bf default bb frak circled scr regular').split())
validate_verbose = ValidateInStrings('verbose', [
 'silent', 'helpful', 'debug', 'debug-annoying'])

def deprecate_savefig_extension(value):
    warnings.warn('savefig.extension is deprecated.  Use savefig.format instead.')


validate_ps_papersize = ValidateInStrings('ps_papersize', [
 'auto', 'letter', 'legal', 'ledger', 
 'a0', 'a1', 'a2', 'a3', 'a4', 
 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 
 'b0', 'b1', 'b2', 'b3', 'b4', 
 'b5', 'b6', 'b7', 'b8', 'b9', 'b10'], ignorecase=True)

def validate_ps_distiller(s):
    if type(s) is str:
        s = s.lower()
    if s in ('none', None):
        return
    else:
        if s in ('false', False):
            return False
        if s in ('ghostscript', 'xpdf'):
            return s
        raise ValueError('matplotlibrc ps.usedistiller must either be none, ghostscript or xpdf')
        return


validate_joinstyle = ValidateInStrings('joinstyle', ['miter', 'round', 'bevel'], ignorecase=True)
validate_capstyle = ValidateInStrings('capstyle', ['butt', 'round', 'projecting'], ignorecase=True)
validate_negative_linestyle = ValidateInStrings('negative_linestyle', ['solid', 'dashed'], ignorecase=True)

def validate_negative_linestyle_legacy(s):
    try:
        res = validate_negative_linestyle(s)
        return res
    except ValueError:
        dashes = validate_nseq_float(2)(s)
        warnings.warn("Deprecated negative_linestyle specification; use 'solid' or 'dashed'")
        return (0, dashes)


def validate_tkpythoninspect(s):
    warnings.warn('tk.pythoninspect is obsolete, and has no effect')
    return validate_bool(s)


validate_legend_loc = ValidateInStrings('legend_loc', [
 'best', 
 'upper right', 
 'upper left', 
 'lower left', 
 'lower right', 
 'right', 
 'center left', 
 'center right', 
 'lower center', 
 'upper center', 
 'center'], ignorecase=True)

def deprecate_svg_embed_char_paths(value):
    warnings.warn('svg.embed_char_paths is deprecated.  Use svg.fonttype instead.')


validate_svg_fonttype = ValidateInStrings('fonttype', ['none', 'path', 'svgfont'])

def validate_hinting(s):
    if s in (True, False):
        return s
    if s.lower() in ('auto', 'native', 'either', 'none'):
        return s.lower()
    raise ValueError("hinting should be 'auto', 'native', 'either' or 'none'")


validate_pgf_texsystem = ValidateInStrings('pgf.texsystem', [
 'xelatex', 'lualatex', 'pdflatex'])
validate_movie_writer = ValidateInStrings('animation.writer', [
 'ffmpeg', 'ffmpeg_file', 'mencoder', 'mencoder_file'])
validate_movie_frame_fmt = ValidateInStrings('animation.frame_format', [
 'png', 'jpeg', 'tiff', 'raw', 'rgba'])

def validate_bbox(s):
    if type(s) is str:
        s = s.lower()
        if s == 'tight':
            return s
        if s == 'standard':
            return
        raise ValueError("bbox should be 'tight' or 'standard'")
    return


class ValidateInterval:
    """
    Value must be in interval
    """

    def __init__(self, vmin, vmax, closedmin=True, closedmax=True):
        self.vmin = vmin
        self.vmax = vmax
        self.cmin = closedmin
        self.cmax = closedmax

    def __call__(self, s):
        try:
            s = float(s)
        except:
            raise RuntimeError('Value must be a float; found "%s"' % s)

        if self.cmin and s < self.vmin:
            raise RuntimeError('Value must be >= %f; found "%f"' % (self.vmin, s))
        elif not self.cmin and s <= self.vmin:
            raise RuntimeError('Value must be > %f; found "%f"' % (self.vmin, s))
        if self.cmax and s > self.vmax:
            raise RuntimeError('Value must be <= %f; found "%f"' % (self.vmax, s))
        elif not self.cmax and s >= self.vmax:
            raise RuntimeError('Value must be < %f; found "%f"' % (self.vmax, s))
        return s


defaultParams = {'backend': [
             'Agg', validate_backend], 
   'backend_fallback': [
                      True, validate_bool], 
   'backend.qt4': [
                 'PyQt4', validate_qt4], 
   'toolbar': [
             'toolbar2', validate_toolbar], 
   'datapath': [
              None, validate_path_exists], 
   'interactive': [
                 False, validate_bool], 
   'timezone': [
              'UTC', str], 
   'verbose.level': [
                   'silent', validate_verbose], 
   'verbose.fileo': [
                   'sys.stdout', str], 
   'lines.linewidth': [
                     1.0, validate_float], 
   'lines.linestyle': [
                     '-', str], 
   'lines.color': [
                 'b', validate_color], 
   'lines.marker': [
                  'None', str], 
   'lines.markeredgewidth': [
                           0.5, validate_float], 
   'lines.markersize': [
                      6, validate_float], 
   'lines.antialiased': [
                       True, validate_bool], 
   'lines.dash_joinstyle': [
                          'round', validate_joinstyle], 
   'lines.solid_joinstyle': [
                           'round', validate_joinstyle], 
   'lines.dash_capstyle': [
                         'butt', validate_capstyle], 
   'lines.solid_capstyle': [
                          'projecting', validate_capstyle], 
   'patch.linewidth': [
                     1.0, validate_float], 
   'patch.edgecolor': [
                     'k', validate_color], 
   'patch.facecolor': [
                     'b', validate_color], 
   'patch.antialiased': [
                       True, validate_bool], 
   'font.family': [
                 'sans-serif', str], 
   'font.style': [
                'normal', str], 
   'font.variant': [
                  'normal', str], 
   'font.stretch': [
                  'normal', str], 
   'font.weight': [
                 'normal', str], 
   'font.size': [
               12, validate_float], 
   'font.serif': [
                [
                 'Bitstream Vera Serif', 'DejaVu Serif', 
                 'New Century Schoolbook', 
                 'Century Schoolbook L', 
                 'Utopia', 
                 'ITC Bookman', 'Bookman', 
                 'Nimbus Roman No9 L', 
                 'Times New Roman', 
                 'Times', 
                 'Palatino', 'Charter', 'serif'],
                validate_stringlist], 
   'font.sans-serif': [
                     [
                      'Bitstream Vera Sans', 
                      'DejaVu Sans', 
                      'Lucida Grande', 
                      'Verdana', 'Geneva', 'Lucid', 
                      'Arial', 
                      'Helvetica', 'Avant Garde', 'sans-serif'],
                     validate_stringlist], 
   'font.cursive': [
                  [
                   'Apple Chancery', 'Textile', 
                   'Zapf Chancery', 
                   'Sand', 
                   'cursive'], validate_stringlist], 
   'font.fantasy': [
                  [
                   'Comic Sans MS', 'Chicago', 
                   'Charcoal', 'ImpactWestern', 
                   'fantasy'], validate_stringlist], 
   'font.monospace': [
                    [
                     'Bitstream Vera Sans Mono', 
                     'DejaVu Sans Mono', 
                     'Andale Mono', 
                     'Nimbus Mono L', 'Courier New', 
                     'Courier', 
                     'Fixed', 'Terminal', 'monospace'],
                    validate_stringlist], 
   'text.color': [
                'k', validate_color], 
   'text.usetex': [
                 False, validate_bool], 
   'text.latex.unicode': [
                        False, validate_bool], 
   'text.latex.preamble': [
                         [
                          ''], validate_stringlist], 
   'text.latex.preview': [
                        False, validate_bool], 
   'text.dvipnghack': [
                     None, validate_bool_maybe_none], 
   'text.hinting': [
                  True, validate_hinting], 
   'text.hinting_factor': [
                         8, validate_int], 
   'text.antialiased': [
                      True, validate_bool], 
   'mathtext.cal': [
                  'cursive', validate_font_properties], 
   'mathtext.rm': [
                 'serif', validate_font_properties], 
   'mathtext.tt': [
                 'monospace', validate_font_properties], 
   'mathtext.it': [
                 'serif:italic', validate_font_properties], 
   'mathtext.bf': [
                 'serif:bold', validate_font_properties], 
   'mathtext.sf': [
                 'sans\\-serif', validate_font_properties], 
   'mathtext.fontset': [
                      'cm', validate_fontset], 
   'mathtext.default': [
                      'it', validate_mathtext_default], 
   'mathtext.fallback_to_cm': [
                             True, validate_bool], 
   'image.aspect': [
                  'equal', validate_aspect], 
   'image.interpolation': [
                         'bilinear', str], 
   'image.cmap': [
                'jet', str], 
   'image.lut': [
               256, validate_int], 
   'image.origin': [
                  'upper', str], 
   'image.resample': [
                    False, validate_bool], 
   'contour.negative_linestyle': [
                                'dashed', validate_negative_linestyle_legacy], 
   'axes.axisbelow': [
                    False, validate_bool], 
   'axes.hold': [
               True, validate_bool], 
   'axes.facecolor': [
                    'w', validate_color], 
   'axes.edgecolor': [
                    'k', validate_color], 
   'axes.linewidth': [
                    1.0, validate_float], 
   'axes.titlesize': [
                    'large', validate_fontsize], 
   'axes.grid': [
               False, validate_bool], 
   'axes.labelsize': [
                    'medium', validate_fontsize], 
   'axes.labelweight': [
                      'normal', str], 
   'axes.labelcolor': [
                     'k', validate_color], 
   'axes.formatter.limits': [
                           [
                            -7, 7], validate_nseq_int(2)], 
   'axes.formatter.use_locale': [
                               False, validate_bool], 
   'axes.formatter.use_mathtext': [
                                 False, validate_bool], 
   'axes.unicode_minus': [
                        True, validate_bool], 
   'axes.color_cycle': [
                      [
                       'b', 'g', 'r', 
                       'c', 'm', 'y', 'k'],
                      validate_colorlist], 
   'polaraxes.grid': [
                    True, validate_bool], 
   'axes3d.grid': [
                 True, validate_bool], 
   'legend.fancybox': [
                     False, validate_bool], 
   'legend.loc': [
                'upper right', validate_legend_loc], 
   'legend.isaxes': [
                   True, validate_bool], 
   'legend.numpoints': [
                      2, validate_int], 
   'legend.fontsize': [
                     'large', validate_fontsize], 
   'legend.markerscale': [
                        1.0, validate_float], 
   'legend.shadow': [
                   False, validate_bool], 
   'legend.frameon': [
                    True, validate_bool], 
   'legend.borderpad': [
                      0.4, validate_float], 
   'legend.labelspacing': [
                         0.5, validate_float], 
   'legend.handlelength': [
                         2.0, validate_float], 
   'legend.handleheight': [
                         0.7, validate_float], 
   'legend.handletextpad': [
                          0.8, validate_float], 
   'legend.borderaxespad': [
                          0.5, validate_float], 
   'legend.columnspacing': [
                          2.0, validate_float], 
   'legend.markerscale': [
                        1.0, validate_float], 
   'legend.shadow': [
                   False, validate_bool], 
   'xtick.major.size': [
                      4, validate_float], 
   'xtick.minor.size': [
                      2, validate_float], 
   'xtick.major.width': [
                       0.5, validate_float], 
   'xtick.minor.width': [
                       0.5, validate_float], 
   'xtick.major.pad': [
                     4, validate_float], 
   'xtick.minor.pad': [
                     4, validate_float], 
   'xtick.color': [
                 'k', validate_color], 
   'xtick.labelsize': [
                     'medium', validate_fontsize], 
   'xtick.direction': [
                     'in', str], 
   'ytick.major.size': [
                      4, validate_float], 
   'ytick.minor.size': [
                      2, validate_float], 
   'ytick.major.width': [
                       0.5, validate_float], 
   'ytick.minor.width': [
                       0.5, validate_float], 
   'ytick.major.pad': [
                     4, validate_float], 
   'ytick.minor.pad': [
                     4, validate_float], 
   'ytick.color': [
                 'k', validate_color], 
   'ytick.labelsize': [
                     'medium', validate_fontsize], 
   'ytick.direction': [
                     'in', str], 
   'grid.color': [
                'k', validate_color], 
   'grid.linestyle': [
                    ':', str], 
   'grid.linewidth': [
                    0.5, validate_float], 
   'grid.alpha': [
                1.0, validate_float], 
   'figure.figsize': [
                    [
                     8.0, 6.0], validate_nseq_float(2)], 
   'figure.dpi': [
                80, validate_float], 
   'figure.facecolor': [
                      '0.75', validate_color], 
   'figure.edgecolor': [
                      'w', validate_color], 
   'figure.autolayout': [
                       False, validate_bool], 
   'figure.subplot.left': [
                         0.125, ValidateInterval(0, 1, closedmin=True, closedmax=True)], 
   'figure.subplot.right': [
                          0.9, ValidateInterval(0, 1, closedmin=True, closedmax=True)], 
   'figure.subplot.bottom': [
                           0.1, ValidateInterval(0, 1, closedmin=True, closedmax=True)], 
   'figure.subplot.top': [
                        0.9, ValidateInterval(0, 1, closedmin=True, closedmax=True)], 
   'figure.subplot.wspace': [
                           0.2, ValidateInterval(0, 1, closedmin=True, closedmax=False)], 
   'figure.subplot.hspace': [
                           0.2, ValidateInterval(0, 1, closedmin=True, closedmax=False)], 
   'savefig.dpi': [
                 100, validate_float], 
   'savefig.facecolor': [
                       'w', validate_color], 
   'savefig.edgecolor': [
                       'w', validate_color], 
   'savefig.orientation': [
                         'portrait', validate_orientation], 
   'savefig.extension': [
                       'png', deprecate_savefig_extension], 
   'savefig.format': [
                    'png', str], 
   'savefig.bbox': [
                  None, validate_bbox], 
   'savefig.pad_inches': [
                        0.1, validate_float], 
   'tk.window_focus': [
                     False, validate_bool], 
   'tk.pythoninspect': [
                      False, validate_tkpythoninspect], 
   'ps.papersize': [
                  'letter', validate_ps_papersize], 
   'ps.useafm': [
               False, validate_bool], 
   'ps.usedistiller': [
                     False, validate_ps_distiller], 
   'ps.distiller.res': [
                      6000, validate_int], 
   'ps.fonttype': [
                 3, validate_fonttype], 
   'pdf.compression': [
                     6, validate_int], 
   'pdf.inheritcolor': [
                      False, validate_bool], 
   'pdf.use14corefonts': [
                        False, validate_bool], 
   'pdf.fonttype': [
                  3, validate_fonttype], 
   'pgf.debug': [
               False, validate_bool], 
   'pgf.texsystem': [
                   'xelatex', validate_pgf_texsystem], 
   'pgf.rcfonts': [
                 True, validate_bool], 
   'pgf.preamble': [
                  [
                   ''], validate_stringlist], 
   'svg.image_inline': [
                      True, validate_bool], 
   'svg.image_noscale': [
                       False, validate_bool], 
   'svg.embed_char_paths': [
                          True, deprecate_svg_embed_char_paths], 
   'svg.fonttype': [
                  'path', validate_svg_fonttype], 
   'docstring.hardcopy': [
                        False, validate_bool], 
   'plugins.directory': [
                       '.matplotlib_plugins', str], 
   'path.simplify': [
                   True, validate_bool], 
   'path.simplify_threshold': [
                             1.0 / 9.0, ValidateInterval(0.0, 1.0)], 
   'path.snap': [
               True, validate_bool], 
   'agg.path.chunksize': [
                        0, validate_int], 
   'keymap.fullscreen': [
                       ('f', 'ctrl+f'), validate_stringlist], 
   'keymap.home': [
                 [
                  'h', 'r', 'home'], validate_stringlist], 
   'keymap.back': [
                 [
                  'left', 'c', 'backspace'], validate_stringlist], 
   'keymap.forward': [
                    [
                     'right', 'v'], validate_stringlist], 
   'keymap.pan': [
                'p', validate_stringlist], 
   'keymap.zoom': [
                 'o', validate_stringlist], 
   'keymap.save': [
                 ('s', 'ctrl+s'), validate_stringlist], 
   'keymap.quit': [
                 ('ctrl+w', ), validate_stringlist], 
   'keymap.grid': [
                 'g', validate_stringlist], 
   'keymap.yscale': [
                   'l', validate_stringlist], 
   'keymap.xscale': [
                   [
                    'k', 'L'], validate_stringlist], 
   'keymap.all_axes': [
                     'a', validate_stringlist], 
   'animation.writer': [
                      'ffmpeg', validate_movie_writer], 
   'animation.codec': [
                     'mpeg4', str], 
   'animation.bitrate': [
                       -1, validate_int], 
   'animation.frame_format': [
                            'png', validate_movie_frame_fmt], 
   'animation.ffmpeg_path': [
                           'ffmpeg', str], 
   'animation.ffmpeg_args': [
                           '', validate_stringlist], 
   'animation.mencoder_path': [
                             'mencoder', str], 
   'animation.mencoder_args': [
                             '', validate_stringlist]}
if __name__ == '__main__':
    rc = defaultParams
    rc['datapath'][0] = '/'
    for key in rc:
        if not rc[key][1](rc[key][0]) == rc[key][0]:
            print('%s: %s != %s' % (key, rc[key][1](rc[key][0]), rc[key][0]))