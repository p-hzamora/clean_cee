# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\arff\arffread.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
import re, itertools, numpy as np
from scipy.io.arff.utils import partial
from scipy.lib.six import next
__all__ = [
 'MetaData', 'loadarff', 'ArffError', 'ParseArffError']
r_meta = re.compile('^\\s*@')
r_comment = re.compile('^%')
r_empty = re.compile('^\\s+$')
r_headerline = re.compile('^@\\S*')
r_datameta = re.compile('^@[Dd][Aa][Tt][Aa]')
r_relation = re.compile('^@[Rr][Ee][Ll][Aa][Tt][Ii][Oo][Nn]\\s*(\\S*)')
r_attribute = re.compile('^@[Aa][Tt][Tt][Rr][Ii][Bb][Uu][Tt][Ee]\\s*(..*$)')
r_comattrval = re.compile("'(..+)'\\s+(..+$)")
r_mcomattrval = re.compile("'([..\\n]+)'\\s+(..+$)")
r_wcomattrval = re.compile('(\\S+)\\s+(..+$)')

class ArffError(IOError):
    pass


class ParseArffError(ArffError):
    pass


def parse_type(attrtype):
    """Given an arff attribute value (meta data), returns its type.

    Expect the value to be a name."""
    uattribute = attrtype.lower().strip()
    if uattribute[0] == '{':
        return 'nominal'
    if uattribute[:len('real')] == 'real':
        return 'numeric'
    if uattribute[:len('integer')] == 'integer':
        return 'numeric'
    if uattribute[:len('numeric')] == 'numeric':
        return 'numeric'
    if uattribute[:len('string')] == 'string':
        return 'string'
    if uattribute[:len('relational')] == 'relational':
        return 'relational'
    raise ParseArffError('unknown attribute %s' % uattribute)


def get_nominal(attribute):
    """If attribute is nominal, returns a list of the values"""
    return attribute.split(',')


def read_data_list(ofile):
    """Read each line of the iterable and put it in a list."""
    data = [
     next(ofile)]
    if data[0].strip()[0] == '{':
        raise ValueError('This looks like a sparse ARFF: not supported yet')
    data.extend([ i for i in ofile ])
    return data


def get_ndata(ofile):
    """Read the whole file to get number of data attributes."""
    data = [
     next(ofile)]
    loc = 1
    if data[0].strip()[0] == '{':
        raise ValueError('This looks like a sparse ARFF: not supported yet')
    for i in ofile:
        loc += 1

    return loc


def maxnomlen(atrv):
    """Given a string containing a nominal type definition, returns the
    string len of the biggest component.

    A nominal type is defined as seomthing framed between brace ({}).

    Parameters
    ----------
    atrv : str
       Nominal type definition

    Returns
    -------
    slen : int
       length of longest component

    Examples
    --------
    maxnomlen("{floup, bouga, fl, ratata}") returns 6 (the size of
    ratata, the longest nominal value).

    >>> maxnomlen("{floup, bouga, fl, ratata}")
    6
    """
    nomtp = get_nom_val(atrv)
    return max(len(i) for i in nomtp)


def get_nom_val(atrv):
    """Given a string containing a nominal type, returns a tuple of the
    possible values.

    A nominal type is defined as something framed between braces ({}).

    Parameters
    ----------
    atrv : str
       Nominal type definition

    Returns
    -------
    poss_vals : tuple
       possible values

    Examples
    --------
    >>> get_nom_val("{floup, bouga, fl, ratata}")
    ('floup', 'bouga', 'fl', 'ratata')
    """
    r_nominal = re.compile('{(..+)}')
    m = r_nominal.match(atrv)
    if m:
        return tuple(i.strip() for i in m.group(1).split(','))
    raise ValueError('This does not look like a nominal string')


def go_data(ofile):
    """Skip header.

    the first next() call of the returned iterator will be the @data line"""
    return itertools.dropwhile((lambda x: not r_datameta.match(x)), ofile)


def tokenize_attribute(iterable, attribute):
    """Parse a raw string in header (eg starts by @attribute).

    Given a raw string attribute, try to get the name and type of the
    attribute. Constraints:

    * The first line must start with @attribute (case insensitive, and
      space like characters before @attribute are allowed)
    * Works also if the attribute is spread on multilines.
    * Works if empty lines or comments are in between

    Parameters
    ----------
    attribute : str
       the attribute string.

    Returns
    -------
    name : str
       name of the attribute
    value : str
       value of the attribute
    next : str
       next line to be parsed

    Examples
    --------
    If attribute is a string defined in python as r"floupi real", will
    return floupi as name, and real as value.

    >>> iterable = iter([0] * 10) # dummy iterator
    >>> tokenize_attribute(iterable, r"@attribute floupi real")
    ('floupi', 'real', 0)

    If attribute is r"'floupi 2' real", will return 'floupi 2' as name,
    and real as value.

    >>> tokenize_attribute(iterable, r"  @attribute 'floupi 2' real   ")
    ('floupi 2', 'real', 0)

    """
    sattr = attribute.strip()
    mattr = r_attribute.match(sattr)
    if mattr:
        atrv = mattr.group(1)
        if r_comattrval.match(atrv):
            name, type = tokenize_single_comma(atrv)
            next_item = next(iterable)
        else:
            if r_wcomattrval.match(atrv):
                name, type = tokenize_single_wcomma(atrv)
                next_item = next(iterable)
            else:
                raise ValueError('multi line not supported yet')
    else:
        raise ValueError('First line unparsable: %s' % sattr)
    if type == 'relational':
        raise ValueError('relational attributes not supported yet')
    return (
     name, type, next_item)


