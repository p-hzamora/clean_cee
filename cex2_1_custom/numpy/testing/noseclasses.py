# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: numpy\testing\noseclasses.pyc
# Compiled at: 2013-04-07 07:04:04
import os, doctest, nose
from nose.plugins import doctests as npd
from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin
from nose.plugins.base import Plugin
from nose.util import src
import numpy
from nosetester import get_package_name
import inspect

class NumpyDocTestFinder(doctest.DocTestFinder):

    def _from_module(self, module, object):
        """
        Return true if the given object is defined in the given
        module.
        """
        if module is None:
            return True
        else:
            if inspect.isfunction(object):
                return module.__dict__ is object.func_globals
            if inspect.isbuiltin(object):
                return module.__name__ == object.__module__
            if inspect.isclass(object):
                return module.__name__ == object.__module__
            if inspect.ismethod(object):
                return module.__name__ == object.im_class.__module__
            if inspect.getmodule(object) is not None:
                return module is inspect.getmodule(object)
            if hasattr(object, '__module__'):
                return module.__name__ == object.__module__
            if isinstance(object, property):
                return True
            raise ValueError('object must be a class or function')
            return

    def _find(self, tests, obj, name, module, source_lines, globs, seen):
        """
        Find tests for the given object and any contained objects, and
        add them to `tests`.
        """
        doctest.DocTestFinder._find(self, tests, obj, name, module, source_lines, globs, seen)
        from inspect import isroutine, isclass, ismodule, isfunction, ismethod
        if ismodule(obj) and self._recurse:
            for valname, val in obj.__dict__.items():
                valname1 = '%s.%s' % (name, valname)
                if (isroutine(val) or isclass(val)) and self._from_module(module, val):
                    self._find(tests, val, valname1, module, source_lines, globs, seen)

        if isclass(obj) and self._recurse:
            for valname, val in obj.__dict__.items():
                if isinstance(val, staticmethod):
                    val = getattr(obj, valname)
                if isinstance(val, classmethod):
                    val = getattr(obj, valname).im_func
                if (isfunction(val) or isclass(val) or ismethod(val) or isinstance(val, property)) and self._from_module(module, val):
                    valname = '%s.%s' % (name, valname)
                    self._find(tests, val, valname, module, source_lines, globs, seen)


class NumpyOutputChecker(doctest.OutputChecker):

    def check_output(self, want, got, optionflags):
        ret = doctest.OutputChecker.check_output(self, want, got, optionflags)
        if not ret:
            if '#random' in want:
                return True
            got = got.replace("'>", "'<")
            want = want.replace("'>", "'<")
            for sz in [4, 8]:
                got = got.replace("'<i%d'" % sz, 'int')
                want = want.replace("'<i%d'" % sz, 'int')

            ret = doctest.OutputChecker.check_output(self, want, got, optionflags)
        return ret


class NumpyDocTestCase(npd.DocTestCase):

    def __init__(self, test, optionflags=0, setUp=None, tearDown=None, checker=None, obj=None, result_var='_'):
        self._result_var = result_var
        self._nose_obj = obj
        doctest.DocTestCase.__init__(self, test, optionflags=optionflags, setUp=setUp, tearDown=tearDown, checker=checker)


print_state = numpy.get_printoptions()

