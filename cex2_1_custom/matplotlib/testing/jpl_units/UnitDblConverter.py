# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\jpl_units\UnitDblConverter.pyc
# Compiled at: 2012-10-30 18:11:14
"""UnitDblConverter module containing class UnitDblConverter."""
from __future__ import print_function
import numpy as np, matplotlib.units as units, matplotlib.ticker as ticker, matplotlib.projections.polar as polar
from matplotlib.cbook import iterable
__all__ = [
 'UnitDblConverter']

def rad_fn(x, pos=None):
    """Radian function formatter."""
    n = int(x / np.pi * 2.0 + 0.25)
    if n == 0:
        return str(x)
    else:
        if n == 1:
            return '$\\pi/2$'
        if n == 2:
            return '$\\pi$'
        if n % 2 == 0:
            return '$%s\\pi$' % (n / 2,)
        return '$%s\\pi/2$' % (n,)


class UnitDblConverter(units.ConversionInterface):
    """: A matplotlib converter class.  Provides matplotlib conversion
        functionality for the Monte UnitDbl class.
   """
    defaults = {'distance': 'km', 
       'angle': 'deg', 
       'time': 'sec'}

    @staticmethod
    def axisinfo(unit, axis):
        """: Returns information on how to handle an axis that has Epoch data.

      = INPUT VARIABLES
      - unit    The units to use for a axis with Epoch data.

      = RETURN VALUE
      - Returns a matplotlib AxisInfo data structure that contains
        minor/major formatters, major/minor locators, and default
        label information.
      """
        import matplotlib.testing.jpl_units as U
        if unit:
            if isinstance(unit, str):
                label = unit
            else:
                label = unit.label()
        else:
            label = None
        if label == 'deg' and isinstance(axis.axes, polar.PolarAxes):
            majfmt = polar.PolarAxes.ThetaFormatter()
        else:
            majfmt = U.UnitDblFormatter(useOffset=False)
        return units.AxisInfo(majfmt=majfmt, label=label)

    @staticmethod
    def convert(value, unit, axis):
        """: Convert value using unit to a float.  If value is a sequence, return
      the converted sequence.

      = INPUT VARIABLES
      - value   The value or list of values that need to be converted.
      - unit    The units to use for a axis with Epoch data.

      = RETURN VALUE
      - Returns the value parameter converted to floats.
      """
        import matplotlib.testing.jpl_units as U
        isNotUnitDbl = True
        if iterable(value) and not isinstance(value, str):
            if len(value) == 0:
                return []
            else:
                return [ UnitDblConverter.convert(x, unit, axis) for x in value ]

        if isinstance(value, U.UnitDbl):
            isNotUnitDbl = False
        if isNotUnitDbl and units.ConversionInterface.is_numlike(value):
            return value
        else:
            if unit == None:
                unit = UnitDblConverter.default_units(value, axis)
            if isinstance(axis.axes, polar.PolarAxes) and value.type() == 'angle':
                return value.convert('rad')
            return value.convert(unit)

    @staticmethod
    def default_units(value, axis):
        """: Return the default unit for value, or None.

      = INPUT VARIABLES
      - value   The value or list of values that need units.

      = RETURN VALUE
      - Returns the default units to use for value.
      Return the default unit for value, or None.
      """
        if iterable(value) and not isinstance(value, str):
            return UnitDblConverter.default_units(value[0], axis)
        else:
            return UnitDblConverter.defaults[value.type()]