def tokenize_multilines(iterable, val):
    """Can tokenize an attribute spread over several lines."""
    if not r_mcomattrval.match(val):
        all = [
         val]
        i = next(iterable)
        while not r_meta.match(i):
            all.append(i)
            i = next(iterable)

        if r_mend.search(i):
            raise ValueError('relational attribute not supported yet')
        print(('').join(all[:-1]))
        m = r_comattrval.match(('').join(all[:-1]))
        return (
         m.group(1), m.group(2), i)
    raise ValueError('Cannot parse attribute names spread over multi lines yet')


def tokenize_single_comma(val):
    m = r_comattrval.match(val)
    if m:
        try:
            name = m.group(1).strip()
            type = m.group(2).strip()
        except IndexError:
            raise ValueError('Error while tokenizing attribute')

    else:
        raise ValueError('Error while tokenizing single %s' % val)
    return (
     name, type)


def tokenize_single_wcomma(val):
    m = r_wcomattrval.match(val)
    if m:
        try:
            name = m.group(1).strip()
            type = m.group(2).strip()
        except IndexError:
            raise ValueError('Error while tokenizing attribute')

    else:
        raise ValueError('Error while tokenizing single %s' % val)
    return (
     name, type)


def read_header(ofile):
    """Read the header of the iterable ofile."""
    i = next(ofile)
    while r_comment.match(i):
        i = next(ofile)

    relation = None
    attributes = []
    while not r_datameta.match(i):
        m = r_headerline.match(i)
        if m:
            isattr = r_attribute.match(i)
            if isattr:
                name, type, i = tokenize_attribute(ofile, i)
                attributes.append((name, type))
            else:
                isrel = r_relation.match(i)
                if isrel:
                    relation = isrel.group(1)
                else:
                    raise ValueError('Error parsing line %s' % i)
                i = next(ofile)
        else:
            i = next(ofile)

    return (
     relation, attributes)


def safe_float(x):
    r"""given a string x, convert it to a float. If the stripped string is a ?,
    return a Nan (missing value).

    Parameters
    ----------
    x : str
       string to convert

    Returns
    -------
    f : float
       where float can be nan

    Examples
    --------
    >>> safe_float('1')
    1.0
    >>> safe_float('1\n')
    1.0
    >>> safe_float('?\n')
    nan
    """
    if '?' in x:
        return np.nan
    else:
        return np.float(x)


def safe_nominal(value, pvalue):
    svalue = value.strip()
    if svalue in pvalue:
        return svalue
    if svalue == '?':
        return svalue
    raise ValueError('%s value not in %s' % (str(svalue), str(pvalue)))


def get_delim(line):
    """Given a string representing a line of data, check whether the
    delimiter is ',' or space.

    Parameters
    ----------
    line : str
       line of data

    Returns
    -------
    delim : {',', ' '}

    Examples
    --------
    >>> get_delim(',')
    ','
    >>> get_delim(' ')
    ' '
    >>> get_delim(', ')
    ','
    >>> get_delim('x')
    Traceback (most recent call last):
       ...
    ValueError: delimiter not understood: x
    """
    if ',' in line:
        return ','
    if ' ' in line:
        return ' '
    raise ValueError('delimiter not understood: ' + line)


class MetaData(object):
    """Small container to keep useful informations on a ARFF dataset.

    Knows about attributes names and types.

    Examples
    --------
    data, meta = loadarff('iris.arff')
    # This will print the attributes names of the iris.arff dataset
    for i in meta:
        print i
    # This works too
    meta.names()
    # Getting attribute type
    types = meta.types()

    Notes
    -----
    Also maintains the list of attributes in order, i.e. doing for i in
    meta, where meta is an instance of MetaData, will return the
    different attribute names in the order they were defined.
    """

    def __init__(self, rel, attr):
        self.name = rel
        self._attributes = {}
        self._attrnames = []
        for name, value in attr:
            tp = parse_type(value)
            self._attrnames.append(name)
            if tp == 'nominal':
                self._attributes[name] = (
                 tp, get_nom_val(value))
            else:
                self._attributes[name] = (
                 tp, None)

        return

    def __repr__(self):
        msg = ''
        msg += 'Dataset: %s\n' % self.name
        for i in self._attrnames:
            msg += "\t%s's type is %s" % (i, self._attributes[i][0])
            if self._attributes[i][1]:
                msg += ', range is %s' % str(self._attributes[i][1])
            msg += '\n'

        return msg

    def __iter__(self):
        return iter(self._attrnames)

    def __getitem__(self, key):
        return self._attributes[key]

    def names(self):
        """Return the list of attribute names."""
        return self._attrnames

    def types(self):
        """Return the list of attribute types."""
        attr_types = [ self._attributes[name][0] for name in self._attrnames ]
        return attr_types


