# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\signal\filter_design.pyc
# Compiled at: 2013-02-16 13:27:32
"""Filter design.
"""
from __future__ import division, print_function, absolute_import
import types, warnings, numpy
from numpy import atleast_1d, poly, polyval, roots, real, asarray, allclose, resize, pi, absolute, logspace, r_, sqrt, tan, log10, arctan, arcsinh, cos, exp, cosh, arccosh, ceil, conjugate, zeros, sinh
from numpy import mintypecode
from scipy import special, optimize
from scipy.misc import comb
__all__ = [
 'findfreqs', 'freqs', 'freqz', 'tf2zpk', 'zpk2tf', 'normalize', 
 'lp2lp', 
 'lp2hp', 'lp2bp', 'lp2bs', 'bilinear', 'iirdesign', 
 'iirfilter', 'butter', 
 'cheby1', 'cheby2', 'ellip', 'bessel', 
 'band_stop_obj', 'buttord', 'cheb1ord', 
 'cheb2ord', 'ellipord', 
 'buttap', 'cheb1ap', 'cheb2ap', 'ellipap', 'besselap', 
 'filter_dict', 
 'band_dict', 'BadCoefficients']

class BadCoefficients(UserWarning):
    pass


abs = absolute

def findfreqs(num, den, N):
    ep = atleast_1d(roots(den)) + complex(0.0, 0.0)
    tz = atleast_1d(roots(num)) + complex(0.0, 0.0)
    if len(ep) == 0:
        ep = atleast_1d(-1000) + complex(0.0, 0.0)
    ez = r_[('-1',
     numpy.compress(ep.imag >= 0, ep, axis=-1),
     numpy.compress((abs(tz) < 100000.0) & (tz.imag >= 0), tz, axis=-1))]
    integ = abs(ez) < 1e-10
    hfreq = numpy.around(numpy.log10(numpy.max(3 * abs(ez.real + integ) + 1.5 * ez.imag)) + 0.5)
    lfreq = numpy.around(numpy.log10(0.1 * numpy.min(abs(real(ez + integ)) + 2 * ez.imag)) - 0.5)
    w = logspace(lfreq, hfreq, N)
    return w


def freqs(b, a, worN=None, plot=None):
    """
    Compute frequency response of analog filter.

    Given the numerator `b` and denominator `a` of a filter, compute its
    frequency response::

             b[0]*(jw)**(nb-1) + b[1]*(jw)**(nb-2) + ... + b[nb-1]
     H(w) = -------------------------------------------------------
             a[0]*(jw)**(na-1) + a[1]*(jw)**(na-2) + ... + a[na-1]

    Parameters
    ----------
    b : ndarray
        Numerator of a linear filter.
    a : ndarray
        Denominator of a linear filter.
    worN : {None, int}, optional
        If None, then compute at 200 frequencies around the interesting parts
        of the response curve (determined by pole-zero locations).  If a single
        integer, then compute at that many frequencies.  Otherwise, compute the
        response at frequencies given in `worN`.
    plot : callable
        A callable that takes two arguments. If given, the return parameters
        `w` and `h` are passed to plot. Useful for plotting the frequency
        response inside `freqs`.

    Returns
    -------
    w : ndarray
        The frequencies at which h was computed.
    h : ndarray
        The frequency response.

    See Also
    --------
    freqz : Compute the frequency response of a digital filter.

    Notes
    -----
    Using Matplotlib's "plot" function as the callable for `plot` produces
    unexpected results,  this plots the real part of the complex transfer
    function, not the magnitude.

    Examples
    --------
    >>> from scipy.signal import freqs, iirfilter

    >>> b, a = iirfilter(4, [1, 10], 1, 60, analog=True, ftype='cheby1')

    >>> w, h = freqs(b, a, worN=np.logspace(-1, 2, 1000))

    >>> import matplotlib.pyplot as plt
    >>> plt.semilogx(w, abs(h))
    >>> plt.xlabel('Frequency')
    >>> plt.ylabel('Amplitude response')
    >>> plt.grid()
    >>> plt.show()

    """
    if worN is None:
        w = findfreqs(b, a, 200)
    elif isinstance(worN, int):
        N = worN
        w = findfreqs(b, a, N)
    else:
        w = worN
    w = atleast_1d(w)
    s = complex(0.0, 1.0) * w
    h = polyval(b, s) / polyval(a, s)
    if plot is not None:
        plot(w, h)
    return (
     w, h)


def freqz(b, a=1, worN=None, whole=0, plot=None):
    """
    Compute the frequency response of a digital filter.

    Given the numerator `b` and denominator `a` of a digital filter,
    compute its frequency response::

               jw               -jw            -jmw
        jw  B(e)    b[0] + b[1]e + .... + b[m]e
     H(e) = ---- = ------------------------------------
               jw               -jw            -jnw
            A(e)    a[0] + a[1]e + .... + a[n]e

    Parameters
    ----------
    b : ndarray
        numerator of a linear filter
    a : ndarray
        denominator of a linear filter
    worN : {None, int}, optional
        If None, then compute at 512 frequencies around the unit circle.
        If a single integer, then compute at that many frequencies.
        Otherwise, compute the response at frequencies given in worN
    whole : bool, optional
        Normally, frequencies are computed from 0 to pi (upper-half of
        unit-circle).  If `whole` is True, compute frequencies from 0 to 2*pi.
    plot : callable
        A callable that takes two arguments. If given, the return parameters
        `w` and `h` are passed to plot. Useful for plotting the frequency
        response inside `freqz`.

    Returns
    -------
    w : ndarray
        The frequencies at which h was computed.
    h : ndarray
        The frequency response.

    Notes
    -----
    Using Matplotlib's "plot" function as the callable for `plot` produces
    unexpected results,  this plots the real part of the complex transfer
    function, not the magnitude.

    Examples
    --------
    >>> from scipy import signal
    >>> b = signal.firwin(80, 0.5, window=('kaiser', 8))
    >>> w, h = signal.freqz(b)

    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> plt.title('Digital filter frequency response')
    >>> ax1 = fig.add_subplot(111)

    >>> plt.semilogy(w, np.abs(h), 'b')
    >>> plt.ylabel('Amplitude (dB)', color='b')
    >>> plt.xlabel('Frequency (rad/sample)')

    >>> ax2 = ax1.twinx()
    >>> angles = np.unwrap(np.angle(h))
    >>> plt.plot(w, angles, 'g')
    >>> plt.ylabel('Angle (radians)', color='g')
    >>> plt.grid()
    >>> plt.axis('tight')
    >>> plt.show()

    """
    b, a = map(atleast_1d, (b, a))
    if whole:
        lastpoint = 2 * pi
    else:
        lastpoint = pi
    if worN is None:
        N = 512
        w = numpy.linspace(0, lastpoint, N, endpoint=False)
    elif isinstance(worN, int):
        N = worN
        w = numpy.linspace(0, lastpoint, N, endpoint=False)
    else:
        w = worN
    w = atleast_1d(w)
    zm1 = exp(complex(0.0, -1.0) * w)
    h = polyval(b[::-1], zm1) / polyval(a[::-1], zm1)
    if plot is not None:
        plot(w, h)
    return (
     w, h)


def tf2zpk(b, a):
    """Return zero, pole, gain (z,p,k) representation from a numerator,
    denominator representation of a linear filter.

    Parameters
    ----------
    b : ndarray
        Numerator polynomial.
    a : ndarray
        Denominator polynomial.

    Returns
    -------
    z : ndarray
        Zeros of the transfer function.
    p : ndarray
        Poles of the transfer function.
    k : float
        System gain.

    Notes
    -----
    If some values of `b` are too close to 0, they are removed. In that case, 
    a BadCoefficients warning is emitted.
    """
    b, a = normalize(b, a)
    b = (b + 0.0) / a[0]
    a = (a + 0.0) / a[0]
    k = b[0]
    b /= b[0]
    z = roots(b)
    p = roots(a)
    return (z, p, k)


def zpk2tf(z, p, k):
    """Return polynomial transfer function representation from zeros
    and poles

    Parameters
    ----------
    z : ndarray
        Zeros of the transfer function.
    p : ndarray
        Poles of the transfer function.
    k : float
        System gain.

    Returns
    -------
    b : ndarray
        Numerator polynomial.
    a : ndarray
        Denominator polynomial.

    """
    z = atleast_1d(z)
    k = atleast_1d(k)
    if len(z.shape) > 1:
        temp = poly(z[0])
        b = zeros((z.shape[0], z.shape[1] + 1), temp.dtype.char)
        if len(k) == 1:
            k = [
             k[0]] * z.shape[0]
        for i in range(z.shape[0]):
            b[i] = k[i] * poly(z[i])

    else:
        b = k * poly(z)
    a = atleast_1d(poly(p))
    return (b, a)


