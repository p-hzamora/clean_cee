# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\oographics.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import hstack, ravel, isnan, asfarray, log10, array, isfinite, array, asarray
from openopt import __version__ as ooversion
ooversion = str(ooversion)
from setDefaultIterFuncs import stopcase

class Graphics:

    def __init__(self):
        self.drawFuncs = [
         self.oodraw]
        self.specifierStart = 'd'
        self.specifierFailed = 'x'
        self.specifierOK = 'p'
        self.specifierUndefined = 'o'
        self.specifierContinueFeasible = 'v'
        self.specifierContinueInfeasible = '>'
        self.specifierError = 's'
        self.REDUCE = 100000000.0
        self.axLineStyle = '-'
        self.axLineWidth = 2
        self.axMarker = ''
        self.axMarkerSize = 1
        self.markerEdgeWidth = 1
        self.axMarkerEdgeColor = 'b'
        self.axFaceColor = 'y'
        self.rate = 0.5
        self.drawingInOneWindow = True
        self.markerSize = 12
        self.iterMarkerSize = 1
        self.plotIterMarkers = True

    def oodraw(self, p):
        try:
            import pylab
        except:
            p.pWarn('to use OpenOpt graphics you need pylab (Python module) installed. Turning graphics off...')
            p.plot = 0
            return

        needNewFigure = not p.iter
        colors = [
         'b', 'k', 'c', 'r', 'g']
        specifiers = ['-', ':', '-.', '--']
        pylab.ion()
        if needNewFigure:
            self.colorCount = -1
            self.specifierCount = 0
            self.nTrajectories = 0
            self.ghandlers = []
            if p.probType in ('NLSP', 'SNLE'):
                Y_LABELS = [
                 'maxResidual']
            elif p.probType == 'NLLSP':
                Y_LABELS = [
                 'sum(residuals^2)']
            else:
                Y_LABELS = [
                 'objective function']
            isIterPointAlwaysFeasible = p.solver.__isIterPointAlwaysFeasible__ if type(p.solver.__isIterPointAlwaysFeasible__) == bool else p.solver.__isIterPointAlwaysFeasible__(p)
            if not (p._isUnconstrained() or isIterPointAlwaysFeasible):
                self.isMaxConstraintSubplotRequired = True
                if p.useScaledResidualOutput:
                    Y_LABELS.append('MaxConstraint/ConTol')
                else:
                    Y_LABELS.append('maxConstraint')
            else:
                self.isMaxConstraintSubplotRequired = False
            if self.isMaxConstraintSubplotRequired:
                self.nSubPlots = 2
            else:
                self.nSubPlots = 1
        isNewTrajectory = not p.iter
        if isNewTrajectory:
            self.colorCount += 1
            if self.drawingInOneWindow:
                if self.colorCount > len(colors) - 1:
                    self.colorCount = 0
                    self.specifierCount += 1
                    if self.specifierCount > len(specifiers) - 1:
                        p.warn('line types number exeeded')
                        self.specifierCount = 0
        color = p.color
        specifier = p.specifier
        tx = p.xlabel.lower()
        if isNewTrajectory:
            self.nTrajectories += 1
            pTitle = 'problem: ' + p.name
            if p.showGoal:
                pTitle += '       goal: ' + p.goal
            if self.nSubPlots > 1:
                pylab.subplot(self.nSubPlots, 1, 1)
            p.figure = pylab.gcf()
            pylab.title(pTitle)
            p.figure.canvas.set_window_title('OpenOpt ' + ooversion)
            if tx == 'cputime':
                xlabel = 'CPU Time elapsed (without graphic output), sec'
                d_x = 0.01
            elif tx == 'time':
                xlabel = 'Time elapsed (without graphic output), sec'
                d_x = 0.01
            elif tx in ('niter', 'iter'):
                xlabel = 'iter'
                d_x = 4
            elif tx == 'nf':
                xlabel = 'Number of objective function evaluations'
                d_x = 4
            else:
                p.err('unknown graphic output xlabel: "' + tx + '", should be in "time", "cputime", "iter", "nf"')
            self.nPointsPlotted = 0
            for ind in range(self.nSubPlots):
                if self.nSubPlots > 1 and ind != 0 or p.probType in ('NLSP', 'SNLE'):
                    ax = pylab.subplot(self.nSubPlots, 1, ind + 1)
                    ax.set_yscale('log')
                pylab.hold(1)
                pylab.grid(1)
                pylab.ylabel(Y_LABELS[ind])

            pylab.xlabel(xlabel)
        if p.iter > 0:
            IND_start, IND_end = self.nPointsPlotted - 1, p.iter + 1
        else:
            IND_start, IND_end = (0, 1)
        if p.plotOnlyCurrentMinimum:
            yy = array(p.iterValues.f[IND_start:])
            if isNewTrajectory:
                self.currMin = yy[0]
            k = 0
            for j in range(IND_start, IND_start + len(yy)):
                yy[k] = min(self.currMin, p.iterValues.f[j])
                self.currMin = yy[k]
                k += 1

            if IND_start <= IND_end:
                if len(p.iterValues.f) >= 1:
                    yySave = [
                     p.iterValues.f[-1]]
                else:
                    yySave = [
                     p.f(p.x0)]
        else:
            yy = array(p.iterValues.f[IND_start:IND_end])
            if IND_start <= IND_end:
                if len(p.iterValues.f) >= 1:
                    yySave = [p.iterValues.f[-1]]
                else:
                    yySave = [
                     p.f(p.x0)]
            if tx == 'iter':
                xx = range(IND_start, IND_end)
            elif tx == 'cputime':
                if len(p.iterTime) != len(p.cpuTimeElapsedForPlotting):
                    p.iterTime.append(p.iterTime[-1])
                xx = asfarray(p.iterCPUTime[IND_start:IND_end]) - asfarray(p.cpuTimeElapsedForPlotting[IND_start:IND_end])
            elif tx == 'time':
                if len(p.iterTime) != len(p.timeElapsedForPlotting):
                    p.iterTime.append(p.iterTime[-1])
                xx = asfarray(p.iterTime[IND_start:IND_end]) - asfarray(p.timeElapsedForPlotting[IND_start:IND_end])
            elif tx == 'nf':
                xx = asfarray(p.iterValues.nf[IND_start:IND_end])
            else:
                p.err('unknown labelX case')
            if len(xx) > len(yy):
                if p.isFinished:
                    xx = xx[:-1]
                else:
                    p.err('OpenOpt graphics ERROR - FIXME!')
            if p.probType in ('NLSP', 'SNLE'):
                yy = yy + p.ftol / self.REDUCE
            YY = [
             yy]
            if self.isMaxConstraintSubplotRequired:
                yy22 = p.contol / self.REDUCE + asfarray(p.iterValues.r[IND_start:IND_end])
                if p.useScaledResidualOutput:
                    yy22 /= p.contol
                YY.append(yy22)
                if IND_start <= IND_end:
                    if len(p.iterValues.r) == 0:
                        return
                    rr = p.iterValues.r[-1]
                    if p.useScaledResidualOutput:
                        rr /= p.contol
                    if len(p.iterValues.r) >= 1:
                        yySave.append(p.contol / self.REDUCE + asfarray(rr))
                    else:
                        yySave.append(p.contol / self.REDUCE + asfarray(p.getMaxResidual(p.x0)))
            if needNewFigure:
                if self.nSubPlots > 1:
                    pylab.subplot(2, 1, 2)
                    tmp = 1 if p.useScaledResidualOutput else p.contol
                    pylab.plot([xx[0]], [tmp / 31.622776601683793])
                    pylab.plot([xx[0] + d_x], [tmp / 31.622776601683793])
                    pylab.plot([xx[0]], [YY[1][0] * 10])
                    pylab.plot([xx[0] + d_x], [YY[1][0] * 10])
                    pylab.subplot(2, 1, 1)
                pylab.plot([xx[0]], [YY[0][0]])
                pylab.plot([xx[0] + d_x], [YY[0][0]])
            if self.plotIterMarkers:
                usualMarker = 'o'
            else:
                usualMarker = ''
            for ind in range(self.nSubPlots):
                if self.nSubPlots > 1:
                    pylab.subplot(self.nSubPlots, 1, ind + 1)
                yy2 = ravel(YY[ind])
                if len(yy2) < len(xx):
                    if IND_start > IND_end:
                        yy2 = ravel(yySave[ind])
                    else:
                        if yy2.size == 0:
                            yy2 = ravel(yySave[ind])
                        else:
                            yy2 = hstack((yy2, yy2[-1]))
                if isNewTrajectory:
                    if isfinite(p.xlim[0]):
                        pylab.plot([p.xlim[0]], [yy2[0]], color='w')
                    if isfinite(p.xlim[1]):
                        pylab.plot([p.xlim[1]], [yy2[0]], color='w')
                    if ind == 0:
                        if isfinite(p.ylim[0]):
                            pylab.plot([xx[0]], [p.ylim[0]], color='w')
                        if isfinite(p.ylim[1]):
                            pylab.plot([xx[0]], [p.ylim[1]], color='w')
                        if p.probType in ('NLSP', 'SNLE'):
                            pylab.plot([xx[0]], [p.ftol / self.REDUCE], color='w')
                if ind == 1:
                    horz_line_value = 1 if p.useScaledResidualOutput else p.primalConTol
                    pylab.plot([xx[0], xx[-1]], [horz_line_value, horz_line_value], ls=self.axLineStyle, linewidth=self.axLineWidth, color='g', marker=self.axMarker, ms=self.axMarkerSize, mew=self.markerEdgeWidth, mec=self.axMarkerEdgeColor, mfc=self.axFaceColor)
                elif p.probType in ('NLSP', 'SNLE'):
                    pylab.plot([xx[0], xx[-1]], [p.ftol, p.ftol], ls=self.axLineStyle, linewidth=self.axLineWidth, color='g', marker=self.axMarker, ms=self.axMarkerSize, mew=self.markerEdgeWidth, mec=self.axMarkerEdgeColor, mfc=self.axFaceColor)
                if isNewTrajectory:
                    p2 = pylab.plot([xx[0]], [yy2[0]], color=color, marker=self.specifierStart, markersize=self.markerSize)
                    p3 = pylab.plot([xx[0], xx[0] + 1e-50], [yy2[0], yy2[0]], color=color, markersize=self.markerSize)
                    p._p3 = p3
                    if p.legend == '':
                        pylab.legend([p3[0]], [p.solver.__name__], shadow=True)
                    elif type(p.legend) in (tuple, list):
                        pylab.legend([p3[0]], p.legend, shadow=True)
                    else:
                        pylab.legend([p3[0]], [p.legend], shadow=True)
                    pylab.plot(xx[1:], yy2[1:], color, marker=usualMarker, markersize=self.markerSize / 3)
                else:
                    pylab.plot(xx, ravel(yy2), color + specifier, marker=usualMarker, markersize=self.iterMarkerSize)
                if p.isFinished:
                    pylab.legend([p._p3[0]], [p.solver.__name__], shadow=True, loc=0)
                    if p.istop < 0:
                        if stopcase(p.istop) == 0:
                            if p.isFeas(p.xf):
                                s = self.specifierContinueFeasible
                            else:
                                s = self.specifierContinueInfeasible
                        else:
                            s = self.specifierFailed
                    elif p.isFeasible:
                        if p.istop > 0:
                            s = self.specifierOK
                        else:
                            s = self.specifierUndefined
                    else:
                        s = self.specifierError
                    if s == self.specifierOK:
                        marker = (5, 1, 0)
                    else:
                        marker = s
                    if isnan(yy2[-1]):
                        yy2[-1] = 0
                    pylab.scatter(ravel(xx[-1]), [yy2[-1]], c=color, marker=marker, s=[150])
                    xmin, xmax, ymin, ymax = pylab.axis()
                    if ymax - ymin > 25 * (yy2[-1] - ymin):
                        delta = 0.04 * (ymax - ymin)
                        pylab.scatter([(xmin + xmax) / 2, (xmin + xmax) / 2], [ymin - delta, ymax + delta], s=1, c='w', edgecolors='none', marker='o')
                        pylab.draw()
                    if ind == 0 and p.probType in ('NLSP', 'SNLE'):
                        pylab.plot([xmin, xmax], [log10(p.ftol), log10(p.ftol)], linewidth=self.axLineWidth, ls=self.axLineStyle, color='g', marker=self.axMarker, ms=self.axMarkerSize, mew=self.markerEdgeWidth, mec=self.axMarkerEdgeColor, mfc=self.axFaceColor)
                    if ind == 1:
                        horz_line_value = 0 if p.useScaledResidualOutput else log10(p.primalConTol)
                        pylab.plot([xmin, xmax], [horz_line_value, horz_line_value], linewidth=self.axLineWidth, ls=self.axLineStyle, color='g', marker=self.axMarker, ms=self.axMarkerSize, mew=self.markerEdgeWidth, mec=self.axMarkerEdgeColor, mfc=self.axFaceColor)
                        pylab.subplot(self.nSubPlots, 1, 1)
                        pylab.plot([xmax], [yy2[-1]], color='w')

        self.nPointsPlotted = p.iter + 1
        pylab.draw()