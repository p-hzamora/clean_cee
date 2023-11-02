# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\idl.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
import struct, numpy as np
from numpy.compat import asstr
import tempfile, zlib, warnings
DTYPE_DICT = {}
DTYPE_DICT[1] = '>u1'
DTYPE_DICT[2] = '>i2'
DTYPE_DICT[3] = '>i4'
DTYPE_DICT[4] = '>f4'
DTYPE_DICT[5] = '>f8'
DTYPE_DICT[6] = '>c8'
DTYPE_DICT[7] = '|O'
DTYPE_DICT[8] = '|O'
DTYPE_DICT[9] = '>c16'
DTYPE_DICT[10] = '|O'
DTYPE_DICT[11] = '|O'
DTYPE_DICT[12] = '>u2'
DTYPE_DICT[13] = '>u4'
DTYPE_DICT[14] = '>i8'
DTYPE_DICT[15] = '>u8'
RECTYPE_DICT = {}
RECTYPE_DICT[0] = 'START_MARKER'
RECTYPE_DICT[1] = 'COMMON_VARIABLE'
RECTYPE_DICT[2] = 'VARIABLE'
RECTYPE_DICT[3] = 'SYSTEM_VARIABLE'
RECTYPE_DICT[6] = 'END_MARKER'
RECTYPE_DICT[10] = 'TIMESTAMP'
RECTYPE_DICT[12] = 'COMPILED'
RECTYPE_DICT[13] = 'IDENTIFICATION'
RECTYPE_DICT[14] = 'VERSION'
RECTYPE_DICT[15] = 'HEAP_HEADER'
RECTYPE_DICT[16] = 'HEAP_DATA'
RECTYPE_DICT[17] = 'PROMOTE64'
RECTYPE_DICT[19] = 'NOTICE'
STRUCT_DICT = {}

def _align_32(f):
    """Align to the next 32-bit position in a file"""
    pos = f.tell()
    if pos % 4 != 0:
        f.seek(pos + 4 - pos % 4)


def _skip_bytes(f, n):
    """Skip `n` bytes"""
    f.read(n)


def _read_bytes(f, n):
    """Read the next `n` bytes"""
    return f.read(n)


def _read_byte(f):
    """Read a single byte"""
    return np.uint8(struct.unpack('>B', f.read(4)[:1])[0])


def _read_long(f):
    """Read a signed 32-bit integer"""
    return np.int32(struct.unpack('>l', f.read(4))[0])


def _read_int16(f):
    """Read a signed 16-bit integer"""
    return np.int16(struct.unpack('>h', f.read(4)[2:4])[0])


def _read_int32(f):
    """Read a signed 32-bit integer"""
    return np.int32(struct.unpack('>i', f.read(4))[0])


def _read_int64(f):
    """Read a signed 64-bit integer"""
    return np.int64(struct.unpack('>q', f.read(8))[0])


def _read_uint16(f):
    """Read an unsigned 16-bit integer"""
    return np.uint16(struct.unpack('>H', f.read(4)[2:4])[0])


def _read_uint32(f):
    """Read an unsigned 32-bit integer"""
    return np.uint32(struct.unpack('>I', f.read(4))[0])


def _read_uint64(f):
    """Read an unsigned 64-bit integer"""
    return np.uint64(struct.unpack('>Q', f.read(8))[0])


def _read_float32(f):
    """Read a 32-bit float"""
    return np.float32(struct.unpack('>f', f.read(4))[0])


def _read_float64(f):
    """Read a 64-bit float"""
    return np.float64(struct.unpack('>d', f.read(8))[0])


class Pointer(object):
    """Class used to define pointers"""

    def __init__(self, index):
        self.index = index


class ObjectPointer(Pointer):
    """Class used to define object pointers"""
    pass


def _read_string(f):
    """Read a string"""
    length = _read_long(f)
    if length > 0:
        chars = _read_bytes(f, length)
        _align_32(f)
        chars = asstr(chars)
    else:
        warnings.warn("warning: empty strings are now set to '' instead of None")
        chars = ''
    return chars


def _read_string_data(f):
    """Read a data string (length is specified twice)"""
    length = _read_long(f)
    if length > 0:
        length = _read_long(f)
        string_data = _read_bytes(f, length)
        _align_32(f)
    else:
        warnings.warn("warning: empty strings are now set to '' instead of None")
        string_data = ''
    return string_data