def normalize(b, a):
    """Normalize polynomial representation of a transfer function.

    If values of `b` are too close to 0, they are removed. In that case, a
    BadCoefficients warning is emitted.
    """
    b, a = map(atleast_1d, (b, a))
    if len(a.shape) != 1:
        raise ValueError('Denominator polynomial must be rank-1 array.')
    if len(b.shape) > 2:
        raise ValueError('Numerator polynomial must be rank-1 or rank-2 array.')
    if len(b.shape) == 1:
        b = asarray([b], b.dtype.char)
    while a[0] == 0.0 and len(a) > 1:
        a = a[1:]

    outb = b * 1.0 / a[0]
    outa = a * 1.0 / a[0]
    if allclose(0, outb[:, 0], atol=1e-14):
        warnings.warn('Badly conditioned filter coefficients (numerator): the results may be meaningless', BadCoefficients)
        while allclose(0, outb[:, 0], atol=1e-14) and outb.shape[-1] > 1:
            outb = outb[:, 1:]

    if outb.shape[0] == 1:
        outb = outb[0]
    return (
     outb, outa)


def lp2lp(b, a, wo=1.0):
    """Return a low-pass filter with cutoff frequency `wo`
    from a low-pass filter prototype with unity cutoff frequency.
    """
    a, b = map(atleast_1d, (a, b))
    try:
        wo = float(wo)
    except TypeError:
        wo = float(wo[0])

    d = len(a)
    n = len(b)
    M = max((d, n))
    pwo = pow(wo, numpy.arange(M - 1, -1, -1))
    start1 = max((n - d, 0))
    start2 = max((d - n, 0))
    b = b * pwo[start1] / pwo[start2:]
    a = a * pwo[start1] / pwo[start1:]
    return normalize(b, a)


def lp2hp(b, a, wo=1.0):
    """Return a high-pass filter with cutoff frequency `wo`
    from a low-pass filter prototype with unity cutoff frequency.
    """
    a, b = map(atleast_1d, (a, b))
    try:
        wo = float(wo)
    except TypeError:
        wo = float(wo[0])

    d = len(a)
    n = len(b)
    if wo != 1:
        pwo = pow(wo, numpy.arange(max((d, n))))
    else:
        pwo = numpy.ones(max((d, n)), b.dtype.char)
    if d >= n:
        outa = a[::-1] * pwo
        outb = resize(b, (d,))
        outb[n:] = 0.0
        outb[:n] = b[::-1] * pwo[:n]
    else:
        outb = b[::-1] * pwo
        outa = resize(a, (n,))
        outa[d:] = 0.0
        outa[:d] = a[::-1] * pwo[:d]
    return normalize(outb, outa)


def lp2bp(b, a, wo=1.0, bw=1.0):
    """Return a band-pass filter with center frequency `wo` and bandwidth `bw`
    from a low-pass filter prototype with unity cutoff frequency.
    """
    a, b = map(atleast_1d, (a, b))
    D = len(a) - 1
    N = len(b) - 1
    artype = mintypecode((a, b))
    ma = max([N, D])
    Np = N + ma
    Dp = D + ma
    bprime = numpy.zeros(Np + 1, artype)
    aprime = numpy.zeros(Dp + 1, artype)
    wosq = wo * wo
    for j in range(Np + 1):
        val = 0.0
        for i in range(0, N + 1):
            for k in range(0, i + 1):
                if ma - i + 2 * k == j:
                    val += comb(i, k) * b[N - i] * wosq ** (i - k) / bw ** i

        bprime[Np - j] = val

    for j in range(Dp + 1):
        val = 0.0
        for i in range(0, D + 1):
            for k in range(0, i + 1):
                if ma - i + 2 * k == j:
                    val += comb(i, k) * a[D - i] * wosq ** (i - k) / bw ** i

        aprime[Dp - j] = val

    return normalize(bprime, aprime)


def lp2bs(b, a, wo=1, bw=1):
    """Return a band-stop filter with center frequency `wo` and bandwidth `bw`
    from a low-pass filter prototype with unity cutoff frequency.
    """
    a, b = map(atleast_1d, (a, b))
    D = len(a) - 1
    N = len(b) - 1
    artype = mintypecode((a, b))
    M = max([N, D])
    Np = M + M
    Dp = M + M
    bprime = numpy.zeros(Np + 1, artype)
    aprime = numpy.zeros(Dp + 1, artype)
    wosq = wo * wo
    for j in range(Np + 1):
        val = 0.0
        for i in range(0, N + 1):
            for k in range(0, M - i + 1):
                if i + 2 * k == j:
                    val += comb(M - i, k) * b[N - i] * wosq ** (M - i - k) * bw ** i

        bprime[Np - j] = val

    for j in range(Dp + 1):
        val = 0.0
        for i in range(0, D + 1):
            for k in range(0, M - i + 1):
                if i + 2 * k == j:
                    val += comb(M - i, k) * a[D - i] * wosq ** (M - i - k) * bw ** i

        aprime[Dp - j] = val

    return normalize(bprime, aprime)


def bilinear(b, a, fs=1.0):
    """Return a digital filter from an analog one using a bilinear transform.

    The bilinear transform substitutes ``(z-1) / (z+1)`` for ``s``.
    """
    fs = float(fs)
    a, b = map(atleast_1d, (a, b))
    D = len(a) - 1
    N = len(b) - 1
    artype = float
    M = max([N, D])
    Np = M
    Dp = M
    bprime = numpy.zeros(Np + 1, artype)
    aprime = numpy.zeros(Dp + 1, artype)
    for j in range(Np + 1):
        val = 0.0
        for i in range(N + 1):
            for k in range(i + 1):
                for l in range(M - i + 1):
                    if k + l == j:
                        val += comb(i, k) * comb(M - i, l) * b[N - i] * pow(2 * fs, i) * (-1) ** k

        bprime[j] = real(val)

    for j in range(Dp + 1):
        val = 0.0
        for i in range(D + 1):
            for k in range(i + 1):
                for l in range(M - i + 1):
                    if k + l == j:
                        val += comb(i, k) * comb(M - i, l) * a[D - i] * pow(2 * fs, i) * (-1) ** k

        aprime[j] = real(val)

    return normalize(bprime, aprime)


def iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba'):
    """Complete IIR digital and analog filter design.

    Given passband and stopband frequencies and gains, construct an analog or
    digital IIR filter of minimum order for a given basic type.  Return the
    output in numerator, denominator ('ba') or pole-zero ('zpk') form.

    Parameters
    ----------
    wp, ws : float
        Passband and stopband edge frequencies.  
        For digital filters, these are normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`wp` and `ws` are thus in 
        half-cycles / sample.)  For example:

            - Lowpass:   wp = 0.2,          ws = 0.3
            - Highpass:  wp = 0.3,          ws = 0.2
            - Bandpass:  wp = [0.2, 0.5],   ws = [0.1, 0.6]
            - Bandstop:  wp = [0.1, 0.6],   ws = [0.2, 0.5]
            
        For analog filters, `wp` and `ws` are in radians / second.

    gpass : float
        The maximum loss in the passband (dB).
    gstop : float
        The minimum attenuation in the stopband (dB).
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    ftype : str, optional
        The type of IIR filter to design:

            - elliptic    : 'ellip'
            - Butterworth : 'butter',
            - Chebyshev I : 'cheby1',
            - Chebyshev II: 'cheby2',
            - Bessel :      'bessel'

    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter. 
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer 
        function.  Only returned if ``output='zpk'``.

    """
    try:
        ordfunc = filter_dict[ftype][1]
    except KeyError:
        raise ValueError('Invalid IIR filter type: %s' % ftype)
    except IndexError:
        raise ValueError('%s does not have order selection use iirfilter function.' % ftype)

    wp = atleast_1d(wp)
    ws = atleast_1d(ws)
    band_type = 2 * (len(wp) - 1)
    band_type += 1
    if wp[0] >= ws[0]:
        band_type += 1
    btype = {1: 'lowpass', 2: 'highpass', 3: 'bandstop', 
       4: 'bandpass'}[band_type]
    N, Wn = ordfunc(wp, ws, gpass, gstop, analog=analog)
    return iirfilter(N, Wn, rp=gpass, rs=gstop, analog=analog, btype=btype, ftype=ftype, output=output)


