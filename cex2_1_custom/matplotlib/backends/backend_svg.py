# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\backend_svg.pyc
# Compiled at: 2012-11-06 08:42:20
from __future__ import division
import os, base64, tempfile, urllib, gzip, io, sys, codecs, numpy as np
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

from matplotlib import verbose, __version__, rcParams
from matplotlib.backend_bases import RendererBase, GraphicsContextBase, FigureManagerBase, FigureCanvasBase
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.cbook import is_string_like, is_writable_file_like, maxdict
from matplotlib.colors import rgb2hex
from matplotlib.figure import Figure
from matplotlib.font_manager import findfont, FontProperties
from matplotlib.ft2font import FT2Font, KERNING_DEFAULT, LOAD_NO_HINTING
from matplotlib.mathtext import MathTextParser
from matplotlib.path import Path
from matplotlib import _path
from matplotlib.transforms import Affine2D, Affine2DBase
from matplotlib import _png
from xml.sax.saxutils import escape as escape_xml_text
backend_version = __version__

def escape_cdata(s):
    s = s.replace('&', '&amp;')
    s = s.replace('<', '&lt;')
    s = s.replace('>', '&gt;')
    return s


def escape_attrib(s):
    s = s.replace('&', '&amp;')
    s = s.replace("'", '&apos;')
    s = s.replace('"', '&quot;')
    s = s.replace('<', '&lt;')
    s = s.replace('>', '&gt;')
    return s


class XMLWriter():

    def __init__(self, file):
        self.__write = file.write
        if hasattr(file, 'flush'):
            self.flush = file.flush
        self.__open = 0
        self.__tags = []
        self.__data = []
        self.__indentation = ' ' * 64

    def __flush(self, indent=True):
        if self.__open:
            if indent:
                self.__write('>\n')
            else:
                self.__write('>')
            self.__open = 0
        if self.__data:
            data = ('').join(self.__data)
            self.__write(escape_cdata(data))
            self.__data = []

    def start(self, tag, attrib={}, **extra):
        self.__flush()
        tag = escape_cdata(tag)
        self.__data = []
        self.__tags.append(tag)
        self.__write(self.__indentation[:len(self.__tags) - 1])
        self.__write('<%s' % tag)
        if attrib or extra:
            attrib = attrib.copy()
            attrib.update(extra)
            attrib = attrib.items()
            attrib.sort()
            for k, v in attrib:
                if not v == '':
                    k = escape_cdata(k)
                    v = escape_attrib(v)
                    self.__write(' %s="%s"' % (k, v))

        self.__open = 1
        return len(self.__tags) - 1

    def comment(self, comment):
        self.__flush()
        self.__write(self.__indentation[:len(self.__tags)])
        self.__write('<!-- %s -->\n' % escape_cdata(comment))

    def data(self, text):
        self.__data.append(text)

    def end(self, tag=None, indent=True):
        if tag:
            assert self.__tags, 'unbalanced end(%s)' % tag
            assert escape_cdata(tag) == self.__tags[-1], 'expected end(%s), got %s' % (self.__tags[-1], tag)
        else:
            assert self.__tags, 'unbalanced end()'
        tag = self.__tags.pop()
        if self.__data:
            self.__flush(indent)
        elif self.__open:
            self.__open = 0
            self.__write('/>\n')
            return
        if indent:
            self.__write(self.__indentation[:len(self.__tags)])
        self.__write('</%s>\n' % tag)

    def close(self, id):
        while len(self.__tags) > id:
            self.end()

    def element(self, tag, text=None, attrib={}, **extra):
        apply(self.start, (tag, attrib), extra)
        if text:
            self.data(text)
        self.end(indent=False)

    def flush(self):
        pass


def generate_transform(transform_list=[]):
    if len(transform_list):
        output = io.StringIO()
        for type, value in transform_list:
            if type == 'scale' and (value == (1.0, ) or value == (1.0, 1.0)):
                continue
            if type == 'translate' and value == (0.0, 0.0):
                continue
            if type == 'rotate' and value == (0.0, ):
                continue
            if type == 'matrix' and isinstance(value, Affine2DBase):
                value = value.to_values()
            output.write('%s(%s)' % (type, (' ').join(str(x) for x in value)))

        return output.getvalue()
    return ''


