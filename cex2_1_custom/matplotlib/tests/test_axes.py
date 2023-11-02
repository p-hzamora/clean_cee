# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_axes.pyc
# Compiled at: 2012-11-06 11:15:48
import numpy as np
from numpy import ma
import matplotlib
from matplotlib.testing.decorators import image_comparison, cleanup
import matplotlib.pyplot as plt

@image_comparison(baseline_images=['formatter_ticker_001', 
 'formatter_ticker_002', 
 'formatter_ticker_003', 
 'formatter_ticker_004', 
 'formatter_ticker_005'])
def test_formatter_ticker():
    import matplotlib.testing.jpl_units as units
    units.register()
    matplotlib.rcParams['lines.markeredgewidth'] = 30
    xdata = [ x * units.sec for x in range(10) ]
    ydata1 = [ (1.5 * y - 0.5) * units.km for y in range(10) ]
    ydata2 = [ (1.75 * y - 1.0) * units.km for y in range(10) ]
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set_xlabel('x-label 001')
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set_xlabel('x-label 001')
    ax.plot(xdata, ydata1, color='blue', xunits='sec')
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set_xlabel('x-label 001')
    ax.plot(xdata, ydata1, color='blue', xunits='sec')
    ax.set_xlabel('x-label 003')
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(xdata, ydata1, color='blue', xunits='sec')
    ax.plot(xdata, ydata2, color='green', xunits='hour')
    ax.set_xlabel('x-label 004')
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(xdata, ydata1, color='blue', xunits='sec')
    ax.plot(xdata, ydata2, color='green', xunits='hour')
    ax.set_xlabel('x-label 005')
    ax.autoscale_view()


@image_comparison(baseline_images=['formatter_large_small'])
def test_formatter_large_small():
    fig, ax = plt.subplots(1)
    x = [0.500000001, 0.500000002]
    y = [500000001, 500000002]
    ax.plot(x, y)


@image_comparison(baseline_images=['twin_axis_locaters_formatters'])
def test_twin_axis_locaters_formatters():
    vals = np.linspace(0, 1, num=5, endpoint=True)
    locs = np.sin(np.pi * vals / 2.0)
    majl = plt.FixedLocator(locs)
    minl = plt.FixedLocator([0.1, 0.2, 0.3])
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot([0.1, 100], [0, 1])
    ax1.yaxis.set_major_locator(majl)
    ax1.yaxis.set_minor_locator(minl)
    ax1.yaxis.set_major_formatter(plt.FormatStrFormatter('%08.2lf'))
    ax1.yaxis.set_minor_formatter(plt.FixedFormatter(['tricks', 'mind', 'jedi']))
    ax1.xaxis.set_major_locator(plt.LinearLocator())
    ax1.xaxis.set_minor_locator(plt.FixedLocator([15, 35, 55, 75]))
    ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%05.2lf'))
    ax1.xaxis.set_minor_formatter(plt.FixedFormatter(['c', '3', 'p', 'o']))
    ax2 = ax1.twiny()
    ax3 = ax1.twinx()


@image_comparison(baseline_images=['autoscale_tiny_range'], remove_text=True)
def test_autoscale_tiny_range():
    fig, ax = plt.subplots(2, 2)
    ax = ax.flatten()
    for i in xrange(4):
        y1 = 10 ** (-11 - i)
        ax[i].plot([0, 1], [1, 1 + y1])


@image_comparison(baseline_images=['offset_points'], remove_text=True)
def test_basic_annotate():
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2.0 * np.pi * t)
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 5), ylim=(-3, 5))
    line, = ax.plot(t, s, lw=3, color='purple')
    ax.annotate('local max', xy=(3, 1), xycoords='data', xytext=(3, 3), textcoords='offset points')


@image_comparison(baseline_images=['polar_axes'])
def test_polar_annotations():
    r = np.arange(0.0, 1.0, 0.001)
    theta = 4.0 * np.pi * r
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    line, = ax.plot(theta, r, color='#ee8d18', lw=3)
    ind = 800
    thisr, thistheta = r[ind], theta[ind]
    ax.plot([thistheta], [thisr], 'o')
    ax.annotate('a polar annotation', xy=(
     thistheta, thisr), xytext=(0.05, 0.05), textcoords='figure fraction', arrowprops=dict(facecolor='black', shrink=0.05), horizontalalignment='left', verticalalignment='baseline')