def iirfilter(N, Wn, rp=None, rs=None, btype='band', analog=False, ftype='butter', output='ba'):
    """
    IIR digital and analog filter design given order and critical points.

    Design an Nth order digital or analog filter and return the filter
    coefficients in (B,A) (numerator, denominator) or (Z,P,K) form.

    Parameters
    ----------
    N : int
        The order of the filter.
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    rp : float, optional
        For Chebyshev and elliptic filters, provides the maximum ripple
        in the passband. (dB)
    rs : float, optional
        For Chebyshev and elliptic filters, provides the minimum attenuation
        in the stop band. (dB)
    btype : {'bandpass', 'lowpass', 'highpass', 'bandstop'}, optional
        The type of filter.  Default is 'bandpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    ftype : str, optional
        The type of IIR filter to design:

            - elliptic    : 'ellip'
            - Butterworth : 'butter'
            - Chebyshev I : 'cheby1'
            - Chebyshev II: 'cheby2'
            - Bessel :      'bessel'

    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    See Also
    --------
    buttord, cheb1ord, cheb2ord, ellipord

    """
    ftype, btype, output = [ x.lower() for x in (ftype, btype, output) ]
    Wn = asarray(Wn)
    try:
        btype = band_dict[btype]
    except KeyError:
        raise ValueError('%s is an invalid bandtype for filter.' % btype)

    try:
        typefunc = filter_dict[ftype][0]
    except KeyError:
        raise ValueError('%s is not a valid basic iir filter.' % ftype)

    if output not in ('ba', 'zpk'):
        raise ValueError('%s is not a valid output form.' % output)
    if not analog:
        fs = 2.0
        warped = 2 * fs * tan(pi * Wn / fs)
    else:
        warped = Wn
    if btype in ('lowpass', 'highpass'):
        wo = warped
    else:
        bw = warped[1] - warped[0]
        wo = sqrt(warped[0] * warped[1])
    if typefunc in [buttap, besselap]:
        z, p, k = typefunc(N)
    elif typefunc == cheb1ap:
        if rp is None:
            raise ValueError('passband ripple (rp) must be provided to design a Chebyshev I filter.')
        z, p, k = typefunc(N, rp)
    elif typefunc == cheb2ap:
        if rs is None:
            raise ValueError('stopband atteunatuion (rs) must be provided to design an Chebyshev II filter.')
        z, p, k = typefunc(N, rs)
    else:
        if rs is None or rp is None:
            raise ValueError('Both rp and rs must be provided to design an elliptic filter.')
        z, p, k = typefunc(N, rp, rs)
    b, a = zpk2tf(z, p, k)
    if btype == 'lowpass':
        b, a = lp2lp(b, a, wo=wo)
    elif btype == 'highpass':
        b, a = lp2hp(b, a, wo=wo)
    elif btype == 'bandpass':
        b, a = lp2bp(b, a, wo=wo, bw=bw)
    else:
        b, a = lp2bs(b, a, wo=wo, bw=bw)
    if not analog:
        b, a = bilinear(b, a, fs=fs)
    if output == 'zpk':
        return tf2zpk(b, a)
    else:
        return (
         b, a)
        return


def butter(N, Wn, btype='low', analog=False, output='ba'):
    """
    Butterworth digital and analog filter design.

    Design an Nth order digital or analog Butterworth filter and return
    the filter coefficients in (B,A) or (Z,P,K) form.

    Parameters
    ----------
    N : int
        The order of the filter.
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    btype : {'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter.  Default is 'lowpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter.
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer
        function.  Only returned if ``output='zpk'``.

    See also
    --------
    buttord

    """
    return iirfilter(N, Wn, btype=btype, analog=analog, output=output, ftype='butter')


def cheby1(N, rp, Wn, btype='low', analog=False, output='ba'):
    """
    Chebyshev type I digital and analog filter design.

    Design an Nth order digital or analog Chebyshev type I filter and
    return the filter coefficients in (B,A) or (Z,P,K) form.

    Parameters
    ----------
    N : int
        The order of the filter.
    rp : float
        Provides the maximum ripple in the passband. (dB)
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    btype : {'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter.  Default is 'lowpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter.
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer
        function.  Only returned if ``output='zpk'``.

    See also
    --------
    cheb1ord

    """
    return iirfilter(N, Wn, rp=rp, btype=btype, analog=analog, output=output, ftype='cheby1')


def cheby2(N, rs, Wn, btype='low', analog=False, output='ba'):
    """
    Chebyshev type II digital and analog filter design.

    Design an Nth order digital or analog Chebyshev type II filter and
    return the filter coefficients in (B,A) or (Z,P,K) form.

    Parameters
    ----------
    N : int
        The order of the filter.
    rs : float
        Provides the minimum attenuation in the stop band. (dB)
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    btype : {'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter.  Default is 'lowpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter.
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer
        function.  Only returned if ``output='zpk'``.

    See also
    --------
    cheb2ord

    """
    return iirfilter(N, Wn, rs=rs, btype=btype, analog=analog, output=output, ftype='cheby2')


def ellip(N, rp, rs, Wn, btype='low', analog=False, output='ba'):
    """
    Elliptic (Cauer) digital and analog filter design.

    Design an Nth order digital or analog elliptic filter and return
    the filter coefficients in (B,A) or (Z,P,K) form.

    Parameters
    ----------
    N : int
        The order of the filter.
    rp : float
        Provides the maximum ripple in the passband. (dB)
    rs : float
        Provides the minimum attenuation in the stop band. (dB)
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    btype : {'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter.  Default is 'lowpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.

    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter.
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer
        function.  Only returned if ``output='zpk'``.

    See also
    --------
    ellipord

    """
    return iirfilter(N, Wn, rs=rs, rp=rp, btype=btype, analog=analog, output=output, ftype='elliptic')


def bessel(N, Wn, btype='low', analog=False, output='ba'):
    """Bessel digital and analog filter design.

    Design an Nth order digital or analog Bessel filter and return the
    filter coefficients in (B,A) or (Z,P,K) form.
    
    Parameters
    ----------
    N : int
        The order of the filter.
    Wn : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For digital filters, `Wn` is normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`Wn` is thus in 
        half-cycles / sample.)
        For analog filters, `Wn` is in radians / second.
    btype : {'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter.  Default is 'lowpass'.
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.
    output : {'ba', 'zpk'}, optional
        Type of output:  numerator/denominator ('ba') or pole-zero ('zpk').
        Default is 'ba'.
    
    Returns
    -------
    b, a : ndarray, ndarray
        Numerator (`b`) and denominator (`a`) polynomials of the IIR filter. 
        Only returned if ``output='ba'``.
    z, p, k : ndarray, ndarray, float
        Zeros, poles, and system gain of the IIR filter transfer 
        function.  Only returned if ``output='zpk'``.
    
    """
    return iirfilter(N, Wn, btype=btype, analog=analog, output=output, ftype='bessel')


def maxflat():
    pass


def yulewalk():
    pass


def band_stop_obj(wp, ind, passb, stopb, gpass, gstop, type):
    """
    Band Stop Objective Function for order minimization.

    Returns the non-integer order for an analog band stop filter.

    Parameters
    ----------
    wp : float
        Edge of passband `passb`.
    ind : int, {0, 1}
        Index specifying which `passb` edge to vary (0 or 1).
    passb : ndarray
        Two element sequence of fixed passband edges.
    stopb : ndarray
        Two element sequence of fixed stopband edges.
    gstop : float
        Amount of attenuation in stopband in dB.
    gpass : float
        Amount of ripple in the passband in dB.
    type : {'butter', 'cheby', 'ellip'}
        Type of filter.

    Returns
    -------
    n : scalar
        Filter order (possibly non-integer).

    """
    passbC = passb.copy()
    passbC[ind] = wp
    nat = stopb * (passbC[0] - passbC[1]) / (stopb ** 2 - passbC[0] * passbC[1])
    nat = min(abs(nat))
    if type == 'butter':
        GSTOP = 10 ** (0.1 * abs(gstop))
        GPASS = 10 ** (0.1 * abs(gpass))
        n = log10((GSTOP - 1.0) / (GPASS - 1.0)) / (2 * log10(nat))
    elif type == 'cheby':
        GSTOP = 10 ** (0.1 * abs(gstop))
        GPASS = 10 ** (0.1 * abs(gpass))
        n = arccosh(sqrt((GSTOP - 1.0) / (GPASS - 1.0))) / arccosh(nat)
    elif type == 'ellip':
        GSTOP = 10 ** (0.1 * gstop)
        GPASS = 10 ** (0.1 * gpass)
        arg1 = sqrt((GPASS - 1.0) / (GSTOP - 1.0))
        arg0 = 1.0 / nat
        d0 = special.ellipk([arg0 ** 2, 1 - arg0 ** 2])
        d1 = special.ellipk([arg1 ** 2, 1 - arg1 ** 2])
        n = d0[0] * d1[1] / (d0[1] * d1[0])
    else:
        raise ValueError('Incorrect type: %s' % type)
    return n