class NumpyDoctest(npd.Doctest):
    name = 'numpydoctest'
    score = 1000
    doctest_optflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest_ignore = [
     'generate_numpy_api.py',
     'scons_support.py',
     'setupscons.py',
     'setup.py']
    doctest_case_class = NumpyDocTestCase
    out_check_class = NumpyOutputChecker
    test_finder_class = NumpyDocTestFinder

    def options(self, parser, env=os.environ):
        Plugin.options(self, parser, env)
        self.doctest_tests = True
        self.doctest_result_var = None
        return

    def configure(self, options, config):
        Plugin.configure(self, options, config)
        self.finder = self.test_finder_class()
        self.parser = doctest.DocTestParser()
        if self.enabled:
            config.plugins.plugins = [ p for p in config.plugins.plugins if p.name != 'doctest'
                                     ]

    def set_test_context(self, test):
        """ Configure `test` object to set test context

        We set the numpy / scipy standard doctest namespace

        Parameters
        ----------
        test : test object
            with ``globs`` dictionary defining namespace

        Returns
        -------
        None

        Notes
        -----
        `test` object modified in place
        """
        pkg_name = get_package_name(os.path.dirname(test.filename))
        test.globs = {'__builtins__': __builtins__, '__file__': '__main__', 
           '__name__': '__main__', 
           'np': numpy}
        if 'scipy' in pkg_name:
            p = pkg_name.split('.')
            p2 = p[-1]
            test.globs[p2] = __import__(pkg_name, test.globs, {}, [p2])

    def loadTestsFromModule(self, module):
        if not self.matches(module.__name__):
            npd.log.debug("Doctest doesn't want module %s", module)
            return
        try:
            tests = self.finder.find(module)
        except AttributeError:
            return

        if not tests:
            return
        tests.sort()
        module_file = src(module.__file__)
        for test in tests:
            if not test.examples:
                continue
            if not test.filename:
                test.filename = module_file
            self.set_test_context(test)
            yield self.doctest_case_class(test, optionflags=self.doctest_optflags, checker=self.out_check_class(), result_var=self.doctest_result_var)

    def afterContext(self):
        numpy.set_printoptions(**print_state)

    def wantFile(self, file):
        bn = os.path.basename(file)
        if bn in self.doctest_ignore:
            return False
        return npd.Doctest.wantFile(self, file)


class Unplugger(object):
    """ Nose plugin to remove named plugin late in loading

    By default it removes the "doctest" plugin.
    """
    name = 'unplugger'
    enabled = True
    score = 4000

    def __init__(self, to_unplug='doctest'):
        self.to_unplug = to_unplug

    def options(self, parser, env):
        pass

    def configure(self, options, config):
        config.plugins.plugins = [ p for p in config.plugins.plugins if p.name != self.to_unplug
                                 ]


class KnownFailureTest(Exception):
    """Raise this exception to mark a test as a known failing test."""
    pass


class KnownFailure(ErrorClassPlugin):
    """Plugin that installs a KNOWNFAIL error class for the
    KnownFailureClass exception.  When KnownFailureTest is raised,
    the exception will be logged in the knownfail attribute of the
    result, 'K' or 'KNOWNFAIL' (verbose) will be output, and the
    exception will not be counted as an error or failure."""
    enabled = True
    knownfail = ErrorClass(KnownFailureTest, label='KNOWNFAIL', isfailure=False)

    def options(self, parser, env=os.environ):
        env_opt = 'NOSE_WITHOUT_KNOWNFAIL'
        parser.add_option('--no-knownfail', action='store_true', dest='noKnownFail', default=env.get(env_opt, False), help='Disable special handling of KnownFailureTest exceptions')

    def configure(self, options, conf):
        if not self.can_configure:
            return
        self.conf = conf
        disable = getattr(options, 'noKnownFail', False)
        if disable:
            self.enabled = False


class NumpyTestProgram(nose.core.TestProgram):

    def runTests(self):
        """Run Tests. Returns true on success, false on failure, and
        sets self.success to the same value.

        Because nose currently discards the test result object, but we need
        to return it to the user, override TestProgram.runTests to retain
        the result
        """
        if self.testRunner is None:
            self.testRunner = nose.core.TextTestRunner(stream=self.config.stream, verbosity=self.config.verbosity, config=self.config)
        plug_runner = self.config.plugins.prepareTestRunner(self.testRunner)
        if plug_runner is not None:
            self.testRunner = plug_runner
        self.result = self.testRunner.run(self.test)
        self.success = self.result.wasSuccessful()
        return self.success