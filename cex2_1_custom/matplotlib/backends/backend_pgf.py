# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_pgf.pyc
# Compiled at: 2012-11-06 08:42:20
from __future__ import division
import math, os, sys, re, shutil, tempfile, codecs, subprocess, atexit, weakref, matplotlib as mpl
from matplotlib.backend_bases import RendererBase, GraphicsContextBase, FigureManagerBase, FigureCanvasBase
from matplotlib.figure import Figure
from matplotlib.text import Text
from matplotlib.path import Path
from matplotlib import _png, rcParams
from matplotlib import font_manager
from matplotlib.ft2font import FT2Font
from matplotlib.cbook import is_string_like, is_writable_file_like
from matplotlib.cbook import check_output
system_fonts = []
for f in font_manager.findSystemFonts():
    try:
        system_fonts.append(FT2Font(str(f)).family_name)
    except RuntimeError:
        pass
    except:
        pass

def get_texcommand():
    """Get chosen TeX system from rc."""
    texsystem_options = ['xelatex', 'lualatex', 'pdflatex']
    texsystem = rcParams.get('pgf.texsystem', 'xelatex')
    if texsystem in texsystem_options:
        return texsystem
    return 'xelatex'


def get_fontspec():
    """Build fontspec preamble from rc."""
    latex_fontspec = []
    texcommand = get_texcommand()
    if texcommand is not 'pdflatex':
        latex_fontspec.append('\\usepackage{fontspec}')
    if texcommand is not 'pdflatex' and rcParams.get('pgf.rcfonts', True):
        families = ['serif', 'sans-serif', 'monospace']
        fontspecs = ['\\setmainfont{%s}', '\\setsansfont{%s}',
         '\\setmonofont{%s}']
        for family, fontspec in zip(families, fontspecs):
            matches = [ f for f in rcParams['font.' + family] if f in system_fonts ]
            if matches:
                latex_fontspec.append(fontspec % matches[0])

    return ('\n').join(latex_fontspec)


def get_preamble():
    """Get LaTeX preamble from rc."""
    latex_preamble = rcParams.get('pgf.preamble', '')
    if type(latex_preamble) == list:
        latex_preamble = ('\n').join(latex_preamble)
    return latex_preamble


latex_pt_to_in = 1.0 / 72.27
latex_in_to_pt = 1.0 / latex_pt_to_in
mpl_pt_to_in = 1.0 / 72.0
mpl_in_to_pt = 1.0 / mpl_pt_to_in
NO_ESCAPE = '(?<!\\\\)(?:\\\\\\\\)*'
re_mathsep = re.compile(NO_ESCAPE + '\\$')
re_escapetext = re.compile(NO_ESCAPE + '([_^$%])')
repl_escapetext = lambda m: '\\' + m.group(1)
re_mathdefault = re.compile(NO_ESCAPE + '(\\\\mathdefault)')
repl_mathdefault = lambda m: m.group(0)[:-len(m.group(1))]

def common_texification(text):
    """
    Do some necessary and/or useful substitutions for texts to be included in
    LaTeX documents.
    """
    text = re_mathdefault.sub(repl_mathdefault, text)
    parts = re_mathsep.split(text)
    for i, s in enumerate(parts):
        if not i % 2:
            s = re_escapetext.sub(repl_escapetext, s)
        else:
            s = '\\(\\displaystyle %s\\)' % s
        parts[i] = s

    return ('').join(parts)


def writeln(fh, line):
    fh.write(line)
    fh.write('%\n')


def _font_properties_str(prop):
    commands = []
    families = {'serif': '\\rmfamily', 'sans': '\\sffamily', 'sans-serif': '\\sffamily', 
       'monospace': '\\ttfamily'}
    family = prop.get_family()[0]
    if family in families:
        commands.append(families[family])
    elif family in system_fonts and get_texcommand() is not 'pdflatex':
        commands.append('\\setmainfont{%s}\\rmfamily' % family)
    size = prop.get_size_in_points()
    commands.append('\\fontsize{%f}{%f}' % (size, size * 1.2))
    styles = {'normal': '', 'italic': '\\itshape', 'oblique': '\\slshape'}
    commands.append(styles[prop.get_style()])
    boldstyles = [
     'semibold', 'demibold', 'demi', 'bold', 'heavy', 
     'extra bold', 
     'black']
    if prop.get_weight() in boldstyles:
        commands.append('\\bfseries')
    commands.append('\\selectfont')
    return ('').join(commands)


