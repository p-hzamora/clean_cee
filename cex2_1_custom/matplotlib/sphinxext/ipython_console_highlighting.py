# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\sphinxext\ipython_console_highlighting.pyc
# Compiled at: 2012-10-30 18:11:14
"""reST directive for syntax-highlighting ipython interactive sessions.

XXX - See what improvements can be made based on the new (as of Sept 2009)
'pycon' lexer for the python console.  At the very least it will give better
highlighted tracebacks.
"""
from __future__ import print_function
import re
from pygments.lexer import Lexer, do_insertions
from pygments.lexers.agile import PythonConsoleLexer, PythonLexer, PythonTracebackLexer
from pygments.token import Comment, Generic
from sphinx import highlighting
line_re = re.compile('.*?\n')

class IPythonConsoleLexer(Lexer):
    """
    For IPython console output or doctests, such as:

    .. sourcecode:: ipython

      In [1]: a = 'foo'

      In [2]: a
      Out[2]: 'foo'

      In [3]: print a
      foo

      In [4]: 1 / 0

    Notes:

      - Tracebacks are not currently supported.

      - It assumes the default IPython prompts, not customized ones.
    """
    name = 'IPython console session'
    aliases = ['ipython']
    mimetypes = ['text/x-ipython-console']
    input_prompt = re.compile('(In \\[[0-9]+\\]: )|(   \\.\\.\\.+:)')
    output_prompt = re.compile('(Out\\[[0-9]+\\]: )|(   \\.\\.\\.+:)')
    continue_prompt = re.compile('   \\.\\.\\.+:')
    tb_start = re.compile('\\-+')

    def get_tokens_unprocessed(self, text):
        pylexer = PythonLexer(**self.options)
        tblexer = PythonTracebackLexer(**self.options)
        curcode = ''
        insertions = []
        for match in line_re.finditer(text):
            line = match.group()
            input_prompt = self.input_prompt.match(line)
            continue_prompt = self.continue_prompt.match(line.rstrip())
            output_prompt = self.output_prompt.match(line)
            if line.startswith('#'):
                insertions.append((len(curcode),
                 [
                  (
                   0, Comment, line)]))
            elif input_prompt is not None:
                insertions.append((len(curcode),
                 [
                  (
                   0, Generic.Prompt, input_prompt.group())]))
                curcode += line[input_prompt.end():]
            elif continue_prompt is not None:
                insertions.append((len(curcode),
                 [
                  (
                   0, Generic.Prompt, continue_prompt.group())]))
                curcode += line[continue_prompt.end():]
            elif output_prompt is not None:
                insertions.append((len(curcode),
                 [
                  (
                   0, Generic.Error, output_prompt.group())]))
                curcode += line[output_prompt.end():]
            else:
                if curcode:
                    for item in do_insertions(insertions, pylexer.get_tokens_unprocessed(curcode)):
                        yield item
                        curcode = ''
                        insertions = []

                yield (
                 match.start(), Generic.Output, line)

        if curcode:
            for item in do_insertions(insertions, pylexer.get_tokens_unprocessed(curcode)):
                yield item

        return


def setup(app):
    """Setup as a sphinx extension."""
    pass


highlighting.lexers['ipython'] = IPythonConsoleLexer()