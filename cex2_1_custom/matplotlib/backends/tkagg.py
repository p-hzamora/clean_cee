# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\tkagg.pyc
# Compiled at: 2012-10-30 18:11:14
from __future__ import print_function
from matplotlib.backends import _tkagg
import Tkinter as Tk

def blit(photoimage, aggimage, bbox=None, colormode=1):
    tk = photoimage.tk
    if bbox is not None:
        bbox_array = bbox.__array__()
    else:
        bbox_array = None
    try:
        tk.call('PyAggImagePhoto', photoimage, id(aggimage), colormode, id(bbox_array))
    except Tk.TclError:
        try:
            try:
                _tkagg.tkinit(tk.interpaddr(), 1)
            except AttributeError:
                _tkagg.tkinit(id(tk), 0)

            tk.call('PyAggImagePhoto', photoimage, id(aggimage), colormode, id(bbox_array))
        except (ImportError, AttributeError, Tk.TclError):
            raise

    return


def test(aggimage):
    import time
    r = Tk.Tk()
    c = Tk.Canvas(r, width=aggimage.width, height=aggimage.height)
    c.pack()
    p = Tk.PhotoImage(width=aggimage.width, height=aggimage.height)
    blit(p, aggimage)
    c.create_image(aggimage.width, aggimage.height, image=p)
    blit(p, aggimage)
    while 1:
        r.update_idletasks()