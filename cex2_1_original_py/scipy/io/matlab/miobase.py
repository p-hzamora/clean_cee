# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\io\matlab\miobase.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Base classes for MATLAB file stream reading.

MATLAB is a registered trademark of the Mathworks inc.
"""
from __future__ import division, print_function, absolute_import
import sys, numpy as np
if sys.version_info[0] >= 3:
    byteord = int
else:
    byteord = ord
from scipy.misc import doccer
from . import byteordercodes as boc

class MatReadError(Exception):
    pass


class MatWriteError(Exception):
    pass


class MatReadWarning(UserWarning):
    pass


doc_dict = {'file_arg': 'file_name : str\n   Name of the mat file (do not need .mat extension if\n   appendmat==True) Can also pass open file-like object.', 
   'append_arg': 'appendmat : bool, optional\n   True to append the .mat extension to the end of the given\n   filename, if not already present.', 
   'load_args': "byte_order : str or None, optional\n   None by default, implying byte order guessed from mat\n   file. Otherwise can be one of ('native', '=', 'little', '<',\n   'BIG', '>').\nmat_dtype : bool, optional\n   If True, return arrays in same dtype as would be loaded into\n   MATLAB (instead of the dtype with which they are saved).\nsqueeze_me : bool, optional\n   Whether to squeeze unit matrix dimensions or not.\nchars_as_strings : bool, optional\n   Whether to convert char arrays to string arrays.\nmatlab_compatible : bool, optional\n   Returns matrices as would be loaded by MATLAB (implies\n   squeeze_me=False, chars_as_strings=False, mat_dtype=True,\n   struct_as_record=True).", 
   'struct_arg': 'struct_as_record : bool, optional\n   Whether to load MATLAB structs as numpy record arrays, or as\n   old-style numpy arrays with dtype=object.  Setting this flag to\n   False replicates the behavior of scipy version 0.7.x (returning\n   numpy object arrays).  The default setting is True, because it\n   allows easier round-trip load and save of MATLAB files.', 
   'matstream_arg': 'mat_stream : file-like\n   Object with file API, open for reading.', 
   'long_fields': 'long_field_names : bool, optional\n   * False - maximum field name length in a structure is 31 characters\n     which is the documented maximum length. This is the default.\n   * True - maximum field name length in a structure is 63 characters\n     which works for MATLAB 7.6', 
   'do_compression': 'do_compression : bool, optional\n   Whether to compress matrices on write. Default is False.', 
   'oned_as': "oned_as : {'column', 'row'}, optional\n   If 'column', write 1-D numpy arrays as column vectors.\n   If 'row', write 1D numpy arrays as row vectors.", 
   'unicode_strings': 'unicode_strings : bool, optional\n   If True, write strings as Unicode, else MATLAB usual encoding.'}
docfiller = doccer.filldoc(doc_dict)

def convert_dtypes(dtype_template, order_code):
    """ Convert dtypes in mapping to given order

    Parameters
    ----------
    dtype_template : mapping
       mapping with values returning numpy dtype from ``np.dtype(val)``
    order_code : str
       an order code suitable for using in ``dtype.newbyteorder()``

    Returns
    -------
    dtypes : mapping
       mapping where values have been replaced by
       ``np.dtype(val).newbyteorder(order_code)``

    """
    dtypes = dtype_template.copy()
    for k in dtypes:
        dtypes[k] = np.dtype(dtypes[k]).newbyteorder(order_code)

    return dtypes


def read_dtype(mat_stream, a_dtype):
    """
    Generic get of byte stream data of known type

    Parameters
    ----------
    mat_stream : file_like object
        MATLAB (tm) mat file stream
    a_dtype : dtype
        dtype of array to read.  `a_dtype` is assumed to be correct
        endianness.

    Returns
    -------
    arr : ndarray
        Array of dtype `a_dtype` read from stream.

    """
    num_bytes = a_dtype.itemsize
    arr = np.ndarray(shape=(), dtype=a_dtype, buffer=mat_stream.read(num_bytes), order='F')
    return arr


def get_matfile_version(fileobj):
    """
    Return major, minor tuple depending on apparent mat file type

    Where:

     #. 0,x -> version 4 format mat files
     #. 1,x -> version 5 format mat files
     #. 2,x -> version 7.3 format mat files (HDF format)

    Parameters
    ----------
    fileobj : file_like
        object implementing seek() and read()

    Returns
    -------
    major_version : {0, 1, 2}
        major MATLAB File format version
    minor_version : int
        minor MATLAB file format version

    Notes
    -----
    Has the side effect of setting the file read pointer to 0

    """
    fileobj.seek(0)
    mopt_bytes = np.ndarray(shape=(4, ), dtype=np.uint8, buffer=fileobj.read(4))
    if 0 in mopt_bytes:
        fileobj.seek(0)
        return (0, 0)
    fileobj.seek(124)
    tst_str = fileobj.read(4)
    fileobj.seek(0)
    maj_ind = int(tst_str[2] == 'I')
    maj_val = byteord(tst_str[maj_ind])
    min_val = byteord(tst_str[1 - maj_ind])
    ret = (maj_val, min_val)
    if maj_val in (1, 2):
        return ret
    raise ValueError('Unknown mat file type, version %s, %s' % ret)


def matdims(arr, oned_as='column'):
    """
    Determine equivalent MATLAB dimensions for given array

    Parameters
    ----------
    arr : ndarray
        Input array
    oned_as : {'column', 'row'}, optional
        Whether 1-D arrays are returned as MATLAB row or column matrices.
        Default is 'column'.

    Returns
    -------
    dims : tuple
        Shape tuple, in the form MATLAB expects it.

    Notes
    -----
    We had to decide what shape a 1 dimensional array would be by
    default.  ``np.atleast_2d`` thinks it is a row vector.  The
    default for a vector in MATLAB (e.g. ``>> 1:12``) is a row vector.

    Versions of scipy up to and including 0.11 resulted (accidentally)
    in 1-D arrays being read as column vectors.  For the moment, we
    maintain the same tradition here.

    Examples
    --------
    >>> matdims(np.array(1)) # numpy scalar
    (1, 1)
    >>> matdims(np.array([1])) # 1d array, 1 element
    (1, 1)
    >>> matdims(np.array([1,2])) # 1d array, 2 elements
    (2, 1)
    >>> matdims(np.array([[2],[3]])) # 2d array, column vector
    (2, 1)
    >>> matdims(np.array([[2,3]])) # 2d array, row vector
    (1, 2)
    >>> matdims(np.array([[[2,3]]])) # 3d array, rowish vector
    (1, 1, 2)
    >>> matdims(np.array([])) # empty 1d array
    (0, 0)
    >>> matdims(np.array([[]])) # empty 2d
    (0, 0)
    >>> matdims(np.array([[[]]])) # empty 3d
    (0, 0, 0)

    Optional argument flips 1-D shape behavior.

    >>> matdims(np.array([1,2]), 'row') # 1d array, 2 elements
    (1, 2)

    The argument has to make sense though

    >>> matdims(np.array([1,2]), 'bizarre')
    Traceback (most recent call last):
       ...
    ValueError: 1D option "bizarre" is strange

    """
    if arr.size == 0:
        return (0, ) * np.max([arr.ndim, 2])
    shape = arr.shape
    if shape == ():
        return (1, 1)
    if len(shape) == 1:
        if oned_as == 'column':
            return shape + (1, )
        if oned_as == 'row':
            return (1, ) + shape
        raise ValueError('1D option "%s" is strange' % oned_as)
    return shape


class MatVarReader(object):
    """ Abstract class defining required interface for var readers"""

    def __init__(self, file_reader):
        pass

    def read_header(self):
        """ Returns header """
        pass

    def array_from_header(self, header):
        """ Reads array given header """
        pass


class MatFileReader(object):
    """ Base object for reading mat files

    To make this class functional, you will need to override the
    following methods:

    matrix_getter_factory   - gives object to fetch next matrix from stream
    guess_byte_order        - guesses file byte order from file
    """

    @docfiller
    def __init__(self, mat_stream, byte_order=None, mat_dtype=False, squeeze_me=False, chars_as_strings=True, matlab_compatible=False, struct_as_record=True):
        """
        Initializer for mat file reader

        mat_stream : file-like
            object with file API, open for reading
    %(load_args)s
        """
        self.mat_stream = mat_stream
        self.dtypes = {}
        if not byte_order:
            byte_order = self.guess_byte_order()
        else:
            byte_order = boc.to_numpy_code(byte_order)
        self.byte_order = byte_order
        self.struct_as_record = struct_as_record
        if matlab_compatible:
            self.set_matlab_compatible()
        else:
            self.squeeze_me = squeeze_me
            self.chars_as_strings = chars_as_strings
            self.mat_dtype = mat_dtype

    def set_matlab_compatible(self):
        """ Sets options to return arrays as MATLAB loads them """
        self.mat_dtype = True
        self.squeeze_me = False
        self.chars_as_strings = False

    def guess_byte_order(self):
        """ As we do not know what file type we have, assume native """
        return boc.native_code

    def end_of_stream(self):
        b = self.mat_stream.read(1)
        curpos = self.mat_stream.tell()
        self.mat_stream.seek(curpos - 1)
        return len(b) == 0


def arr_dtype_number(arr, num):
    """ Return dtype for given number of items per element"""
    return np.dtype(arr.dtype.str[:2] + str(num))


def arr_to_chars(arr):
    """ Convert string array to char array """
    dims = list(arr.shape)
    if not dims:
        dims = [
         1]
    dims.append(int(arr.dtype.str[2:]))
    arr = np.ndarray(shape=dims, dtype=arr_dtype_number(arr, 1), buffer=arr)
    empties = [arr == '']
    if not np.any(empties):
        return arr
    arr = arr.copy()
    arr[empties] = ' '
    return arr