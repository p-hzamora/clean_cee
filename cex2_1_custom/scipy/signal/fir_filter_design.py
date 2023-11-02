# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\signal\fir_filter_design.pyc
# Compiled at: 2013-02-16 13:27:32
"""Functions for FIR filter design."""
from __future__ import division, print_function, absolute_import
from math import ceil, log
import numpy as np
from numpy.fft import irfft
from scipy.special import sinc
from . import sigtools
__all__ = [
 'kaiser_beta', 'kaiser_atten', 'kaiserord', 
 'firwin', 'firwin2', 'remez']

def kaiser_beta(a):
    """Compute the Kaiser parameter `beta`, given the attenuation `a`.

    Parameters
    ----------
    a : float
        The desired attenuation in the stopband and maximum ripple in
        the passband, in dB.  This should be a *positive* number.

    Returns
    -------
    beta : float
        The `beta` parameter to be used in the formula for a Kaiser window.

    References
    ----------
    Oppenheim, Schafer, "Discrete-Time Signal Processing", p.475-476.
    """
    if a > 50:
        beta = 0.1102 * (a - 8.7)
    elif a > 21:
        beta = 0.5842 * (a - 21) ** 0.4 + 0.07886 * (a - 21)
    else:
        beta = 0.0
    return beta


def kaiser_atten(numtaps, width):
    """Compute the attenuation of a Kaiser FIR filter.

    Given the number of taps `N` and the transition width `width`, compute the
    attenuation `a` in dB, given by Kaiser's formula:

        a = 2.285 * (N - 1) * pi * width + 7.95

    Parameters
    ----------
    N : int
        The number of taps in the FIR filter.
    width : float
        The desired width of the transition region between passband and
        stopband (or, in general, at any discontinuity) for the filter.

    Returns
    -------
    a : float
        The attenuation of the ripple, in dB.

    See Also
    --------
    kaiserord, kaiser_beta
    """
    a = 2.285 * (numtaps - 1) * np.pi * width + 7.95
    return a


def kaiserord(ripple, width):
    """
    Design a Kaiser window to limit ripple and width of transition region.

    Parameters
    ----------
    ripple : float
        Positive number specifying maximum ripple in passband (dB) and minimum
        ripple in stopband.
    width : float
        Width of transition region (normalized so that 1 corresponds to pi
        radians / sample).

    Returns
    -------
    numtaps : int
        The length of the kaiser window.
    beta :
        The beta parameter for the kaiser window.

    See Also
    --------
    kaiser_beta, kaiser_atten

    Notes
    -----
    There are several ways to obtain the Kaiser window:

    - ``signal.kaiser(numtaps, beta, sym=0)``
    - ``signal.get_window(beta, numtaps)``
    - ``signal.get_window(('kaiser', beta), numtaps)``

    The empirical equations discovered by Kaiser are used.

    References
    ----------
    Oppenheim, Schafer, "Discrete-Time Signal Processing", p.475-476.

    """
    A = abs(ripple)
    if A < 8:
        raise ValueError('Requested maximum ripple attentuation %f is too small for the Kaiser formula.' % A)
    beta = kaiser_beta(A)
    numtaps = (A - 7.95) / 2.285 / (np.pi * width) + 1
    return (
     int(ceil(numtaps)), beta)


