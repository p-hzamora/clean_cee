# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\decorators.pyc
# Compiled at: 2012-11-08 06:38:04
from __future__ import print_function
from matplotlib.testing.noseclasses import KnownFailureTest, KnownFailureDidNotFailTest, ImageComparisonFailure
import os, sys, shutil, nose, matplotlib, matplotlib.tests, matplotlib.units
from matplotlib import ticker
from matplotlib import pyplot as plt
from matplotlib import ft2font
import numpy as np
from matplotlib.testing.compare import comparable_formats, compare_images, make_test_filename
import warnings

def knownfailureif(fail_condition, msg=None, known_exception_class=None):
    """

    Assume a will fail if *fail_condition* is True. *fail_condition*
    may also be False or the string 'indeterminate'.

    *msg* is the error message displayed for the test.

    If *known_exception_class* is not None, the failure is only known
    if the exception is an instance of this class. (Default = None)

    """
    if msg is None:
        msg = 'Test known to fail'

    def known_fail_decorator(f):
        import nose

        def failer(*args, **kwargs):
            try:
                result = f(*args, **kwargs)
            except Exception as err:
                if fail_condition:
                    if known_exception_class is not None:
                        if not isinstance(err, known_exception_class):
                            raise
                    raise KnownFailureTest(msg)
                else:
                    raise

            if fail_condition and fail_condition != 'indeterminate':
                raise KnownFailureDidNotFailTest(msg)
            return result

        return nose.tools.make_decorator(f)(failer)

    return known_fail_decorator


class CleanupTest(object):

    @classmethod
    def setup_class(cls):
        cls.original_units_registry = matplotlib.units.registry.copy()

    @classmethod
    def teardown_class(cls):
        plt.close('all')
        matplotlib.tests.setup()
        matplotlib.units.registry.clear()
        matplotlib.units.registry.update(cls.original_units_registry)
        warnings.resetwarnings()

    def test(self):
        self._func()


def cleanup(func):
    name = func.__name__
    func = staticmethod(func)
    func.__get__(1).__name__ = '_private'
    new_class = type(name, (
     CleanupTest,), {'_func': func})
    return new_class


def check_freetype_version(ver):
    if ver is None:
        return True
    else:
        from distutils import version
        if isinstance(ver, str):
            ver = (
             ver, ver)
        ver = [ version.StrictVersion(x) for x in ver ]
        found = version.StrictVersion(ft2font.__freetype_version__)
        return found >= ver[0] and found <= ver[1]


class ImageComparisonTest(CleanupTest):

    @classmethod
    def setup_class(cls):
        CleanupTest.setup_class()
        cls._func()

    @staticmethod
    def remove_text(figure):
        figure.suptitle('')
        for ax in figure.get_axes():
            ax.set_title('')
            ax.xaxis.set_major_formatter(ticker.NullFormatter())
            ax.xaxis.set_minor_formatter(ticker.NullFormatter())
            ax.yaxis.set_major_formatter(ticker.NullFormatter())
            ax.yaxis.set_minor_formatter(ticker.NullFormatter())

    def test(self):
        baseline_dir, result_dir = _image_directories(self._func)
        for fignum, baseline in zip(plt.get_fignums(), self._baseline_images):
            figure = plt.figure(fignum)
            for extension in self._extensions:
                will_fail = extension not in comparable_formats()
                if will_fail:
                    fail_msg = 'Cannot compare %s files on this system' % extension
                else:
                    fail_msg = 'No failure expected'
                orig_expected_fname = os.path.join(baseline_dir, baseline) + '.' + extension
                if extension == 'eps' and not os.path.exists(orig_expected_fname):
                    orig_expected_fname = os.path.join(baseline_dir, baseline) + '.pdf'
                expected_fname = make_test_filename(os.path.join(result_dir, os.path.basename(orig_expected_fname)), 'expected')
                actual_fname = os.path.join(result_dir, baseline) + '.' + extension
                if os.path.exists(orig_expected_fname):
                    shutil.copyfile(orig_expected_fname, expected_fname)
                else:
                    will_fail = True
                    fail_msg = 'Do not have baseline image %s' % expected_fname

                @knownfailureif(will_fail, fail_msg, known_exception_class=ImageComparisonFailure)
                def do_test():
                    if self._remove_text:
                        self.remove_text(figure)
                    figure.savefig(actual_fname)
                    err = compare_images(expected_fname, actual_fname, self._tol, in_decorator=True)
                    try:
                        if not os.path.exists(expected_fname):
                            raise ImageComparisonFailure('image does not exist: %s' % expected_fname)
                        if err:
                            raise ImageComparisonFailure('images not close: %(actual)s vs. %(expected)s (RMS %(rms).3f)' % err)
                    except ImageComparisonFailure:
                        if not check_freetype_version(self._freetype_version):
                            raise KnownFailureTest("Mismatched version of freetype.  Test requires '%s', you have '%s'" % (
                             self._freetype_version, ft2font.__freetype_version__))
                        raise

                yield (
                 do_test,)