def _read_data(f, dtype):
    """Read a variable with a specified data type"""
    if dtype == 1:
        if _read_int32(f) != 1:
            raise Exception('Error occurred while reading byte variable')
        return _read_byte(f)
    if dtype == 2:
        return _read_int16(f)
    if dtype == 3:
        return _read_int32(f)
    if dtype == 4:
        return _read_float32(f)
    if dtype == 5:
        return _read_float64(f)
    if dtype == 6:
        real = _read_float32(f)
        imag = _read_float32(f)
        return np.complex64(real + imag * complex(0.0, 1.0))
    if dtype == 7:
        return _read_string_data(f)
    if dtype == 8:
        raise Exception('Should not be here - please report this')
    else:
        if dtype == 9:
            real = _read_float64(f)
            imag = _read_float64(f)
            return np.complex128(real + imag * complex(0.0, 1.0))
        if dtype == 10:
            return Pointer(_read_int32(f))
        if dtype == 11:
            return ObjectPointer(_read_int32(f))
        if dtype == 12:
            return _read_uint16(f)
        if dtype == 13:
            return _read_uint32(f)
        if dtype == 14:
            return _read_int64(f)
        if dtype == 15:
            return _read_uint64(f)
        raise Exception('Unknown IDL type: %i - please report this' % dtype)


def _read_structure(f, array_desc, struct_desc):
    """
    Read a structure, with the array and structure descriptors given as
    `array_desc` and `structure_desc` respectively.
    """
    nrows = array_desc['nelements']
    ncols = struct_desc['ntags']
    columns = struct_desc['tagtable']
    dtype = []
    for col in columns:
        if col['structure'] or col['array']:
            dtype.append(((col['name'].lower(), col['name']), np.object_))
        elif col['typecode'] in DTYPE_DICT:
            dtype.append(((col['name'].lower(), col['name']),
             DTYPE_DICT[col['typecode']]))
        else:
            raise Exception('Variable type %i not implemented' % col['typecode'])

    structure = np.recarray((nrows,), dtype=dtype)
    for i in range(nrows):
        for col in columns:
            dtype = col['typecode']
            if col['structure']:
                structure[col['name']][i] = _read_structure(f, struct_desc['arrtable'][col['name']], struct_desc['structtable'][col['name']])
            elif col['array']:
                structure[col['name']][i] = _read_array(f, dtype, struct_desc['arrtable'][col['name']])
            else:
                structure[col['name']][i] = _read_data(f, dtype)

    if array_desc['ndims'] > 1:
        warnings.warn('warning: multi-dimensional structures are now correctly reshaped')
        dims = array_desc['dims'][:int(array_desc['ndims'])]
        dims.reverse()
        structure = structure.reshape(dims)
    return structure


def _read_array(f, typecode, array_desc):
    """
    Read an array of type `typecode`, with the array descriptor given as
    `array_desc`.
    """
    if typecode in (1, 3, 4, 5, 6, 9, 13, 14, 15):
        if typecode == 1:
            nbytes = _read_int32(f)
            if nbytes != array_desc['nbytes']:
                raise Exception('Error occurred while reading byte array')
        array = np.fromstring(f.read(array_desc['nbytes']), dtype=DTYPE_DICT[typecode])
    elif typecode in (2, 12):
        array = np.fromstring(f.read(array_desc['nbytes'] * 2), dtype=DTYPE_DICT[typecode])[1::2]
    else:
        array = []
        for i in range(array_desc['nelements']):
            dtype = typecode
            data = _read_data(f, dtype)
            array.append(data)

        array = np.array(array, dtype=np.object_)
    if array_desc['ndims'] > 1:
        dims = array_desc['dims'][:int(array_desc['ndims'])]
        dims.reverse()
        array = array.reshape(dims)
    _align_32(f)
    return array