def buttord(wp, ws, gpass, gstop, analog=False):
    """Butterworth filter order selection.

    Return the order of the lowest order digital or analog Butterworth filter 
    that loses no more than `gpass` dB in the passband and has at least 
    `gstop` dB attenuation in the stopband.

    Parameters
    ----------
    wp, ws : float
        Passband and stopband edge frequencies.  
        For digital filters, these are normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`wp` and `ws` are thus in 
        half-cycles / sample.)  For example:

            - Lowpass:   wp = 0.2,          ws = 0.3
            - Highpass:  wp = 0.3,          ws = 0.2
            - Bandpass:  wp = [0.2, 0.5],   ws = [0.1, 0.6]
            - Bandstop:  wp = [0.1, 0.6],   ws = [0.2, 0.5]
            
        For analog filters, `wp` and `ws` are in radians / second.

    gpass : float
        The maximum loss in the passband (dB).
    gstop : float
        The minimum attenuation in the stopband (dB).
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.

    Returns
    -------
    ord : int
        The lowest order for a Butterworth filter which meets specs.
    wn : ndarray or float
        The Butterworth natural frequency (i.e. the "3dB frequency").  Should
        be used with `butter` to give filter results.

    """
    wp = atleast_1d(wp)
    ws = atleast_1d(ws)
    filter_type = 2 * (len(wp) - 1)
    filter_type += 1
    if wp[0] >= ws[0]:
        filter_type += 1
    if not analog:
        passb = tan(wp * pi / 2.0)
        stopb = tan(ws * pi / 2.0)
    else:
        passb = wp * 1.0
        stopb = ws * 1.0
    if filter_type == 1:
        nat = stopb / passb
    else:
        if filter_type == 2:
            nat = passb / stopb
        else:
            if filter_type == 3:
                wp0 = optimize.fminbound(band_stop_obj, passb[0], stopb[0] - 1e-12, args=(
                 0, passb, stopb, gpass, gstop,
                 'butter'), disp=0)
                passb[0] = wp0
                wp1 = optimize.fminbound(band_stop_obj, stopb[1] + 1e-12, passb[1], args=(
                 1, passb, stopb, gpass, gstop,
                 'butter'), disp=0)
                passb[1] = wp1
                nat = stopb * (passb[0] - passb[1]) / (stopb ** 2 - passb[0] * passb[1])
            elif filter_type == 4:
                nat = (stopb ** 2 - passb[0] * passb[1]) / (stopb * (passb[0] - passb[1]))
        nat = min(abs(nat))
        GSTOP = 10 ** (0.1 * abs(gstop))
        GPASS = 10 ** (0.1 * abs(gpass))
        ord = int(ceil(log10((GSTOP - 1.0) / (GPASS - 1.0)) / (2 * log10(nat))))
        try:
            W0 = nat / (10 ** (0.1 * abs(gstop)) - 1) ** (1.0 / (2.0 * ord))
        except ZeroDivisionError:
            W0 = nat
            print('Warning, order is zero...check input parametegstop.')

    if filter_type == 1:
        WN = W0 * passb
    elif filter_type == 2:
        WN = passb / W0
    elif filter_type == 3:
        WN = numpy.zeros(2, float)
        discr = sqrt((passb[1] - passb[0]) ** 2 + 4 * W0 ** 2 * passb[0] * passb[1])
        WN[0] = (passb[1] - passb[0] + discr) / (2 * W0)
        WN[1] = (passb[1] - passb[0] - discr) / (2 * W0)
        WN = numpy.sort(abs(WN))
    elif filter_type == 4:
        W0 = numpy.array([-W0, W0], float)
        WN = -W0 * (passb[1] - passb[0]) / 2.0 + sqrt(W0 ** 2 / 4.0 * (passb[1] - passb[0]) ** 2 + passb[0] * passb[1])
        WN = numpy.sort(abs(WN))
    else:
        raise ValueError('Bad type: %s' % filter_type)
    if not analog:
        wn = 2.0 / pi * arctan(WN)
    else:
        wn = WN
    if len(wn) == 1:
        wn = wn[0]
    return (
     ord, wn)


def cheb1ord(wp, ws, gpass, gstop, analog=False):
    """Chebyshev type I filter order selection.

    Return the order of the lowest order digital or analog Chebyshev Type I 
    filter that loses no more than `gpass` dB in the passband and has at 
    least `gstop` dB attenuation in the stopband.

    Parameters
    ----------
    wp, ws : float
        Passband and stopband edge frequencies.  
        For digital filters, these are normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`wp` and `ws` are thus in 
        half-cycles / sample.)  For example:

            - Lowpass:   wp = 0.2,          ws = 0.3
            - Highpass:  wp = 0.3,          ws = 0.2
            - Bandpass:  wp = [0.2, 0.5],   ws = [0.1, 0.6]
            - Bandstop:  wp = [0.1, 0.6],   ws = [0.2, 0.5]
            
        For analog filters, `wp` and `ws` are in radians / second.

    gpass : float
        The maximum loss in the passband (dB).
    gstop : float
        The minimum attenuation in the stopband (dB).
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.

    Returns
    -------
    ord : int
        The lowest order for a Chebyshev type I filter that meets specs.
    wn : ndarray or float
        The Chebyshev natural frequency (the "3dB frequency") for use with
        `cheby1` to give filter results.

    """
    wp = atleast_1d(wp)
    ws = atleast_1d(ws)
    filter_type = 2 * (len(wp) - 1)
    if wp[0] < ws[0]:
        filter_type += 1
    else:
        filter_type += 2
    if not analog:
        passb = tan(pi * wp / 2.0)
        stopb = tan(pi * ws / 2.0)
    else:
        passb = wp * 1.0
        stopb = ws * 1.0
    if filter_type == 1:
        nat = stopb / passb
    elif filter_type == 2:
        nat = passb / stopb
    elif filter_type == 3:
        wp0 = optimize.fminbound(band_stop_obj, passb[0], stopb[0] - 1e-12, args=(
         0, passb, stopb, gpass, gstop, 'cheby'), disp=0)
        passb[0] = wp0
        wp1 = optimize.fminbound(band_stop_obj, stopb[1] + 1e-12, passb[1], args=(
         1, passb, stopb, gpass, gstop, 'cheby'), disp=0)
        passb[1] = wp1
        nat = stopb * (passb[0] - passb[1]) / (stopb ** 2 - passb[0] * passb[1])
    elif filter_type == 4:
        nat = (stopb ** 2 - passb[0] * passb[1]) / (stopb * (passb[0] - passb[1]))
    nat = min(abs(nat))
    GSTOP = 10 ** (0.1 * abs(gstop))
    GPASS = 10 ** (0.1 * abs(gpass))
    ord = int(ceil(arccosh(sqrt((GSTOP - 1.0) / (GPASS - 1.0))) / arccosh(nat)))
    if not analog:
        wn = 2.0 / pi * arctan(passb)
    else:
        wn = passb
    if len(wn) == 1:
        wn = wn[0]
    return (
     ord, wn)