@image_comparison(baseline_images=['polar_coords'], remove_text=True)
def test_polar_coord_annotations():
    from matplotlib.patches import Ellipse
    el = Ellipse((0, 0), 10, 20, facecolor='r', alpha=0.5)
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_artist(el)
    el.set_clip_box(ax.bbox)
    ax.annotate('the top', xy=(
     np.pi / 2.0, 10.0), xytext=(
     np.pi / 3, 20.0), xycoords='polar', textcoords='polar', arrowprops=dict(facecolor='black', shrink=0.05), horizontalalignment='left', verticalalignment='baseline', clip_on=True)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)


@image_comparison(baseline_images=['fill_units'])
def test_fill_units():
    from datetime import datetime
    import matplotlib.testing.jpl_units as units
    units.register()
    t = units.Epoch('ET', dt=datetime(2009, 4, 27))
    value = 10.0 * units.deg
    day = units.Duration('ET', 86400.0)
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.plot([t], [value], yunits='deg', color='red')
    ax1.fill([733525.0, 733525.0, 733526.0, 733526.0], [
     0.0, 0.0, 90.0, 0.0], 'b')
    ax2 = fig.add_subplot(222)
    ax2.plot([t], [value], yunits='deg', color='red')
    ax2.fill([t, t, t + day, t + day], [
     0.0, 0.0, 90.0, 0.0], 'b')
    ax3 = fig.add_subplot(223)
    ax3.plot([t], [value], yunits='deg', color='red')
    ax3.fill([733525.0, 733525.0, 733526.0, 733526.0], [
     0 * units.deg, 0 * units.deg, 90 * units.deg, 0 * units.deg], 'b')
    ax4 = fig.add_subplot(224)
    ax4.plot([t], [value], yunits='deg', color='red')
    ax4.fill([t, t, t + day, t + day], [
     0 * units.deg, 0 * units.deg, 90 * units.deg, 0 * units.deg], facecolor='blue')
    fig.autofmt_xdate()


@image_comparison(baseline_images=['single_point'])
def test_single_point():
    fig = plt.figure()
    plt.subplot(211)
    plt.plot([0], [0], 'o')
    plt.subplot(212)
    plt.plot([1], [1], 'o')


@image_comparison(baseline_images=['single_date'])
def test_single_date():
    time1 = [721964.0]
    data1 = [-65.54]
    fig = plt.figure()
    plt.subplot(211)
    plt.plot_date(time1, data1, 'o', color='r')
    plt.subplot(212)
    plt.plot(time1, data1, 'o', color='r')


@image_comparison(baseline_images=['shaped_data'])
def test_shaped_data():
    xdata = np.array([
     [0.53295185, 0.23052951, 0.19057629, 0.66724975, 0.96577916, 
      0.73136095, 
      0.60823287, 0.017921, 0.29744742, 0.27164665],
     [
      0.2798012, 0.25814229, 0.02818193, 0.12966456, 0.57446277, 
      0.58167607, 
      0.71028245, 0.69112737, 0.89923072, 0.99072476],
     [
      0.81218578, 0.80464528, 0.76071809, 0.85616314, 0.12757994, 
      0.94324936, 
      0.73078663, 0.09658102, 0.60703967, 0.77664978],
     [
      0.28332265, 0.81479711, 0.86985333, 0.43797066, 0.32540082, 
      0.43819229, 
      0.92230363, 0.49414252, 0.68168256, 0.05922372],
     [
      0.10721335, 0.93904142, 0.79163075, 0.73232848, 0.90283839, 
      0.68408046, 
      0.25502302, 0.95976614, 0.59214115, 0.13663711],
     [
      0.28087456, 0.33127607, 0.15530412, 0.76558121, 0.83389773, 
      0.03735974, 
      0.98717738, 0.71432229, 0.54881366, 0.86893953],
     [
      0.77995937, 0.995556, 0.29688434, 0.15646162, 0.051848, 
      0.37161935, 
      0.12998491, 0.09377296, 0.36882507, 0.36583435],
     [
      0.37851836, 0.05315792, 0.63144617, 0.25003433, 0.69586032, 
      0.11393988, 
      0.92362096, 0.88045438, 0.93530252, 0.68275072],
     [
      0.86486596, 0.83236675, 0.82960664, 0.5779663, 0.25724233, 
      0.84841095, 
      0.90862812, 0.64414887, 0.3565272, 0.71026066],
     [
      0.01383268, 0.3406093, 0.76084285, 0.70800694, 0.87634056, 
      0.08213693, 
      0.54655021, 0.98123181, 0.44080053, 0.86815815]])
    y1 = np.arange(10)
    y1.shape = (1, 10)
    y2 = np.arange(10)
    y2.shape = (10, 1)
    fig = plt.figure()
    plt.subplot(411)
    plt.plot(y1)
    plt.subplot(412)
    plt.plot(y2)
    plt.subplot(413)
    from nose.tools import assert_raises
    assert_raises(ValueError, plt.plot, (y1, y2))
    plt.subplot(414)
    plt.plot(xdata[:, 1], xdata[1, :], 'o')


