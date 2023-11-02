# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\constants\constants.pyc
# Compiled at: 2013-02-16 13:27:30
"""
Collection of physical constants and conversion factors.

Most constants are in SI units, so you can do
print '10 mile per minute is', 10*mile/minute, 'm/s or', 10*mile/(minute*knot), 'knots'

The list is not meant to be comprehensive, but just a convenient list for everyday use.
"""
from __future__ import division, print_function, absolute_import
import math as _math
from .codata import value as _cd
import numpy as _np
pi = _math.pi
golden = golden_ratio = (1 + _math.sqrt(5)) / 2
yotta = 1e+24
zetta = 1e+21
exa = 1e+18
peta = 1000000000000000.0
tera = 1000000000000.0
giga = 1000000000.0
mega = 1000000.0
kilo = 1000.0
hecto = 100.0
deka = 10.0
deci = 0.1
centi = 0.01
milli = 0.001
micro = 1e-06
nano = 1e-09
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
kibi = 1024
mebi = 1048576
gibi = 1073741824
tebi = 1099511627776
pebi = 1125899906842624
exbi = 1152921504606846976
zebi = 1180591620717411303424
yobi = 1208925819614629174706176
c = speed_of_light = _cd('speed of light in vacuum')
mu_0 = 4e-07 * pi
epsilon_0 = 1 / (mu_0 * c * c)
h = Planck = _cd('Planck constant')
hbar = h / (2 * pi)
G = gravitational_constant = _cd('Newtonian constant of gravitation')
g = _cd('standard acceleration of gravity')
e = elementary_charge = _cd('elementary charge')
R = gas_constant = _cd('molar gas constant')
alpha = fine_structure = _cd('fine-structure constant')
N_A = Avogadro = _cd('Avogadro constant')
k = Boltzmann = _cd('Boltzmann constant')
sigma = Stefan_Boltzmann = _cd('Stefan-Boltzmann constant')
Wien = _cd('Wien wavelength displacement law constant')
Rydberg = _cd('Rydberg constant')
gram = 0.001
metric_ton = 1000.0
grain = 6.479891e-05
lb = pound = 7000 * grain
oz = ounce = pound / 16
stone = 14 * pound
long_ton = 2240 * pound
short_ton = 2000 * pound
troy_ounce = 480 * grain
troy_pound = 12 * troy_ounce
carat = 0.0002
m_e = electron_mass = _cd('electron mass')
m_p = proton_mass = _cd('proton mass')
m_n = neutron_mass = _cd('neutron mass')
m_u = u = atomic_mass = _cd('atomic mass constant')
degree = pi / 180
arcmin = arcminute = degree / 60
arcsec = arcsecond = arcmin / 60
minute = 60.0
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365 * day
Julian_year = 365.25 * day
inch = 0.0254
foot = 12 * inch
yard = 3 * foot
mile = 1760 * yard
mil = inch / 1000
pt = point = inch / 72
survey_foot = 0.3048006096012192
survey_mile = 5280 * survey_foot
nautical_mile = 1852.0
fermi = 1e-15
angstrom = 1e-10
micron = 1e-06
au = astronomical_unit = 149597870691.0
light_year = Julian_year * c
parsec = au / arcsec
atm = atmosphere = _cd('standard atmosphere')
bar = 100000.0
torr = mmHg = atm / 760
psi = pound * g / (inch * inch)
hectare = 10000.0
acre = 43560 * foot ** 2
litre = liter = 0.001
gallon = gallon_US = 231 * inch ** 3
fluid_ounce = fluid_ounce_US = gallon_US / 128
bbl = barrel = 42 * gallon_US
gallon_imp = 0.00454609
fluid_ounce_imp = gallon_imp / 160
kmh = 1000.0 / hour
mph = mile / hour
mach = speed_of_sound = 340.5
knot = nautical_mile / hour
zero_Celsius = 273.15
degree_Fahrenheit = 0.5555555555555556
eV = electron_volt = elementary_charge
calorie = calorie_th = 4.184
calorie_IT = 4.1868
erg = 1e-07
Btu_th = pound * degree_Fahrenheit * calorie_th / gram
Btu = Btu_IT = pound * degree_Fahrenheit * calorie_IT / gram
ton_TNT = 1000000000.0 * calorie_th
hp = horsepower = 550 * foot * pound * g
dyn = dyne = 1e-05
lbf = pound_force = pound * g
kgf = kilogram_force = g