def _read_record(f):
    """Function to read in a full record"""
    record = {}
    recpos = f.tell()
    record['rectype'] = _read_long(f)
    nextrec = _read_uint32(f)
    nextrec += _read_uint32(f) * 4294967296
    _skip_bytes(f, 4)
    if record['rectype'] not in RECTYPE_DICT:
        raise Exception('Unknown RECTYPE: %i' % record['rectype'])
    record['rectype'] = RECTYPE_DICT[record['rectype']]
    if record['rectype'] in ('VARIABLE', 'HEAP_DATA'):
        if record['rectype'] == 'VARIABLE':
            record['varname'] = _read_string(f)
        else:
            record['heap_index'] = _read_long(f)
            _skip_bytes(f, 4)
        rectypedesc = _read_typedesc(f)
        varstart = _read_long(f)
        if varstart != 7:
            raise Exception('VARSTART is not 7')
        if rectypedesc['structure']:
            record['data'] = _read_structure(f, rectypedesc['array_desc'], rectypedesc['struct_desc'])
        elif rectypedesc['array']:
            record['data'] = _read_array(f, rectypedesc['typecode'], rectypedesc['array_desc'])
        else:
            dtype = rectypedesc['typecode']
            record['data'] = _read_data(f, dtype)
    elif record['rectype'] == 'TIMESTAMP':
        _skip_bytes(f, 1024)
        record['date'] = _read_string(f)
        record['user'] = _read_string(f)
        record['host'] = _read_string(f)
    elif record['rectype'] == 'VERSION':
        record['format'] = _read_long(f)
        record['arch'] = _read_string(f)
        record['os'] = _read_string(f)
        record['release'] = _read_string(f)
    elif record['rectype'] == 'IDENTIFICATON':
        record['author'] = _read_string(f)
        record['title'] = _read_string(f)
        record['idcode'] = _read_string(f)
    elif record['rectype'] == 'NOTICE':
        record['notice'] = _read_string(f)
    elif record['rectype'] == 'HEAP_HEADER':
        record['nvalues'] = _read_long(f)
        record['indices'] = []
        for i in range(record['nvalues']):
            record['indices'].append(_read_long(f))

    elif record['rectype'] == 'COMMONBLOCK':
        record['nvars'] = _read_long(f)
        record['name'] = _read_string(f)
        record['varnames'] = []
        for i in range(record['nvars']):
            record['varnames'].append(_read_string(f))

    elif record['rectype'] == 'END_MARKER':
        record['end'] = True
    elif record['rectype'] == 'UNKNOWN':
        warnings.warn('Skipping UNKNOWN record')
    elif record['rectype'] == 'SYSTEM_VARIABLE':
        warnings.warn('Skipping SYSTEM_VARIABLE record')
    else:
        raise Exception("record['rectype']=%s not implemented" % record['rectype'])
    f.seek(nextrec)
    return record


def _read_typedesc(f):
    """Function to read in a type descriptor"""
    typedesc = {}
    typedesc['typecode'] = _read_long(f)
    typedesc['varflags'] = _read_long(f)
    if typedesc['varflags'] & 2 == 2:
        raise Exception('System variables not implemented')
    typedesc['array'] = typedesc['varflags'] & 4 == 4
    typedesc['structure'] = typedesc['varflags'] & 32 == 32
    if typedesc['structure']:
        typedesc['array_desc'] = _read_arraydesc(f)
        typedesc['struct_desc'] = _read_structdesc(f)
    elif typedesc['array']:
        typedesc['array_desc'] = _read_arraydesc(f)
    return typedesc


def _read_arraydesc(f):
    """Function to read in an array descriptor"""
    arraydesc = {}
    arraydesc['arrstart'] = _read_long(f)
    if arraydesc['arrstart'] == 8:
        _skip_bytes(f, 4)
        arraydesc['nbytes'] = _read_long(f)
        arraydesc['nelements'] = _read_long(f)
        arraydesc['ndims'] = _read_long(f)
        _skip_bytes(f, 8)
        arraydesc['nmax'] = _read_long(f)
        arraydesc['dims'] = []
        for d in range(arraydesc['nmax']):
            arraydesc['dims'].append(_read_long(f))

    elif arraydesc['arrstart'] == 18:
        warnings.warn('Using experimental 64-bit array read')
        _skip_bytes(f, 8)
        arraydesc['nbytes'] = _read_uint64(f)
        arraydesc['nelements'] = _read_uint64(f)
        arraydesc['ndims'] = _read_long(f)
        _skip_bytes(f, 8)
        arraydesc['nmax'] = 8
        arraydesc['dims'] = []
        for d in range(arraydesc['nmax']):
            v = _read_long(f)
            if v != 0:
                raise Exception('Expected a zero in ARRAY_DESC')
            arraydesc['dims'].append(_read_long(f))

    else:
        raise Exception('Unknown ARRSTART: %i' % arraydesc['arrstart'])
    return arraydesc