@image_comparison(baseline_images=['const_xy'])
def test_const_xy():
    fig = plt.figure()
    plt.subplot(311)
    plt.plot(np.arange(10), np.ones((10, )))
    plt.subplot(312)
    plt.plot(np.ones((10, )), np.arange(10))
    plt.subplot(313)
    plt.plot(np.ones((10, )), np.ones((10, )), 'o')


@image_comparison(baseline_images=['polar_wrap_180',
 'polar_wrap_360'])
def test_polar_wrap():
    D2R = np.pi / 180.0
    fig = plt.figure()
    plt.subplot(111, polar=True)
    plt.polar([179 * D2R, -179 * D2R], [0.2, 0.1], 'b.-')
    plt.polar([179 * D2R, 181 * D2R], [0.2, 0.1], 'g.-')
    plt.rgrids([0.05, 0.1, 0.15, 0.2, 0.25, 0.3])
    assert len(fig.axes) == 1, 'More than one polar axes created.'
    fig = plt.figure()
    plt.subplot(111, polar=True)
    plt.polar([2 * D2R, -2 * D2R], [0.2, 0.1], 'b.-')
    plt.polar([2 * D2R, 358 * D2R], [0.2, 0.1], 'g.-')
    plt.polar([358 * D2R, 2 * D2R], [0.2, 0.1], 'r.-')
    plt.rgrids([0.05, 0.1, 0.15, 0.2, 0.25, 0.3])


@image_comparison(baseline_images=['polar_units', 'polar_units_2'], freetype_version=('2.4.5',
                                                                                      '2.4.9'))
def test_polar_units():
    import matplotlib.testing.jpl_units as units
    from nose.tools import assert_true
    units.register()
    pi = np.pi
    deg = units.UnitDbl(1.0, 'deg')
    km = units.UnitDbl(1.0, 'km')
    x1 = [
     pi / 6.0, pi / 4.0, pi / 3.0, pi / 2.0]
    x2 = [30.0 * deg, 45.0 * deg, 60.0 * deg, 90.0 * deg]
    y1 = [
     1.0, 2.0, 3.0, 4.0]
    y2 = [4.0, 3.0, 2.0, 1.0]
    fig = plt.figure()
    plt.polar(x2, y1, color='blue')
    fig = plt.figure()
    y1 = [ y * km for y in y1 ]
    plt.polar(x2, y1, color='blue', thetaunits='rad', runits='km')
    assert_true(isinstance(plt.gca().get_xaxis().get_major_formatter(), units.UnitDblFormatter))


@image_comparison(baseline_images=['polar_rmin'])
def test_polar_rmin():
    r = np.arange(0, 3.0, 0.01)
    theta = 2 * np.pi * r
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    ax.plot(theta, r)
    ax.set_rmax(2.0)
    ax.set_rmin(0.5)


@image_comparison(baseline_images=['polar_theta_position'])
def test_polar_theta_position():
    r = np.arange(0, 3.0, 0.01)
    theta = 2 * np.pi * r
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    ax.plot(theta, r)
    ax.set_theta_zero_location('NW')
    ax.set_theta_direction('clockwise')