def make_pdf_to_png_converter():
    """
    Returns a function that converts a pdf file to a png file.
    """
    tools_available = []
    try:
        check_output(['pdftocairo', '-v'], stderr=subprocess.STDOUT)
        tools_available.append('pdftocairo')
    except:
        pass

    try:
        gs = 'gs' if sys.platform is not 'win32' else 'gswin32c'
        check_output([gs, '-v'], stderr=subprocess.STDOUT)
        tools_available.append('gs')
    except:
        pass

    if 'pdftocairo' in tools_available:

        def cairo_convert(pdffile, pngfile, dpi):
            cmd = [
             'pdftocairo', '-singlefile', '-png',
             '-r %d' % dpi, pdffile, os.path.splitext(pngfile)[0]]
            check_output((' ').join(cmd), shell=True, stderr=subprocess.STDOUT)

        return cairo_convert
    if 'gs' in tools_available:

        def gs_convert(pdffile, pngfile, dpi):
            cmd = [
             gs, '-dQUIET', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dNOPROMPT',
             '-sDEVICE=png16m', '-dUseCIEColor', '-dTextAlphaBits=4',
             '-dGraphicsAlphaBits=4', '-dDOINTERPOLATE', '-sOutputFile=%s' % pngfile,
             '-r%d' % dpi, pdffile]
            check_output(cmd, stderr=subprocess.STDOUT)

        return gs_convert
    raise RuntimeError('No suitable pdf to png renderer found.')


class LatexError(Exception):

    def __init__(self, message, latex_output=''):
        Exception.__init__(self, message)
        self.latex_output = latex_output


class LatexManagerFactory():
    previous_instance = None

    @staticmethod
    def get_latex_manager():
        texcommand = get_texcommand()
        latex_header = LatexManager._build_latex_header()
        prev = LatexManagerFactory.previous_instance
        if prev and prev.latex_header == latex_header and prev.texcommand == texcommand:
            if rcParams.get('pgf.debug', False):
                print 'reusing LatexManager'
            return prev
        if rcParams.get('pgf.debug', False):
            print 'creating LatexManager'
        new_inst = LatexManager()
        LatexManagerFactory.previous_instance = new_inst
        return new_inst


class WeakSet():

    def __init__(self):
        self.weak_key_dict = weakref.WeakKeyDictionary()

    def add(self, item):
        self.weak_key_dict[item] = None
        return

    def discard(self, item):
        if item in self.weak_key_dict:
            del self.weak_key_dict[item]

    def __iter__(self):
        return self.weak_key_dict.iterkeys()


