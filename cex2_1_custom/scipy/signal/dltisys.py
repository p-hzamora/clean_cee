# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\signal\dltisys.pyc
# Compiled at: 2013-02-16 13:27:32
"""
dltisys - Code related to discrete linear time-invariant systems
"""
from __future__ import division, print_function, absolute_import
import numpy as np
from scipy.interpolate import interp1d
from .ltisys import tf2ss, zpk2ss
__all__ = [
 'dlsim', 'dstep', 'dimpulse']

def dlsim(system, u, t=None, x0=None):
    """
    Simulate output of a discrete-time linear system.

    Parameters
    ----------
    system : class instance or tuple
        An instance of the LTI class, or a tuple describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:

          - 3: (num, den, dt)
          - 4: (zeros, poles, gain, dt)
          - 5: (A, B, C, D, dt)

    u : array_like
        An input array describing the input at each time `t` (interpolation is
        assumed between given times).  If there are multiple inputs, then each
        column of the rank-2 array represents an input.
    t : array_like, optional
        The time steps at which the input is defined.  If `t` is given, the
        final value in `t` determines the number of steps returned in the
        output.
    x0 : arry_like, optional
        The initial conditions on the state vector (zero by default).

    Returns
    -------
    tout : ndarray
        Time values for the output, as a 1-D array.
    yout : ndarray
        System response, as a 1-D array.
    xout : ndarray, optional
        Time-evolution of the state-vector.  Only generated if the input is a
        state-space systems.

    See Also
    --------
    lsim, dstep, dimpulse, cont2discrete

    Examples
    --------
    A simple integrator transfer function with a discrete time step of 1.0
    could be implemented as:

    >>> from scipy import signal
    >>> tf = ([1.0,], [1.0, -1.0], 1.0)
    >>> t_in = [0.0, 1.0, 2.0, 3.0]
    >>> u = np.asarray([0.0, 0.0, 1.0, 1.0])
    >>> t_out, y = signal.dlsim(tf, u, t=t_in)
    >>> y
    array([ 0.,  0.,  0.,  1.])

    """
    if len(system) == 3:
        a, b, c, d = tf2ss(system[0], system[1])
        dt = system[2]
    else:
        if len(system) == 4:
            a, b, c, d = zpk2ss(system[0], system[1], system[2])
            dt = system[3]
        elif len(system) == 5:
            a, b, c, d, dt = system
        else:
            raise ValueError('System argument should be a discrete transfer ' + 'function, zeros-poles-gain specification, or ' + 'state-space system')
        if t is None:
            out_samples = max(u.shape)
            stoptime = (out_samples - 1) * dt
        else:
            stoptime = t[-1]
            out_samples = int(np.floor(stoptime / dt)) + 1
        xout = np.zeros((out_samples, a.shape[0]))
        yout = np.zeros((out_samples, c.shape[0]))
        tout = np.linspace(0.0, stoptime, num=out_samples)
        if x0 is None:
            xout[0, :] = np.zeros((a.shape[1],))
        else:
            xout[0, :] = np.asarray(x0)
        if t is None:
            u_dt = u
        else:
            if len(u.shape) == 1:
                u = u[:, np.newaxis]
            u_dt_interp = interp1d(t, u.transpose(), copy=False, bounds_error=True)
            u_dt = u_dt_interp(tout).transpose()
        for i in range(0, out_samples - 1):
            xout[i + 1, :] = np.dot(a, xout[i, :]) + np.dot(b, u_dt[i, :])
            yout[i, :] = np.dot(c, xout[i, :]) + np.dot(d, u_dt[i, :])

    yout[out_samples - 1, :] = np.dot(c, xout[out_samples - 1, :]) + np.dot(d, u_dt[out_samples - 1, :])
    if len(system) == 5:
        return (tout, yout, xout)
    else:
        return (
         tout, yout)
        return


def dimpulse(system, x0=None, t=None, n=None):
    """Impulse response of discrete-time system.

    Parameters
    ----------
    system : tuple
        The following gives the number of elements in the tuple and
        the interpretation:

          * 3: (num, den, dt)
          * 4: (zeros, poles, gain, dt)
          * 5: (A, B, C, D, dt)

    x0 : array_like, optional
        Initial state-vector.  Defaults to zero.
    t : array_like, optional
        Time points.  Computed if not given.
    n : int, optional
        The number of time points to compute (if `t` is not given).

    Returns
    -------
    t : ndarray
        A 1-D array of time points.
    yout : tuple of array_like
        Step response of system.  Each element of the tuple represents
        the output of the system based on an impulse in each input.

    See Also
    --------
    impulse, dstep, dlsim, cont2discrete

    """
    if len(system) == 3:
        n_inputs = 1
        dt = system[2]
    else:
        if len(system) == 4:
            n_inputs = 1
            dt = system[3]
        elif len(system) == 5:
            n_inputs = system[1].shape[1]
            dt = system[4]
        else:
            raise ValueError('System argument should be a discrete transfer ' + 'function, zeros-poles-gain specification, or ' + 'state-space system')
        if n is None:
            n = 100
        if t is None:
            t = np.arange(0, n * dt, dt)
        yout = None
        for i in range(0, n_inputs):
            u = np.zeros((t.shape[0], n_inputs))
            u[(0, i)] = 1.0
            one_output = dlsim(system, u, t=t, x0=x0)
            if yout is None:
                yout = (
                 one_output[1],)
            else:
                yout = yout + (one_output[1],)
            tout = one_output[0]

    return (
     tout, yout)


def dstep(system, x0=None, t=None, n=None):
    """Step response of discrete-time system.

    Parameters
    ----------
    system : a tuple describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:

          * 3: (num, den, dt)
          * 4: (zeros, poles, gain, dt)
          * 5: (A, B, C, D, dt)

    x0 : array_like, optional
        Initial state-vector (default is zero).
    t : array_like, optional
        Time points (computed if not given).
    n : int, optional
        Number of time points to compute if `t` is not given.

    Returns
    -------
    t : ndarray
        Output time points, as a 1-D array.
    yout : tuple of array_like
        Step response of system.  Each element of the tuple represents
        the output of the system based on a step response to each input.

    See Also
    --------
    step, dimpulse, dlsim, cont2discrete

    """
    if len(system) == 3:
        n_inputs = 1
        dt = system[2]
    else:
        if len(system) == 4:
            n_inputs = 1
            dt = system[3]
        elif len(system) == 5:
            n_inputs = system[1].shape[1]
            dt = system[4]
        else:
            raise ValueError('System argument should be a discrete transfer ' + 'function, zeros-poles-gain specification, or ' + 'state-space system')
        if n is None:
            n = 100
        if t is None:
            t = np.arange(0, n * dt, dt)
        yout = None
        for i in range(0, n_inputs):
            u = np.zeros((t.shape[0], n_inputs))
            u[:, i] = np.ones((t.shape[0],))
            one_output = dlsim(system, u, t=t, x0=x0)
            if yout is None:
                yout = (
                 one_output[1],)
            else:
                yout = yout + (one_output[1],)
            tout = one_output[0]

    return (
     tout, yout)