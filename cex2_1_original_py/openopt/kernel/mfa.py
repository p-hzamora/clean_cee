# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: openopt\kernel\mfa.pyc
# Compiled at: 2012-12-08 11:04:59
from numpy import inf, copy, floor, log10, asfarray, asscalar, argsort
TkinterIsInstalled = True
try:
    from Tkinter import Tk, Button, Entry, Label, Frame, StringVar, DISABLED, END, IntVar, Radiobutton, Canvas
    from tkFileDialog import asksaveasfilename, askopenfile
    from tkMessageBox import showerror
except ImportError:
    TkinterIsInstalled = False

xtolScaleFactor = 1e-05

class mfa():
    filename = None
    x0 = None
    solved = False

    def startSession(self):
        assert TkinterIsInstalled, '\n        Tkinter is not installed. \n        If you have Linux you could try using \n        "apt-get install python-tk"'
        try:
            import nlopt
        except ImportError:
            s = '\n            To use OpenOpt multifactor analysis tool \n            you should have nlopt with its Python API installed,\n            see http://openopt.org/nlopt'
            print s
            showerror('OpenOpt', s)
            raw_input()
            return

        import os
        hd = os.getenv('HOME')
        self.hd = hd
        root = Tk()
        self.root = root
        from openopt import __version__ as oover
        root.wm_title(' OpenOpt %s Multifactor analysis tool for experiment planning ' % oover)
        SessionSelectFrame = Frame(root)
        SessionSelectFrame.pack(side='top', padx=230, ipadx=40, fill='x', expand=True)
        var = StringVar()
        var.set('asdf')
        Radiobutton(SessionSelectFrame, variable=var, text='New', indicatoron=0, command=(lambda : (
         SessionSelectFrame.destroy(), self.create()))).pack(side='top', fill='x', pady=5)
        Radiobutton(SessionSelectFrame, variable=var, text='Load', indicatoron=0, command=(lambda : self.load(SessionSelectFrame))).pack(side='top', fill='x', pady=5)
        root.protocol('WM_DELETE_WINDOW', self.exit)
        root.mainloop()
        self.exit()

    def create(self, S={}):
        root = self.root
        RootFrame = Canvas(root)
        RootFrame.pack()
        self.NameEntriesList, self.LB_EntriesList, self.UB_EntriesList, self.TolEntriesList, self.ValueEntriesList = ([], [], [], [], [])
        self.calculated_points = S.get('calculated_points', [])
        C = Canvas(root)
        Frame(RootFrame).pack(ipady=4)
        UpperFrame = Frame(RootFrame)
        ProjectNameFrame = Frame(UpperFrame)
        Label(ProjectNameFrame, text='Project name:').pack(side='left')
        ProjectNameEntry = Entry(ProjectNameFrame)
        ProjectNameEntry.pack(side='left')
        self.ProjectNameEntry = ProjectNameEntry
        ProjectNameFrame.pack(side='left')
        GoalSelectFrame = Frame(UpperFrame, relief='ridge', bd=2)
        GoalSelectText = StringVar(value='Goal:')
        Label(GoalSelectFrame, textvariable=GoalSelectText).pack(side='left')
        goal = StringVar()
        r1 = Radiobutton(GoalSelectFrame, text='Minimum', value='min', variable=goal)
        r1.pack(side='left')
        r2 = Radiobutton(GoalSelectFrame, text='Maximum', value='max', variable=goal)
        r2.pack(side='left')
        goal.set('min')
        GoalSelectFrame.pack(side='left', padx=10)
        self.goal = goal
        ObjectiveToleranceFrame = Frame(UpperFrame, relief='ridge', bd=2)
        ObjectiveToleranceFrame.pack(side='left')
        Label(ObjectiveToleranceFrame, text='Objective function tolerance:').pack(side='left')
        ObjTolEntry = Entry(ObjectiveToleranceFrame)
        ObjTolEntry.pack(side='left')
        self.ObjTolEntry = ObjTolEntry
        UpperFrame.pack(side='top', expand=True, fill='x')
        varsRoot = Frame(RootFrame)
        LowerFrame = Frame(varsRoot)
        LowerFrame.pack(side='bottom', expand=True, fill='x')
        from webbrowser import open_new_tab
        About = Button(LowerFrame, text='About', command=(lambda : open_new_tab('http://openopt.org/MultiFactorAnalysis')))
        About.pack(side='left')
        SaveButton = Button(LowerFrame, text='Save', command=self.save)
        SaveButton.pack(side='left', padx=15)
        SaveAsButton = Button(LowerFrame, text='Save As ...', command=self.save)
        SaveAsButton.pack(side='left')
        Write_xls_Button = Button(LowerFrame, text='Write xls report', command=self.write_xls_report)
        Write_xls_Button.pack(side='left', padx=15)
        ExperimentNumber = IntVar()
        ExperimentNumber.set(1)
        self.ExperimentNumber = ExperimentNumber
        ObjVal = StringVar()
        ObjEntry = Entry(LowerFrame, textvariable=ObjVal)
        self.ObjEntry = ObjEntry
        NN = StringVar(LowerFrame)
        NN_Label = Label(LowerFrame, textvariable=NN)
        names, lbs, ubs, tols, currValues = (
         Frame(varsRoot), Frame(varsRoot), Frame(varsRoot), Frame(varsRoot), Frame(varsRoot))
        Label(names, text=' Variable Name ').pack(side='top')
        Label(lbs, text=' Lower Bound ').pack(side='top')
        Label(ubs, text=' Upper Bound ').pack(side='top')
        Label(tols, text=' Tolerance ').pack(side='top')
        ValsColumnName = StringVar()
        ValsColumnName.set(' Initial Point ')
        Label(currValues, textvariable=ValsColumnName).pack(side='top')
        self.ValsColumnName = ValsColumnName
        CommandsRoot = Frame(RootFrame)
        CommandsRoot.pack(side='right', expand=False, fill='y')
        AddVar = Button(CommandsRoot, text='Add Variable', command=(lambda : self.addVar(names, lbs, ubs, tols, currValues)))
        AddVar.pack(side='top', fill='x')
        Next = Button(CommandsRoot, text='Next', command=(lambda : ExperimentNumber.set(ExperimentNumber.get() + 1)))
        names.pack(side='left', ipady=5)
        lbs.pack(side='left', ipady=5)
        ubs.pack(side='left', ipady=5)
        tols.pack(side='left', ipady=5)
        currValues.pack(side='left', ipady=5)
        varsRoot.pack()
        Start = Button(CommandsRoot, text='Start', command=(lambda : (
         Start.destroy(),
         Next.pack(side='bottom', fill='x'),
         r1.config(state=DISABLED),
         r2.config(state=DISABLED),
         ObjTolEntry.config(state=DISABLED),
         ObjEntry.pack(side='right', ipady=4),
         NN_Label.pack(side='right'),
         self.startOptimization(root, varsRoot, AddVar, currValues, ValsColumnName, ObjEntry, ExperimentNumber, Next, NN, goal.get(), float(ObjTolEntry.get()), C))))
        Start.pack(side='bottom', fill='x')
        self.Start = Start
        if len(S) != 0:
            for i in range(len(S['names'])):
                tmp = S['values'][i] if self.x0 is None else self.x0.split(' ')[i]
                self.addVar(names, lbs, ubs, tols, currValues, S['names'][i], S['lbs'][i], S['ubs'][i], S['tols'][i], tmp)

        else:
            self.addVar(names, lbs, ubs, tols, currValues)
        return

    def addVar(self, names, lbs, ubs, tols, currValues, _name='', _lb='', _ub='', _tol='', _val=''):
        nameEntry, lb, ub, tol, valEntry = (
         Entry(names), Entry(lbs), Entry(ubs), Entry(tols), Entry(currValues))
        nameEntry.insert(0, _name)
        lb.insert(0, _lb)
        ub.insert(0, _ub)
        tol.insert(0, _tol)
        valEntry.insert(0, _val)
        self.NameEntriesList.append(nameEntry)
        self.LB_EntriesList.append(lb)
        self.UB_EntriesList.append(ub)
        self.TolEntriesList.append(tol)
        self.ValueEntriesList.append(valEntry)
        nameEntry.pack(side='top')
        lb.pack(side='top')
        ub.pack(side='top')
        tol.pack(side='top')
        valEntry.pack(side='top')

    def startOptimization(self, root, varsRoot, AddVar, currValues, ValsColumnName, ObjEntry, ExperimentNumber, Next, NN, goal, objtol, C):
        AddVar.destroy()
        ValsColumnName.set('Experiment parameters')
        n = len(self.NameEntriesList)
        Names, Lb, Ub, Tol, x0 = ([], [], [], [], [])
        for i in range(n):
            N, L, U, T, valEntry = (self.NameEntriesList[i], self.LB_EntriesList[i], self.UB_EntriesList[i], self.TolEntriesList[i], self.ValueEntriesList[i])
            N.config(state=DISABLED)
            L.config(state=DISABLED)
            U.config(state=DISABLED)
            T.config(state=DISABLED)
            name, lb, ub, tol, val = (
             N.get(), L.get(), U.get(), T.get(), valEntry.get())
            Names.append(name)
            x0.append(float(val))
            Lb.append(float(lb) if lb != '' else -inf)
            Ub.append(float(ub) if ub != '' else inf)
            Tol.append(float(tol) if tol != '' else 0)

        x0, Tol, Lb, Ub = (asfarray(x0), asfarray(Tol), asfarray(Lb), asfarray(Ub))
        x0 *= xtolScaleFactor / Tol
        from openopt import NLP, oosolver
        p = NLP(objective, x0, lb=Lb * xtolScaleFactor / Tol, ub=Ub * xtolScaleFactor / Tol)
        self.prob = p
        p.args = (
         Tol, self, ObjEntry, p, root, ExperimentNumber, Next, NN, objtol, C)
        solver = oosolver('bobyqa', useStopByException=False)
        p.solve(solver, iprint=1, goal=goal)
        self.solved = True
        if p.stopcase >= 0:
            self.ValsColumnName.set('Best parameters')
            NN.set('Best obtained objective value:')
        Next.destroy()
        calculated_items = self.calculated_points.items() if isinstance(self.calculated_points, dict) else self.calculated_points
        vals = [ calculated_items[i][1] for i in range(len(calculated_items)) ]
        ind = argsort(vals)
        j = ind[0] if goal == 'min' else ind[-1]
        key, val = calculated_items[j]
        text_coords = key.split(' ')
        for i in range(len(self.ValueEntriesList)):
            self.ValueEntriesList[i].delete(0, END)
            self.ValueEntriesList[i].insert(0, text_coords[i])

        ObjEntry.delete(0, END)
        obj_tol = self.ObjTolEntry.get()
        val = float(val) * 10000.0 * objtol
        ObjEntry.insert(0, str(val))
        ObjEntry.config(state=DISABLED)

    def Plot(C, p):
        pass

    def load(self, SessionSelectFrame):
        file = askopenfile(defaultextension='.pck', initialdir=self.hd, filetypes=[('Python pickle files', '.pck')])
        if file in (None, ''):
            return
        else:
            SessionSelectFrame.destroy()
            import pickle
            S = pickle.load(file)
            if type(S['calculated_points']) == dict:
                S['calculated_points'] = S['calculated_points'].items()
            self.x0 = S.get('x0', None)
            self.create(S)
            self.ObjTolEntry.insert(0, S['ObjTol'])
            self.ProjectNameEntry.insert(0, S.get('ProjectName', ''))
            self.goal.set(S['goal'])
            self.ExperimentNumber.set(len(self.calculated_points))
            if len(S['calculated_points']) != 0:
                self.Start.invoke()
            return

    def save_as(self, filename=None):
        if filename is None:
            filename = asksaveasfilename(defaultextension='.pck', initialdir=self.hd, filetypes=[('Python pickle files', '.pck')])
        if filename in (None, ''):
            return
        else:
            if not self.solved and self.ObjEntry.get() != '':
                s = 'For the sake of more safety and some other circumstances saving with non-empty objective entry is forbidden'
                print s
                showerror('OpenOpt', s)
                return
            self.filename = filename
            names = [ s.get() for s in self.NameEntriesList ]
            lbs = [ s.get() for s in self.LB_EntriesList ]
            ubs = [ s.get() for s in self.UB_EntriesList ]
            tols = [ s.get() for s in self.TolEntriesList ]
            values = [ s.get() for s in self.ValueEntriesList ]
            goal = self.goal.get()
            ObjTol = self.ObjTolEntry.get()
            calculated_points = self.calculated_points
            ProjectName = self.ProjectNameEntry.get()
            S = {'names': names, 'lbs': lbs, 'ubs': ubs, 'tols': tols, 'values': values, 'goal': goal, 'ObjTol': ObjTol, 
               'calculated_points': calculated_points, 'ProjectName': ProjectName, 'x0': self.x0}
            file = open(filename, 'w')
            import pickle
            pickle.dump(S, file)
            file.close()
            return

    save = lambda self: self.save_as(self.filename)

    def write_xls_report(self):
        try:
            import xlwt
        except ImportError:
            s = 'To create xls reports \n            you should have xlwt installed, \n            see http://www.python-excel.org/\n            you could use easy_install xlwt (with admin rights)\n            also, in Linux you could use \n            [sudo] aptitude install python-xlwt\n            '
            print s
            showerror('OpenOpt', s)
            return

        xls_file = asksaveasfilename(defaultextension='.xls', initialdir=self.hd, filetypes=[('xls files', '.xls')])
        if xls_file in (None, ''):
            return
        else:
            wb = xlwt.Workbook()
            ws = wb.add_sheet('OpenOpt factor analysis report')
            ws.write(0, 0, 'Name')
            ws.write(0, 1, self.ProjectNameEntry.get())
            ws.write(1, 0, 'Goal')
            ws.write(1, 1, self.goal.get() + 'imum')
            ws.write(2, 0, 'Objective Tolerance')
            ws.write(2, 1, self.ObjTolEntry.get())
            names = [ s.get() for s in self.NameEntriesList ]
            lbs = [ s.get() for s in self.LB_EntriesList ]
            ubs = [ s.get() for s in self.UB_EntriesList ]
            tols = [ s.get() for s in self.TolEntriesList ]
            ws.write(4, 0, 'Variable')
            ws.write(5, 0, 'Lower Bound')
            ws.write(6, 0, 'Upper Bound')
            ws.write(7, 0, 'Tolerance')
            for i in range(len(names)):
                ws.write(4, i + 1, names[i])
                ws.write(5, i + 1, float(lbs[i]))
                ws.write(6, i + 1, float(ubs[i]))
                ws.write(7, i + 1, float(tols[i]))

            ws.write(9, 0, 'Exp Number')
            ws.write(9, len(names) + 1, 'Objective')
            CP = self.calculated_points
            if isinstance(CP, dict):
                CP = CP.items()
            for i in range(len(CP)):
                key, val = CP[i]
                ws.write(10 + i, 0, i + 1)
                coords = key.split()
                for j, coordVal in enumerate(coords):
                    ws.write(10 + i, j + 1, float(coordVal))

                ws.write(10 + i, len(coords) + 1, float(val))

            wb.save(xls_file)
            return

    def exit(self):
        try:
            self.root.quit()
        except:
            pass

        try:
            self.root.destroy()
        except:
            pass