class LatexManager():
    """
    The LatexManager opens an instance of the LaTeX application for
    determining the metrics of text elements. The LaTeX environment can be
    modified by setting fonts and/or a custem preamble in the rc parameters.
    """
    _unclean_instances = WeakSet()

    @staticmethod
    def _build_latex_header():
        latex_preamble = get_preamble()
        latex_fontspec = get_fontspec()
        latex_header = [
         '\\documentclass{minimal}', 
         'latex_preamble', 
         'latex_fontspec', 
         '\\begin{document}', 
         'text $math \\mu$', 
         '\\typeout{pgf_backend_query_start}']
        return ('\n').join(latex_header)

    @staticmethod
    def _cleanup_remaining_instances():
        unclean_instances = list(LatexManager._unclean_instances)
        for latex_manager in unclean_instances:
            latex_manager._cleanup()

    def _stdin_writeln(self, s):
        self.latex_stdin_utf8.write(s)
        self.latex_stdin_utf8.write('\n')
        self.latex_stdin_utf8.flush()

    def _expect(self, s):
        exp = s.encode('utf8')
        buf = bytearray()
        while True:
            b = self.latex.stdout.read(1)
            buf += b
            if buf[-len(exp):] == exp:
                break
            if not len(b):
                raise LatexError('LaTeX process halted', buf.decode('utf8'))

        return buf.decode('utf8')

    def _expect_prompt(self):
        return self._expect('\n*')

    def __init__(self):
        self.tmpdir = tempfile.mkdtemp(prefix='mpl_pgf_lm_')
        LatexManager._unclean_instances.add(self)
        self.texcommand = get_texcommand()
        self.latex_header = LatexManager._build_latex_header()
        latex_end = '\n\\makeatletter\n\\@@end\n'
        latex = subprocess.Popen([self.texcommand, '-halt-on-error'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=self.tmpdir)
        test_input = self.latex_header + latex_end
        stdout, stderr = latex.communicate(test_input.encode('utf-8'))
        if latex.returncode != 0:
            raise LatexError('LaTeX returned an error, probably missing font or error in preamble:\n%s' % stdout)
        latex = subprocess.Popen([self.texcommand, '-halt-on-error'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=self.tmpdir)
        self.latex = latex
        self.latex_stdin_utf8 = codecs.getwriter('utf8')(self.latex.stdin)
        self._stdin_writeln(self._build_latex_header())
        self._expect('*pgf_backend_query_start')
        self._expect_prompt()
        self.str_cache = {}

    def _cleanup(self):
        if not os.path.isdir(self.tmpdir):
            return
        try:
            self.latex_stdin_utf8.close()
            self.latex.communicate()
            self.latex.wait()
        except:
            pass

        try:
            shutil.rmtree(self.tmpdir)
            LatexManager._unclean_instances.discard(self)
        except:
            sys.stderr.write('error deleting tmp directory %s\n' % self.tmpdir)

    def __del__(self):
        if rcParams.get('pgf.debug', False):
            print 'deleting LatexManager'
        self._cleanup()

    def get_width_height_descent(self, text, prop):
        """
        Get the width, total height and descent for a text typesetted by the
        current LaTeX environment.
        """
        prop_cmds = _font_properties_str(prop)
        textbox = '\\sbox0{%s %s}' % (prop_cmds, text)
        if textbox in self.str_cache:
            return self.str_cache[textbox]
        self._stdin_writeln(textbox)
        try:
            self._expect_prompt()
        except LatexError as e:
            msg = "Error processing '%s'\nLaTeX Output:\n%s"
            raise ValueError(msg % (text, e.latex_output))

        self._stdin_writeln('\\typeout{\\the\\wd0,\\the\\ht0,\\the\\dp0}')
        try:
            answer = self._expect_prompt()
        except LatexError as e:
            msg = "Error processing '%s'\nLaTeX Output:\n%s"
            raise ValueError(msg % (text, e.latex_output))

        try:
            width, height, offset = answer.splitlines()[0].split(',')
        except:
            msg = "Error processing '%s'\nLaTeX Output:\n%s" % (text, answer)
            raise ValueError(msg)

        w, h, o = float(width[:-2]), float(height[:-2]), float(offset[:-2])
        self.str_cache[textbox] = (
         w, h + o, o)
        return (w, h + o, o)


class RendererPgf(RendererBase):

    def __init__(self, figure, fh):
        """
        Creates a new PGF renderer that translates any drawing instruction
        into text commands to be interpreted in a latex pgfpicture environment.

        Attributes:
        * figure: Matplotlib figure to initialize height, width and dpi from.
        * fh: File handle for the output of the drawing commands.
        """
        RendererBase.__init__(self)
        self.dpi = figure.dpi
        self.fh = fh
        self.figure = figure
        self.image_counter = 0
        self.latexManager = LatexManagerFactory.get_latex_manager()

    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace=None):
        writeln(self.fh, '\\begin{pgfscope}')
        f = 1.0 / self.dpi
        self._print_pgf_clip(gc)
        self._print_pgf_path_styles(gc, rgbFace)
        bl, tr = marker_path.get_extents(marker_trans).get_points()
        coords = (bl[0] * f, bl[1] * f, tr[0] * f, tr[1] * f)
        writeln(self.fh, '\\pgfsys@defobject{currentmarker}{\\pgfqpoint{%fin}{%fin}}{\\pgfqpoint{%fin}{%fin}}{' % coords)
        self._print_pgf_path(marker_path, marker_trans)
        self._pgf_path_draw(stroke=gc.get_linewidth() != 0.0, fill=rgbFace is not None)
        writeln(self.fh, '}')
        for point, code in path.iter_segments(trans, simplify=False):
            x, y = point[0] * f, point[1] * f
            writeln(self.fh, '\\begin{pgfscope}')
            writeln(self.fh, '\\pgfsys@transformshift{%fin}{%fin}' % (x, y))
            writeln(self.fh, '\\pgfsys@useobject{currentmarker}{}')
            writeln(self.fh, '\\end{pgfscope}')

        writeln(self.fh, '\\end{pgfscope}')
        return

    def draw_path(self, gc, path, transform, rgbFace=None):
        writeln(self.fh, '\\begin{pgfscope}')
        self._print_pgf_clip(gc)
        self._print_pgf_path_styles(gc, rgbFace)
        self._print_pgf_path(path, transform)
        self._pgf_path_draw(stroke=gc.get_linewidth() != 0.0, fill=rgbFace is not None)
        writeln(self.fh, '\\end{pgfscope}')
        if gc.get_hatch():
            writeln(self.fh, '\\begin{pgfscope}')
            self._print_pgf_clip(gc)
            self._print_pgf_path(path, transform)
            writeln(self.fh, '\\pgfusepath{clip}')
            writeln(self.fh, '\\pgfsys@defobject{currentpattern}{\\pgfqpoint{0in}{0in}}{\\pgfqpoint{1in}{1in}}{')
            writeln(self.fh, '\\begin{pgfscope}')
            writeln(self.fh, '\\pgfpathrectangle{\\pgfqpoint{0in}{0in}}{\\pgfqpoint{1in}{1in}}')
            writeln(self.fh, '\\pgfusepath{clip}')
            scale = mpl.transforms.Affine2D().scale(self.dpi)
            self._print_pgf_path(gc.get_hatch_path(), scale)
            self._pgf_path_draw(stroke=True)
            writeln(self.fh, '\\end{pgfscope}')
            writeln(self.fh, '}')
            f = 1.0 / self.dpi
            (xmin, ymin), (xmax, ymax) = path.get_extents(transform).get_points()
            xmin, xmax = f * xmin, f * xmax
            ymin, ymax = f * ymin, f * ymax
            repx, repy = int(math.ceil(xmax - xmin)), int(math.ceil(ymax - ymin))
            writeln(self.fh, '\\pgfsys@transformshift{%fin}{%fin}' % (xmin, ymin))
            for iy in range(repy):
                for ix in range(repx):
                    writeln(self.fh, '\\pgfsys@useobject{currentpattern}{}')
                    writeln(self.fh, '\\pgfsys@transformshift{1in}{0in}')

                writeln(self.fh, '\\pgfsys@transformshift{-%din}{0in}' % repx)
                writeln(self.fh, '\\pgfsys@transformshift{0in}{1in}')

            writeln(self.fh, '\\end{pgfscope}')
        return

    def _print_pgf_clip(self, gc):
        f = 1.0 / self.dpi
        bbox = gc.get_clip_rectangle()
        if bbox:
            p1, p2 = bbox.get_points()
            w, h = p2 - p1
            coords = (p1[0] * f, p1[1] * f, w * f, h * f)
            writeln(self.fh, '\\pgfpathrectangle{\\pgfqpoint{%fin}{%fin}}{\\pgfqpoint{%fin}{%fin}} ' % coords)
            writeln(self.fh, '\\pgfusepath{clip}')
        clippath, clippath_trans = gc.get_clip_path()
        if clippath is not None:
            self._print_pgf_path(clippath, clippath_trans)
            writeln(self.fh, '\\pgfusepath{clip}')
        return

    def _print_pgf_path_styles(self, gc, rgbFace):
        capstyles = {'butt': '\\pgfsetbuttcap', 'round': '\\pgfsetroundcap', 
           'projecting': '\\pgfsetrectcap'}
        writeln(self.fh, capstyles[gc.get_capstyle()])
        joinstyles = {'miter': '\\pgfsetmiterjoin', 'round': '\\pgfsetroundjoin', 
           'bevel': '\\pgfsetbeveljoin'}
        writeln(self.fh, joinstyles[gc.get_joinstyle()])
        has_fill = rgbFace is not None
        path_is_transparent = gc.get_alpha() != 1.0
        fill_is_transparent = has_fill and len(rgbFace) > 3 and rgbFace[3] != 1.0
        if has_fill:
            writeln(self.fh, '\\definecolor{currentfill}{rgb}{%f,%f,%f}' % tuple(rgbFace[:3]))
            writeln(self.fh, '\\pgfsetfillcolor{currentfill}')
        if has_fill and (path_is_transparent or fill_is_transparent):
            opacity = gc.get_alpha() * 1.0 if not fill_is_transparent else rgbFace[3]
            writeln(self.fh, '\\pgfsetfillopacity{%f}' % opacity)
        lw = gc.get_linewidth() * mpl_pt_to_in * latex_in_to_pt
        stroke_rgba = gc.get_rgb()
        writeln(self.fh, '\\pgfsetlinewidth{%fpt}' % lw)
        writeln(self.fh, '\\definecolor{currentstroke}{rgb}{%f,%f,%f}' % stroke_rgba[:3])
        writeln(self.fh, '\\pgfsetstrokecolor{currentstroke}')
        if gc.get_alpha() != 1.0:
            writeln(self.fh, '\\pgfsetstrokeopacity{%f}' % gc.get_alpha())
        dash_offset, dash_list = gc.get_dashes()
        ls = gc.get_linestyle(None)
        if ls == 'solid':
            writeln(self.fh, '\\pgfsetdash{}{0pt}')
        elif ls == 'dashed' or ls == 'dashdot' or ls == 'dotted':
            dash_str = '\\pgfsetdash{'
            for dash in dash_list:
                dash_str += '{%fpt}' % dash

            dash_str += '}{%fpt}' % dash_offset
            writeln(self.fh, dash_str)
        return

    def _print_pgf_path(self, path, transform):
        f = 1.0 / self.dpi
        for points, code in path.iter_segments(transform):
            if code == Path.MOVETO:
                x, y = tuple(points)
                writeln(self.fh, '\\pgfpathmoveto{\\pgfqpoint{%fin}{%fin}}' % (
                 f * x, f * y))
            elif code == Path.CLOSEPOLY:
                writeln(self.fh, '\\pgfpathclose')
            elif code == Path.LINETO:
                x, y = tuple(points)
                writeln(self.fh, '\\pgfpathlineto{\\pgfqpoint{%fin}{%fin}}' % (
                 f * x, f * y))
            elif code == Path.CURVE3:
                cx, cy, px, py = tuple(points)
                coords = (cx * f, cy * f, px * f, py * f)
                writeln(self.fh, '\\pgfpathquadraticcurveto{\\pgfqpoint{%fin}{%fin}}{\\pgfqpoint{%fin}{%fin}}' % coords)
            elif code == Path.CURVE4:
                c1x, c1y, c2x, c2y, px, py = tuple(points)
                coords = (c1x * f, c1y * f, c2x * f, c2y * f, px * f, py * f)
                writeln(self.fh, '\\pgfpathcurveto{\\pgfqpoint{%fin}{%fin}}{\\pgfqpoint{%fin}{%fin}}{\\pgfqpoint{%fin}{%fin}}' % coords)

    def _pgf_path_draw(self, stroke=True, fill=False):
        actions = []
        if stroke:
            actions.append('stroke')
        if fill:
            actions.append('fill')
        writeln(self.fh, '\\pgfusepath{%s}' % (',').join(actions))

    def draw_image(self, gc, x, y, im):
        path = os.path.dirname(self.fh.name)
        fname = os.path.splitext(os.path.basename(self.fh.name))[0]
        fname_img = '%s-img%d.png' % (fname, self.image_counter)
        self.image_counter += 1
        im.flipud_out()
        rows, cols, buf = im.as_rgba_str()
        _png.write_png(buf, cols, rows, os.path.join(path, fname_img))
        writeln(self.fh, '\\begin{pgfscope}')
        self._print_pgf_clip(gc)
        h, w = im.get_size_out()
        f = 1.0 / self.dpi
        writeln(self.fh, '\\pgftext[at=\\pgfqpoint{%fin}{%fin},left,bottom]{\\pgfimage[interpolate=true,width=%fin,height=%fin]{%s}}' % (x * f, y * f, w * f, h * f, fname_img))
        writeln(self.fh, '\\end{pgfscope}')

    def draw_tex(self, gc, x, y, s, prop, angle, ismath='TeX!'):
        self.draw_text(gc, x, y, s, prop, angle, ismath)

    def draw_text(self, gc, x, y, s, prop, angle, ismath=False):
        s = common_texification(s)
        prop_cmds = _font_properties_str(prop)
        s = '{%s %s}' % (prop_cmds, s)
        x = x * 1.0 / self.dpi
        y = y * 1.0 / self.dpi
        writeln(self.fh, '\\begin{pgfscope}')
        alpha = gc.get_alpha()
        if alpha != 1.0:
            writeln(self.fh, '\\pgfsetfillopacity{%f}' % alpha)
            writeln(self.fh, '\\pgfsetstrokeopacity{%f}' % alpha)
        stroke_rgb = tuple(gc.get_rgb())[:3]
        if stroke_rgb != (0, 0, 0):
            writeln(self.fh, '\\definecolor{textcolor}{rgb}{%f,%f,%f}' % stroke_rgb)
            writeln(self.fh, '\\pgfsetstrokecolor{textcolor}')
            writeln(self.fh, '\\pgfsetfillcolor{textcolor}')
        writeln(self.fh, '\\pgftext[left,bottom,x=%fin,y=%fin,rotate=%f]{%s}\n' % (x, y, angle, s))
        writeln(self.fh, '\\end{pgfscope}')

    def get_text_width_height_descent(self, s, prop, ismath):
        s = common_texification(s)
        w, h, d = self.latexManager.get_width_height_descent(s, prop)
        f = mpl_pt_to_in * self.dpi
        return (w * f, h * f, d * f)

    def flipy(self):
        return False

    def get_canvas_width_height(self):
        return (
         self.figure.get_figwidth(), self.figure.get_figheight())

    def points_to_pixels(self, points):
        return points * mpl_pt_to_in * self.dpi

    def new_gc(self):
        return GraphicsContextPgf()


class GraphicsContextPgf(GraphicsContextBase):
    pass


def draw_if_interactive():
    pass


def new_figure_manager(num, *args, **kwargs):
    """
    Create a new figure manager instance
    """
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasPgf(figure)
    manager = FigureManagerPgf(canvas, num)
    return manager


class TmpDirCleaner():
    remaining_tmpdirs = set()

    @staticmethod
    def add(tmpdir):
        TmpDirCleaner.remaining_tmpdirs.add(tmpdir)

    @staticmethod
    def cleanup_remaining_tmpdirs():
        for tmpdir in TmpDirCleaner.remaining_tmpdirs:
            try:
                shutil.rmtree(tmpdir)
            except:
                sys.stderr.write('error deleting tmp directory %s\n' % tmpdir)


class FigureCanvasPgf(FigureCanvasBase):
    filetypes = {'pgf': 'LaTeX PGF picture', 'pdf': 'LaTeX compiled PGF picture', 
       'png': 'Portable Network Graphics'}

    def __init__(self, *args):
        FigureCanvasBase.__init__(self, *args)

    def get_default_filetype(self):
        return 'pdf'

    def _print_pgf_to_fh(self, fh):
        header_text = '%% Creator: Matplotlib, PGF backend\n%%\n%% To include the figure in your LaTeX document, write\n%%   \\input{<filename>.pgf}\n%%\n%% Make sure the required packages are loaded in your preamble\n%%   \\usepackage{pgf}\n%%\n%% Figures using additional raster images can only be included by \\input if\n%% they are in the same directory as the main LaTeX file. For loading figures\n%% from other directories you can use the `import` package\n%%   \\usepackage{import}\n%% and then include the figures with\n%%   \\import{<path to file>}{<filename>.pgf}\n%%\n'
        header_info_preamble = [
         '%% Matplotlib used the following preamble']
        for line in get_preamble().splitlines():
            header_info_preamble.append('%%   ' + line)

        for line in get_fontspec().splitlines():
            header_info_preamble.append('%%   ' + line)

        header_info_preamble.append('%%')
        header_info_preamble = ('\n').join(header_info_preamble)
        w, h = self.figure.get_figwidth(), self.figure.get_figheight()
        fh.write(header_text)
        fh.write(header_info_preamble)
        fh.write('\n')
        writeln(fh, '\\begingroup')
        writeln(fh, '\\makeatletter')
        writeln(fh, '\\begin{pgfpicture}')
        writeln(fh, '\\pgfpathrectangle{\\pgfpointorigin}{\\pgfqpoint{%fin}{%fin}}' % (w, h))
        writeln(fh, '\\pgfusepath{use as bounding box}')
        renderer = RendererPgf(self.figure, fh)
        self.figure.draw(renderer)
        writeln(fh, '\\end{pgfpicture}')
        writeln(fh, '\\makeatother')
        writeln(fh, '\\endgroup')

    def print_pgf(self, fname_or_fh, *args, **kwargs):
        """
        Output pgf commands for drawing the figure so it can be included and
        rendered in latex documents.
        """
        if kwargs.get('dryrun', False):
            return
        if is_string_like(fname_or_fh):
            with codecs.open(fname_or_fh, 'w', encoding='utf-8') as (fh):
                self._print_pgf_to_fh(fh)
        elif is_writable_file_like(fname_or_fh):
            raise ValueError('saving pgf to a stream is not supported, ' + 'consider using the pdf option of the pgf-backend')
        else:
            raise ValueError('filename must be a path')

    def _print_pdf_to_fh(self, fh):
        w, h = self.figure.get_figwidth(), self.figure.get_figheight()
        try:
            tmpdir = tempfile.mkdtemp(prefix='mpl_pgf_')
            fname_pgf = os.path.join(tmpdir, 'figure.pgf')
            fname_tex = os.path.join(tmpdir, 'figure.tex')
            fname_pdf = os.path.join(tmpdir, 'figure.pdf')
            self.print_pgf(fname_pgf)
            latex_preamble = get_preamble()
            latex_fontspec = get_fontspec()
            latexcode = '\n\\documentclass[12pt]{minimal}\n\\usepackage[paperwidth=%fin, paperheight=%fin, margin=0in]{geometry}\n%s\n%s\n\\usepackage{pgf}\n\n\\begin{document}\n\\centering\n\\input{figure.pgf}\n\\end{document}' % (w, h, latex_preamble, latex_fontspec)
            with codecs.open(fname_tex, 'w', 'utf-8') as (fh_tex):
                fh_tex.write(latexcode)
            texcommand = get_texcommand()
            cmdargs = [texcommand, '-interaction=nonstopmode',
             '-halt-on-error', 'figure.tex']
            try:
                check_output(cmdargs, stderr=subprocess.STDOUT, cwd=tmpdir)
            except subprocess.CalledProcessError as e:
                raise RuntimeError('%s was not able to process your file.\n\nFull log:\n%s' % (texcommand, e.output))

            with open(fname_pdf, 'rb') as (fh_src):
                shutil.copyfileobj(fh_src, fh)
        finally:
            try:
                shutil.rmtree(tmpdir)
            except:
                TmpDirCleaner.add(tmpdir)

    def print_pdf(self, fname_or_fh, *args, **kwargs):
        """
        Use LaTeX to compile a Pgf generated figure to PDF.
        """
        if is_string_like(fname_or_fh):
            with open(fname_or_fh, 'wb') as (fh):
                self._print_pdf_to_fh(fh)
        elif is_writable_file_like(fname_or_fh):
            self._print_pdf_to_fh(fname_or_fh)
        else:
            raise ValueError('filename must be a path or a file-like object')

    def _print_png_to_fh(self, fh):
        converter = make_pdf_to_png_converter()
        try:
            tmpdir = tempfile.mkdtemp(prefix='mpl_pgf_')
            fname_pdf = os.path.join(tmpdir, 'figure.pdf')
            fname_png = os.path.join(tmpdir, 'figure.png')
            self.print_pdf(fname_pdf)
            converter(fname_pdf, fname_png, dpi=self.figure.dpi)
            with open(fname_png, 'rb') as (fh_src):
                shutil.copyfileobj(fh_src, fh)
        finally:
            try:
                shutil.rmtree(tmpdir)
            except:
                TmpDirCleaner.add(tmpdir)

    def print_png(self, fname_or_fh, *args, **kwargs):
        """
        Use LaTeX to compile a pgf figure to pdf and convert it to png.
        """
        if is_string_like(fname_or_fh):
            with open(fname_or_fh, 'wb') as (fh):
                self._print_png_to_fh(fh)
        elif is_writable_file_like(fname_or_fh):
            self._print_png_to_fh(fname_or_fh)
        else:
            raise ValueError('filename must be a path or a file-like object')

    def _render_texts_pgf(self, fh):
        valign = {'top': 'top', 'bottom': 'bottom', 'baseline': 'base', 'center': ''}
        halign = {'left': 'left', 'right': 'right', 'center': ''}
        rvalign = {'top': 'left', 'bottom': 'right', 'baseline': 'right', 'center': ''}
        rhalign = {'left': 'top', 'right': 'bottom', 'center': ''}
        for tick in self.figure.findobj(mpl.axis.Tick):
            tick.label1.set_visible(tick.label1On)
            tick.label2.set_visible(tick.label2On)

        for legend in self.figure.findobj(mpl.legend.Legend):
            labels = legend.findobj(mpl.text.Text)
            labels[0].set_visible(False)

        texts = self.figure.findobj(match=Text, include_self=False)
        texts = list(set(texts))
        for text in texts:
            s = text.get_text()
            if not s or not text.get_visible():
                continue
            s = common_texification(s)
            fontsize = text.get_fontsize()
            angle = text.get_rotation()
            transform = text.get_transform()
            x, y = transform.transform_point(text.get_position())
            x = x * 1.0 / self.figure.dpi
            y = y * 1.0 / self.figure.dpi
            if angle == 90.0:
                align = rvalign[text.get_va()] + ',' + rhalign[text.get_ha()]
            else:
                align = valign[text.get_va()] + ',' + halign[text.get_ha()]
            s = '{\\fontsize{%f}{%f}\\selectfont %s}' % (fontsize, fontsize * 1.2, s)
            writeln(fh, '\\pgftext[%s,x=%fin,y=%fin,rotate=%f]{%s}' % (align, x, y, angle, s))

    def get_renderer(self):
        return RendererPgf(self.figure, None)


class FigureManagerPgf(FigureManagerBase):

    def __init__(self, *args):
        FigureManagerBase.__init__(self, *args)


FigureManager = FigureManagerPgf

def _cleanup_all():
    LatexManager._cleanup_remaining_instances()
    TmpDirCleaner.cleanup_remaining_tmpdirs()


atexit.register(_cleanup_all)