@image_comparison(baseline_images=['axvspan_epoch'])
def test_axvspan_epoch():
    from datetime import datetime
    import matplotlib.testing.jpl_units as units
    units.register()
    t0 = units.Epoch('ET', dt=datetime(2009, 1, 20))
    tf = units.Epoch('ET', dt=datetime(2009, 1, 21))
    dt = units.Duration('ET', units.day.convert('sec'))
    fig = plt.figure()
    plt.axvspan(t0, tf, facecolor='blue', alpha=0.25)
    ax = plt.gca()
    ax.set_xlim(t0 - 5.0 * dt, tf + 5.0 * dt)


@image_comparison(baseline_images=['axhspan_epoch'])
def test_axhspan_epoch():
    from datetime import datetime
    import matplotlib.testing.jpl_units as units
    units.register()
    t0 = units.Epoch('ET', dt=datetime(2009, 1, 20))
    tf = units.Epoch('ET', dt=datetime(2009, 1, 21))
    dt = units.Duration('ET', units.day.convert('sec'))
    fig = plt.figure()
    plt.axhspan(t0, tf, facecolor='blue', alpha=0.25)
    ax = plt.gca()
    ax.set_ylim(t0 - 5.0 * dt, tf + 5.0 * dt)


@image_comparison(baseline_images=['hexbin_extent'], remove_text=True)
def test_hexbin_extent():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    data = np.arange(2000.0) / 2000.0
    data.shape = (2, 1000)
    x, y = data
    ax.hexbin(x, y, extent=[0.1, 0.3, 0.6, 0.7])


@image_comparison(baseline_images=['nonfinite_limits'])
def test_nonfinite_limits():
    x = np.arange(0.0, np.e, 0.01)
    olderr = np.seterr(divide='ignore')
    try:
        y = np.log(x)
    finally:
        np.seterr(**olderr)

    x[len(x) / 2] = np.nan
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)


@image_comparison(baseline_images=['imshow'], remove_text=True)
def test_imshow():
    N = 100
    x, y = np.indices((N, N))
    x -= N // 2
    y -= N // 2
    r = np.sqrt(x ** 2 + y ** 2 - x * y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(r)


@image_comparison(baseline_images=['imshow_clip'], tol=0.01)
def test_imshow_clip():
    N = 100
    x, y = np.indices((N, N))
    x -= N // 2
    y -= N // 2
    r = np.sqrt(x ** 2 + y ** 2 - x * y)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    c = ax.contour(r, [N / 4])
    x = c.collections[0]
    clipPath = x.get_paths()[0]
    clipTransform = x.get_transform()
    from matplotlib.transforms import TransformedPath
    clip_path = TransformedPath(clipPath, clipTransform)
    ax.imshow(r, clip_path=clip_path)


@image_comparison(baseline_images=['polycollection_joinstyle'], remove_text=True)
def test_polycollection_joinstyle():
    from matplotlib import collections as mcoll
    fig = plt.figure()
    ax = fig.add_subplot(111)
    verts = np.array([[1, 1], [1, 2], [2, 2], [2, 1]])
    c = mcoll.PolyCollection([verts], linewidths=40)
    ax.add_collection(c)
    ax.set_xbound(0, 3)
    ax.set_ybound(0, 3)


@image_comparison(baseline_images=['fill_between_interpolate'], tol=0.01, remove_text=True)
def test_fill_between_interpolate():
    x = np.arange(0.0, 2, 0.02)
    y1 = np.sin(2 * np.pi * x)
    y2 = 1.2 * np.sin(4 * np.pi * x)
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.plot(x, y1, x, y2, color='black')
    ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
    ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
    y2 = np.ma.masked_greater(y2, 1.0)
    ax1 = fig.add_subplot(212, sharex=ax)
    ax1.plot(x, y1, x, y2, color='black')
    ax1.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
    ax1.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)


@image_comparison(baseline_images=['symlog'])
def test_symlog():
    x = np.array([0, 1, 2, 4, 6, 9, 12, 24])
    y = np.array([1000000, 500000, 100000, 100, 5, 0, 0, 0])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_yscale('symlog')
    ax.set_xscale = 'linear'
    ax.set_ylim(-1, 10000000)


