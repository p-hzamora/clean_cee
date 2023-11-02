# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\slice_handler.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
from .ast_tools import token, symbol, ast_to_string, match, atom_list

def slice_ast_to_dict(ast_seq):
    sl_vars = {}
    if isinstance(ast_seq, (list, tuple)):
        for pattern in slice_patterns:
            found, data = match(pattern, ast_seq)
            if found:
                sl_vars = {'begin': '_beg', 'end': '_end', 'step': '_stp', 
                   'single_index': '_index'}
                for key in data.keys():
                    data[key] = ast_to_string(data[key])

                sl_vars.update(data)
                break

    return sl_vars


def build_slice_atom(slice_vars, position):
    if slice_vars['single_index'] != '_index':
        expr = '%(single_index)s' % slice_vars
    else:
        begin = slice_vars['begin'].strip()
        if begin[0] == '-':
            slice_vars['begin'] = 'N' + slice_vars['var'] + repr(position) + begin
        end = slice_vars['end'].strip()
        if end != '_end' and end[0] != '-':
            slice_vars['end'] = end + '-1'
        if end[0] == '-':
            slice_vars['end'] = 'N%s[%d]%s-1' % (slice_vars['var'], position, end)
        if slice_vars['step'] == '_stp':
            expr = 'slice(%(begin)s,%(end)s)' % slice_vars
        else:
            expr = 'slice(%(begin)s,%(end)s,%(step)s)' % slice_vars
    val = atom_list(expr)
    return val


def transform_subscript_list(subscript_dict):
    subscript_list = subscript_dict['subscript_list']
    var = subscript_dict['var']
    slice_position = -1
    for i in range(1, len(subscript_list)):
        if subscript_list[i][0] != token.COMMA:
            slice_position += 1
            slice_vars = slice_ast_to_dict(subscript_list[i])
            slice_vars['var'] = var
            subscript_list[i] = build_slice_atom(slice_vars, slice_position)


def harvest_subscript_dicts(ast_list):
    """ Needs Tests!
    """
    subscript_lists = []
    if isinstance(ast_list, list):
        found, data = match(indexed_array_pattern, ast_list)
        if found:
            subscript_lists.append(data)
        for item in ast_list:
            if isinstance(item, list):
                subscript_lists.extend(harvest_subscript_dicts(item))

    return subscript_lists


def transform_slices(ast_list):
    """ Walk through an ast_list converting all x:y:z subscripts
        to slice(x,y,z) subscripts.
    """
    all_dicts = harvest_subscript_dicts(ast_list)
    for subscript_dict in all_dicts:
        transform_subscript_list(subscript_dict)


slice_patterns = []
CLN = (token.COLON, ':')
CLN2 = (symbol.sliceop, (token.COLON, ':'))
CLN2_STEP = (symbol.sliceop, (token.COLON, ':'), ['step'])
slice_patterns.append((symbol.subscript, ['begin'], CLN, ['end'], CLN2_STEP))
slice_patterns.append((symbol.subscript, CLN, ['end'], CLN2_STEP))
slice_patterns.append((symbol.subscript, ['begin'], CLN, CLN2_STEP))
slice_patterns.append((symbol.subscript, ['begin'], CLN, ['end'], CLN2))
slice_patterns.append((symbol.subscript, ['begin'], CLN, CLN2))
slice_patterns.append((symbol.subscript, CLN, ['end'], CLN2))
slice_patterns.append((symbol.subscript, CLN, CLN2_STEP))
slice_patterns.append((symbol.subscript, CLN, CLN2))
slice_patterns.append((symbol.subscript, ['begin'], CLN, ['end']))
slice_patterns.append((symbol.subscript, CLN, ['end']))
slice_patterns.append((symbol.subscript, ['begin'], CLN))
slice_patterns.append((symbol.subscript, CLN))
slice_patterns.append((symbol.subscript, ['single_index']))
indexed_array_pattern = (
 symbol.power,
 (
  symbol.atom, (token.NAME, ['var'])),
 (
  symbol.trailer,
  (
   token.LSQB, '['),
  [
   'subscript_list'],
  (
   token.RSQB, ']')))