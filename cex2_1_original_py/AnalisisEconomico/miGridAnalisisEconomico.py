# File: m (Python 2.7)

__doc__ = '\nModulo: gridCopy1.py\nModulo que implementa la tabla que se muestra en panelCosteMedidas\n'
import wx
import logging

class MyGrid(wx.grid.Grid):
    '''
    Clase: MyGrid del modulo gridCopy1.py
    Clase que hereda de wx.grid.Grid y que le a\xf1ade la funcionalidad de poder copiar y pegar en sus campos

    '''
    
    def __init__(self, parent, id, pos, size, style):
        '''
        Constructor de la clase


        ARGUMENTOS:
    \t\tparent: instancia del panel al que pertenece
    \t\tid: identificador num\xe9rico (entero)
    \t\tpos: posicion que ocupa en coordenadas x,y (enteros)
    \t\tsize: tama\xf1o en notaci\xf3n x,y (enteros)
    \t\tstyle: estilo(wx.grid.Grid styles)
        '''
        wx.grid.Grid.__init__(self, parent, id, pos, size, style)
        wx.EVT_KEY_DOWN(self, self.Key)

    
    def currentcell(self):
        '''
        Metodo: currentcell
        funci\xf3n que devuelve en notaci\xf3n (x,y) la celda que est\xe1 seleccionada  
        
        '''
        row = self.GetGridCursorRow()
        col = self.GetGridCursorCol()
        cell = (row, col)
        return cell

    
    def Key(self, event):
        '''
        Metodo: Key
        Manejador del evento de que el usuario pulse alguna tecla de teclado

        ARGUMENTOS:
    \t\tevent: Instancia de la clase manejadora del evento de que el usuario pulse una tecla
        '''
        if event.ControlDown() and event.GetKeyCode() == 67:
            self.copy()
        if event.GetKeyCode():
            event.Skip()
            return None

    
    def copy(self):
        '''
        Metodo: copy
        funci\xf3n que copia en las celdas correspondientes lo almacenado en el clipboard

        '''
        data = ''
        casillas = []
        for i in range(self.GetNumberRows()):
            for j in range(self.GetNumberCols()):
                if self.IsInSelection(i, j) == True:
                    casillas.append((i, j))
                    continue
        
        for i in range(len(casillas)):
            data = data + self.GetCellValue(casillas[i][0], casillas[i][1])
            
            try:
                if casillas[i][0] == casillas[i + 1][0]:
                    data = data + '\t'
                else:
                    data = data + '\n'
            continue
            logging.info(u'Excepcion en: %s' % __name__)
            continue

        
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(data))
            wx.TheClipboard.Close()