@image_comparison(baseline_images=['symlog2'], remove_text=True)
def test_symlog2():
    x = np.arange(-50, 50, 0.001)
    fig = plt.figure()
    ax = fig.add_subplot(511)
    ax.plot(x, x)
    ax.set_xscale('symlog', linthreshx=20.0)
    ax.grid(True)
    ax = fig.add_subplot(512)
    ax.plot(x, x)
    ax.set_xscale('symlog', linthreshx=2.0)
    ax.grid(True)
    ax = fig.add_subplot(513)
    ax.plot(x, x)
    ax.set_xscale('symlog', linthreshx=1.0)
    ax.grid(True)
    ax = fig.add_subplot(514)
    ax.plot(x, x)
    ax.set_xscale('symlog', linthreshx=0.1)
    ax.grid(True)
    ax = fig.add_subplot(515)
    ax.plot(x, x)
    ax.set_xscale('symlog', linthreshx=0.01)
    ax.grid(True)
    ax.set_ylim(-0.1, 0.1)


@image_comparison(baseline_images=['pcolormesh'], tol=0.02, remove_text=True)
def test_pcolormesh():
    n = 12
    x = np.linspace(-1.5, 1.5, n)
    y = np.linspace(-1.5, 1.5, n * 2)
    X, Y = np.meshgrid(x, y)
    Qx = np.cos(Y) - np.cos(X)
    Qz = np.sin(Y) + np.sin(X)
    Qx = Qx + 1.1
    Z = np.sqrt(X ** 2 + Y ** 2) / 5
    Z = (Z - Z.min()) / (Z.max() - Z.min())
    Zm = ma.masked_where(np.fabs(Qz) < 0.5 * np.amax(Qz), Z)
    fig = plt.figure()
    ax = fig.add_subplot(131)
    ax.pcolormesh(Qx, Qz, Z, lw=0.5, edgecolors='k')
    ax = fig.add_subplot(132)
    ax.pcolormesh(Qx, Qz, Z, lw=2, edgecolors=['b', 'w'])
    ax = fig.add_subplot(133)
    ax.pcolormesh(Qx, Qz, Z, shading='gouraud')


@image_comparison(baseline_images=['canonical'])
def test_canonical():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])


@image_comparison(baseline_images=['arc_ellipse'], remove_text=True)
def test_arc_ellipse():
    from matplotlib import patches
    xcenter, ycenter = (0.38, 0.52)
    width, height = (0.1, 0.3)
    angle = -30
    theta = np.arange(0.0, 360.0, 1.0) * np.pi / 180.0
    x = width / 2.0 * np.cos(theta)
    y = height / 2.0 * np.sin(theta)
    rtheta = angle * np.pi / 180.0
    R = np.array([
     [
      np.cos(rtheta), -np.sin(rtheta)],
     [
      np.sin(rtheta), np.cos(rtheta)]])
    x, y = np.dot(R, np.array([x, y]))
    x += xcenter
    y += ycenter
    fig = plt.figure()
    ax = fig.add_subplot(211, aspect='auto')
    ax.fill(x, y, alpha=0.2, facecolor='yellow', edgecolor='yellow', linewidth=1, zorder=1)
    e1 = patches.Arc((xcenter, ycenter), width, height, angle=angle, linewidth=2, fill=False, zorder=2)
    ax.add_patch(e1)
    ax = fig.add_subplot(212, aspect='equal')
    ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
    e2 = patches.Arc((xcenter, ycenter), width, height, angle=angle, linewidth=2, fill=False, zorder=2)
    ax.add_patch(e2)


@image_comparison(baseline_images=['units_strings'])
def test_units_strings():
    Id = [
     '50', '100', '150', '200', '250']
    pout = ['0', '7.4', '11.4', '14.2', '16.3']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(Id, pout)


@image_comparison(baseline_images=['markevery'], remove_text=True)
def test_markevery():
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.sqrt(x / 10 + 0.5)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o', label='default')
    ax.plot(x, y, 'd', markevery=None, label='mark all')
    ax.plot(x, y, 's', markevery=10, label='mark every 10')
    ax.plot(x, y, '+', markevery=(5, 20), label='mark every 5 starting at 10')
    ax.legend()
    return