def objective(x, Tol, mfa, ObjEntry, p, root, ExperimentNumber, Next, NN, objtol, C):
    Key = ''
    Values = []
    ValueEntriesList = mfa.ValueEntriesList
    calculated_points = mfa.calculated_points
    for i in range(x.size):
        Format = '%0.9f' if Tol[i] == 0 else '%0.' + '%d' % -floor(log10(Tol[i])) + 'f' if Tol[i] < 1 else '%d'
        tmp = x[i] * Tol[i] / xtolScaleFactor
        key = Format % tmp
        Key += key + ' '
        Values.append(key)

    if mfa.x0 is None:
        mfa.x0 = Key
    if Key in dict(calculated_points):
        return dict(calculated_points)[Key]
    else:
        for i in range(x.size):
            ValueEntriesList[i].delete(0, END)
            ValueEntriesList[i].insert(0, Values[i])

        NN.set('Enter experiment %i result:' % int(len(calculated_points) + 1))
        ObjEntry.delete(0, END)
        root.wait_variable(ExperimentNumber)
        r = float(ObjEntry.get())
        r *= 0.0001 / objtol
        if isinstance(calculated_points, list):
            calculated_points.append((Key, asscalar(copy(r))))
        else:
            calculated_points[Key] = asscalar(copy(r))
        return r


MFA = lambda : mfa().startSession()
if __name__ == '__main__':
    MFA()