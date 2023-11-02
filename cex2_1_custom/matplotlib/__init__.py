# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\__init__.pyc
# Compiled at: 2012-11-08 09:38:18
"""
This is an object-oriented plotting library.

A procedural interface is provided by the companion pyplot module,
which may be imported directly, e.g::

    from matplotlib.pyplot import *

To include numpy functions too, use::

    from pylab import *

or using ipython::

    ipython -pylab

For the most part, direct use of the object-oriented library is
encouraged when programming; pyplot is primarily for working
interactively.  The
exceptions are the pyplot commands :func:`~matplotlib.pyplot.figure`,
:func:`~matplotlib.pyplot.subplot`,
:func:`~matplotlib.pyplot.subplots`,
:func:`~matplotlib.backends.backend_qt4agg.show`, and
:func:`~pyplot.savefig`, which can greatly simplify scripting.

Modules include:

    :mod:`matplotlib.axes`
        defines the :class:`~matplotlib.axes.Axes` class.  Most pylab
        commands are wrappers for :class:`~matplotlib.axes.Axes`
        methods.  The axes module is the highest level of OO access to
        the library.

    :mod:`matplotlib.figure`
        defines the :class:`~matplotlib.figure.Figure` class.

    :mod:`matplotlib.artist`
        defines the :class:`~matplotlib.artist.Artist` base class for
        all classes that draw things.

    :mod:`matplotlib.lines`
        defines the :class:`~matplotlib.lines.Line2D` class for
        drawing lines and markers

    :mod:`matplotlib.patches`
        defines classes for drawing polygons

    :mod:`matplotlib.text`
        defines the :class:`~matplotlib.text.Text`,
        :class:`~matplotlib.text.TextWithDash`, and
        :class:`~matplotlib.text.Annotate` classes

    :mod:`matplotlib.image`
        defines the :class:`~matplotlib.image.AxesImage` and
        :class:`~matplotlib.image.FigureImage` classes

    :mod:`matplotlib.collections`
        classes for efficient drawing of groups of lines or polygons

    :mod:`matplotlib.colors`
        classes for interpreting color specifications and for making
        colormaps

    :mod:`matplotlib.cm`
        colormaps and the :class:`~matplotlib.image.ScalarMappable`
        mixin class for providing color mapping functionality to other
        classes

    :mod:`matplotlib.ticker`
        classes for calculating tick mark locations and for formatting
        tick labels

    :mod:`matplotlib.backends`
        a subpackage with modules for various gui libraries and output
        formats

The base matplotlib namespace includes:

    :data:`~matplotlib.rcParams`
        a global dictionary of default configuration settings.  It is
        initialized by code which may be overridded by a matplotlibrc
        file.

    :func:`~matplotlib.rc`
        a function for setting groups of rcParams values

    :func:`~matplotlib.use`
        a function for setting the matplotlib backend.  If used, this
        function must be called immediately after importing matplotlib
        for the first time.  In particular, it must be called
        **before** importing pylab (if pylab is imported).

matplotlib was initially written by John D. Hunter (1968-2012) and is now
developed and maintained by a host of others.

Occasionally the internal documentation (python docstrings) will refer
to MATLAB&reg;, a registered trademark of The MathWorks, Inc.

"""
from __future__ import print_function
__version__ = '1.2.0'
__version__numpy__ = '1.4'
import os, re, shutil, subprocess, sys, warnings, distutils.sysconfig, distutils.version
try:
    reload
except NameError:
    from imp import reload

if not hasattr(sys, 'argv'):
    sys.argv = [
     'modpython']
import sys, os, tempfile
if sys.version_info[0] >= 3:

    def ascii(s):
        return bytes(s, 'ascii')


    def byte2str(b):
        return b.decode('ascii')


else:
    ascii = str

    def byte2str(b):
        return b


from matplotlib.rcsetup import defaultParams, validate_backend, validate_toolbar
major, minor1, minor2, s, tmp = sys.version_info
_python24 = major == 2 and minor1 >= 4 or major >= 3
_havedate = True
if not _python24:
    raise ImportError('matplotlib requires Python 2.4 or later')
