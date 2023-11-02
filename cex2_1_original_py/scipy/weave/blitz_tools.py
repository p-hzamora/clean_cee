# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\blitz_tools.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
import parser, sys
from . import ast_tools
from . import slice_handler
from . import size_check
from . import converters
import numpy, copy
from . import inline_tools
from .inline_tools import attempt_function_call
function_catalog = inline_tools.function_catalog
function_cache = inline_tools.function_cache

def blitz(expr, local_dict=None, global_dict=None, check_size=1, verbose=0, **kw):
    global function_catalog
    call_frame = sys._getframe().f_back
    if local_dict is None:
        local_dict = call_frame.f_locals
    if global_dict is None:
        global_dict = call_frame.f_globals
    if check_size and not size_check.check_expr(expr, local_dict, global_dict):
        raise ValueError('inputs failed to pass size check.')
    try:
        results = apply(function_cache[expr], (local_dict, global_dict))
        return results
    except:
        pass

    try:
        results = attempt_function_call(expr, local_dict, global_dict)
    except ValueError:
        ast = parser.suite(expr)
        ast_list = ast.tolist()
        expr_code = ast_to_blitz_expr(ast_list)
        arg_names = ast_tools.harvest_variables(ast_list)
        module_dir = global_dict.get('__file__', None)
        func = inline_tools.compile_function(expr_code, arg_names, local_dict, global_dict, module_dir, compiler='gcc', auto_downcast=1, verbose=verbose, type_converters=converters.blitz, **kw)
        function_catalog.add_function(expr, func, module_dir)
        try:
            results = attempt_function_call(expr, local_dict, global_dict)
        except ValueError:
            print('warning: compilation failed. Executing as python code')
            exec (
             expr, global_dict, local_dict)

    return


def ast_to_blitz_expr(ast_seq):
    """ Convert an ast_sequence to a blitz expression.
    """
    ast_seq = copy.deepcopy(ast_seq)
    slice_handler.transform_slices(ast_seq)
    expr = ast_tools.ast_to_string(ast_seq)
    expr = expr.replace('slice(_beg,_end)', '_all')
    expr = expr.replace('slice', 'blitz::Range')
    expr = expr.replace('[', '(')
    expr = expr.replace(']', ')')
    expr = expr.replace('_stp', '1')
    return expr + ';\n'


def test_function():
    expr = 'ex[:,1:,1:] = k +  ca_x[:,1:,1:] * ex[:,1:,1:]+ cb_y_x[:,1:,1:] * (hz[:,1:,1:] - hz[:,:-1,1:])- cb_z_x[:,1:,1:] * (hy[:,1:,1:] - hy[:,1:,:-1])'
    ast = parser.suite(expr)
    k = 1.0
    ex = numpy.ones((1, 1, 1), dtype=numpy.float32)
    ca_x = numpy.ones((1, 1, 1), dtype=numpy.float32)
    cb_y_x = numpy.ones((1, 1, 1), dtype=numpy.float32)
    cb_z_x = numpy.ones((1, 1, 1), dtype=numpy.float32)
    hz = numpy.ones((1, 1, 1), dtype=numpy.float32)
    hy = numpy.ones((1, 1, 1), dtype=numpy.float32)
    blitz(expr)