def firwin(numtaps, cutoff, width=None, window='hamming', pass_zero=True, scale=True, nyq=1.0):
    """
    FIR filter design using the window method.

    This function computes the coefficients of a finite impulse response
    filter.  The filter will have linear phase; it will be Type I if
    `numtaps` is odd and Type II if `numtaps` is even.

    Type II filters always have zero response at the Nyquist rate, so a
    ValueError exception is raised if firwin is called with `numtaps` even and
    having a passband whose right end is at the Nyquist rate.

    Parameters
    ----------
    numtaps : int
        Length of the filter (number of coefficients, i.e. the filter
        order + 1).  `numtaps` must be even if a passband includes the
        Nyquist frequency.
    cutoff : float or 1D array_like
        Cutoff frequency of filter (expressed in the same units as `nyq`)
        OR an array of cutoff frequencies (that is, band edges). In the
        latter case, the frequencies in `cutoff` should be positive and
        monotonically increasing between 0 and `nyq`.  The values 0 and
        `nyq` must not be included in `cutoff`.
    width : float or None
        If `width` is not None, then assume it is the approximate width
        of the transition region (expressed in the same units as `nyq`)
        for use in Kaiser FIR filter design.  In this case, the `window`
        argument is ignored.
    window : string or tuple of string and parameter values
        Desired window to use. See `scipy.signal.get_window` for a list
        of windows and required parameters.
    pass_zero : bool
        If True, the gain at the frequency 0 (i.e. the "DC gain") is 1.
        Otherwise the DC gain is 0.
    scale : bool
        Set to True to scale the coefficients so that the frequency
        response is exactly unity at a certain frequency.
        That frequency is either:

            0 (DC) if the first passband starts at 0 (i.e. pass_zero
              is True)

            `nyq` (the Nyquist rate) if the first passband ends at
              `nyq` (i.e the filter is a single band highpass filter);
              center of first passband otherwise

    nyq : float
        Nyquist frequency.  Each frequency in `cutoff` must be between 0
        and `nyq`.

    Returns
    -------
    h : (numtaps,) ndarray
        Coefficients of length `numtaps` FIR filter.

    Raises
    ------
    ValueError
        If any value in `cutoff` is less than or equal to 0 or greater
        than or equal to `nyq`, if the values in `cutoff` are not strictly
        monotonically increasing, or if `numtaps` is even but a passband
        includes the Nyquist frequency.

    See also
    --------
    scipy.signal.firwin2

    Examples
    --------
    Low-pass from 0 to f::

    >>> from scipy import signal
    >>> signal.firwin(numtaps, f)

    Use a specific window function::

    >>> signal.firwin(numtaps, f, window='nuttall')

    High-pass ('stop' from 0 to f)::

    >>> signal.firwin(numtaps, f, pass_zero=False)

    Band-pass::

    >>> signal.firwin(numtaps, [f1, f2], pass_zero=False)

    Band-stop::

    >>> signal.firwin(numtaps, [f1, f2])

    Multi-band (passbands are [0, f1], [f2, f3] and [f4, 1])::

    >>> signal.firwin(numtaps, [f1, f2, f3, f4])

    Multi-band (passbands are [f1, f2] and [f3,f4])::

    >>> signal.firwin(numtaps, [f1, f2, f3, f4], pass_zero=False)

    """
    cutoff = np.atleast_1d(cutoff) / float(nyq)
    if cutoff.ndim > 1:
        raise ValueError('The cutoff argument must be at most one-dimensional.')
    if cutoff.size == 0:
        raise ValueError('At least one cutoff frequency must be given.')
    if cutoff.min() <= 0 or cutoff.max() >= 1:
        raise ValueError('Invalid cutoff frequency: frequencies must be greater than 0 and less than nyq.')
    if np.any(np.diff(cutoff) <= 0):
        raise ValueError('Invalid cutoff frequencies: the frequencies must be strictly increasing.')
    if width is not None:
        atten = kaiser_atten(numtaps, float(width) / nyq)
        beta = kaiser_beta(atten)
        window = ('kaiser', beta)
    pass_nyquist = bool(cutoff.size & 1) ^ pass_zero
    if pass_nyquist and numtaps % 2 == 0:
        raise ValueError('A filter with an even number of coefficients must have zero response at the Nyquist rate.')
    cutoff = np.hstack(([0.0] * pass_zero, cutoff, [1.0] * pass_nyquist))
    bands = cutoff.reshape(-1, 2)
    alpha = 0.5 * (numtaps - 1)
    m = np.arange(0, numtaps) - alpha
    h = 0
    for left, right in bands:
        h += right * sinc(right * m)
        h -= left * sinc(left * m)

    from .signaltools import get_window
    win = get_window(window, numtaps, fftbins=False)
    h *= win
    if scale:
        left, right = bands[0]
        if left == 0:
            scale_frequency = 0.0
        elif right == 1:
            scale_frequency = 1.0
        else:
            scale_frequency = 0.5 * (left + right)
        c = np.cos(np.pi * m * scale_frequency)
        s = np.sum(h * c)
        h /= s
    return h