import numpy
from distutils import version
expected_version = version.LooseVersion(__version__numpy__)
found_version = version.LooseVersion(numpy.__version__)
if not found_version >= expected_version:
    raise ImportError('numpy %s or later is required; you have %s' % (
     __version__numpy__, numpy.__version__))
del version

def is_string_like(obj):
    if hasattr(obj, 'shape'):
        return 0
    try:
        obj + ''
    except (TypeError, ValueError):
        return 0

    return 1


def _is_writable_dir(p):
    """
    p is a string pointing to a putative writable dir -- return True p
    is such a string, else False
    """
    try:
        p + ''
    except TypeError:
        return False

    try:
        t = tempfile.TemporaryFile(dir=p)
        try:
            t.write(ascii('1'))
        finally:
            t.close()

    except OSError:
        return False

    return True


class Verbose:
    """
    A class to handle reporting.  Set the fileo attribute to any file
    instance to handle the output.  Default is sys.stdout
    """
    levels = ('silent', 'helpful', 'debug', 'debug-annoying')
    vald = dict([ (level, i) for i, level in enumerate(levels) ])
    _commandLineVerbose = None
    for arg in sys.argv[1:]:
        if not arg.startswith('--verbose-'):
            continue
        level_str = arg[10:]
        if level_str in levels:
            _commandLineVerbose = level_str

    def __init__(self):
        self.set_level('silent')
        self.fileo = sys.stdout

    def set_level(self, level):
        """set the verbosity to one of the Verbose.levels strings"""
        if self._commandLineVerbose is not None:
            level = self._commandLineVerbose
        if level not in self.levels:
            warnings.warn('matplotlib: unrecognized --verbose-* string "%s". Legal values are %s' % (
             level, self.levels))
        else:
            self.level = level
        return

    def set_fileo(self, fname):
        std = {'sys.stdout': sys.stdout, 'sys.stderr': sys.stderr}
        if fname in std:
            self.fileo = std[fname]
        else:
            try:
                fileo = open(fname, 'w')
            except IOError:
                raise ValueError('Verbose object could not open log file "%s" for writing.\nCheck your matplotlibrc verbose.fileo setting' % fname)
            else:
                self.fileo = fileo

    def report(self, s, level='helpful'):
        """
        print message s to self.fileo if self.level>=level.  Return
        value indicates whether a message was issued

        """
        if self.ge(level):
            print(s, file=self.fileo)
            return True
        return False

    def wrap(self, fmt, func, level='helpful', always=True):
        """
        return a callable function that wraps func and reports it
        output through the verbose handler if current verbosity level
        is higher than level

        if always is True, the report will occur on every function
        call; otherwise only on the first time the function is called
        """
        assert callable(func)

        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if always or not wrapper._spoke:
                spoke = self.report(fmt % ret, level)
                if not wrapper._spoke:
                    wrapper._spoke = spoke
            return ret

        wrapper._spoke = False
        wrapper.__doc__ = func.__doc__
        return wrapper

    def ge(self, level):
        """return true if self.level is >= level"""
        return self.vald[self.level] >= self.vald[level]


verbose = Verbose()