def loadarff(f):
    """
    Read an arff file.

    The data is returned as a record array, which can be accessed much like
    a dictionary of numpy arrays.  For example, if one of the attributes is
    called 'pressure', then its first 10 data points can be accessed from the
    ``data`` record array like so: ``data['pressure'][0:10]``

    Parameters
    ----------
    f : file-like or str
       File-like object to read from, or filename to open.

    Returns
    -------
    data : record array
       The data of the arff file, accessible by attribute names.
    meta : `MetaData`
       Contains information about the arff file such as name and
       type of attributes, the relation (name of the dataset), etc...

    Raises
    ------
    `ParseArffError`
        This is raised if the given file is not ARFF-formatted.
    NotImplementedError
        The ARFF file has an attribute which is not supported yet.

    Notes
    -----

    This function should be able to read most arff files. Not
    implemented functionality include:

    * date type attributes
    * string type attributes

    It can read files with numeric and nominal attributes.  It cannot read
    files with sparse data ({} in the file).  However, this function can
    read files with missing data (? in the file), representing the data
    points as NaNs.

    """
    if hasattr(f, 'read'):
        ofile = f
    else:
        ofile = open(f, 'rt')
    try:
        return _loadarff(ofile)
    finally:
        if ofile is not f:
            ofile.close()


def _loadarff(ofile):
    try:
        rel, attr = read_header(ofile)
    except ValueError as e:
        msg = 'Error while parsing header, error was: ' + str(e)
        raise ParseArffError(msg)

    hasstr = False
    for name, value in attr:
        type = parse_type(value)
        if type == 'string':
            hasstr = True

    meta = MetaData(rel, attr)
    acls2dtype = {'real': np.float, 'integer': np.float, 'numeric': np.float}
    acls2conv = {'real': safe_float, 'integer': safe_float, 'numeric': safe_float}
    descr = []
    convertors = []
    if not hasstr:
        for name, value in attr:
            type = parse_type(value)
            if type == 'date':
                raise ValueError('date type not supported yet, sorry')
            elif type == 'nominal':
                n = maxnomlen(value)
                descr.append((name, 'S%d' % n))
                pvalue = get_nom_val(value)
                convertors.append(partial(safe_nominal, pvalue=pvalue))
            else:
                descr.append((name, acls2dtype[type]))
                convertors.append(safe_float)

    else:
        raise NotImplementedError('String attributes not supported yet, sorry')
    ni = len(convertors)

    def next_data_line(row_iter):
        """Assumes we are already in the data part (eg after @data)."""
        raw = next(row_iter)
        while r_empty.match(raw):
            raw = next(row_iter)

        while r_comment.match(raw):
            raw = next(row_iter)

        return raw

    try:
        try:
            dtline = next_data_line(ofile)
            delim = get_delim(dtline)
        except ValueError as e:
            raise ParseArffError('Error while parsing delimiter: ' + str(e))

    finally:
        ofile.seek(0, 0)
        ofile = go_data(ofile)
        next(ofile)

    def generator(row_iter, delim=','):
        raw = next(row_iter)
        while r_empty.match(raw):
            raw = next(row_iter)

        while r_comment.match(raw):
            raw = next(row_iter)

        elems = list(range(ni))
        row = raw.split(delim)
        yield tuple([ convertors[i](row[i]) for i in elems ])
        for raw in row_iter:
            while r_comment.match(raw):
                raw = next(row_iter)

            while r_empty.match(raw):
                raw = next(row_iter)

            row = raw.split(delim)
            yield tuple([ convertors[i](row[i]) for i in elems ])

    a = generator(ofile, delim=delim)
    data = np.fromiter(a, descr)
    return (data, meta)


def basic_stats(data):
    nbfac = data.size * 1.0 / (data.size - 1)
    return (np.nanmin(data), np.nanmax(data), np.mean(data), np.std(data) * nbfac)


def print_attribute(name, tp, data):
    type = tp[0]
    if type == 'numeric' or type == 'real' or type == 'integer':
        min, max, mean, std = basic_stats(data)
        print('%s,%s,%f,%f,%f,%f' % (name, type, min, max, mean, std))
    else:
        msg = name + ',{'
        for i in range(len(tp[1]) - 1):
            msg += tp[1][i] + ','

        msg += tp[1][-1]
        msg += '}'
        print(msg)


def test_weka(filename):
    data, meta = loadarff(filename)
    print(len(data.dtype))
    print(data.size)
    for i in meta:
        print_attribute(i, meta[i], data[i])


test_weka.__test__ = False

def floupi(filename):
    data, meta = loadarff(filename)
    from attrselect import print_dataset_info
    print_dataset_info(data)
    print('relation %s, has %d instances' % (meta.name, data.size))
    itp = iter(types)
    for i in data.dtype.names:
        print_attribute(i, next(itp), data[i])


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    test_weka(filename)