def cheb2ord(wp, ws, gpass, gstop, analog=False):
    """Chebyshev type II filter order selection.

    Return the order of the lowest order digital or analog Chebyshev Type II 
    filter that loses no more than `gpass` dB in the passband and has at least
    `gstop` dB attenuation in the stopband.

    Parameters
    ----------
    wp, ws : float
        Passband and stopband edge frequencies.  
        For digital filters, these are normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`wp` and `ws` are thus in 
        half-cycles / sample.)  For example:

            - Lowpass:   wp = 0.2,          ws = 0.3
            - Highpass:  wp = 0.3,          ws = 0.2
            - Bandpass:  wp = [0.2, 0.5],   ws = [0.1, 0.6]
            - Bandstop:  wp = [0.1, 0.6],   ws = [0.2, 0.5]
            
        For analog filters, `wp` and `ws` are in radians / second.

    gpass : float
        The maximum loss in the passband (dB).
    gstop : float
        The minimum attenuation in the stopband (dB).
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.

    Returns
    -------
    ord : int
        The lowest order for a Chebyshev type II filter that meets specs.
    wn : ndarray or float
        The Chebyshev natural frequency (the "3dB frequency") for use with
        `cheby2` to give filter results.

    """
    wp = atleast_1d(wp)
    ws = atleast_1d(ws)
    filter_type = 2 * (len(wp) - 1)
    if wp[0] < ws[0]:
        filter_type += 1
    else:
        filter_type += 2
    if not analog:
        passb = tan(pi * wp / 2.0)
        stopb = tan(pi * ws / 2.0)
    else:
        passb = wp * 1.0
        stopb = ws * 1.0
    if filter_type == 1:
        nat = stopb / passb
    elif filter_type == 2:
        nat = passb / stopb
    elif filter_type == 3:
        wp0 = optimize.fminbound(band_stop_obj, passb[0], stopb[0] - 1e-12, args=(
         0, passb, stopb, gpass, gstop, 'cheby'), disp=0)
        passb[0] = wp0
        wp1 = optimize.fminbound(band_stop_obj, stopb[1] + 1e-12, passb[1], args=(
         1, passb, stopb, gpass, gstop, 'cheby'), disp=0)
        passb[1] = wp1
        nat = stopb * (passb[0] - passb[1]) / (stopb ** 2 - passb[0] * passb[1])
    elif filter_type == 4:
        nat = (stopb ** 2 - passb[0] * passb[1]) / (stopb * (passb[0] - passb[1]))
    nat = min(abs(nat))
    GSTOP = 10 ** (0.1 * abs(gstop))
    GPASS = 10 ** (0.1 * abs(gpass))
    ord = int(ceil(arccosh(sqrt((GSTOP - 1.0) / (GPASS - 1.0))) / arccosh(nat)))
    new_freq = cosh(1.0 / ord * arccosh(sqrt((GSTOP - 1.0) / (GPASS - 1.0))))
    new_freq = 1.0 / new_freq
    if filter_type == 1:
        nat = passb / new_freq
    elif filter_type == 2:
        nat = passb * new_freq
    elif filter_type == 3:
        nat = numpy.zeros(2, float)
        nat[0] = new_freq / 2.0 * (passb[0] - passb[1]) + sqrt(new_freq ** 2 * (passb[1] - passb[0]) ** 2 / 4.0 + passb[1] * passb[0])
        nat[1] = passb[1] * passb[0] / nat[0]
    elif filter_type == 4:
        nat = numpy.zeros(2, float)
        nat[0] = 1.0 / (2.0 * new_freq) * (passb[0] - passb[1]) + sqrt((passb[1] - passb[0]) ** 2 / (4.0 * new_freq ** 2) + passb[1] * passb[0])
        nat[1] = passb[0] * passb[1] / nat[0]
    if not analog:
        wn = 2.0 / pi * arctan(nat)
    else:
        wn = nat
    if len(wn) == 1:
        wn = wn[0]
    return (
     ord, wn)


def ellipord(wp, ws, gpass, gstop, analog=False):
    """Elliptic (Cauer) filter order selection.

    Return the order of the lowest order digital or analog elliptic filter 
    that loses no more than `gpass` dB in the passband and has at least 
    `gstop` dB attenuation in the stopband.

    Parameters
    ----------
    wp, ws : float
        Passband and stopband edge frequencies.  
        For digital filters, these are normalized from 0 to 1, where 1 is the 
        Nyquist frequency, pi radians / sample.  (`wp` and `ws` are thus in 
        half-cycles / sample.)  For example:

            - Lowpass:   wp = 0.2,          ws = 0.3
            - Highpass:  wp = 0.3,          ws = 0.2
            - Bandpass:  wp = [0.2, 0.5],   ws = [0.1, 0.6]
            - Bandstop:  wp = [0.1, 0.6],   ws = [0.2, 0.5]
            
        For analog filters, `wp` and `ws` are in radians / second.

    gpass : float
        The maximum loss in the passband (dB).
    gstop : float
        The minimum attenuation in the stopband (dB).
    analog : bool, optional
        When True, return an analog filter, otherwise a digital filter is
        returned.

    Returns
    -------
    ord : int
        The lowest order for an Elliptic (Cauer) filter that meets specs.
    wn : ndarray or float
        The Chebyshev natural frequency (the "3dB frequency") for use with
        `ellip` to give filter results.

    """
    wp = atleast_1d(wp)
    ws = atleast_1d(ws)
    filter_type = 2 * (len(wp) - 1)
    filter_type += 1
    if wp[0] >= ws[0]:
        filter_type += 1
    if analog:
        passb = wp * 1.0
        stopb = ws * 1.0
    else:
        passb = tan(wp * pi / 2.0)
        stopb = tan(ws * pi / 2.0)
    if filter_type == 1:
        nat = stopb / passb
    elif filter_type == 2:
        nat = passb / stopb
    elif filter_type == 3:
        wp0 = optimize.fminbound(band_stop_obj, passb[0], stopb[0] - 1e-12, args=(
         0, passb, stopb, gpass, gstop, 'ellip'), disp=0)
        passb[0] = wp0
        wp1 = optimize.fminbound(band_stop_obj, stopb[1] + 1e-12, passb[1], args=(
         1, passb, stopb, gpass, gstop, 'ellip'), disp=0)
        passb[1] = wp1
        nat = stopb * (passb[0] - passb[1]) / (stopb ** 2 - passb[0] * passb[1])
    elif filter_type == 4:
        nat = (stopb ** 2 - passb[0] * passb[1]) / (stopb * (passb[0] - passb[1]))
    nat = min(abs(nat))
    GSTOP = 10 ** (0.1 * gstop)
    GPASS = 10 ** (0.1 * gpass)
    arg1 = sqrt((GPASS - 1.0) / (GSTOP - 1.0))
    arg0 = 1.0 / nat
    d0 = special.ellipk([arg0 ** 2, 1 - arg0 ** 2])
    d1 = special.ellipk([arg1 ** 2, 1 - arg1 ** 2])
    ord = int(ceil(d0[0] * d1[1] / (d0[1] * d1[0])))
    if not analog:
        wn = arctan(passb) * 2.0 / pi
    else:
        wn = passb
    if len(wn) == 1:
        wn = wn[0]
    return (
     ord, wn)


def buttap(N):
    """Return (z,p,k) zero, pole, gain for analog prototype of an Nth
    order Butterworth filter."""
    z = []
    n = numpy.arange(1, N + 1)
    p = numpy.exp(complex(0.0, 1.0) * (2 * n - 1) / (2.0 * N) * pi) * complex(0.0, 1.0)
    k = 1
    return (z, p, k)


def cheb1ap(N, rp):
    """Return (z,p,k) zero, pole, gain for Nth order Chebyshev type I lowpass
    analog filter prototype with `rp` decibels of ripple in the passband.
    """
    z = []
    eps = numpy.sqrt(10 ** (0.1 * rp) - 1.0)
    n = numpy.arange(1, N + 1)
    mu = 1.0 / N * numpy.log((1.0 + numpy.sqrt(1 + eps * eps)) / eps)
    theta = pi / 2.0 * (2 * n - 1.0) / N
    p = -numpy.sinh(mu) * numpy.sin(theta) + complex(0.0, 1.0) * numpy.cosh(mu) * numpy.cos(theta)
    k = numpy.prod(-p, axis=0).real
    if N % 2 == 0:
        k = k / sqrt(1 + eps * eps)
    return (
     z, p, k)