def image_comparison(baseline_images=None, extensions=None, tol=0.001, freetype_version=None, remove_text=False):
    """
    call signature::

      image_comparison(baseline_images=['my_figure'], extensions=None)

    Compare images generated by the test with those specified in
    *baseline_images*, which must correspond else an
    ImageComparisonFailure exception will be raised.

    Keyword arguments:

      *baseline_images*: list
        A list of strings specifying the names of the images generated
        by calls to :meth:`matplotlib.figure.savefig`.

      *extensions*: [ None | list ]

        If *None*, default to all supported extensions.

        Otherwise, a list of extensions to test. For example ['png','pdf'].

      *tol*: (default 1e-3)
        The RMS threshold above which the test is considered failed.

      *freetype_version*: str or tuple
        The expected freetype version or range of versions for this
        test to pass.

      *remove_text*: bool
        Remove the title and tick text from the figure before
        comparison.  This does not remove other, more deliberate,
        text, such as legends and annotations.
    """
    if baseline_images is None:
        raise ValueError('baseline_images must be specified')
    if extensions is None:
        extensions = ['png', 'pdf', 'svg']

    def compare_images_decorator(func):
        name = func.__name__
        func = staticmethod(func)
        func.__get__(1).__name__ = '_private'
        new_class = type(name, (
         ImageComparisonTest,), {'_func': func, '_baseline_images': baseline_images, 
           '_extensions': extensions, 
           '_tol': tol, 
           '_freetype_version': freetype_version, 
           '_remove_text': remove_text})
        return new_class

    return compare_images_decorator


def _image_directories(func):
    """
    Compute the baseline and result image directories for testing *func*.
    Create the result directory if it doesn't exist.
    """
    module_name = func.__module__
    if module_name == '__main__':
        warnings.warn('test module run as script. guessing baseline image locations')
        script_name = sys.argv[0]
        basedir = os.path.abspath(os.path.dirname(script_name))
        subdir = os.path.splitext(os.path.split(script_name)[1])[0]
    else:
        mods = module_name.split('.')
        mods.pop(0)
        assert mods.pop(0) == 'tests'
        subdir = os.path.join(*mods)
        import imp

        def find_dotted_module(module_name, path=None):
            """A version of imp which can handle dots in the module name"""
            res = None
            for sub_mod in module_name.split('.'):
                res = _, path, _ = imp.find_module(sub_mod, path)
                path = [path]

            return res

        mod_file = find_dotted_module(func.__module__)[1]
        basedir = os.path.dirname(mod_file)
    baseline_dir = os.path.join(basedir, 'baseline_images', subdir)
    result_dir = os.path.abspath(os.path.join('result_images', subdir))
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    return (baseline_dir, result_dir)