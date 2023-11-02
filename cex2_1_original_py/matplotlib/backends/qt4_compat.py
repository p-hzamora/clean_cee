# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: matplotlib\backends\qt4_compat.pyc
# Compiled at: 2012-08-28 11:32:46
""" A Qt API selector that can be used to switch between PyQt and PySide.
"""
import os
from matplotlib import rcParams, verbose
QT_API_PYQT = 'PyQt4'
QT_API_PYQTv2 = 'PyQt4v2'
QT_API_PYSIDE = 'PySide'
ETS = dict(pyqt=QT_API_PYQTv2, pyside=QT_API_PYSIDE)
QT_API_ENV = os.environ.get('QT_API')
if QT_API_ENV is not None:
    try:
        QT_API = ETS[QT_API_ENV]
    except KeyError:
        raise RuntimeError('Unrecognized environment variable %r, valid values are: %r or %r' % (
         QT_API_ENV, 'pyqt', 'pyside'))

else:
    QT_API = rcParams['backend.qt4']
_getSaveFileName = None
if QT_API in (QT_API_PYQT, QT_API_PYQTv2):
    import sip
    if QT_API == QT_API_PYQTv2:
        if QT_API_ENV == 'pyqt':
            cond = "Found 'QT_API=pyqt' environment variable. Setting PyQt4 API accordingly.\n"
        else:
            cond = 'PyQt API v2 specified.'
        try:
            sip.setapi('QString', 2)
        except:
            res = 'QString API v2 specification failed. Defaulting to v1.'
            verbose.report(cond + res, 'helpful')
            cond = ''

        try:
            sip.setapi('QVariant', 2)
        except:
            res = 'QVariant API v2 specification failed. Defaulting to v1.'
            verbose.report(cond + res, 'helpful')

    from PyQt4 import QtCore, QtGui
    QtCore.Signal = QtCore.pyqtSignal
    try:
        QtCore.Slot = QtCore.pyqtSlot
    except AttributeError:
        QtCore.Slot = pyqtSignature

    QtCore.Property = QtCore.pyqtProperty
    __version__ = QtCore.PYQT_VERSION_STR
    try:
        if sip.getapi('QString') > 1:
            _get_save = QtGui.QFileDialog.getSaveFileNameAndFilter
        else:
            _getSaveFileName = QtGui.QFileDialog.getSaveFileName
    except (AttributeError, KeyError):
        _getSaveFileName = QtGui.QFileDialog.getSaveFileName

else:
    from PySide import QtCore, QtGui, __version__, __version_info__
    if __version_info__ < (1, 0, 3):
        raise ImportError('Matplotlib backend_qt4 and backend_qt4agg require PySide >=1.0.3')
    _get_save = QtGui.QFileDialog.getSaveFileName
if _getSaveFileName is None:

    def _getSaveFileName(self, msg, start, filters, selectedFilter):
        return _get_save(self, msg, start, filters, selectedFilter)[0]