def cheb2ap(N, rs):
    """Return (z,p,k) zero, pole, gain for Nth order Chebyshev type II lowpass
    analog filter prototype with `rs` decibels of ripple in the stopband.
    """
    de = 1.0 / sqrt(10 ** (0.1 * rs) - 1)
    mu = arcsinh(1.0 / de) / N
    if N % 2:
        m = N - 1
        n = numpy.concatenate((numpy.arange(1, N - 1, 2),
         numpy.arange(N + 2, 2 * N, 2)))
    else:
        m = N
        n = numpy.arange(1, 2 * N, 2)
    z = conjugate(complex(0.0, 1.0) / cos(n * pi / (2.0 * N)))
    p = exp(complex(0.0, 1.0) * (pi * numpy.arange(1, 2 * N, 2) / (2.0 * N) + pi / 2.0))
    p = sinh(mu) * p.real + complex(0.0, 1.0) * cosh(mu) * p.imag
    p = 1.0 / p
    k = (numpy.prod(-p, axis=0) / numpy.prod(-z, axis=0)).real
    return (z, p, k)


EPSILON = 2e-16

def _vratio(u, ineps, mp):
    s, c, d, phi = special.ellipj(u, mp)
    ret = abs(ineps - s / c)
    return ret


def _kratio(m, k_ratio):
    m = float(m)
    if m < 0:
        m = 0.0
    if m > 1:
        m = 1.0
    if abs(m) > EPSILON and abs(m) + EPSILON < 1:
        k = special.ellipk([m, 1 - m])
        r = k[0] / k[1] - k_ratio
    elif abs(m) > EPSILON:
        r = -k_ratio
    else:
        r = 1e+20
    return abs(r)


def ellipap(N, rp, rs):
    """Return (z,p,k) zeros, poles, and gain of an Nth order normalized
    prototype elliptic analog lowpass filter with `rp` decibels of ripple in
    the passband and a stopband `rs` decibels down.

    References
    ----------
    Lutova, Tosic, and Evans, "Filter Design for Signal Processing", Chapters 5
    and 12.

    """
    if N == 1:
        p = -sqrt(1.0 / (10 ** (0.1 * rp) - 1.0))
        k = -p
        z = []
        return (
         z, p, k)
    eps = numpy.sqrt(10 ** (0.1 * rp) - 1)
    ck1 = eps / numpy.sqrt(10 ** (0.1 * rs) - 1)
    ck1p = numpy.sqrt(1 - ck1 * ck1)
    if ck1p == 1:
        raise ValueError('Cannot design a filter with given rp and rs specifications.')
    wp = 1
    val = special.ellipk([ck1 * ck1, ck1p * ck1p])
    if abs(1 - ck1p * ck1p) < EPSILON:
        krat = 0
    else:
        krat = N * val[0] / val[1]
    m = optimize.fmin(_kratio, [0.5], args=(krat,), maxfun=250, maxiter=250, disp=0)
    if m < 0 or m > 1:
        m = optimize.fminbound(_kratio, 0, 1, args=(krat,), maxfun=250, maxiter=250, disp=0)
    capk = special.ellipk(m)
    ws = wp / sqrt(m)
    m1 = 1 - m
    j = numpy.arange(1 - N % 2, N, 2)
    jj = len(j)
    s, c, d, phi = special.ellipj(j * capk / N, m * numpy.ones(jj))
    snew = numpy.compress(abs(s) > EPSILON, s, axis=-1)
    z = 1.0 / (sqrt(m) * snew)
    z = complex(0.0, 1.0) * z
    z = numpy.concatenate((z, conjugate(z)))
    r = optimize.fmin(_vratio, special.ellipk(m), args=(1.0 / eps, ck1p * ck1p), maxfun=250, maxiter=250, disp=0)
    v0 = capk * r / (N * val[0])
    sv, cv, dv, phi = special.ellipj(v0, 1 - m)
    p = -(c * d * sv * cv + complex(0.0, 1.0) * s * dv) / (1 - (d * sv) ** 2.0)
    if N % 2:
        newp = numpy.compress(abs(p.imag) > EPSILON * numpy.sqrt(numpy.sum(p * numpy.conjugate(p), axis=0).real), p, axis=-1)
        p = numpy.concatenate((p, conjugate(newp)))
    else:
        p = numpy.concatenate((p, conjugate(p)))
    k = (numpy.prod(-p, axis=0) / numpy.prod(-z, axis=0)).real
    if N % 2 == 0:
        k = k / numpy.sqrt(1 + eps * eps)
    return (z, p, k)