def _read_structdesc(f):
    """Function to read in a structure descriptor"""
    structdesc = {}
    structstart = _read_long(f)
    if structstart != 9:
        raise Exception('STRUCTSTART should be 9')
    structdesc['name'] = _read_string(f)
    predef = _read_long(f)
    structdesc['ntags'] = _read_long(f)
    structdesc['nbytes'] = _read_long(f)
    structdesc['predef'] = predef & 1
    structdesc['inherits'] = predef & 2
    structdesc['is_super'] = predef & 4
    if not structdesc['predef']:
        structdesc['tagtable'] = []
        for t in range(structdesc['ntags']):
            structdesc['tagtable'].append(_read_tagdesc(f))

        for tag in structdesc['tagtable']:
            tag['name'] = _read_string(f)

        structdesc['arrtable'] = {}
        for tag in structdesc['tagtable']:
            if tag['array']:
                structdesc['arrtable'][tag['name']] = _read_arraydesc(f)

        structdesc['structtable'] = {}
        for tag in structdesc['tagtable']:
            if tag['structure']:
                structdesc['structtable'][tag['name']] = _read_structdesc(f)

        if structdesc['inherits'] or structdesc['is_super']:
            structdesc['classname'] = _read_string(f)
            structdesc['nsupclasses'] = _read_long(f)
            structdesc['supclassnames'] = []
            for s in range(structdesc['nsupclasses']):
                structdesc['supclassnames'].append(_read_string(f))

            structdesc['supclasstable'] = []
            for s in range(structdesc['nsupclasses']):
                structdesc['supclasstable'].append(_read_structdesc(f))

        STRUCT_DICT[structdesc['name']] = structdesc
    else:
        if structdesc['name'] not in STRUCT_DICT:
            raise Exception("PREDEF=1 but can't find definition")
        structdesc = STRUCT_DICT[structdesc['name']]
    return structdesc


def _read_tagdesc(f):
    """Function to read in a tag descriptor"""
    tagdesc = {}
    tagdesc['offset'] = _read_long(f)
    if tagdesc['offset'] == -1:
        tagdesc['offset'] = _read_uint64(f)
    tagdesc['typecode'] = _read_long(f)
    tagflags = _read_long(f)
    tagdesc['array'] = tagflags & 4 == 4
    tagdesc['structure'] = tagflags & 32 == 32
    tagdesc['scalar'] = tagdesc['typecode'] in DTYPE_DICT
    return tagdesc


def _replace_heap(variable, heap):
    if isinstance(variable, Pointer):
        while isinstance(variable, Pointer):
            if variable.index == 0:
                variable = None
            else:
                variable = heap[variable.index]

        replace, new = _replace_heap(variable, heap)
        if replace:
            variable = new
        return (
         True, variable)
    else:
        if isinstance(variable, np.core.records.recarray):
            for ir, record in enumerate(variable):
                replace, new = _replace_heap(record, heap)
                if replace:
                    variable[ir] = new

            return (False, variable)
        else:
            if isinstance(variable, np.core.records.record):
                for iv, value in enumerate(variable):
                    replace, new = _replace_heap(value, heap)
                    if replace:
                        variable[iv] = new

                return (False, variable)
            if isinstance(variable, np.ndarray):
                if variable.dtype.type is np.object_:
                    for iv in range(variable.size):
                        replace, new = _replace_heap(variable.item(iv), heap)
                        if replace:
                            variable.itemset(iv, new)

                return (
                 False, variable)
            return (
             False, variable)

        return


class AttrDict(dict):
    """
    A case-insensitive dictionary with access via item, attribute, and call
    notations:

        >>> d = AttrDict()
        >>> d['Variable'] = 123
        >>> d['Variable']
        123
        >>> d.Variable
        123
        >>> d.variable
        123
        >>> d('VARIABLE')
        123
    """

    def __init__(self, init={}):
        dict.__init__(self, init)

    def __getitem__(self, name):
        return super(AttrDict, self).__getitem__(name.lower())

    def __setitem__(self, key, value):
        return super(AttrDict, self).__setitem__(key.lower(), value)

    __getattr__ = __getitem__
    __setattr__ = __setitem__
    __call__ = __getitem__


