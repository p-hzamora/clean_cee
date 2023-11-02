# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\testing\jpl_units\UnitDblFormatter.pyc
# Compiled at: 2012-10-30 18:11:14
"""UnitDblFormatter module containing class UnitDblFormatter."""
from __future__ import print_function
import matplotlib.ticker as ticker
__all__ = [
 'UnitDblFormatter']

class UnitDblFormatter(ticker.ScalarFormatter):
    """The formatter for UnitDbl data types.  This allows for formatting
      with the unit string.
   """

    def __init__(self, *args, **kwargs):
        """The arguments are identical to matplotlib.ticker.ScalarFormatter."""
        ticker.ScalarFormatter.__init__(self, *args, **kwargs)

    def __call__(self, x, pos=None):
        """Return the format for tick val x at position pos"""
        if len(self.locs) == 0:
            return ''
        else:
            return str(x)

    def format_data_short(self, value):
        """Return the value formatted in 'short' format."""
        return str(value)

    def format_data(self, value):
        """Return the value formatted into a string."""
        return str(value)