def C2K(C):
    """
    Convert Celsius to Kelvin

    Parameters
    ----------
    C : array_like
        Celsius temperature(s) to be converted.

    Returns
    -------
    K : float or array of floats
        Equivalent Kelvin temperature(s).

    Notes
    -----
    Computes ``K = C + zero_Celsius`` where `zero_Celsius` = 273.15, i.e.,
    (the absolute value of) temperature "absolute zero" as measured in Celsius.

    Examples
    --------
    >>> from scipy.constants.constants import C2K
    >>> C2K(_np.array([-40, 40.0]))
    array([ 233.15,  313.15])

    """
    return _np.asanyarray(C) + zero_Celsius


def K2C(K):
    """
    Convert Kelvin to Celsius

    Parameters
    ----------
    K : array_like
        Kelvin temperature(s) to be converted.

    Returns
    -------
    C : float or array of floats
        Equivalent Celsius temperature(s).

    Notes
    -----
    Computes ``C = K - zero_Celsius`` where `zero_Celsius` = 273.15, i.e.,
    (the absolute value of) temperature "absolute zero" as measured in Celsius.

    Examples
    --------
    >>> from scipy.constants.constants import K2C
    >>> K2C(_np.array([233.15, 313.15]))
    array([-40.,  40.])

    """
    return _np.asanyarray(K) - zero_Celsius


def F2C(F):
    """
    Convert Fahrenheit to Celsius

    Parameters
    ----------
    F : array_like
        Fahrenheit temperature(s) to be converted.

    Returns
    -------
    C : float or array of floats
        Equivalent Celsius temperature(s).

    Notes
    -----
    Computes ``C = (F - 32) / 1.8``.

    Examples
    --------
    >>> from scipy.constants.constants import F2C
    >>> F2C(_np.array([-40, 40.0]))
    array([-40.        ,   4.44444444])

    """
    return (_np.asanyarray(F) - 32) / 1.8


def C2F(C):
    """
    Convert Celsius to Fahrenheit

    Parameters
    ----------
    C : array_like
        Celsius temperature(s) to be converted.

    Returns
    -------
    F : float or array of floats
        Equivalent Fahrenheit temperature(s).

    Notes
    -----
    Computes ``F = 1.8 * C + 32``.

    Examples
    --------
    >>> from scipy.constants.constants import C2F
    >>> C2F(_np.array([-40, 40.0]))
    array([ -40.,  104.])

    """
    return 1.8 * _np.asanyarray(C) + 32


def F2K(F):
    """
    Convert Fahrenheit to Kelvin

    Parameters
    ----------
    F : array_like
        Fahrenheit temperature(s) to be converted.

    Returns
    -------
    K : float or array of floats
        Equivalent Kelvin temperature(s).

    Notes
    -----
    Computes ``K = (F - 32)/1.8 + zero_Celsius`` where `zero_Celsius` =
    273.15, i.e., (the absolute value of) temperature "absolute zero" as
    measured in Celsius.

    Examples
    --------
    >>> from scipy.constants.constants import F2K
    >>> F2K(_np.array([-40, 104]))
    array([ 233.15,  313.15])

    """
    return C2K(F2C(_np.asanyarray(F)))


def K2F(K):
    """
    Convert Kelvin to Fahrenheit

    Parameters
    ----------
    K : array_like
        Kelvin temperature(s) to be converted.

    Returns
    -------
    F : float or array of floats
        Equivalent Fahrenheit temperature(s).

    Notes
    -----
    Computes ``F = 1.8 * (K - zero_Celsius) + 32`` where `zero_Celsius` =
    273.15, i.e., (the absolute value of) temperature "absolute zero" as
    measured in Celsius.

    Examples
    --------
    >>> from scipy.constants.constants import K2F
    >>> K2F(_np.array([233.15,  313.15]))
    array([ -40.,  104.])

    """
    return C2F(K2C(_np.asanyarray(K)))


def lambda2nu(lambda_):
    """
    Convert wavelength to optical frequency

    Parameters
    ----------
    lambda : array_like
        Wavelength(s) to be converted.

    Returns
    -------
    nu : float or array of floats
        Equivalent optical frequency.

    Notes
    -----
    Computes ``nu = c / lambda`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants.constants import lambda2nu
    >>> lambda2nu(_np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
    return _np.asanyarray(c) / lambda_


def nu2lambda(nu):
    """
    Convert optical frequency to wavelength.

    Parameters
    ----------
    nu : array_like
        Optical frequency to be converted.

    Returns
    -------
    lambda : float or array of floats
        Equivalent wavelength(s).

    Notes
    -----
    Computes ``lambda = c / nu`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants.constants import nu2lambda
    >>> nu2lambda(_np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
    return c / _np.asanyarray(nu)