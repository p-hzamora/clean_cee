# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\weave\ast_tools.pyc
# Compiled at: 2013-03-29 22:51:36
from __future__ import absolute_import, print_function
import token, symbol, parser

def issequence(t):
    return isinstance(t, (list, tuple))


def int_to_symbol(i):
    """ Convert numeric symbol or token to a desriptive name.
    """
    try:
        return symbol.sym_name[i]
    except KeyError:
        return token.tok_name[i]


def translate_symbols(ast_tuple):
    """ Translate numeric grammar symbols in an ast_tuple descriptive names.

        This simply traverses the tree converting any integer value to values
        found in symbol.sym_name or token.tok_name.
    """
    new_list = []
    for item in ast_tuple:
        if isinstance(item, int):
            new_list.append(int_to_symbol(item))
        elif issequence(item):
            new_list.append(translate_symbols(item))
        else:
            new_list.append(item)

    if isinstance(ast_tuple, tuple):
        return tuple(new_list)
    else:
        return new_list


def ast_to_string(ast_seq):
    """* Traverse an ast tree sequence, printing out all leaf nodes.

         This effectively rebuilds the expression the tree was built
         from.  I guess its probably missing whitespace.  How bout
         indent stuff and new lines?  Haven't checked this since we're
         currently only dealing with simple expressions.
    *"""
    output = ''
    for item in ast_seq:
        if isinstance(item, str):
            output = output + item
        elif issequence(item):
            output = output + ast_to_string(item)

    return output


def build_atom(expr_string):
    """ Build an ast for an atom from the given expr string.

        If expr_string is not a string, it is converted to a string
        before parsing to an ast_tuple.
    """
    if isinstance(expr_string, str):
        ast = parser.expr(expr_string).totuple()[1][1]
    else:
        ast = parser.expr(repr(expr_string)).totuple()[1][1]
    return ast


def atom_tuple(expr_string):
    return build_atom(expr_string)


def atom_list(expr_string):
    return tuples_to_lists(build_atom(expr_string))


def find_first_pattern(ast_tuple, pattern_list):
    """* Find the first occurence of a pattern one of a list of patterns
        in ast_tuple.

        Used for testing at the moment.

        ast_tuple    -- tuple or list created by ast.totuple() or ast.tolist().
        pattern_list -- A single pattern or list of patterns to search
                        for in the ast_tuple.  If a single pattern is
                        used, it MUST BE A IN A TUPLE format.
        Returns:
            found -- true/false indicating whether pattern was found
            data  -- dictionary of data from first matching pattern in tree.
                     (see match function by Jeremy Hylton).
    *"""
    found, data = 0, {}
    if not isinstance(pattern_list, list):
        pattern_list = [
         pattern_list]
    for pattern in pattern_list:
        found, data = match(pattern, ast_tuple)
        if found:
            break

    if not found:
        for item in ast_tuple:
            if issequence(item):
                found, data = find_first_pattern(item, pattern_list)
            if found:
                break

    return (
     found, data)


name_pattern = (
 token.NAME, ['var'])

def remove_duplicates(lst):
    output = []
    for item in lst:
        if item not in output:
            output.append(item)

    return output


reserved_names = [
 'sin']

def remove_reserved_names(lst):
    """ These are functions names -- don't create variables for them
        There is a more reobust approach, but this ought to work pretty
        well.
    """
    output = []
    for item in lst:
        if item not in reserved_names:
            output.append(item)

    return output


def harvest_variables(ast_list):
    """ Retreive all the variables that need to be defined.
    """
    variables = []
    if issequence(ast_list):
        found, data = match(name_pattern, ast_list)
        if found:
            variables.append(data['var'])
        for item in ast_list:
            if issequence(item):
                variables.extend(harvest_variables(item))

    variables = remove_duplicates(variables)
    variables = remove_reserved_names(variables)
    return variables


def match(pattern, data, vars=None):
    """match `data' to `pattern', with variable extraction.

    pattern
        Pattern to match against, possibly containing variables.

    data
        Data to be checked and against which variables are extracted.

    vars
        Dictionary of variables which have already been found.  If not
        provided, an empty dictionary is created.

    The `pattern' value may contain variables of the form ['varname'] which
    are allowed to match anything.  The value that is matched is returned as
    part of a dictionary which maps 'varname' to the matched value.  'varname'
    is not required to be a string object, but using strings makes patterns
    and the code which uses them more readable.

    This function returns two values: a boolean indicating whether a match
    was found and a dictionary mapping variable names to their associated
    values.

    From the Demo/Parser/example.py file
    """
    if vars is None:
        vars = {}
    if isinstance(pattern, list):
        vars[pattern[0]] = data
        return (
         1, vars)
    else:
        if not isinstance(pattern, tuple):
            return (pattern == data, vars)
        if len(data) != len(pattern):
            return (0, vars)
        for pattern, data in zip(pattern, data):
            same, vars = match(pattern, data, vars)
            if not same:
                break

        return (
         same, vars)


def tuples_to_lists(ast_tuple):
    """ Convert an ast object tree in tuple form to list form.
    """
    if not issequence(ast_tuple):
        return ast_tuple
    new_list = []
    for item in ast_tuple:
        new_list.append(tuples_to_lists(item))

    return new_list