def checkdep_dvipng():
    try:
        s = subprocess.Popen(['dvipng', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        line = s.stdout.readlines()[1]
        v = byte2str(line.split()[-1])
        return v
    except (IndexError, ValueError, OSError):
        return

    return


def checkdep_ghostscript():
    try:
        if sys.platform == 'win32':
            command_args = [
             'gswin32c', '--version']
        else:
            command_args = [
             'gs', '--version']
        s = subprocess.Popen(command_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        v = byte2str(s.stdout.read()[:-1])
        return v
    except (IndexError, ValueError, OSError):
        return

    return


def checkdep_tex():
    try:
        s = subprocess.Popen(['tex', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        line = byte2str(s.stdout.readlines()[0])
        pattern = '3\\.1\\d+'
        match = re.search(pattern, line)
        v = match.group(0)
        return v
    except (IndexError, ValueError, AttributeError, OSError):
        return

    return


def checkdep_pdftops():
    try:
        s = subprocess.Popen(['pdftops', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in s.stderr:
            if 'version' in line:
                v = byte2str(line.split()[-1])

        return v
    except (IndexError, ValueError, UnboundLocalError, OSError):
        return

    return


def checkdep_inkscape():
    try:
        s = subprocess.Popen(['inkscape', '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in s.stdout:
            if 'Inkscape' in line:
                v = byte2str(line.split()[1])
                break

        return v
    except (IndexError, ValueError, UnboundLocalError, OSError):
        return

    return


def checkdep_xmllint():
    try:
        s = subprocess.Popen(['xmllint', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in s.stderr:
            if 'version' in line:
                v = byte2str(line.split()[-1])
                break

        return v
    except (IndexError, ValueError, UnboundLocalError, OSError):
        return

    return


def compare_versions(a, b):
    """return True if a is greater than or equal to b"""
    if a:
        a = distutils.version.LooseVersion(a)
        b = distutils.version.LooseVersion(b)
        if a >= b:
            return True
        return False
    else:
        return False


def checkdep_ps_distiller(s):
    if not s:
        return False
    else:
        flag = True
        gs_req = '7.07'
        gs_sugg = '7.07'
        gs_v = checkdep_ghostscript()
        if compare_versions(gs_v, gs_sugg):
            pass
        else:
            if compare_versions(gs_v, gs_req):
                verbose.report('ghostscript-%s found. ghostscript-%s or later is recommended to use the ps.usedistiller option.' % (
                 gs_v, gs_sugg))
            else:
                flag = False
                warnings.warn('matplotlibrc ps.usedistiller option can not be used unless ghostscript-%s or later is installed on your system' % gs_req)
            if s == 'xpdf':
                pdftops_req = '3.0'
                pdftops_req_alt = '0.9'
                pdftops_v = checkdep_pdftops()
                if compare_versions(pdftops_v, pdftops_req):
                    pass
                elif compare_versions(pdftops_v, pdftops_req_alt) and not compare_versions(pdftops_v, '1.0'):
                    pass
                else:
                    flag = False
                    warnings.warn('matplotlibrc ps.usedistiller can not be set to xpdf unless xpdf-%s or later is installed on your system' % pdftops_req)
            if flag:
                return s
        return False


def checkdep_usetex(s):
    if not s:
        return False
    tex_req = '3.1415'
    gs_req = '7.07'
    gs_sugg = '7.07'
    dvipng_req = '1.5'
    flag = True
    tex_v = checkdep_tex()
    if compare_versions(tex_v, tex_req):
        pass
    else:
        flag = False
        warnings.warn('matplotlibrc text.usetex option can not be used unless TeX-%s or later is installed on your system' % tex_req)
    dvipng_v = checkdep_dvipng()
    if compare_versions(dvipng_v, dvipng_req):
        pass
    else:
        flag = False
        warnings.warn('matplotlibrc text.usetex can not be used with *Agg backend unless dvipng-1.5 or later is installed on your system')
    gs_v = checkdep_ghostscript()
    if compare_versions(gs_v, gs_sugg):
        pass
    elif compare_versions(gs_v, gs_req):
        verbose.report('ghostscript-%s found. ghostscript-%s or later is recommended for use with the text.usetex option.' % (
         gs_v, gs_sugg))
    else:
        flag = False
        warnings.warn('matplotlibrc text.usetex can not be used unless ghostscript-%s or later is installed on your system' % gs_req)
    return flag


def _get_home():
    """Find user's home directory if possible.
    Otherwise raise error.

    :see:  http://mail.python.org/pipermail/python-list/2005-February/263921.html
    """
    path = ''
    try:
        path = os.path.expanduser('~')
    except:
        pass

    if not os.path.isdir(path):
        for evar in ('HOME', 'USERPROFILE', 'TMP'):
            try:
                path = os.environ[evar]
                if os.path.isdir(path):
                    break
            except:
                pass

    if path:
        return path
    raise RuntimeError('please define environment variable $HOME')


def _create_tmp_config_dir():
    """
    If the config directory can not be created, create a temporary
    directory.
    """
    import getpass, tempfile
    tempdir = os.path.join(tempfile.gettempdir(), 'matplotlib-%s' % getpass.getuser())
    os.environ['MPLCONFIGDIR'] = tempdir
    return tempdir


get_home = verbose.wrap('$HOME=%s', _get_home, always=False)

def _get_configdir():
    """
    Return the string representing the configuration directory.

    Default is HOME/.matplotlib.  You can override this with the
    MPLCONFIGDIR environment variable.  If the default is not
    writable, and MPLCONFIGDIR is not set, then
    tempfile.gettempdir() is used to provide a directory in
    which a matplotlib subdirectory is created as the configuration
    directory.
    """
    configdir = os.environ.get('MPLCONFIGDIR')
    if configdir is not None:
        if not os.path.exists(configdir):
            os.makedirs(configdir)
        if not _is_writable_dir(configdir):
            return _create_tmp_config_dir()
        return configdir
    h = get_home()
    p = os.path.join(get_home(), '.matplotlib')
    if os.path.exists(p):
        if not _is_writable_dir(p):
            return _create_tmp_config_dir()
    else:
        if not _is_writable_dir(h):
            return _create_tmp_config_dir()
        from matplotlib.cbook import mkdirs
        mkdirs(p)
    return p


get_configdir = verbose.wrap('CONFIGDIR=%s', _get_configdir, always=False)

def _get_data_path():
    """get the path to matplotlib data"""
    if 'MATPLOTLIBDATA' in os.environ:
        path = os.environ['MATPLOTLIBDATA']
        if not os.path.isdir(path):
            raise RuntimeError('Path in environment MATPLOTLIBDATA not a directory')
        return path
    path = os.sep.join([os.path.dirname(__file__), 'mpl-data'])
    if os.path.isdir(path):
        return path
    else:
        import matplotlib.afm
        path = os.sep.join([os.path.dirname(matplotlib.afm.__file__), 'mpl-data'])
        if os.path.isdir(path):
            return path
        if getattr(sys, 'frozen', None):
            exe_path = os.path.dirname(sys.executable)
            path = os.path.join(exe_path, 'mpl-data')
            if os.path.isdir(path):
                return path
            path = os.path.join(os.path.split(exe_path)[0], 'mpl-data')
            if os.path.isdir(path):
                return path
            path = os.path.join(sys.path[0], 'mpl-data')
            if os.path.isdir(path):
                return path
        raise RuntimeError('Could not find the matplotlib data files')
        return


def _get_data_path_cached():
    if defaultParams['datapath'][0] is None:
        defaultParams['datapath'][0] = _get_data_path()
    return defaultParams['datapath'][0]


get_data_path = verbose.wrap('matplotlib data path %s', _get_data_path_cached, always=False)

def get_example_data(fname):
    """
    get_example_data is deprecated -- use matplotlib.cbook.get_sample_data instead
    """
    raise NotImplementedError('get_example_data is deprecated -- use matplotlib.cbook.get_sample_data instead')


def get_py2exe_datafiles():
    datapath = get_data_path()
    head, tail = os.path.split(datapath)
    d = {}
    for root, dirs, files in os.walk(datapath):
        if 'Matplotlib.nib' in files:
            files.remove('Matplotlib.nib')
        files = [ os.path.join(root, filename) for filename in files ]
        root = root.replace(tail, 'mpl-data')
        root = root[root.index('mpl-data'):]
        d[root] = files

    return list(d.items())


def matplotlib_fname():
    """
    Return the path to the rc file

    Search order:

     * current working dir
     * environ var MATPLOTLIBRC
     * HOME/.matplotlib/matplotlibrc
     * MATPLOTLIBDATA/matplotlibrc

    """
    oldname = os.path.join(os.getcwd(), '.matplotlibrc')
    if os.path.exists(oldname):
        print('WARNING: Old rc filename ".matplotlibrc" found in working dir\n  and and renamed to new default rc file name "matplotlibrc"\n  (no leading"dot"). ', file=sys.stderr)
        shutil.move('.matplotlibrc', 'matplotlibrc')
    home = get_home()
    oldname = os.path.join(home, '.matplotlibrc')
    if os.path.exists(oldname):
        configdir = get_configdir()
        newname = os.path.join(configdir, 'matplotlibrc')
        print('WARNING: Old rc filename "%s" found and renamed to\n  new default rc file name "%s".' % (oldname, newname), file=sys.stderr)
        shutil.move(oldname, newname)
    fname = os.path.join(os.getcwd(), 'matplotlibrc')
    if os.path.exists(fname):
        return fname
    if 'MATPLOTLIBRC' in os.environ:
        path = os.environ['MATPLOTLIBRC']
        if os.path.exists(path):
            fname = os.path.join(path, 'matplotlibrc')
            if os.path.exists(fname):
                return fname
    fname = os.path.join(get_configdir(), 'matplotlibrc')
    if os.path.exists(fname):
        return fname
    path = get_data_path()
    fname = os.path.join(path, 'matplotlibrc')
    if not os.path.exists(fname):
        warnings.warn('Could not find matplotlibrc; using defaults')
    return fname


_deprecated_map = {'text.fontstyle': 'font.style', 
   'text.fontangle': 'font.style', 
   'text.fontvariant': 'font.variant', 
   'text.fontweight': 'font.weight', 
   'text.fontsize': 'font.size', 
   'tick.size': 'tick.major.size', 
   'svg.embed_char_paths': 'svg.fonttype', 
   'savefig.extension': 'savefig.format'}
_deprecated_ignore_map = {'legend.pad': 'legend.borderpad', 
   'legend.labelsep': 'legend.labelspacing', 
   'legend.handlelen': 'legend.handlelength', 
   'legend.handletextsep': 'legend.handletextpad', 
   'legend.axespad': 'legend.borderaxespad'}

class RcParams(dict):
    """
    A dictionary object including validation

    validating functions are defined and associated with rc parameters in
    :mod:`matplotlib.rcsetup`
    """
    validate = dict([ (key, converter) for key, (default, converter) in defaultParams.iteritems()
                    ])
    msg_depr = '%s is deprecated and replaced with %s; please use the latter.'
    msg_depr_ignore = '%s is deprecated and ignored. Use %s'

    def __setitem__(self, key, val):
        try:
            if key in _deprecated_map:
                alt = _deprecated_map[key]
                warnings.warn(self.msg_depr % (key, alt))
                key = alt
            elif key in _deprecated_ignore_map:
                alt = _deprecated_ignore_map[key]
                warnings.warn(self.msg_depr_ignore % (key, alt))
                return
            cval = self.validate[key](val)
            dict.__setitem__(self, key, cval)
        except KeyError:
            raise KeyError('%s is not a valid rc parameter.See rcParams.keys() for a list of valid parameters.' % (key,))

    def __getitem__(self, key):
        if key in _deprecated_map:
            alt = _deprecated_map[key]
            warnings.warn(self.msg_depr % (key, alt))
            key = alt
        elif key in _deprecated_ignore_map:
            alt = _deprecated_ignore_map[key]
            warnings.warn(self.msg_depr_ignore % (key, alt))
            key = alt
        return dict.__getitem__(self, key)

    def keys(self):
        """
        Return sorted list of keys.
        """
        k = dict.keys(self)
        k.sort()
        return k

    def values(self):
        """
        Return values in order of sorted keys.
        """
        return [ self[k] for k in self.iterkeys() ]


def rc_params(fail_on_error=False):
    """Return the default params updated from the values in the rc file"""
    fname = matplotlib_fname()
    if not os.path.exists(fname):
        message = 'could not find rc file; returning defaults'
        ret = RcParams([ (key, default) for key, (default, converter) in defaultParams.iteritems()
                       ])
        warnings.warn(message)
        return ret
    return rc_params_from_file(fname, fail_on_error)


def rc_params_from_file(fname, fail_on_error=False):
    """Load and return params from fname."""
    cnt = 0
    rc_temp = {}
    with open(fname) as (fd):
        for line in fd:
            cnt += 1
            strippedline = line.split('#', 1)[0].strip()
            if not strippedline:
                continue
            tup = strippedline.split(':', 1)
            if len(tup) != 2:
                warnings.warn('Illegal line #%d\n\t%s\n\tin file "%s"' % (
                 cnt, line, fname))
                continue
            key, val = tup
            key = key.strip()
            val = val.strip()
            if key in rc_temp:
                warnings.warn('Duplicate key in file "%s", line #%d' % (fname, cnt))
            rc_temp[key] = (
             val, line, cnt)

    ret = RcParams([ (key, default) for key, (default, converter) in defaultParams.iteritems()
                   ])
    for key in ('verbose.level', 'verbose.fileo'):
        if key in rc_temp:
            val, line, cnt = rc_temp.pop(key)
            if fail_on_error:
                ret[key] = val
            else:
                try:
                    ret[key] = val
                except Exception as msg:
                    warnings.warn('Bad val "%s" on line #%d\n\t"%s"\n\tin file "%s"\n\t%s' % (val, cnt, line, fname, msg))

    verbose.set_level(ret['verbose.level'])
    verbose.set_fileo(ret['verbose.fileo'])
    for key, (val, line, cnt) in rc_temp.iteritems():
        if key in defaultParams:
            if fail_on_error:
                ret[key] = val
            else:
                try:
                    ret[key] = val
                except Exception as msg:
                    warnings.warn('Bad val "%s" on line #%d\n\t"%s"\n\tin file "%s"\n\t%s' % (val, cnt, line, fname, msg))

        elif key in _deprecated_ignore_map:
            warnings.warn('%s is deprecated. Update your matplotlibrc to use %s instead.' % (key, _deprecated_ignore_map[key]))
        else:
            print('\nBad key "%s" on line %d in\n%s.\nYou probably need to get an updated matplotlibrc file from\nhttp://matplotlib.sf.net/_static/matplotlibrc or from the matplotlib source\ndistribution' % (key, cnt, fname), file=sys.stderr)

    if ret['datapath'] is None:
        ret['datapath'] = get_data_path()
    if not ret['text.latex.preamble'] == ['']:
        verbose.report('\n*****************************************************************\nYou have the following UNSUPPORTED LaTeX preamble customizations:\n%s\nPlease do not ask for support with these customizations active.\n*****************************************************************\n' % ('\n').join(ret['text.latex.preamble']), 'helpful')
    verbose.report('loaded rc file %s' % fname)
    return ret


rcParams = rc_params()
rcParamsOrig = rcParams.copy()
rcParamsDefault = RcParams([ (key, default) for key, (default, converter) in defaultParams.iteritems()
                           ])
rcParams['ps.usedistiller'] = checkdep_ps_distiller(rcParams['ps.usedistiller'])
rcParams['text.usetex'] = checkdep_usetex(rcParams['text.usetex'])
if rcParams['axes.formatter.use_locale']:
    import locale
    locale.setlocale(locale.LC_ALL, '')

def rc(group, **kwargs):
    """
    Set the current rc params.  Group is the grouping for the rc, eg.
    for ``lines.linewidth`` the group is ``lines``, for
    ``axes.facecolor``, the group is ``axes``, and so on.  Group may
    also be a list or tuple of group names, eg. (*xtick*, *ytick*).
    *kwargs* is a dictionary attribute name/value pairs, eg::

      rc('lines', linewidth=2, color='r')

    sets the current rc params and is equivalent to::

      rcParams['lines.linewidth'] = 2
      rcParams['lines.color'] = 'r'

    The following aliases are available to save typing for interactive
    users:

    =====   =================
    Alias   Property
    =====   =================
    'lw'    'linewidth'
    'ls'    'linestyle'
    'c'     'color'
    'fc'    'facecolor'
    'ec'    'edgecolor'
    'mew'   'markeredgewidth'
    'aa'    'antialiased'
    =====   =================

    Thus you could abbreviate the above rc command as::

          rc('lines', lw=2, c='r')

    Note you can use python's kwargs dictionary facility to store
    dictionaries of default parameters.  Eg, you can customize the
    font rc as follows::

      font = {'family' : 'monospace',
              'weight' : 'bold',
              'size'   : 'larger'}

      rc('font', **font)  # pass in the font dict as kwargs

    This enables you to easily switch between several configurations.
    Use :func:`~matplotlib.pyplot.rcdefaults` to restore the default
    rc params after changes.
    """
    aliases = {'lw': 'linewidth', 
       'ls': 'linestyle', 
       'c': 'color', 
       'fc': 'facecolor', 
       'ec': 'edgecolor', 
       'mew': 'markeredgewidth', 
       'aa': 'antialiased'}
    if is_string_like(group):
        group = (
         group,)
    for g in group:
        for k, v in kwargs.iteritems():
            name = aliases.get(k) or k
            key = '%s.%s' % (g, name)
            try:
                rcParams[key] = v
            except KeyError:
                raise KeyError('Unrecognized key "%s" for group "%s" and name "%s"' % (
                 key, g, name))


def rcdefaults():
    """
    Restore the default rc params.  These are not the params loaded by
    the rc file, but mpl's internal params.  See rc_file_defaults for
    reloading the default params from the rc file
    """
    rcParams.update(rcParamsDefault)


def rc_file(fname):
    """
    Update rc params from file.
    """
    rcParams.update(rc_params_from_file(fname))


class rc_context(object):
    """
    Return a context manager for managing rc settings.

    This allows one to do::

    >>> with mpl.rc_context(fname='screen.rc'):
    >>>     plt.plot(x, a)
    >>>     with mpl.rc_context(fname='print.rc'):
    >>>         plt.plot(x, b)
    >>>     plt.plot(x, c)

    The 'a' vs 'x' and 'c' vs 'x' plots would have settings from
    'screen.rc', while the 'b' vs 'x' plot would have settings from
    'print.rc'.

    A dictionary can also be passed to the context manager::

    >>> with mpl.rc_context(rc={'text.usetex': True}, fname='screen.rc'):
    >>>     plt.plot(x, a)

    The 'rc' dictionary takes precedence over the settings loaded from
    'fname'.  Passing a dictionary only is also valid.
    """

    def __init__(self, rc=None, fname=None):
        self.rcdict = rc
        self.fname = fname

    def __enter__(self):
        self._rcparams = rcParams.copy()
        if self.fname:
            rc_file(self.fname)
        if self.rcdict:
            rcParams.update(self.rcdict)

    def __exit__(self, type, value, tb):
        rcParams.update(self._rcparams)


def rc_file_defaults():
    """
    Restore the default rc params from the original matplotlib rc that
    was loaded
    """
    rcParams.update(rcParamsOrig)


_use_error_msg = ' This call to matplotlib.use() has no effect\nbecause the the backend has already been chosen;\nmatplotlib.use() must be called *before* pylab, matplotlib.pyplot,\nor matplotlib.backends is imported for the first time.\n'

def use(arg, warn=True, force=False):
    """
    Set the matplotlib backend to one of the known backends.

    The argument is case-insensitive. *warn* specifies whether a
    warning should be issued if a backend has already been set up.
    *force* is an **experimental** flag that tells matplotlib to
    attempt to initialize a new backend by reloading the backend
    module.

    .. note::

        This function must be called *before* importing pyplot for
        the first time; or, if you are not using pyplot, it must be called
        before importing matplotlib.backends.  If warn is True, a warning
        is issued if you try and call this after pylab or pyplot have been
        loaded.  In certain black magic use cases, e.g.
        :func:`pyplot.switch_backend`, we are doing the reloading necessary to
        make the backend switch work (in some cases, e.g. pure image
        backends) so one can set warn=False to suppress the warnings.

    To find out which backend is currently set, see
    :func:`matplotlib.get_backend`.

    """
    if 'matplotlib.backends' in sys.modules:
        if warn:
            warnings.warn(_use_error_msg)
        if not force:
            return
        need_reload = True
    else:
        need_reload = False
    if arg.startswith('module://'):
        name = arg
    else:
        arg = arg.lower()
        name = validate_backend(arg)
    rcParams['backend'] = name
    if need_reload:
        reload(sys.modules['matplotlib.backends'])


def get_backend():
    """Returns the current backend."""
    return rcParams['backend']


def interactive(b):
    """
    Set interactive mode to boolean b.

    If b is True, then draw after every plotting command, eg, after xlabel
    """
    rcParams['interactive'] = b


def is_interactive():
    """Return true if plot mode is interactive"""
    b = rcParams['interactive']
    return b


def tk_window_focus():
    """Return true if focus maintenance under TkAgg on win32 is on.
     This currently works only for python.exe and IPython.exe.
     Both IDLE and Pythonwin.exe fail badly when tk_window_focus is on."""
    if rcParams['backend'] != 'TkAgg':
        return False
    return rcParams['tk.window_focus']


for s in sys.argv[1:]:
    if s.startswith('-d') and len(s) > 2:
        try:
            use(s[2:])
        except (KeyError, ValueError):
            pass

default_test_modules = [
 'matplotlib.tests.test_agg', 
 'matplotlib.tests.test_artist', 
 'matplotlib.tests.test_axes', 
 'matplotlib.tests.test_backend_svg', 
 'matplotlib.tests.test_backend_pgf', 
 'matplotlib.tests.test_basic', 
 'matplotlib.tests.test_cbook', 
 'matplotlib.tests.test_colorbar', 
 'matplotlib.tests.test_colors', 
 'matplotlib.tests.test_dates', 
 'matplotlib.tests.test_delaunay', 
 'matplotlib.tests.test_figure', 
 'matplotlib.tests.test_image', 
 'matplotlib.tests.test_legend', 
 'matplotlib.tests.test_mathtext', 
 'matplotlib.tests.test_mlab', 
 'matplotlib.tests.test_patches', 
 'matplotlib.tests.test_pickle', 
 'matplotlib.tests.test_rcparams', 
 'matplotlib.tests.test_scale', 
 'matplotlib.tests.test_simplification', 
 'matplotlib.tests.test_spines', 
 'matplotlib.tests.test_subplots', 
 'matplotlib.tests.test_text', 
 'matplotlib.tests.test_ticker', 
 'matplotlib.tests.test_tightlayout', 
 'matplotlib.tests.test_triangulation', 
 'matplotlib.tests.test_transforms', 
 'matplotlib.tests.test_arrow_patches']

def test(verbosity=1):
    """run the matplotlib test suite"""
    old_backend = rcParams['backend']
    try:
        use('agg')
        import nose, nose.plugins.builtin
        from .testing.noseclasses import KnownFailure
        from nose.plugins.manager import PluginManager
        plugins = []
        plugins.append(KnownFailure())
        plugins.extend([ plugin() for plugin in nose.plugins.builtin.plugins ])
        manager = PluginManager(plugins=plugins)
        config = nose.config.Config(verbosity=verbosity, plugins=manager)
        success = nose.run(defaultTest=default_test_modules, config=config)
    finally:
        if old_backend.lower() != 'agg':
            use(old_backend)

    return success


test.__test__ = False
verbose.report('matplotlib version %s' % __version__)
verbose.report('verbose.level %s' % verbose.level)
verbose.report('interactive is %s' % rcParams['interactive'])
verbose.report('platform is %s' % sys.platform)
verbose.report('loaded modules: %s' % sys.modules.iterkeys(), 'debug')