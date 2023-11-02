# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: compiler\__init__.pyc
# Compiled at: 2011-03-08 09:43:14
"""Package for parsing and compiling Python source code

There are several functions defined at the top level that are imported
from modules contained in the package.

parse(buf, mode="exec") -> AST
    Converts a string containing Python source code to an abstract
    syntax tree (AST).  The AST is defined in compiler.ast.

parseFile(path) -> AST
    The same as parse(open(path))

walk(ast, visitor, verbose=None)
    Does a pre-order walk over the ast using the visitor instance.
    See compiler.visitor for details.

compile(source, filename, mode, flags=None, dont_inherit=None)
    Returns a code object.  A replacement for the builtin compile() function.

compileFile(filename)
    Generates a .pyc file by compiling filename.
"""
import warnings
warnings.warn('The compiler package is deprecated and removed in Python 3.x.', DeprecationWarning, stacklevel=2)
from compiler.transformer import parse, parseFile
from compiler.visitor import walk
from compiler.pycodegen import compile, compileFile