@image_comparison(baseline_images=['markevery_line'], remove_text=True)
def test_markevery_line():
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.sqrt(x / 10 + 0.5)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, '-o', label='default')
    ax.plot(x, y, '-d', markevery=None, label='mark all')
    ax.plot(x, y, '-s', markevery=10, label='mark every 10')
    ax.plot(x, y, '-+', markevery=(5, 20), label='mark every 5 starting at 10')
    ax.legend()
    return


@image_comparison(baseline_images=['marker_edges'], remove_text=True)
def test_marker_edges():
    x = np.linspace(0, 1, 10)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, np.sin(x), 'y.', ms=30.0, mew=0, mec='r')
    ax.plot(x + 0.1, np.sin(x), 'y.', ms=30.0, mew=1, mec='r')
    ax.plot(x + 0.2, np.sin(x), 'y.', ms=30.0, mew=2, mec='b')


@image_comparison(baseline_images=['hist_log'], remove_text=True)
def test_hist_log():
    data0 = np.linspace(0, 1, 200) ** 3
    data = np.r_[(1 - data0, 1 + data0)]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(data, fill=False, log=True)


def contour_dat():
    x = np.linspace(-3, 5, 150)
    y = np.linspace(-3, 5, 120)
    z = np.cos(x) + np.sin(y[:, np.newaxis])
    return (x, y, z)


@image_comparison(baseline_images=['contour_hatching'])
def test_contour_hatching():
    x, y, z = contour_dat()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cs = ax.contourf(x, y, z, hatches=['-', '/', '\\', '//'], cmap=plt.get_cmap('gray'), extend='both', alpha=0.5)


@image_comparison(baseline_images=['contour_colorbar'])
def test_contour_colorbar():
    x, y, z = contour_dat()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cs = ax.contourf(x, y, z, levels=np.arange(-1.8, 1.801, 0.2), cmap=plt.get_cmap('RdBu'), vmin=-0.6, vmax=0.6, extend='both')
    cs1 = ax.contour(x, y, z, levels=np.arange(-2.2, -0.599, 0.2), colors=[
     'y'], linestyles='solid', linewidths=2)
    cs2 = ax.contour(x, y, z, levels=np.arange(0.6, 2.2, 0.2), colors=[
     'c'], linewidths=2)
    cbar = fig.colorbar(cs, ax=ax)
    cbar.add_lines(cs1)
    cbar.add_lines(cs2, erase=False)


@image_comparison(baseline_images=['hist2d'])
def test_hist2d():
    np.random.seed(0)
    x = np.random.randn(100) * 2 + 5
    y = np.random.randn(100) - 2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist2d(x, y, bins=10)


@image_comparison(baseline_images=['hist2d_transpose'])
def test_hist2d_transpose():
    np.random.seed(0)
    x = np.array([5] * 100)
    y = np.random.randn(100) - 2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist2d(x, y, bins=10)


@image_comparison(baseline_images=['scatter'])
def test_scatter_plot():
    ax = plt.axes()
    ax.scatter([3, 4, 2, 6], [2, 5, 2, 3], c=['r', 'y', 'b', 'lime'], s=[24, 15, 19, 29])


@cleanup
def test_as_mpl_axes_api():
    from matplotlib.projections.polar import PolarAxes
    import matplotlib.axes as maxes

    class Polar(object):

        def __init__(self):
            self.theta_offset = 0

        def _as_mpl_axes(self):
            return (
             PolarAxes, {'theta_offset': self.theta_offset})

    prj = Polar()
    prj2 = Polar()
    prj2.theta_offset = np.pi
    prj3 = Polar()
    ax = plt.axes([0, 0, 1, 1], projection=prj)
    assert type(ax) == PolarAxes, 'Expected a PolarAxes, got %s' % type(ax)
    ax_via_gca = plt.gca(projection=prj)
    assert ax_via_gca is ax
    plt.close()
    ax = plt.gca(projection=prj)
    assert type(ax) == maxes._subplot_classes[PolarAxes], 'Expected a PolarAxesSubplot, got %s' % type(ax)
    ax_via_gca = plt.gca(projection=prj)
    assert ax_via_gca is ax
    ax_via_gca = plt.gca(projection=prj2)
    assert ax_via_gca is not ax
    assert ax.get_theta_offset() == 0, ax.get_theta_offset()
    assert ax_via_gca.get_theta_offset() == np.pi, ax_via_gca.get_theta_offset()
    ax_via_gca = plt.gca(projection=prj3)
    assert ax_via_gca is ax
    plt.close()
    ax = plt.subplot(121, projection=prj)
    assert type(ax) == maxes._subplot_classes[PolarAxes], 'Expected a PolarAxesSubplot, got %s' % type(ax)
    plt.close()


