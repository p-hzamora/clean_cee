# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\tests\test_pickle.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
import numpy as np
from matplotlib.testing.decorators import cleanup, image_comparison
import matplotlib.pyplot as plt
from nose.tools import assert_equal, assert_not_equal
import cPickle as pickle
from io import BytesIO

def depth_getter(obj, current_depth=0, depth_stack=None, nest_info='top level object'):
    """
    Returns a dictionary mapping:

        id(obj): (shallowest_depth, obj, nest_info)

    for the given object (and its subordinates).

    This, in conjunction with recursive_pickle, can be used to debug
    pickling issues, although finding others is sometimes a case of
    trial and error.

    """
    if depth_stack is None:
        depth_stack = {}
    if id(obj) in depth_stack:
        stack = depth_stack[id(obj)]
        if stack[0] > current_depth:
            del depth_stack[id(obj)]
        else:
            return depth_stack
    depth_stack[id(obj)] = (
     current_depth, obj, nest_info)
    if isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            depth_getter(item, current_depth=current_depth + 1, depth_stack=depth_stack, nest_info='list/tuple item #%s in (%s)' % (i, nest_info))

    else:
        if isinstance(obj, dict):
            state = obj
        else:
            if hasattr(obj, '__getstate__'):
                state = obj.__getstate__()
                if not isinstance(state, dict):
                    state = {}
            elif hasattr(obj, '__dict__'):
                state = obj.__dict__
            else:
                state = {}
            for key, value in state.iteritems():
                depth_getter(value, current_depth=current_depth + 1, depth_stack=depth_stack, nest_info='attribute "%s" in (%s)' % (key, nest_info))

    return depth_stack


def recursive_pickle(top_obj):
    """
    Recursively pickle all of the given objects subordinates, starting with
    the deepest first. **Very** handy for debugging pickling issues, but
    also very slow (as it literally pickles each object in turn).

    Handles circular object references gracefully.

    """
    objs = depth_getter(top_obj)
    objs = sorted(objs.itervalues(), key=(lambda val: (-val[0], val[2])))
    for _, obj, location in objs:
        try:
            pickle.dump(obj, BytesIO(), pickle.HIGHEST_PROTOCOL)
        except Exception as err:
            print(obj)
            print('Failed to pickle %s. \n Type: %s. Traceback follows:' % (location, type(obj)))
            raise


@cleanup
def test_simple():
    fig = plt.figure()
    pickle.dump(fig, BytesIO(), pickle.HIGHEST_PROTOCOL)
    ax = plt.subplot(121)
    pickle.dump(ax, BytesIO(), pickle.HIGHEST_PROTOCOL)
    ax = plt.axes(projection='polar')
    plt.plot(range(10), label='foobar')
    plt.legend()
    pickle.dump(ax, BytesIO(), pickle.HIGHEST_PROTOCOL)


@image_comparison(baseline_images=['multi_pickle'], extensions=[
 'png'], remove_text=True)
def test_complete():
    fig = plt.figure('Figure with a label?', figsize=(10, 6))
    plt.suptitle('Can you fit any more in a figure?')
    x, y = np.arange(8), np.arange(10)
    data = u = v = np.linspace(0, 10, 80).reshape(10, 8)
    v = np.sin(v * -0.6)
    plt.subplot(3, 3, 1)
    plt.plot(range(10))
    plt.subplot(3, 3, 2)
    plt.contourf(data, hatches=['//', 'ooo'])
    plt.colorbar()
    plt.subplot(3, 3, 3)
    plt.pcolormesh(data)
    plt.subplot(3, 3, 4)
    plt.imshow(data)
    plt.subplot(3, 3, 5)
    plt.pcolor(data)
    plt.subplot(3, 3, 6)
    plt.streamplot(x, y, u, v)
    plt.subplot(3, 3, 7)
    plt.quiver(x, y, u, v)
    plt.subplot(3, 3, 8)
    plt.scatter(x, x ** 2, label='$x^2$')
    plt.legend(loc='upper left')
    plt.subplot(3, 3, 9)
    plt.errorbar(x, x * -0.5, xerr=0.2, yerr=0.4)
    result_fh = BytesIO()
    pickle.dump(fig, result_fh, pickle.HIGHEST_PROTOCOL)
    plt.close('all')
    assert_equal(plt._pylab_helpers.Gcf.figs, {})
    result_fh.seek(0)
    fig = pickle.load(result_fh)
    assert_not_equal(plt._pylab_helpers.Gcf.figs, {})
    assert_equal(fig.get_label(), 'Figure with a label?')


def test_no_pyplot():
    import pickle as p
    from matplotlib.backends.backend_pdf import FigureCanvasPdf as fc
    from matplotlib.figure import Figure
    fig = Figure()
    can = fc(fig)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([1, 2, 3], [1, 2, 3])
    pickle.dump(fig, BytesIO(), pickle.HIGHEST_PROTOCOL)