def besselap(N):
    """Return (z,p,k) zero, pole, gain for analog prototype of an Nth order
    Bessel filter."""
    z = []
    k = 1
    if N == 0:
        p = []
    elif N == 1:
        p = [
         -1]
    elif N == 2:
        p = [
         complex(-0.8660254037844386, 0.5),
         complex(-0.8660254037844386, -0.5)]
    elif N == 3:
        p = [
         -0.9416000265332067,
         complex(-0.7456403858480767, -0.7113666249728353),
         complex(-0.7456403858480767, 0.7113666249728353)]
    elif N == 4:
        p = [
         complex(-0.6572111716718829, -0.8301614350048734),
         complex(-0.6572111716718829, 0.8301614350048734),
         complex(-0.904758796788245, -0.27091873300387465),
         complex(-0.904758796788245, 0.27091873300387465)]
    elif N == 5:
        p = [
         -0.9264420773877602, 
         (-0.8515536193688396-0.4427174639443327j), 
         (-0.8515536193688396+0.4427174639443327j), 
         (-0.5905759446119192-0.907206756457455j), 
         (-0.5905759446119192+0.907206756457455j)]
    elif N == 6:
        p = [
         (-0.9093906830472271-0.1856964396793047j), 
         (-0.9093906830472271+0.1856964396793047j), 
         (-0.7996541858328289-0.5621717346937318j), 
         (-0.7996541858328289+0.5621717346937318j), 
         (-0.5385526816693109-0.9616876881954277j), 
         (-0.5385526816693109+0.9616876881954277j)]
    elif N == 7:
        p = [
         -0.919487155649029, 
         (-0.8800029341523374-0.32166527623077396j), 
         (-0.8800029341523374+0.32166527623077396j), 
         (-0.7527355434093215-0.650469630552255j), 
         (-0.7527355434093215+0.650469630552255j), 
         (-0.4966917256672317-1.0025085084544203j), 
         (-0.4966917256672317+1.0025085084544203j)]
    elif N == 8:
        p = [
         (-0.909683154665291-0.1412437976671423j), 
         (-0.909683154665291+0.1412437976671423j), 
         (-0.8473250802359334-0.4259017538272935j), 
         (-0.8473250802359334+0.4259017538272935j), 
         (-0.71113818084854-0.7186517314108402j), 
         (-0.71113818084854+0.7186517314108402j), 
         (-0.4621740412532122-1.034388681126901j), 
         (-0.4621740412532122+1.034388681126901j)]
    elif N == 9:
        p = [
         -0.9154957797499038, 
         (-0.8911217017079759-0.25265809345821644j), 
         (-0.8911217017079759+0.25265809345821644j), 
         (-0.8148021112269013-0.50858156896315j), 
         (-0.8148021112269013+0.50858156896315j), 
         (-0.6743622686854762-0.7730546212691184j), 
         (-0.6743622686854762+0.7730546212691184j), 
         (-0.4331415561553619-1.0600736701359297j), 
         (-0.4331415561553619+1.0600736701359297j)]
    elif N == 10:
        p = [
         (-0.9091347320900502-0.11395831373355111j), 
         (-0.9091347320900502+0.11395831373355111j), 
         (-0.8688459641284765-0.343000823376631j), 
         (-0.8688459641284765+0.343000823376631j), 
         (-0.7837694413101441-0.5759147538499947j), 
         (-0.7837694413101441+0.5759147538499947j), 
         (-0.6417513866988316-0.8175836167191017j), 
         (-0.6417513866988316+0.8175836167191017j), 
         (-0.40832207328688613-1.0812748428191246j), 
         (-0.40832207328688613+1.0812748428191246j)]
    elif N == 11:
        p = [
         -0.9129067244518982, 
         (-0.8963656705721166-0.20804803750710318j), 
         (-0.8963656705721166+0.20804803750710318j), 
         (-0.8453044014712963-0.41786969178012484j), 
         (-0.8453044014712963+0.41786969178012484j), 
         (-0.7546938934722303-0.6319150050721847j), 
         (-0.7546938934722303+0.6319150050721847j), 
         (-0.6126871554915194-0.8547813893314765j), 
         (-0.6126871554915194+0.8547813893314765j), 
         (-0.3868149510055091-1.099117466763121j), 
         (-0.3868149510055091+1.099117466763121j)]
    elif N == 12:
        p = [
         (-0.9084478234140683-0.09550636521345039j), 
         (-0.9084478234140683+0.09550636521345039j), 
         (-0.8802534342016827-0.28717795035242266j), 
         (-0.8802534342016827+0.28717795035242266j), 
         (-0.8217296939939077-0.48102121151006766j), 
         (-0.8217296939939077+0.48102121151006766j), 
         (-0.727668161539516-0.6792961178764694j), 
         (-0.727668161539516+0.6792961178764694j), 
         (-0.5866369321861478-0.8863772751320727j), 
         (-0.5866369321861478+0.8863772751320727j), 
         (-0.3679640085526313-1.1143735756415463j), 
         (-0.3679640085526313+1.1143735756415463j)]
    elif N == 13:
        p = [
         -0.9110914665984183, 
         (-0.8991314665475196-0.17683429561610436j), 
         (-0.8991314665475196+0.17683429561610436j), 
         (-0.8625094198260549-0.3547413731172989j), 
         (-0.8625094198260549+0.3547413731172989j), 
         (-0.7987460692470972-0.5350752120696802j), 
         (-0.7987460692470972+0.5350752120696802j), 
         (-0.7026234675721276-0.7199611890171305j), 
         (-0.7026234675721276+0.7199611890171305j), 
         (-0.5631559842430199-0.9135900338325109j), 
         (-0.5631559842430199+0.9135900338325109j), 
         (-0.3512792323389822-1.1275915483177057j), 
         (-0.3512792323389822+1.1275915483177057j)]
    elif N == 14:
        p = [
         (-0.9077932138396487-0.0821963994194015j), 
         (-0.9077932138396487+0.0821963994194015j), 
         (-0.8869506674916445-0.2470079178765333j), 
         (-0.8869506674916445+0.2470079178765333j), 
         (-0.8441199160909851-0.41316538251026924j), 
         (-0.8441199160909851+0.41316538251026924j), 
         (-0.7766591387063624-0.5819170677377609j), 
         (-0.7766591387063624+0.5819170677377609j), 
         (-0.6794256425119233-0.7552857305042033j), 
         (-0.6794256425119233+0.7552857305042033j), 
         (-0.5418766775112297-0.937304368351692j), 
         (-0.5418766775112297+0.937304368351692j), 
         (-0.33638682249020374-1.13917229783986j), 
         (-0.33638682249020374+1.13917229783986j)]
    elif N == 15:
        p = [
         -0.9097482363849064, 
         (-0.9006981694176979-0.15376811972784393j), 
         (-0.9006981694176979+0.15376811972784393j), 
         (-0.8731264620834985-0.30823524705642674j), 
         (-0.8731264620834985+0.30823524705642674j), 
         (-0.8256631452587146-0.46423487527343255j), 
         (-0.8256631452587146+0.46423487527343255j), 
         (-0.7556027168970728-0.6229396358758267j), 
         (-0.7556027168970728+0.6229396358758267j), 
         (-0.6579196593110999-0.7862895503722516j), 
         (-0.6579196593110999+0.7862895503722516j), 
         (-0.5224954069658331-0.9581787261092527j), 
         (-0.5224954069658331+0.9581787261092527j), 
         (-0.3229963059766444-1.1494161545836294j), 
         (-0.3229963059766444+1.1494161545836294j)]
    elif N == 16:
        p = [
         (-0.9072099595087001-0.07214211304111733j), 
         (-0.9072099595087001+0.07214211304111733j), 
         (-0.8911723070323647-0.21670896599005765j), 
         (-0.8911723070323647+0.21670896599005765j), 
         (-0.858426423152133-0.36216972718020657j), 
         (-0.858426423152133+0.36216972718020657j), 
         (-0.8074790293236004-0.50929337511718j), 
         (-0.8074790293236004+0.50929337511718j), 
         (-0.7356166304713116-0.6591950877860394j), 
         (-0.7356166304713116+0.6591950877860394j), 
         (-0.6379502514039067-0.8137453537108762j), 
         (-0.6379502514039067+0.8137453537108762j), 
         (-0.5047606444424767-0.976713747779909j), 
         (-0.5047606444424767+0.976713747779909j), 
         (-0.3108782755645388-1.1585528411993304j), 
         (-0.3108782755645388+1.1585528411993304j)]
    elif N == 17:
        p = [
         -0.9087141161336397, 
         (-0.9016273850787286-0.13602679951730245j), 
         (-0.9016273850787286+0.13602679951730245j), 
         (-0.8801100704438627-0.2725347156478804j), 
         (-0.8801100704438627+0.2725347156478804j), 
         (-0.8433414495836129-0.41007592829100215j), 
         (-0.8433414495836129+0.41007592829100215j), 
         (-0.7897644147799708-0.5493724405281089j), 
         (-0.7897644147799708+0.5493724405281089j), 
         (-0.7166893842372349-0.6914936286393609j), 
         (-0.7166893842372349+0.6914936286393609j), 
         (-0.6193710717342145-0.8382497252826993j), 
         (-0.6193710717342145+0.8382497252826993j), 
         (-0.4884629337672704-0.9932971956316782j), 
         (-0.4884629337672704+0.9932971956316782j), 
         (-0.2998489459990082-1.166761272925669j), 
         (-0.2998489459990082+1.166761272925669j)]
    elif N == 18:
        p = [
         (-0.9067004324162775-0.0642792410639307j), 
         (-0.9067004324162775+0.0642792410639307j), 
         (-0.8939764278132456-0.19303746408947586j), 
         (-0.8939764278132456+0.19303746408947586j), 
         (-0.868109550362883-0.32242049251632576j), 
         (-0.868109550362883+0.32242049251632576j), 
         (-0.8281885016242837-0.4529385697815917j), 
         (-0.8281885016242837+0.4529385697815917j), 
         (-0.7726285030739559-0.585277816208664j), 
         (-0.7726285030739559+0.585277816208664j), 
         (-0.6987821445005273-0.720469650972663j), 
         (-0.6987821445005273+0.720469650972663j), 
         (-0.6020482668090644-0.8602708961893665j), 
         (-0.6020482668090644+0.8602708961893665j), 
         (-0.47342680699161516-1.008234300314801j), 
         (-0.47342680699161516+1.008234300314801j), 
         (-0.28975920298804897-1.174183010600059j), 
         (-0.28975920298804897+1.174183010600059j)]
    elif N == 19:
        p = [
         -0.9078934217899405, 
         (-0.902193763939066-0.12195683818720265j), 
         (-0.902193763939066+0.12195683818720265j), 
         (-0.8849290585034385-0.24425907575498182j), 
         (-0.8849290585034385+0.24425907575498182j), 
         (-0.8555768765618421-0.36729258963998723j), 
         (-0.8555768765618421+0.36729258963998723j), 
         (-0.8131725551578197-0.4915365035562459j), 
         (-0.8131725551578197+0.4915365035562459j), 
         (-0.7561260971541629-0.6176483917970179j), 
         (-0.7561260971541629+0.6176483917970179j), 
         (-0.6818424412912442-0.7466272357947761j), 
         (-0.6818424412912442+0.7466272357947761j), 
         (-0.5858613321217833-0.8801817131014567j), 
         (-0.5858613321217833+0.8801817131014567j), 
         (-0.45950434497309883-1.0217687769126713j), 
         (-0.45950434497309883+1.0217687769126713j), 
         (-0.280486685143937-1.1809316284532918j), 
         (-0.280486685143937+1.1809316284532918j)]
    elif N == 20:
        p = [
         (-0.9062570115576771-0.05796178027784952j), 
         (-0.9062570115576771+0.05796178027784952j), 
         (-0.8959150941925769-0.1740317175918705j), 
         (-0.8959150941925769+0.1740317175918705j), 
         (-0.8749560316673333-0.2905559296567908j), 
         (-0.8749560316673333+0.2905559296567908j), 
         (-0.8427907479956671-0.4078917326291934j), 
         (-0.8427907479956671+0.4078917326291934j), 
         (-0.7984251191290607-0.5264942388817132j), 
         (-0.7984251191290607+0.5264942388817132j), 
         (-0.7402780309646769-0.6469975237605229j), 
         (-0.7402780309646769+0.6469975237605229j), 
         (-0.6658120544829934-0.7703721701100763j), 
         (-0.6658120544829934+0.7703721701100763j), 
         (-0.5707026806915714-0.8982829066468255j), 
         (-0.5707026806915714+0.8982829066468255j), 
         (-0.44657006982051495-1.0340977025608429j), 
         (-0.44657006982051495+1.0340977025608429j), 
         (-0.2719299580251653-1.187099379810886j), 
         (-0.2719299580251653+1.187099379810886j)]
    elif N == 21:
        p = [
         -0.9072262653142957, 
         (-0.9025428073192696-0.11052525727898564j), 
         (-0.9025428073192696+0.11052525727898564j), 
         (-0.888380810666445-0.22130692150843503j), 
         (-0.888380810666445+0.22130692150843503j), 
         (-0.8643915813643205-0.3326258512522187j), 
         (-0.8643915813643205+0.3326258512522187j), 
         (-0.8299435470674444-0.44481777394079564j), 
         (-0.8299435470674444+0.44481777394079564j), 
         (-0.7840287980408341-0.5583186348022855j), 
         (-0.7840287980408341+0.5583186348022855j), 
         (-0.7250839687106613-0.6737426063024382j), 
         (-0.7250839687106613+0.6737426063024382j), 
         (-0.6506315378609463-0.7920349342629491j), 
         (-0.6506315378609463+0.7920349342629491j), 
         (-0.5564766488918562-0.9148198405846724j), 
         (-0.5564766488918562+0.9148198405846724j), 
         (-0.43451689068152716-1.0453822558569865j), 
         (-0.43451689068152716+1.0453822558569865j), 
         (-0.2640041595834031-1.1927620319480525j), 
         (-0.2640041595834031+1.1927620319480525j)]
    elif N == 22:
        p = [
         (-0.9058702269930873-0.05277490828999905j), 
         (-0.9058702269930873+0.05277490828999905j), 
         (-0.8972983138153531-0.15843519122898655j), 
         (-0.8972983138153531+0.15843519122898655j), 
         (-0.8799661455640176-0.2644363039201535j), 
         (-0.8799661455640176+0.2644363039201535j), 
         (-0.8534754036851687-0.371038931948232j), 
         (-0.8534754036851687+0.371038931948232j), 
         (-0.8171682088462721-0.4785619492202781j), 
         (-0.8171682088462721+0.4785619492202781j), 
         (-0.7700332930556817-0.5874255426351154j), 
         (-0.7700332930556817+0.5874255426351154j), 
         (-0.7105305456418786-0.6982266265924524j), 
         (-0.7105305456418786+0.6982266265924524j), 
         (-0.6362427683267827-0.8118875040246347j), 
         (-0.6362427683267827+0.8118875040246347j), 
         (-0.5430983056306303-0.9299947824439873j), 
         (-0.5430983056306303+0.9299947824439873j), 
         (-0.42325287456426286-1.0557556052275459j), 
         (-0.42325287456426286+1.0557556052275459j), 
         (-0.2566376987939318-1.197982433555213j), 
         (-0.2566376987939318+1.197982433555213j)]
    elif N == 23:
        p = [
         -0.9066732476324988, 
         (-0.9027564979912505-0.1010534335314045j), 
         (-0.9027564979912505+0.1010534335314045j), 
         (-0.8909283242471251-0.20230246993812234j), 
         (-0.8909283242471251+0.20230246993812234j), 
         (-0.8709469395587416-0.3039581993950042j), 
         (-0.8709469395587416+0.3039581993950042j), 
         (-0.8423805948021127-0.4062657948237603j), 
         (-0.8423805948021127+0.4062657948237603j), 
         (-0.8045561642053176-0.5095305912227258j), 
         (-0.8045561642053176+0.5095305912227258j), 
         (-0.756466014682988-0.6141594859476032j), 
         (-0.756466014682988+0.6141594859476032j), 
         (-0.6965966033912705-0.7207341374753047j), 
         (-0.6965966033912705+0.7207341374753047j), 
         (-0.6225903228771342-0.830155830281298j), 
         (-0.6225903228771342+0.830155830281298j), 
         (-0.5304922463810192-0.94397603640183j), 
         (-0.5304922463810192+0.94397603640183j), 
         (-0.4126986617510149-1.0653287944755137j), 
         (-0.4126986617510149+1.0653287944755137j), 
         (-0.2497697202208956-1.2028131878706978j), 
         (-0.2497697202208956+1.2028131878706978j)]
    elif N == 24:
        p = [
         (-0.9055312363372774-0.0484400665404787j), 
         (-0.9055312363372774+0.0484400665404787j), 
         (-0.8983105104397873-0.14540561338736102j), 
         (-0.8983105104397873+0.14540561338736102j), 
         (-0.8837358034555707-0.2426335234401383j), 
         (-0.8837358034555707+0.2426335234401383j), 
         (-0.8615278304016354-0.34032021126186246j), 
         (-0.8615278304016354+0.34032021126186246j), 
         (-0.831232646681324-0.43869859335973055j), 
         (-0.831232646681324+0.43869859335973055j), 
         (-0.7921695462343492-0.5380628490968017j), 
         (-0.7921695462343492+0.5380628490968017j), 
         (-0.7433392285088529-0.6388084216222568j), 
         (-0.7433392285088529+0.6388084216222568j), 
         (-0.6832565803536521-0.7415032695091651j), 
         (-0.6832565803536521+0.7415032695091651j), 
         (-0.6096221567378336-0.8470292433077202j), 
         (-0.6096221567378336+0.8470292433077202j), 
         (-0.5185914574820317-0.9569048385259055j), 
         (-0.5185914574820317+0.9569048385259055j), 
         (-0.4027853855197518-1.0741951965186747j), 
         (-0.4027853855197518+1.0741951965186747j), 
         (-0.24334813375248696-1.2072986837319726j), 
         (-0.24334813375248696+1.2072986837319726j)]
    elif N == 25:
        p = [
         -0.9062073871811709, 
         (-0.902883339022802-0.09307713118510297j), 
         (-0.902883339022802+0.09307713118510297j), 
         (-0.8928551459883549-0.18630689698043007j), 
         (-0.8928551459883549+0.18630689698043007j), 
         (-0.8759497989677858-0.2798521321771409j), 
         (-0.8759497989677858+0.2798521321771409j), 
         (-0.851861688655402-0.3738977875907595j), 
         (-0.851861688655402+0.3738977875907595j), 
         (-0.820122604393688-0.46866685746569664j), 
         (-0.820122604393688+0.46866685746569664j), 
         (-0.7800496278186497-0.564444121034971j), 
         (-0.7800496278186497+0.564444121034971j), 
         (-0.7306549271849968-0.6616149647357749j), 
         (-0.7306549271849968+0.6616149647357749j), 
         (-0.6704827128029559-0.760734885816784j), 
         (-0.6704827128029559+0.760734885816784j), 
         (-0.5972898661335557-0.8626676330388029j), 
         (-0.5972898661335557+0.8626676330388029j), 
         (-0.5073362861078469-0.9689006305344868j), 
         (-0.5073362861078469+0.9689006305344868j), 
         (-0.393452987819108-1.0824339271738317j), 
         (-0.393452987819108+1.0824339271738317j), 
         (-0.2373280669322029-1.2114766583825654j), 
         (-0.2373280669322029+1.2114766583825654j)]
    else:
        raise ValueError('Bessel Filter not supported for order %d' % N)
    return (z, p, k)


filter_dict = {'butter': [buttap, buttord], 'butterworth': [
                 buttap, buttord], 
   'cauer': [
           ellipap, ellipord], 
   'elliptic': [
              ellipap, ellipord], 
   'ellip': [
           ellipap, ellipord], 
   'bessel': [
            besselap], 
   'cheby1': [
            cheb1ap, cheb1ord], 
   'chebyshev1': [
                cheb1ap, cheb1ord], 
   'chebyshevi': [
                cheb1ap, cheb1ord], 
   'cheby2': [
            cheb2ap, cheb2ord], 
   'chebyshev2': [
                cheb2ap, cheb2ord], 
   'chebyshevii': [
                 cheb2ap, cheb2ord]}
band_dict = {'band': 'bandpass', 'bandpass': 'bandpass', 
   'pass': 'bandpass', 
   'bp': 'bandpass', 
   'bs': 'bandstop', 
   'bandstop': 'bandstop', 
   'bands': 'bandstop', 
   'stop': 'bandstop', 
   'l': 'lowpass', 
   'low': 'lowpass', 
   'lowpass': 'lowpass', 
   'high': 'highpass', 
   'highpass': 'highpass', 
   'h': 'highpass'}