@image_comparison(baseline_images=['log_scales'])
def test_log_scales():
    fig = plt.figure()
    ax = plt.gca()
    plt.plot(np.log(np.linspace(0.1, 100)))
    ax.set_yscale('log', basey=5.5)
    ax.set_xscale('log', basex=9.0)


@image_comparison(baseline_images=['stackplot_test_image'])
def test_stackplot():
    fig = plt.figure()
    x = np.linspace(0, 10, 10)
    y1 = 1.0 * x
    y2 = 2.0 * x + 1
    y3 = 3.0 * x + 2
    ax = fig.add_subplot(1, 1, 1)
    ax.stackplot(x, y1, y2, y3)
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 70))


@image_comparison(baseline_images=['boxplot'])
def test_boxplot():
    x = np.linspace(-7, 7, 140)
    x = np.hstack([-25, x, 25])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot([x, x], bootstrap=10000, usermedians=[None, 1.0], conf_intervals=[
     None, (-1.0, 3.5)], notch=1)
    ax.set_ylim((-30, 30))
    return


@image_comparison(baseline_images=['errorbar_basic',
 'errorbar_mixed'])
def test_errorbar():
    x = np.arange(0.1, 4, 0.5)
    y = np.exp(-x)
    yerr = 0.1 + 0.2 * np.sqrt(x)
    xerr = 0.1 + yerr
    fig = plt.figure()
    ax = fig.gca()
    ax.errorbar(x, y, xerr=0.2, yerr=0.4)
    ax.set_title('Simplest errorbars, 0.2 in x, 0.4 in y')
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
    ax = axs[(0, 0)]
    ax.errorbar(x, y, yerr=yerr, fmt='o')
    ax.set_title('Vert. symmetric')
    ax.locator_params(nbins=4)
    ax = axs[(0, 1)]
    ax.errorbar(x, y, xerr=xerr, fmt='o')
    ax.set_title('Hor. symmetric')
    ax = axs[(1, 0)]
    ax.errorbar(x, y, yerr=[yerr, 2 * yerr], xerr=[xerr, 2 * xerr], fmt='--o')
    ax.set_title('H, V asymmetric')
    ax = axs[(1, 1)]
    ax.set_yscale('log')
    ylower = np.maximum(0.01, y - yerr)
    yerr_lower = y - ylower
    ax.errorbar(x, y, yerr=[yerr_lower, 2 * yerr], xerr=xerr, fmt='o', ecolor='g', capthick=2)
    ax.set_title('Mixed sym., log y')
    fig.suptitle('Variable errorbars')


@image_comparison(baseline_images=['hist_stacked'])
def test_hist_stacked():
    d1 = np.linspace(0, 10, 50)
    d2 = np.linspace(1, 3, 20)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist((d1, d2), histtype='stepfilled', stacked=True)


@image_comparison(baseline_images=['hist_stacked_weights'])
def test_hist_stacked_weighted():
    d1 = np.linspace(0, 10, 50)
    d2 = np.linspace(1, 3, 20)
    w1 = np.linspace(0.01, 3.5, 50)
    w2 = np.linspace(0.05, 2.0, 20)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist((d1, d2), weights=(w1, w2), histtype='stepfilled', stacked=True)


@image_comparison(baseline_images=['transparent_markers'], remove_text=True)
def test_transparent_markers():
    np.random.seed(0)
    data = np.random.random(50)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data, 'D', mfc='none', markersize=100)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)