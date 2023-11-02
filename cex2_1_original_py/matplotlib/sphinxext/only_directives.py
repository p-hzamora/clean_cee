# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\sphinxext\only_directives.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from docutils.nodes import Body, Element
from docutils.parsers.rst import directives

class only_base(Body, Element):

    def dont_traverse(self, *args, **kwargs):
        return []


class html_only(only_base):
    pass


class latex_only(only_base):
    pass


def run(content, node_class, state, content_offset):
    text = ('\n').join(content)
    node = node_class(text)
    state.nested_parse(content, content_offset, node)
    return [node]


def html_only_directive(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine):
    return run(content, html_only, state, content_offset)


def latex_only_directive(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine):
    return run(content, latex_only, state, content_offset)


def builder_inited(app):
    if app.builder.name == 'html':
        latex_only.traverse = only_base.dont_traverse
    else:
        html_only.traverse = only_base.dont_traverse


def setup(app):
    app.add_directive('htmlonly', html_only_directive, True, (0, 0, 0))
    app.add_directive('latexonly', latex_only_directive, True, (0, 0, 0))
    app.add_node(html_only)
    app.add_node(latex_only)

    def visit_perform(self, node):
        pass

    def depart_perform(self, node):
        pass

    def visit_ignore(self, node):
        node.children = []

    def depart_ignore(self, node):
        node.children = []

    app.add_node(html_only, html=(visit_perform, depart_perform))
    app.add_node(html_only, latex=(visit_ignore, depart_ignore))
    app.add_node(latex_only, latex=(visit_perform, depart_perform))
    app.add_node(latex_only, html=(visit_ignore, depart_ignore))