def firwin2(numtaps, freq, gain, nfreqs=None, window='hamming', nyq=1.0, antisymmetric=False):
    """
    FIR filter design using the window method.

    From the given frequencies `freq` and corresponding gains `gain`,
    this function constructs an FIR filter with linear phase and
    (approximately) the given frequency response.

    Parameters
    ----------
    numtaps : int
        The number of taps in the FIR filter.  `numtaps` must be less than
        `nfreqs`.
    freq : array_like, 1D
        The frequency sampling points. Typically 0.0 to 1.0 with 1.0 being
        Nyquist.  The Nyquist frequency can be redefined with the argument
        `nyq`.
        The values in `freq` must be nondecreasing.  A value can be repeated
        once to implement a discontinuity.  The first value in `freq` must
        be 0, and the last value must be `nyq`.
    gain : array_like
        The filter gains at the frequency sampling points. Certain
        constraints to gain values, depending on the filter type, are applied,
        see Notes for details.
    nfreqs : int, optional
        The size of the interpolation mesh used to construct the filter.
        For most efficient behavior, this should be a power of 2 plus 1
        (e.g, 129, 257, etc).  The default is one more than the smallest
        power of 2 that is not less than `numtaps`.  `nfreqs` must be greater
        than `numtaps`.
    window : string or (string, float) or float, or None, optional
        Window function to use. Default is "hamming".  See
        `scipy.signal.get_window` for the complete list of possible values.
        If None, no window function is applied.
    nyq : float
        Nyquist frequency.  Each frequency in `freq` must be between 0 and
        `nyq` (inclusive).
    antisymmetric : bool
        Flag setting wither resulting impulse responce is
        symmetric/antisymmetric.
        See Notes for more details.

    Returns
    -------
    taps : ndarray
        The filter coefficients of the FIR filter, as a 1-D array of length
        `numtaps`.

    See also
    --------
    scipy.signal.firwin

    Notes
    -----
    From the given set of frequencies and gains, the desired response is
    constructed in the frequency domain.  The inverse FFT is applied to the
    desired response to create the associated convolution kernel, and the
    first `numtaps` coefficients of this kernel, scaled by `window`, are
    returned.

    The FIR filter will have linear phase. The type of filter is determined by
    the value of 'numtaps` and `antisymmetric` flag.
    There are four possible combinations:

       - odd  `numtaps`, `antisymmetric` is False, type I filter is produced
       - even `numtaps`, `antisymmetric` is False, type II filter is produced
       - odd  `numtaps`, `antisymmetric` is True, type III filter is produced
       - even `numtaps`, `antisymmetric` is True, type IV filter is produced

    Magnitude response of all but type I filters are subjects to following
    constraints:

       - type II  -- zero at the Nyquist frequency
       - type III -- zero at zero and Nyquist frequencies
       - type IV  -- zero at zero frequency

    .. versionadded:: 0.9.0

    References
    ----------
    .. [1] Oppenheim, A. V. and Schafer, R. W., "Discrete-Time Signal
       Processing", Prentice-Hall, Englewood Cliffs, New Jersey (1989).
       (See, for example, Section 7.4.)

    .. [2] Smith, Steven W., "The Scientist and Engineer's Guide to Digital
       Signal Processing", Ch. 17. http://www.dspguide.com/ch17/1.htm

    Examples
    --------
    A lowpass FIR filter with a response that is 1 on [0.0, 0.5], and
    that decreases linearly on [0.5, 1.0] from 1 to 0:

    >>> from scipy import signal
    >>> taps = signal.firwin2(150, [0.0, 0.5, 1.0], [1.0, 1.0, 0.0])
    >>> print(taps[72:78])
    [-0.02286961 -0.06362756  0.57310236  0.57310236 -0.06362756 -0.02286961]

    """
    if len(freq) != len(gain):
        raise ValueError('freq and gain must be of same length.')
    if nfreqs is not None and numtaps >= nfreqs:
        raise ValueError('ntaps must be less than nfreqs, but firwin2 was called with ntaps=%d and nfreqs=%s' % (
         numtaps, nfreqs))
    if freq[0] != 0 or freq[-1] != nyq:
        raise ValueError('freq must start with 0 and end with `nyq`.')
    d = np.diff(freq)
    if (d < 0).any():
        raise ValueError('The values in freq must be nondecreasing.')
    d2 = d[:-1] + d[1:]
    if (d2 == 0).any():
        raise ValueError('A value in freq must not occur more than twice.')
    if antisymmetric:
        if numtaps % 2 == 0:
            ftype = 4
        else:
            ftype = 3
    else:
        if numtaps % 2 == 0:
            ftype = 2
        else:
            ftype = 1
        if ftype == 2 and gain[-1] != 0.0:
            raise ValueError('A Type II filter must have zero gain at the Nyquist rate.')
        elif ftype == 3 and (gain[0] != 0.0 or gain[-1] != 0.0):
            raise ValueError('A Type III filter must have zero gain at zero and Nyquist rates.')
        elif ftype == 4 and gain[0] != 0.0:
            raise ValueError('A Type IV filter must have zero gain at zero rate.')
        if nfreqs is None:
            nfreqs = 1 + 2 ** int(ceil(log(numtaps, 2)))
        eps = np.finfo(float).eps
        for k in range(len(freq)):
            if k < len(freq) - 1 and freq[k] == freq[k + 1]:
                freq[k] = freq[k] - eps
                freq[k + 1] = freq[k + 1] + eps

    x = np.linspace(0.0, nyq, nfreqs)
    fx = np.interp(x, freq, gain)
    shift = np.exp(-(numtaps - 1) / 2.0 * complex(0.0, 1.0) * np.pi * x / nyq)
    if ftype > 2:
        shift *= complex(0.0, 1.0)
    fx2 = fx * shift
    out_full = irfft(fx2)
    if window is not None:
        from .signaltools import get_window
        wind = get_window(window, numtaps, fftbins=False)
    else:
        wind = 1
    out = out_full[:numtaps] * wind
    if ftype == 3:
        out[out.size // 2] = 0.0
    return out


def remez(numtaps, bands, desired, weight=None, Hz=1, type='bandpass', maxiter=25, grid_density=16):
    """
    Calculate the minimax optimal filter using the Remez exchange algorithm.

    Calculate the filter-coefficients for the finite impulse response
    (FIR) filter whose transfer function minimizes the maximum error
    between the desired gain and the realized gain in the specified
    frequency bands using the Remez exchange algorithm.

    Parameters
    ----------
    numtaps : int
        The desired number of taps in the filter. The number of taps is
        the number of terms in the filter, or the filter order plus one.
    bands : array_like
        A monotonic sequence containing the band edges in Hz.
        All elements must be non-negative and less than half the sampling
        frequency as given by `Hz`.
    desired : array_like
        A sequence half the size of bands containing the desired gain
        in each of the specified bands.
    weight : array_like, optional
        A relative weighting to give to each band region. The length of
        `weight` has to be half the length of `bands`.
    Hz : scalar, optional
        The sampling frequency in Hz. Default is 1.
    type : {'bandpass', 'differentiator', 'hilbert'}, optional
        The type of filter:

          'bandpass' : flat response in bands. This is the default.

          'differentiator' : frequency proportional response in bands.

          'hilbert' : filter with odd symmetry, that is, type III
                      (for even order) or type IV (for odd order)
                      linear phase filters.

    maxiter : int, optional
        Maximum number of iterations of the algorithm. Default is 25.
    grid_density : int, optional
        Grid density. The dense grid used in `remez` is of size
        ``(numtaps + 1) * grid_density``. Default is 16.

    Returns
    -------
    out : ndarray
        A rank-1 array containing the coefficients of the optimal
        (in a minimax sense) filter.

    See Also
    --------
    freqz : Compute the frequency response of a digital filter.

    References
    ----------
    .. [1] J. H. McClellan and T. W. Parks, "A unified approach to the
           design of optimum FIR linear phase digital filters",
           IEEE Trans. Circuit Theory, vol. CT-20, pp. 697-701, 1973.
    .. [2] J. H. McClellan, T. W. Parks and L. R. Rabiner, "A Computer
           Program for Designing Optimum FIR Linear Phase Digital
           Filters", IEEE Trans. Audio Electroacoust., vol. AU-21,
           pp. 506-525, 1973.

    Examples
    --------
    We want to construct a filter with a passband at 0.2-0.4 Hz, and
    stop bands at 0-0.1 Hz and 0.45-0.5 Hz. Note that this means that the
    behavior in the frequency ranges between those bands is unspecified and
    may overshoot.

    >>> from scipy import signal
    >>> bpass = signal.remez(72, [0, 0.1, 0.2, 0.4, 0.45, 0.5], [0, 1, 0])
    >>> freq, response = signal.freqz(bpass)
    >>> ampl = np.abs(response)

    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax1 = fig.add_subplot(111)
    >>> ax1.semilogy(freq/(2*np.pi), ampl, 'b-')  # freq in Hz
    >>> plt.show()

    """
    try:
        tnum = {'bandpass': 1, 'differentiator': 2, 'hilbert': 3}[type]
    except KeyError:
        raise ValueError("Type must be 'bandpass', 'differentiator', or 'hilbert'")

    if weight is None:
        weight = [
         1] * len(desired)
    bands = np.asarray(bands).copy()
    return sigtools._remez(numtaps, bands, desired, weight, tnum, Hz, maxiter, grid_density)