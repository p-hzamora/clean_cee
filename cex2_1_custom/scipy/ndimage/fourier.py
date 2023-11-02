# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\ndimage\fourier.pyc
# Compiled at: 2013-02-16 13:27:30
from __future__ import division, print_function, absolute_import
import numpy
from . import _ni_support
from . import _nd_image
__all__ = [
 'fourier_gaussian', 'fourier_uniform', 'fourier_ellipsoid',
 'fourier_shift']

def _get_output_fourier(output, input):
    if output is None:
        if input.dtype.type in [numpy.complex64, numpy.complex128,
         numpy.float32]:
            output = numpy.zeros(input.shape, dtype=input.dtype)
        else:
            output = numpy.zeros(input.shape, dtype=numpy.float64)
        return_value = output
    elif type(output) is type:
        if output not in [numpy.complex64, numpy.complex128,
         numpy.float32, numpy.float64]:
            raise RuntimeError('output type not supported')
        output = numpy.zeros(input.shape, dtype=output)
        return_value = output
    else:
        if output.shape != input.shape:
            raise RuntimeError('output shape not correct')
        return_value = None
    return (
     output, return_value)


def _get_output_fourier_complex(output, input):
    if output is None:
        if input.dtype.type in [numpy.complex64, numpy.complex128]:
            output = numpy.zeros(input.shape, dtype=input.dtype)
        else:
            output = numpy.zeros(input.shape, dtype=numpy.complex128)
        return_value = output
    elif type(output) is type:
        if output not in [numpy.complex64, numpy.complex128]:
            raise RuntimeError('output type not supported')
        output = numpy.zeros(input.shape, dtype=output)
        return_value = output
    else:
        if output.shape != input.shape:
            raise RuntimeError('output shape not correct')
        return_value = None
    return (
     output, return_value)


def fourier_gaussian(input, sigma, n=-1, axis=-1, output=None):
    """
    Multi-dimensional Gaussian fourier filter.

    The array is multiplied with the fourier transform of a Gaussian
    kernel.

    Parameters
    ----------
    input : array_like
        The input array.
    sigma : float or sequence
        The sigma of the Gaussian kernel. If a float, `sigma` is the same for
        all axes. If a sequence, `sigma` has to contain one value for each
        axis.
    n : int, optional
        If `n` is negative (default), then the input is assumed to be the
        result of a complex fft.
        If `n` is larger than or equal to zero, the input is assumed to be the
        result of a real fft, and `n` gives the length of the array before
        transformation along the real transform direction.
    axis : int, optional
        The axis of the real transform.
    output : ndarray, optional
        If given, the result of filtering the input is placed in this array.
        None is returned in this case.

    Returns
    -------
    fourier_gaussian : ndarray or None
        The filtered input. If `output` is given as a parameter, None is
        returned.

    """
    input = numpy.asarray(input)
    output, return_value = _get_output_fourier(output, input)
    axis = _ni_support._check_axis(axis, input.ndim)
    sigmas = _ni_support._normalize_sequence(sigma, input.ndim)
    sigmas = numpy.asarray(sigmas, dtype=numpy.float64)
    if not sigmas.flags.contiguous:
        sigmas = sigmas.copy()
    _nd_image.fourier_filter(input, sigmas, n, axis, output, 0)
    return return_value


def fourier_uniform(input, size, n=-1, axis=-1, output=None):
    """
    Multi-dimensional uniform fourier filter.

    The array is multiplied with the fourier transform of a box of given
    size.

    Parameters
    ----------
    input : array_like
        The input array.
    size : float or sequence
        The size of the box used for filtering.
        If a float, `size` is the same for all axes. If a sequence, `size` has
        to contain one value for each axis.
    n : int, optional
        If `n` is negative (default), then the input is assumed to be the
        result of a complex fft.
        If `n` is larger than or equal to zero, the input is assumed to be the
        result of a real fft, and `n` gives the length of the array before
        transformation along the real transform direction.
    axis : int, optional
        The axis of the real transform.
    output : ndarray, optional
        If given, the result of filtering the input is placed in this array.
        None is returned in this case.

    Returns
    -------
    fourier_uniform : ndarray or None
        The filtered input. If `output` is given as a parameter, None is
        returned.

    """
    input = numpy.asarray(input)
    output, return_value = _get_output_fourier(output, input)
    axis = _ni_support._check_axis(axis, input.ndim)
    sizes = _ni_support._normalize_sequence(size, input.ndim)
    sizes = numpy.asarray(sizes, dtype=numpy.float64)
    if not sizes.flags.contiguous:
        sizes = sizes.copy()
    _nd_image.fourier_filter(input, sizes, n, axis, output, 1)
    return return_value


def fourier_ellipsoid(input, size, n=-1, axis=-1, output=None):
    """
    Multi-dimensional ellipsoid fourier filter.

    The array is multiplied with the fourier transform of a ellipsoid of
    given sizes.

    Parameters
    ----------
    input : array_like
        The input array.
    size : float or sequence
        The size of the box used for filtering.
        If a float, `size` is the same for all axes. If a sequence, `size` has
        to contain one value for each axis.
    n : int, optional
        If `n` is negative (default), then the input is assumed to be the
        result of a complex fft.
        If `n` is larger than or equal to zero, the input is assumed to be the
        result of a real fft, and `n` gives the length of the array before
        transformation along the real transform direction.
    axis : int, optional
        The axis of the real transform.
    output : ndarray, optional
        If given, the result of filtering the input is placed in this array.
        None is returned in this case.

    Returns
    -------
    fourier_ellipsoid : ndarray or None
        The filtered input. If `output` is given as a parameter, None is
        returned.

    Notes
    -----
    This function is implemented for arrays of rank 1, 2, or 3.

    """
    input = numpy.asarray(input)
    output, return_value = _get_output_fourier(output, input)
    axis = _ni_support._check_axis(axis, input.ndim)
    sizes = _ni_support._normalize_sequence(size, input.ndim)
    sizes = numpy.asarray(sizes, dtype=numpy.float64)
    if not sizes.flags.contiguous:
        sizes = sizes.copy()
    _nd_image.fourier_filter(input, sizes, n, axis, output, 2)
    return return_value


def fourier_shift(input, shift, n=-1, axis=-1, output=None):
    """
    Multi-dimensional fourier shift filter.

    The array is multiplied with the fourier transform of a shift operation.

    Parameters
    ----------
    input : array_like
        The input array.
    shift : float or sequence
        The size of the box used for filtering.
        If a float, `shift` is the same for all axes. If a sequence, `shift`
        has to contain one value for each axis.
    n : int, optional
        If `n` is negative (default), then the input is assumed to be the
        result of a complex fft.
        If `n` is larger than or equal to zero, the input is assumed to be the
        result of a real fft, and `n` gives the length of the array before
        transformation along the real transform direction.
    axis : int, optional
        The axis of the real transform.
    output : ndarray, optional
        If given, the result of shifting the input is placed in this array.
        None is returned in this case.

    Returns
    -------
    fourier_shift : ndarray or None
        The shifted input. If `output` is given as a parameter, None is
        returned.

    """
    input = numpy.asarray(input)
    output, return_value = _get_output_fourier_complex(output, input)
    axis = _ni_support._check_axis(axis, input.ndim)
    shifts = _ni_support._normalize_sequence(shift, input.ndim)
    shifts = numpy.asarray(shifts, dtype=numpy.float64)
    if not shifts.flags.contiguous:
        shifts = shifts.copy()
    _nd_image.fourier_shift(input, shifts, n, axis, output)
    return return_value