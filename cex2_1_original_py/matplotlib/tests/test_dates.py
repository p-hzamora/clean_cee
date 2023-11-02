# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_dates.pyc
# Compiled at: 2012-11-06 11:15:50
from __future__ import print_function
import datetime, numpy as np
from matplotlib.testing.decorators import image_comparison, knownfailureif, cleanup
import matplotlib.pyplot as plt
from nose.tools import assert_raises, assert_equal
import warnings

@image_comparison(baseline_images=['date_empty'])
def test_date_empty():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.xaxis_date()


@image_comparison(baseline_images=['date_axhspan'])
def test_date_axhspan():
    t0 = datetime.datetime(2009, 1, 20)
    tf = datetime.datetime(2009, 1, 21)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axhspan(t0, tf, facecolor='blue', alpha=0.25)
    ax.set_ylim(t0 - datetime.timedelta(days=5), tf + datetime.timedelta(days=5))
    fig.subplots_adjust(left=0.25)


@image_comparison(baseline_images=['date_axvspan'])
def test_date_axvspan():
    t0 = datetime.datetime(2000, 1, 20)
    tf = datetime.datetime(2010, 1, 21)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axvspan(t0, tf, facecolor='blue', alpha=0.25)
    ax.set_xlim(t0 - datetime.timedelta(days=720), tf + datetime.timedelta(days=720))
    fig.autofmt_xdate()


@image_comparison(baseline_images=['date_axhline'])
def test_date_axhline():
    t0 = datetime.datetime(2009, 1, 20)
    tf = datetime.datetime(2009, 1, 31)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axhline(t0, color='blue', lw=3)
    ax.set_ylim(t0 - datetime.timedelta(days=5), tf + datetime.timedelta(days=5))
    fig.subplots_adjust(left=0.25)


@image_comparison(baseline_images=['date_axvline'])
def test_date_axvline():
    t0 = datetime.datetime(2000, 1, 20)
    tf = datetime.datetime(2000, 1, 21)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axvline(t0, color='red', lw=3)
    ax.set_xlim(t0 - datetime.timedelta(days=5), tf + datetime.timedelta(days=5))
    fig.autofmt_xdate()


@cleanup
def test_too_many_date_ticks():
    warnings.filterwarnings('ignore', 'Attempting to set identical left==right results\\nin singular transformations; automatically expanding.\\nleft=\\d*\\.\\d*, right=\\d*\\.\\d*', UserWarning, module='matplotlib.axes')
    t0 = datetime.datetime(2000, 1, 20)
    tf = datetime.datetime(2000, 1, 20)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim((t0, tf), auto=True)
    ax.plot([], [])
    from matplotlib.dates import DayLocator, DateFormatter, HourLocator
    ax.xaxis.set_major_locator(DayLocator())
    assert_raises(RuntimeError, fig.savefig, 'junk.png')


@image_comparison(baseline_images=['RRuleLocator_bounds'])
def test_RRuleLocator():
    import pylab, matplotlib.dates as mpldates, matplotlib.testing.jpl_units as units
    from datetime import datetime
    import dateutil
    units.register()
    t0 = datetime(1000, 1, 1)
    tf = datetime(6000, 1, 1)
    fig = pylab.figure()
    ax = pylab.subplot(111)
    ax.set_autoscale_on(True)
    ax.plot([t0, tf], [0.0, 1.0], marker='o')
    rrule = mpldates.rrulewrapper(dateutil.rrule.YEARLY, interval=500)
    locator = mpldates.RRuleLocator(rrule)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mpldates.AutoDateFormatter(locator))
    ax.autoscale_view()
    fig.autofmt_xdate()


@image_comparison(baseline_images=['DateFormatter_fractionalSeconds'])
def test_DateFormatter():
    import pylab
    from datetime import datetime
    import matplotlib.testing.jpl_units as units
    units.register()
    t0 = datetime(2001, 1, 1, 0, 0, 0)
    tf = datetime(2001, 1, 1, 0, 0, 1)
    fig = pylab.figure()
    ax = pylab.subplot(111)
    ax.set_autoscale_on(True)
    ax.plot([t0, tf], [0.0, 1.0], marker='o')
    ax.autoscale_view()
    fig.autofmt_xdate()


def test_drange():
    """This test should check if drange works as expected, and if all the rounding errors
    are fixed"""
    from matplotlib import dates
    start = datetime.datetime(2011, 1, 1, tzinfo=dates.UTC)
    end = datetime.datetime(2011, 1, 2, tzinfo=dates.UTC)
    delta = datetime.timedelta(hours=1)
    assert_equal(24, len(dates.drange(start, end, delta)))
    end = end + datetime.timedelta(microseconds=1)
    assert_equal(25, len(dates.drange(start, end, delta)))
    end = datetime.datetime(2011, 1, 2, tzinfo=dates.UTC)
    delta = datetime.timedelta(hours=4)
    daterange = dates.drange(start, end, delta)
    assert_equal(6, len(daterange))
    assert_equal(dates.num2date(daterange[-1]), end - delta)


@cleanup
@knownfailureif(True)
def test_empty_date_with_year_formatter():
    import matplotlib.dates as dates
    fig = plt.figure()
    ax = fig.add_subplot(111)
    yearFmt = dates.DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearFmt)
    fig.savefig('empty_date_bug')


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)