def readsav(file_name, idict=None, python_dict=False, uncompressed_file_name=None, verbose=False):
    """
    Read an IDL .sav file

    Parameters
    ----------
    file_name : str
        Name of the IDL save file.
    idict : dict, optional
        Dictionary in which to insert .sav file variables
    python_dict : bool, optional
        By default, the object return is not a Python dictionary, but a
        case-insensitive dictionary with item, attribute, and call access
        to variables. To get a standard Python dictionary, set this option
        to True.
    uncompressed_file_name : str, optional
        This option only has an effect for .sav files written with the
        /compress option. If a file name is specified, compressed .sav
        files are uncompressed to this file. Otherwise, readsav will use
        the `tempfile` module to determine a temporary filename
        automatically, and will remove the temporary file upon successfully
        reading it in.
    verbose : bool, optional
        Whether to print out information about the save file, including
        the records read, and available variables.

    Returns
    -------
    idl_dict : AttrDict or dict
        If `python_dict` is set to False (default), this function returns a
        case-insensitive dictionary with item, attribute, and call access
        to variables. If `python_dict` is set to True, this function
        returns a Python dictionary with all variable names in lowercase.
        If `idict` was specified, then variables are written to the
        dictionary specified, and the updated dictionary is returned.

    """
    records = []
    if python_dict or idict:
        variables = {}
    else:
        variables = AttrDict()
    f = open(file_name, 'rb')
    signature = _read_bytes(f, 2)
    if signature != 'SR':
        raise Exception('Invalid SIGNATURE: %s' % signature)
    recfmt = _read_bytes(f, 2)
    if recfmt == '\x00\x04':
        pass
    else:
        if recfmt == '\x00\x06':
            if verbose:
                print('IDL Save file is compressed')
            if uncompressed_file_name:
                fout = open(uncompressed_file_name, 'w+b')
            else:
                fout = tempfile.NamedTemporaryFile(suffix='.sav')
            if verbose:
                print(' -> expanding to %s' % fout.name)
            fout.write('SR\x00\x04')
            while True:
                rectype = _read_long(f)
                fout.write(struct.pack('>l', int(rectype)))
                nextrec = _read_uint32(f)
                nextrec += _read_uint32(f) * 4294967296
                unknown = f.read(4)
                if RECTYPE_DICT[rectype] == 'END_MARKER':
                    fout.write(struct.pack('>I', int(nextrec) % 4294967296))
                    fout.write(struct.pack('>I', int((nextrec - nextrec % 4294967296) / 4294967296)))
                    fout.write(unknown)
                    break
                pos = f.tell()
                rec_string = zlib.decompress(f.read(nextrec - pos))
                nextrec = fout.tell() + len(rec_string) + 12
                fout.write(struct.pack('>I', int(nextrec % 4294967296)))
                fout.write(struct.pack('>I', int((nextrec - nextrec % 4294967296) / 4294967296)))
                fout.write(unknown)
                fout.write(rec_string)

            f.close()
            f = fout
            f.seek(4)
        else:
            raise Exception('Invalid RECFMT: %s' % recfmt)
        while True:
            r = _read_record(f)
            records.append(r)
            if 'end' in r:
                if r['end']:
                    break

        f.close()
        heap = {}
        for r in records:
            if r['rectype'] == 'HEAP_DATA':
                heap[r['heap_index']] = r['data']

        for r in records:
            if r['rectype'] == 'VARIABLE':
                replace, new = _replace_heap(r['data'], heap)
                if replace:
                    r['data'] = new
                variables[r['varname'].lower()] = r['data']

    if verbose:
        for record in records:
            if record['rectype'] == 'TIMESTAMP':
                print('-' * 50)
                print('Date: %s' % record['date'])
                print('User: %s' % record['user'])
                print('Host: %s' % record['host'])
                break

        for record in records:
            if record['rectype'] == 'VERSION':
                print('-' * 50)
                print('Format: %s' % record['format'])
                print('Architecture: %s' % record['arch'])
                print('Operating System: %s' % record['os'])
                print('IDL Version: %s' % record['release'])
                break

        for record in records:
            if record['rectype'] == 'IDENTIFICATON':
                print('-' * 50)
                print('Author: %s' % record['author'])
                print('Title: %s' % record['title'])
                print('ID Code: %s' % record['idcode'])
                break

        print('-' * 50)
        print('Successfully read %i records of which:' % len(records))
        rectypes = [ r['rectype'] for r in records ]
        for rt in set(rectypes):
            if rt != 'END_MARKER':
                print(' - %i are of type %s' % (rectypes.count(rt), rt))

        print('-' * 50)
        if 'VARIABLE' in rectypes:
            print('Available variables:')
            for var in variables:
                print(' - %s [%s]' % (var, type(variables[var])))

            print('-' * 50)
    if idict:
        for var in variables:
            idict[var] = variables[var]

        return idict
    return variables