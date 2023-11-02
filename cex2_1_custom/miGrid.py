# Embedded file name: miGrid.pyc
"""
Modulo: gridCopy.py

"""
import wx

class MyGrid(wx.grid.Grid):
    """
    Clase: MyGrid del modulo gridCopy.py
    
    
    """

    def __init__(self, parent, id, pos, size, style):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                parent:
                id:
                pos:
                size:
                style:
        """
        wx.grid.Grid.__init__(self, parent, id, pos, size, style)
        wx.EVT_KEY_DOWN(self, self.Key)
        self.traduccion = dict()

    def currentcell(self):
        """
        Metodo: currentcell
        
        
        """
        row = self.GetGridCursorRow()
        col = self.GetGridCursorCol()
        cell = (row, col)
        return cell

    def Key(self, event):
        """
        Metodo: Key
        
        
        ARGUMENTOS:
                event:
        """
        if event.ControlDown() and event.GetKeyCode() == 67:
            self.copy()
        if event.ControlDown() and event.GetKeyCode() == 86:
            self.paste()
        if event.GetKeyCode():
            event.Skip()
            return

    def copy(self):
        """
        Metodo: copy
        
        
        """
        data = ''
        for i in range(self.GetNumberRows()):
            for j in range(self.GetNumberCols()):
                if self.IsInSelection(i, j) == True:
                    data = data + self.GetCellValue(i, j) + '\t'
                else:
                    data = data + '\t'
                if j == self.GetNumberCols() - 1:
                    data = data + '\n'

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(data))
            wx.TheClipboard.Close()

    def paste(self):
        """
        Metodo: paste
        
        
        """
        if wx.TheClipboard.Open():
            a = wx.TextDataObject()
            wx.TheClipboard.GetData(a)
        filas = a.GetText().replace('\r', '')
        filas = filas.split('\n')
        columna = []
        for i in range(len(filas)):
            columna.append(filas[i].split('\t'))

        fil = 0
        col = 0
        for i in range(self.GetGridCursorRow(), self.GetNumberRows()):
            for j in range(self.GetGridCursorCol(), self.GetNumberCols()):
                try:
                    self.SetCellValue(i, j, columna[fil][col])
                    col = col + 1
                except IndexError:
                    break

            fil = fil + 1
            col = 0

    def SetCellValue(self, fila, columna, stringSinTraducir):
        """Seleccion me llega en castellano,
        tengo que elegir entre las opciones que est\xe1n traducidas         
        """
        traduccionInversa = dict(((v, k) for k, v in self.traduccion.iteritems()))
        if stringSinTraducir == u'':
            seleccionTraducida = u''
        elif stringSinTraducir in traduccionInversa:
            seleccionTraducida = traduccionInversa[stringSinTraducir]
        else:
            seleccionTraducida = stringSinTraducir
        super(MyGrid, self).SetCellValue(fila, columna, seleccionTraducida)

    def GetCellValue(self, fila, columna):
        stringTraducida = super(MyGrid, self).GetCellValue(fila, columna)
        if stringTraducida in self.traduccion.keys():
            strinSinTraducir = self.traduccion[stringTraducida]
            return strinSinTraducir
        else:
            return stringTraducida

    def ampliaDiccionarioTraduccion(self, nuevoDiccionario):
        """Cada vez que se incorpora un miChoiceGrid a esta tabla, hay que actualizar el 
        diccionario de traducci\xf3n de la tabla, con las traducciones presentes en miChoiceGrid """
        for k in nuevoDiccionario.keys():
            self.traduccion[k] = nuevoDiccionario[k]