def generate_css(attrib={}):
    if attrib:
        output = io.StringIO()
        attrib = attrib.items()
        attrib.sort()
        for k, v in attrib:
            k = escape_attrib(k)
            v = escape_attrib(v)
            output.write('%s:%s;' % (k, v))

        return output.getvalue()
    return ''


_capstyle_d = {'projecting': 'square', 'butt': 'butt', 'round': 'round'}

class RendererSVG(RendererBase):
    FONT_SCALE = 100.0
    fontd = maxdict(50)

    def __init__(self, width, height, svgwriter, basename=None):
        self.width = width
        self.height = height
        self.writer = XMLWriter(svgwriter)
        self._groupd = {}
        if not (rcParams['svg.image_inline'] or basename is not None):
            raise AssertionError
            self.basename = basename
            self._imaged = {}
        self._clipd = {}
        self._char_defs = {}
        self._markers = {}
        self._path_collection_id = 0
        self._imaged = {}
        self._hatchd = {}
        self._has_gouraud = False
        self._n_gradients = 0
        self._fonts = {}
        self.mathtext_parser = MathTextParser('SVG')
        RendererBase.__init__(self)
        self._glyph_map = dict()
        svgwriter.write(svgProlog)
        self._start_id = self.writer.start('svg', width='%ipt' % width, height='%ipt' % height, viewBox='0 0 %i %i' % (width, height), xmlns='http://www.w3.org/2000/svg', version='1.1', attrib={'xmlns:xlink': 'http://www.w3.org/1999/xlink'})
        self._write_default_style()
        return

    def finalize(self):
        self._write_clips()
        self._write_hatches()
        self._write_svgfonts()
        self.writer.close(self._start_id)
        self.writer.flush()

    def _write_default_style(self):
        writer = self.writer
        default_style = generate_css({'stroke-linejoin': 'round', 
           'stroke-linecap': 'square'})
        writer.start('defs')
        writer.start('style', type='text/css')
        writer.data('*{%s}\n' % default_style)
        writer.end('style')
        writer.end('defs')

    def _make_id(self, type, content):
        content = str(content)
        if sys.version_info[0] >= 3:
            content = content.encode('utf8')
        return '%s%s' % (type, md5(content).hexdigest()[:10])

    def _make_flip_transform(self, transform):
        return transform + Affine2D().scale(1.0, -1.0).translate(0.0, self.height)

    def _get_font(self, prop):
        key = hash(prop)
        font = self.fontd.get(key)
        if font is None:
            fname = findfont(prop)
            font = self.fontd.get(fname)
            if font is None:
                font = FT2Font(str(fname))
                self.fontd[fname] = font
            self.fontd[key] = font
        font.clear()
        size = prop.get_size_in_points()
        font.set_size(size, 72.0)
        return font

    def _get_hatch(self, gc, rgbFace):
        """
        Create a new hatch pattern
        """
        if rgbFace is not None:
            rgbFace = tuple(rgbFace)
        edge = gc.get_rgb()
        if edge is not None:
            edge = tuple(edge)
        dictkey = (
         gc.get_hatch(), rgbFace, edge)
        oid = self._hatchd.get(dictkey)
        if oid is None:
            oid = self._make_id('h', dictkey)
            self._hatchd[dictkey] = ((gc.get_hatch_path(), rgbFace, edge), oid)
        else:
            _, oid = oid
        return oid

    def _write_hatches(self):
        if not len(self._hatchd):
            return
        else:
            HATCH_SIZE = 72
            writer = self.writer
            writer.start('defs')
            for (path, face, stroke), oid in self._hatchd.values():
                writer.start('pattern', id=oid, patternUnits='userSpaceOnUse', x='0', y='0', width=unicode(HATCH_SIZE), height=unicode(HATCH_SIZE))
                path_data = self._convert_path(path, Affine2D().scale(HATCH_SIZE).scale(1.0, -1.0).translate(0, HATCH_SIZE), simplify=False)
                if face is None:
                    fill = 'none'
                else:
                    fill = rgb2hex(face)
                writer.element('rect', x='0', y='0', width=unicode(HATCH_SIZE + 1), height=unicode(HATCH_SIZE + 1), fill=fill)
                writer.element('path', d=path_data, style=generate_css({'fill': rgb2hex(stroke), 
                   'stroke': rgb2hex(stroke), 
                   'stroke-width': '1.0', 
                   'stroke-linecap': 'butt', 
                   'stroke-linejoin': 'miter'}))
                writer.end('pattern')

            writer.end('defs')
            return

    def _get_style_dict(self, gc, rgbFace):
        """
        return the style string.  style is generated from the
        GraphicsContext and rgbFace
        """
        attrib = {}
        if gc.get_hatch() is not None:
            attrib['fill'] = 'url(#%s)' % self._get_hatch(gc, rgbFace)
        elif rgbFace is None:
            attrib['fill'] = 'none'
        elif tuple(rgbFace[:3]) != (0, 0, 0):
            attrib['fill'] = rgb2hex(rgbFace)
        if gc.get_alpha() != 1.0:
            attrib['opacity'] = str(gc.get_alpha())
        offset, seq = gc.get_dashes()
        if seq is not None:
            attrib['stroke-dasharray'] = (',').join([ '%f' % val for val in seq ])
            attrib['stroke-dashoffset'] = unicode(float(offset))
        linewidth = gc.get_linewidth()
        if linewidth:
            attrib['stroke'] = rgb2hex(gc.get_rgb())
            if linewidth != 1.0:
                attrib['stroke-width'] = str(linewidth)
            if gc.get_joinstyle() != 'round':
                attrib['stroke-linejoin'] = gc.get_joinstyle()
            if gc.get_capstyle() != 'projecting':
                attrib['stroke-linecap'] = _capstyle_d[gc.get_capstyle()]
        return attrib

    def _get_style(self, gc, rgbFace):
        return generate_css(self._get_style_dict(gc, rgbFace))

    def _get_clip(self, gc):
        cliprect = gc.get_clip_rectangle()
        clippath, clippath_trans = gc.get_clip_path()
        if clippath is not None:
            clippath_trans = self._make_flip_transform(clippath_trans)
            dictkey = (id(clippath), str(clippath_trans))
        elif cliprect is not None:
            x, y, w, h = cliprect.bounds
            y = self.height - (y + h)
            dictkey = (x, y, w, h)
        else:
            return
        clip = self._clipd.get(dictkey)
        if clip is None:
            oid = self._make_id('p', dictkey)
            if clippath is not None:
                self._clipd[dictkey] = (
                 (
                  clippath, clippath_trans), oid)
            else:
                self._clipd[dictkey] = (
                 dictkey, oid)
        else:
            clip, oid = clip
        return oid

    def _write_clips(self):
        if not len(self._clipd):
            return
        writer = self.writer
        writer.start('defs')
        for clip, oid in self._clipd.values():
            writer.start('clipPath', id=oid)
            if len(clip) == 2:
                clippath, clippath_trans = clip
                path_data = self._convert_path(clippath, clippath_trans, simplify=False)
                writer.element('path', d=path_data)
            else:
                x, y, w, h = clip
                writer.element('rect', x=unicode(x), y=unicode(y), width=unicode(w), height=unicode(h))
            writer.end('clipPath')

        writer.end('defs')

    def _write_svgfonts(self):
        if not rcParams['svg.fonttype'] == 'svgfont':
            return
        writer = self.writer
        writer.start('defs')
        for font_fname, chars in self._fonts.items():
            font = FT2Font(font_fname)
            font.set_size(72, 72)
            sfnt = font.get_sfnt()
            writer.start('font', id=sfnt[(1, 0, 0, 4)])
            writer.element('font-face', attrib={'font-family': font.family_name, 
               'font-style': font.style_name.lower(), 
               'units-per-em': '72', 
               'bbox': (' ').join(unicode(x / 64.0) for x in font.bbox)})
            for char in chars:
                glyph = font.load_char(char, flags=LOAD_NO_HINTING)
                verts, codes = font.get_path()
                path = Path(verts, codes)
                path_data = self._convert_path(path)
                writer.element('glyph', d=path_data, attrib={'unicode': unichr(char), 
                   'horiz-adv-x': unicode(glyph.linearHoriAdvance / 65536.0)})

            writer.end('font')

        writer.end('defs')

    def open_group(self, s, gid=None):
        """
        Open a grouping element with label *s*. If *gid* is given, use
        *gid* as the id of the group.
        """
        if gid:
            self.writer.start('g', id=gid)
        else:
            self._groupd[s] = self._groupd.get(s, 0) + 1
            self.writer.start('g', id='%s_%d' % (s, self._groupd[s]))

    def close_group(self, s):
        self.writer.end('g')

    def option_image_nocomposite(self):
        """
        if svg.image_noscale is True, compositing multiple images into one is prohibited
        """
        return rcParams['svg.image_noscale']

    def _convert_path(self, path, transform=None, clip=None, simplify=None):
        if clip:
            clip = (
             0.0, 0.0, self.width, self.height)
        else:
            clip = None
        return _path.convert_to_svg(path, transform, clip, simplify, 6)

    def draw_path(self, gc, path, transform, rgbFace=None):
        trans_and_flip = self._make_flip_transform(transform)
        clip = rgbFace is None and gc.get_hatch_path() is None
        simplify = path.should_simplify and clip
        path_data = self._convert_path(path, trans_and_flip, clip=clip, simplify=simplify)
        attrib = {}
        attrib['style'] = self._get_style(gc, rgbFace)
        clipid = self._get_clip(gc)
        if clipid is not None:
            attrib['clip-path'] = 'url(#%s)' % clipid
        if gc.get_url() is not None:
            self.writer.start('a', {'xlink:href': gc.get_url()})
        self.writer.element('path', d=path_data, attrib=attrib)
        if gc.get_url() is not None:
            self.writer.end('a')
        return

    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace=None):
        if not len(path.vertices):
            return
        else:
            writer = self.writer
            path_data = self._convert_path(marker_path, marker_trans + Affine2D().scale(1.0, -1.0), simplify=False)
            style = self._get_style_dict(gc, rgbFace)
            dictkey = (path_data, generate_css(style))
            oid = self._markers.get(dictkey)
            for key in style.keys():
                if not key.startswith('stroke'):
                    del style[key]

            style = generate_css(style)
            if oid is None:
                oid = self._make_id('m', dictkey)
                writer.start('defs')
                writer.element('path', id=oid, d=path_data, style=style)
                writer.end('defs')
                self._markers[dictkey] = oid
            attrib = {}
            clipid = self._get_clip(gc)
            if clipid is not None:
                attrib['clip-path'] = 'url(#%s)' % clipid
            writer.start('g', attrib=attrib)
            trans_and_flip = self._make_flip_transform(trans)
            attrib = {'xlink:href': '#%s' % oid}
            for vertices, code in path.iter_segments(trans_and_flip, simplify=False):
                if len(vertices):
                    x, y = vertices[-2:]
                    attrib['x'] = unicode(x)
                    attrib['y'] = unicode(y)
                    attrib['style'] = self._get_style(gc, rgbFace)
                    writer.element('use', attrib=attrib)

            writer.end('g')
            return

    def draw_path_collection(self, gc, master_transform, paths, all_transforms, offsets, offsetTrans, facecolors, edgecolors, linewidths, linestyles, antialiaseds, urls, offset_position):
        writer = self.writer
        path_codes = []
        writer.start('defs')
        for i, (path, transform) in enumerate(self._iter_collection_raw_paths(master_transform, paths, all_transforms)):
            transform = Affine2D(transform.get_matrix()).scale(1.0, -1.0)
            d = self._convert_path(path, transform, simplify=False)
            oid = 'C%x_%x_%s' % (self._path_collection_id, i,
             self._make_id('', d))
            writer.element('path', id=oid, d=d)
            path_codes.append(oid)

        writer.end('defs')
        for xo, yo, path_id, gc0, rgbFace in self._iter_collection(gc, master_transform, all_transforms, path_codes, offsets, offsetTrans, facecolors, edgecolors, linewidths, linestyles, antialiaseds, urls, offset_position):
            clipid = self._get_clip(gc0)
            url = gc0.get_url()
            if url is not None:
                writer.start('a', attrib={'xlink:href': url})
            if clipid is not None:
                writer.start('g', attrib={'clip-path': 'url(#%s)' % clipid})
            attrib = {'xlink:href': '#%s' % path_id, 'x': unicode(xo), 
               'y': unicode(self.height - yo), 
               'style': self._get_style(gc0, rgbFace)}
            writer.element('use', attrib=attrib)
            if clipid is not None:
                writer.end('g')
            if url is not None:
                writer.end('a')

        self._path_collection_id += 1
        return

    def draw_gouraud_triangle(self, gc, points, colors, trans):
        writer = self.writer
        if not self._has_gouraud:
            self._has_gouraud = True
            writer.start('filter', id='colorAdd')
            writer.element('feComposite', attrib={'in': 'SourceGraphic'}, in2='BackgroundImage', operator='arithmetic', k2='1', k3='1')
            writer.end('filter')
        avg_color = np.sum(colors[:, :], axis=0) / 3.0
        if avg_color[-1] == 0.0:
            return
        trans_and_flip = self._make_flip_transform(trans)
        tpoints = trans_and_flip.transform(points)
        writer.start('defs')
        for i in range(3):
            x1, y1 = tpoints[i]
            x2, y2 = tpoints[(i + 1) % 3]
            x3, y3 = tpoints[(i + 2) % 3]
            c = colors[i][:]
            if x2 == x3:
                xb = x2
                yb = y1
            elif y2 == y3:
                xb = x1
                yb = y2
            else:
                m1 = (y2 - y3) / (x2 - x3)
                b1 = y2 - m1 * x2
                m2 = -(1.0 / m1)
                b2 = y1 - m2 * x1
                xb = (-b1 + b2) / (m1 - m2)
                yb = m2 * xb + b2
            writer.start('linearGradient', id='GR%x_%d' % (self._n_gradients, i), x1=unicode(x1), y1=unicode(y1), x2=unicode(xb), y2=unicode(yb))
            writer.element('stop', offset='0', style=generate_css({'stop-color': rgb2hex(c), 'stop-opacity': unicode(c[-1])}))
            writer.element('stop', offset='1', style=generate_css({'stop-color': rgb2hex(c), 'stop-opacity': '0'}))
            writer.end('linearGradient')

        writer.element('polygon', id='GT%x' % self._n_gradients, points=(' ').join([ unicode(x) for x in (x1, y1, x2, y2, x3, y3) ]))
        writer.end('defs')
        avg_color = np.sum(colors[:, :], axis=0) / 3.0
        href = '#GT%x' % self._n_gradients
        writer.element('use', attrib={'xlink:href': href, 'fill': rgb2hex(avg_color), 
           'fill-opacity': str(avg_color[-1])})
        for i in range(3):
            writer.element('use', attrib={'xlink:href': href, 'fill': 'url(#GR%x_%d)' % (self._n_gradients, i), 
               'fill-opacity': '1', 
               'filter': 'url(#colorAdd)'})

        self._n_gradients += 1

    def draw_gouraud_triangles(self, gc, triangles_array, colors_array, transform):
        attrib = {}
        clipid = self._get_clip(gc)
        if clipid is not None:
            attrib['clip-path'] = 'url(#%s)' % clipid
        self.writer.start('g', attrib=attrib)
        transform = transform.frozen()
        for tri, col in zip(triangles_array, colors_array):
            self.draw_gouraud_triangle(gc, tri, col, transform)

        self.writer.end('g')
        return

    def option_scale_image(self):
        return True

    def draw_image(self, gc, x, y, im, dx=None, dy=None, transform=None):
        attrib = {}
        clipid = self._get_clip(gc)
        if clipid is not None:
            self.writer.start('g', attrib={'clip-path': 'url(#%s)' % clipid})
        trans = [1, 0, 0, 1, 0, 0]
        if rcParams['svg.image_noscale']:
            trans = list(im.get_matrix())
            trans[5] = -trans[5]
            attrib['transform'] = generate_transform([('matrix', tuple(trans))])
            assert trans[1] == 0
            assert trans[2] == 0
            numrows, numcols = im.get_size()
            im.reset_matrix()
            im.set_interpolation(0)
            im.resize(numcols, numrows)
        h, w = im.get_size_out()
        oid = getattr(im, '_gid', None)
        url = getattr(im, '_url', None)
        if url is not None:
            self.writer.start('a', attrib={'xlink:href': url})
        if rcParams['svg.image_inline']:
            bytesio = io.BytesIO()
            im.flipud_out()
            rows, cols, buffer = im.as_rgba_str()
            _png.write_png(buffer, cols, rows, bytesio)
            im.flipud_out()
            oid = oid or self._make_id('image', bytesio)
            attrib['xlink:href'] = 'data:image/png;base64,\n' + base64.b64encode(bytesio.getvalue()).decode('ascii')
        else:
            self._imaged[self.basename] = self._imaged.get(self.basename, 0) + 1
            filename = '%s.image%d.png' % (self.basename, self._imaged[self.basename])
            verbose.report('Writing image file for inclusion: %s' % filename)
            im.flipud_out()
            rows, cols, buffer = im.as_rgba_str()
            _png.write_png(buffer, cols, rows, filename)
            im.flipud_out()
            oid = oid or 'Im_' + self._make_id('image', filename)
            attrib['xlink:href'] = filename
        alpha = gc.get_alpha()
        if alpha != 1.0:
            attrib['opacity'] = str(alpha)
        attrib['id'] = oid
        if transform is None:
            self.writer.element('image', x=unicode(x / trans[0]), y=unicode((self.height - y) / trans[3] - h), width=unicode(w), height=unicode(h), attrib=attrib)
        else:
            flipped = self._make_flip_transform(transform)
            flipped = np.array(flipped.to_values())
            y = y + dy
            if dy > 0.0:
                flipped[3] *= -1.0
                y *= -1.0
            attrib['transform'] = generate_transform([
             (
              'matrix', flipped)])
            self.writer.element('image', x=unicode(x), y=unicode(y), width=unicode(dx), height=unicode(abs(dy)), attrib=attrib)
        if url is not None:
            self.writer.end('a')
        if clipid is not None:
            self.writer.end('g')
        return

    def _adjust_char_id(self, char_id):
        return char_id.replace('%20', '_')

    def _draw_text_as_path(self, gc, x, y, s, prop, angle, ismath):
        """
        draw the text by converting them to paths using textpath module.

        *prop*
          font property

        *s*
          text to be converted

        *usetex*
          If True, use matplotlib usetex mode.

        *ismath*
          If True, use mathtext parser. If "TeX", use *usetex* mode.
        """
        writer = self.writer
        writer.comment(s)
        glyph_map = self._glyph_map
        text2path = self._text2path
        color = rgb2hex(gc.get_rgb())
        fontsize = prop.get_size_in_points()
        style = {}
        if color != '#000000':
            style['fill'] = color
        if gc.get_alpha() != 1.0:
            style['opacity'] = unicode(gc.get_alpha())
        if not ismath:
            font = text2path._get_font(prop)
            _glyphs = text2path.get_glyphs_with_font(font, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            glyph_info, glyph_map_new, rects = _glyphs
            y -= font.get_descent() / 64.0 * (prop.get_size_in_points() / text2path.FONT_SCALE)
            if glyph_map_new:
                writer.start('defs')
                for char_id, glyph_path in glyph_map_new.iteritems():
                    path = Path(*glyph_path)
                    path_data = self._convert_path(path, simplify=False)
                    writer.element('path', id=char_id, d=path_data)

                writer.end('defs')
                glyph_map.update(glyph_map_new)
            attrib = {}
            attrib['style'] = generate_css(style)
            font_scale = fontsize / text2path.FONT_SCALE
            attrib['transform'] = generate_transform([
             (
              'translate', (x, y)),
             (
              'rotate', (-angle,)),
             (
              'scale', (font_scale, -font_scale))])
            writer.start('g', attrib=attrib)
            for glyph_id, xposition, yposition, scale in glyph_info:
                attrib = {'xlink:href': '#%s' % glyph_id}
                if xposition != 0.0:
                    attrib['x'] = str(xposition)
                if yposition != 0.0:
                    attrib['y'] = str(yposition)
                writer.element('use', attrib=attrib)

            writer.end('g')
        else:
            if ismath == 'TeX':
                _glyphs = text2path.get_glyphs_tex(prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            else:
                _glyphs = text2path.get_glyphs_mathtext(prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            glyph_info, glyph_map_new, rects = _glyphs
            if glyph_map_new:
                writer.start('defs')
                for char_id, glyph_path in glyph_map_new.iteritems():
                    char_id = self._adjust_char_id(char_id)
                    if not len(glyph_path[0]):
                        path_data = ''
                    else:
                        path = Path(*glyph_path)
                        path_data = self._convert_path(path, simplify=False)
                    writer.element('path', id=char_id, d=path_data)

                writer.end('defs')
                glyph_map.update(glyph_map_new)
            attrib = {}
            font_scale = fontsize / text2path.FONT_SCALE
            attrib['style'] = generate_css(style)
            attrib['transform'] = generate_transform([
             (
              'translate', (x, y)),
             (
              'rotate', (-angle,)),
             (
              'scale', (font_scale, -font_scale))])
            writer.start('g', attrib=attrib)
            for char_id, xposition, yposition, scale in glyph_info:
                char_id = self._adjust_char_id(char_id)
                writer.element('use', transform=generate_transform([
                 (
                  'translate', (xposition, yposition)),
                 (
                  'scale', (scale,))]), attrib={'xlink:href': '#%s' % char_id})

            for verts, codes in rects:
                path = Path(verts, codes)
                path_data = self._convert_path(path, simplify=False)
                writer.element('path', d=path_data)

            writer.end('g')

    def _draw_text_as_text(self, gc, x, y, s, prop, angle, ismath):
        writer = self.writer
        color = rgb2hex(gc.get_rgb())
        style = {}
        if color != '#000000':
            style['fill'] = color
        if gc.get_alpha() != 1.0:
            style['opacity'] = unicode(gc.get_alpha())
        if not ismath:
            font = self._get_font(prop)
            font.set_text(s, 0.0, flags=LOAD_NO_HINTING)
            y -= font.get_descent() / 64.0
            fontsize = prop.get_size_in_points()
            fontfamily = font.family_name
            fontstyle = prop.get_style()
            attrib = {}
            style['font-size'] = str(fontsize) + 'px'
            style['font-family'] = str(fontfamily)
            style['font-style'] = prop.get_style().lower()
            attrib['style'] = generate_css(style)
            attrib['transform'] = generate_transform([
             (
              'translate', (x, y)),
             (
              'rotate', (-angle,))])
            writer.element('text', s, attrib=attrib)
            if rcParams['svg.fonttype'] == 'svgfont':
                fontset = self._fonts.setdefault(font.fname, set())
                for c in s:
                    fontset.add(ord(c))

        else:
            writer.comment(s)
            width, height, descent, svg_elements, used_characters = self.mathtext_parser.parse(s, 72, prop)
            svg_glyphs = svg_elements.svg_glyphs
            svg_rects = svg_elements.svg_rects
            attrib = {}
            attrib['style'] = generate_css(style)
            attrib['transform'] = generate_transform([
             (
              'translate', (x, y)),
             (
              'rotate', (-angle,))])
            writer.start('g', attrib=attrib)
            writer.start('text')
            spans = {}
            for font, fontsize, thetext, new_x, new_y, metrics in svg_glyphs:
                style = generate_css({'font-size': unicode(fontsize) + 'px', 
                   'font-family': font.family_name, 
                   'font-style': font.style_name.lower()})
                if thetext == 32:
                    thetext = 160
                spans.setdefault(style, []).append((new_x, -new_y, thetext))

            if rcParams['svg.fonttype'] == 'svgfont':
                for font, fontsize, thetext, new_x, new_y, metrics in svg_glyphs:
                    fontset = self._fonts.setdefault(font.fname, set())
                    fontset.add(thetext)

            for style, chars in spans.items():
                chars.sort()
                same_y = True
                if len(chars) > 1:
                    last_y = chars[0][1]
                    for i in xrange(1, len(chars)):
                        if chars[i][1] != last_y:
                            same_y = False
                            break

                if same_y:
                    ys = unicode(chars[0][1])
                else:
                    ys = (' ').join(unicode(c[1]) for c in chars)
                attrib = {'style': style, 
                   'x': (' ').join(unicode(c[0]) for c in chars), 
                   'y': ys}
                writer.element('tspan', ('').join(unichr(c[2]) for c in chars), attrib=attrib)

            writer.end('text')
            if len(svg_rects):
                for x, y, width, height in svg_rects:
                    writer.element('rect', x=unicode(x), y=unicode(-y + height), width=unicode(width), height=unicode(height))

            writer.end('g')

    def draw_tex(self, gc, x, y, s, prop, angle):
        self._draw_text_as_path(gc, x, y, s, prop, angle, ismath='TeX')

    def draw_text(self, gc, x, y, s, prop, angle, ismath):
        clipid = self._get_clip(gc)
        if clipid is not None:
            self.writer.start('g', attrib={'clip-path': 'url(#%s)' % clipid})
        if rcParams['svg.fonttype'] == 'path':
            self._draw_text_as_path(gc, x, y, s, prop, angle, ismath)
        else:
            self._draw_text_as_text(gc, x, y, s, prop, angle, ismath)
        if clipid is not None:
            self.writer.end('g')
        return

    def flipy(self):
        return True

    def get_canvas_width_height(self):
        return (
         self.width, self.height)

    def get_text_width_height_descent(self, s, prop, ismath):
        return self._text2path.get_text_width_height_descent(s, prop, ismath)


class FigureCanvasSVG(FigureCanvasBase):
    filetypes = {'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics'}

    def print_svg(self, filename, *args, **kwargs):
        if is_string_like(filename):
            fh_to_close = svgwriter = io.open(filename, 'w', encoding='utf-8')
        elif is_writable_file_like(filename):
            if not isinstance(filename, io.TextIOBase):
                if sys.version_info[0] >= 3:
                    svgwriter = io.TextIOWrapper(filename, 'utf-8')
                else:
                    svgwriter = codecs.getwriter('utf-8')(filename)
            else:
                svgwriter = filename
            fh_to_close = None
        else:
            raise ValueError('filename must be a path or a file-like object')
        return self._print_svg(filename, svgwriter, fh_to_close, **kwargs)

    def print_svgz(self, filename, *args, **kwargs):
        if is_string_like(filename):
            fh_to_close = gzipwriter = gzip.GzipFile(filename, 'w')
            svgwriter = io.TextIOWrapper(gzipwriter, 'utf-8')
        elif is_writable_file_like(filename):
            fh_to_close = gzipwriter = gzip.GzipFile(fileobj=filename, mode='w')
            svgwriter = io.TextIOWrapper(gzipwriter, 'utf-8')
        else:
            raise ValueError('filename must be a path or a file-like object')
        return self._print_svg(filename, svgwriter, fh_to_close)

    def _print_svg(self, filename, svgwriter, fh_to_close=None, **kwargs):
        try:
            self.figure.set_dpi(72.0)
            width, height = self.figure.get_size_inches()
            w, h = width * 72, height * 72
            if rcParams['svg.image_noscale']:
                renderer = RendererSVG(w, h, svgwriter, filename)
            else:
                image_dpi = 72
                _bbox_inches_restore = kwargs.pop('bbox_inches_restore', None)
                renderer = MixedModeRenderer(self.figure, width, height, image_dpi, RendererSVG(w, h, svgwriter, filename), bbox_inches_restore=_bbox_inches_restore)
            self.figure.draw(renderer)
            renderer.finalize()
        finally:
            if fh_to_close is not None:
                svgwriter.close()

        return

    def get_default_filetype(self):
        return 'svg'


class FigureManagerSVG(FigureManagerBase):
    pass


FigureManager = FigureManagerSVG

def new_figure_manager(num, *args, **kwargs):
    FigureClass = kwargs.pop('FigureClass', Figure)
    thisFig = FigureClass(*args, **kwargs)
    return new_figure_manager_given_figure(num, thisFig)


def new_figure_manager_given_figure(num, figure):
    """
    Create a new figure manager instance for the given figure.
    """
    canvas = FigureCanvasSVG(figure)
    manager = FigureManagerSVG(canvas, num)
    return manager


svgProlog = '<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n<!-- Created with matplotlib (http://matplotlib.org/) -->\n'