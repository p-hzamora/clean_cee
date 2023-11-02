# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: scipy\cluster\__init__.pyc
# Compiled at: 2013-02-16 13:27:30
"""
=========================================
Clustering package (:mod:`scipy.cluster`)
=========================================

.. currentmodule:: scipy.cluster

:mod:`scipy.cluster.vq`

Clustering algorithms are useful in information theory, target detection,
communications, compression, and other areas.  The `vq` module only
supports vector quantization and the k-means algorithms.

:mod:`scipy.cluster.hierarchy`

The `hierarchy` module provides functions for hierarchical and
agglomerative clustering.  Its features include generating hierarchical
clusters from distance matrices, computing distance matrices from
observation vectors, calculating statistics on clusters, cutting linkages
to generate flat clusters, and visualizing clusters with dendrograms.

"""
from __future__ import division, print_function, absolute_import
__all__ = [
 'vq', 'hierarchy']
from . import vq, hierarchy
from numpy.testing import Tester
test = Tester().test