# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\jpl_units\StrConverter.pyc
# Compiled at: 2012-10-30 18:11:14
"""StrConverter module containing class StrConverter."""
from __future__ import print_function
import matplotlib.units as units
from matplotlib.cbook import iterable
__all__ = [
 'StrConverter']

class StrConverter(units.ConversionInterface):
    """: A matplotlib converter class.  Provides matplotlib conversion
        functionality for string data values.

   Valid units for string are:
   - 'indexed' : Values are indexed as they are specified for plotting.
   - 'sorted'  : Values are sorted alphanumerically.
   - 'inverted' : Values are inverted so that the first value is on top.
   - 'sorted-inverted' :  A combination of 'sorted' and 'inverted'
   """

    @staticmethod
    def axisinfo(unit, axis):
        """: Returns information on how to handle an axis that has string data.

      = INPUT VARIABLES
      - axis    The axis using this converter.
      - unit    The units to use for a axis with string data.

      = RETURN VALUE
      - Returns a matplotlib AxisInfo data structure that contains
        minor/major formatters, major/minor locators, and default
        label information.
      """
        return

    @staticmethod
    def convert(value, unit, axis):
        """: Convert value using unit to a float.  If value is a sequence, return
      the converted sequence.

      = INPUT VARIABLES
      - axis    The axis using this converter.
      - value   The value or list of values that need to be converted.
      - unit    The units to use for a axis with Epoch data.

      = RETURN VALUE
      - Returns the value parameter converted to floats.
      """
        if units.ConversionInterface.is_numlike(value):
            return value
        if value == []:
            return []
        ax = axis.axes
        if axis is ax.get_xaxis():
            isXAxis = True
        else:
            isXAxis = False
        axis.get_major_ticks()
        ticks = axis.get_ticklocs()
        labels = axis.get_ticklabels()
        labels = [ l.get_text() for l in labels if l.get_text() ]
        if not labels:
            ticks = []
            labels = []
        if not iterable(value):
            value = [
             value]
        newValues = []
        for v in value:
            if v not in labels and v not in newValues:
                newValues.append(v)

        for v in newValues:
            if labels:
                labels.append(v)
            else:
                labels = [
                 v]

        labels = [
         ''] + labels + ['']
        ticks = range(len(labels))
        ticks[0] = 0.5
        ticks[-1] = ticks[-1] - 0.5
        axis.set_ticks(ticks)
        axis.set_ticklabels(labels)
        loc = axis.get_major_locator()
        loc.set_bounds(ticks[0], ticks[-1])
        if isXAxis:
            ax.set_xlim(ticks[0], ticks[-1])
        else:
            ax.set_ylim(ticks[0], ticks[-1])
        result = []
        for v in value:
            errmsg = 'This is due to a logic error in the StrConverter class.  '
            errmsg += 'Please report this error and its message in bugzilla.'
            assert v in labels, errmsg
            result.append(ticks[labels.index(v)])

        ax.viewLim.ignore(-1)
        return result

    @staticmethod
    def default_units(value, axis):
        """: Return the default unit for value, or None.

      = INPUT VARIABLES
      - axis    The axis using this converter.
      - value   The value or list of values that need units.

      = RETURN VALUE
      - Returns the default units to use for value.
      Return the default unit for value, or None.
      """
        return 'indexed'