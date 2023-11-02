# Embedded file name: Envolvente\panelPuentesTermicosPorDefecto.pyc
"""
Modulo: panelPuentesTermicosPorDefecto.py

"""
import wx
import Envolvente.tablasValores as tablasValores
import Envolvente.dialogoCargarPT as dialogoCargarPT
import directorios
Directorio = directorios.BuscaDirectorios().Directorio
wxID_PANEL1, wxID_PANEL1CHECKBOX1, wxID_PANEL1CHECKBOX2, wxID_PANEL1CHECKBOX3, wxID_PANEL1CHECKBOX4, wxID_PANEL1CHECKBOX5, wxID_PANEL1CHECKBOX6, wxID_PANEL1CHECKBOX7, wxID_PANEL1CHECKBOX9, wxID_PANEL1CHECKBOX10, wxID_PANEL1CHECKBOX11, wxID_PANEL1CARGARBOTON, wxID_PANEL1BORRARBOTON, wxID_PANEL1DEFINIR, wxID_PANEL1PANEL1 = [ wx.NewId() for _init_ctrls in range(15) ]

class panelPuentesTermicosPorDefecto(wx.Panel):
    """
    Clase: panelPuentesTermicosPorDefecto del modulo panelPuentesTermicosPorDefecto.py
    
    
    """

    def _init_ctrls(self, prnt, ide, posi, siz, styl, nam):
        """
        Metodo: _init_ctrls
        
        
        ARGUMENTOS:
                 prnt:
                ide:
                 posi:
                 siz:
                 styl:
                 nam:
        """
        wx.Panel.__init__(self, id=ide, name=nam, parent=prnt, pos=posi, size=siz, style=styl)
        self.SetBackgroundColour('white')
        self.DefinirPTDefectoLineaText = wx.StaticBox(id=wxID_PANEL1DEFINIR, label=_(u'Definir puentes t\xe9rmicos por defecto'), name='LineaText', parent=self, pos=wx.Point(0, 16), size=wx.Size(710, 326), style=0)
        self.DefinirPTDefectoLineaText.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Tahoma'))
        self.DefinirPTDefectoLineaText.SetForegroundColour(wx.Colour(0, 0, 100))
        self.pilarEnFachada = wx.CheckBox(id=wxID_PANEL1CHECKBOX1, label=_(u'Pilar integrado en fachada'), name='pilarEnFachada', parent=self, pos=wx.Point(15, 42), size=wx.Size(400, 13), style=0)
        self.pilarEnFachada.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX1)
        self.pilarEnEsquina = wx.CheckBox(id=wxID_PANEL1CHECKBOX2, label=_(u'Pilar en esquina'), name='pilarEnEsquina', parent=self, pos=wx.Point(15, 66), size=wx.Size(400, 13), style=0)
        self.pilarEnEsquina.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX2)
        self.contornoDeHueco = wx.CheckBox(id=wxID_PANEL1CHECKBOX3, label=_(u'Contorno de hueco'), name='contornoDeHueco', parent=self, pos=wx.Point(15, 90), size=wx.Size(400, 13), style=0)
        self.contornoDeHueco.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX3)
        self.cajaPersiana = wx.CheckBox(id=wxID_PANEL1CHECKBOX4, label=_(u'Caja de persiana'), name='cajaPersiana', parent=self, pos=wx.Point(15, 114), size=wx.Size(400, 13), style=0)
        self.cajaPersiana.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX4)
        self.fachadaConForjado = wx.CheckBox(id=wxID_PANEL1CHECKBOX5, label=_(u'Encuentro de fachada con forjado'), name='fachadaConForjado', parent=self, pos=wx.Point(15, 138), size=wx.Size(400, 13), style=0)
        self.fachadaConForjado.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX5)
        self.fachadaConCubierta = wx.CheckBox(id=wxID_PANEL1CHECKBOX7, label=_(u'Encuentro de fachada con cubierta'), name='fachadaConCubierta', parent=self, pos=wx.Point(15, 162), size=wx.Size(400, 13), style=0)
        self.fachadaConCubierta.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX7)
        self.fachadaConSuelo = wx.CheckBox(id=wxID_PANEL1CHECKBOX9, label=_(u'Encuentro de fachada con suelo en contacto con el aire'), name='fachadaConSuelo', parent=self, pos=wx.Point(15, 186), size=wx.Size(400, 13), style=0)
        self.fachadaConSuelo.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX9)
        self.fachadaConSolera = wx.CheckBox(id=wxID_PANEL1CHECKBOX10, label=_(u'Encuentro de fachada con solera'), name='fachadaConSolera', parent=self, pos=wx.Point(15, 210), size=wx.Size(400, 13), style=0)
        self.fachadaConSolera.Bind(wx.EVT_CHECKBOX, self.onCheckBoxes, id=wxID_PANEL1CHECKBOX10)
        self.cargarBoton = wx.Button(id=wxID_PANEL1CARGARBOTON, label=_(u'Cargar'), name=u'cargarBoton', parent=self, pos=wx.Point(15, 311), size=wx.Size(80, 21), style=0)
        self.cargarBoton.Bind(wx.EVT_BUTTON, self.OnCargarButton, id=wxID_PANEL1CARGARBOTON)
        self.borrarBoton = wx.Button(id=wxID_PANEL1BORRARBOTON, label=_(u'Borrar'), name=u'borrarBoton', parent=self, pos=wx.Point(125, 311), size=wx.Size(80, 21), style=0)
        self.borrarBoton.Bind(wx.EVT_BUTTON, self.OnBorrarButton, id=wxID_PANEL1BORRARBOTON)
        self.panel1 = wx.Panel(id=wxID_PANEL1PANEL1, name='panel1', parent=self, pos=wx.Point(510, 40), size=wx.Size(190, 180), style=wx.BORDER_NONE)
        self.panel1.SetBackgroundColour(wx.Colour(252, 245, 201))
        self.panel1.Bind(wx.EVT_PAINT, self.onPaint)

    def onCheckBoxes(self, event):
        """
        Metodo: onCheckBoxes
        
        
        ARGUMENTOS:
                event:
        """
        self.panel1.Refresh()

    def onPaint(self, event):
        """
        Metodo: onPaint
        
        
        ARGUMENTOS:
                event:
        """
        pintor = wx.PaintDC(self.panel1)
        pintor.Clear()
        im = wx.Image(Directorio + '/Imagenes/PTdefecto.jpg', wx.BITMAP_TYPE_JPEG)
        bitmap = wx.BitmapFromImage(im)
        pintor.DrawBitmap(bitmap, 0, 0, False)
        brush = wx.Brush(wx.Colour(245, 185, 31), wx.TRANSPARENT)
        pintor.SetBrush(brush)
        if self.pilarEnFachada.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(78, 10, 78, 40)
            pintor.DrawLine(78, 49, 78, 81)
            pintor.DrawLine(78, 92, 78, 123)
            pintor.DrawLine(120, 10, 120, 40)
            pintor.DrawLine(120, 49, 120, 81)
            pintor.DrawLine(120, 92, 120, 123)
            pintor.DrawLine(120, 132, 120, 164)
            boli = wx.Pen((150, 150, 150), 0.1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(75, 7, 6, 37)
            pintor.DrawRectangle(75, 47, 6, 38)
            pintor.DrawRectangle(75, 89, 6, 37)
            pintor.DrawRectangle(117, 7, 6, 37)
            pintor.DrawRectangle(117, 47, 6, 38)
            pintor.DrawRectangle(117, 89, 6, 37)
            pintor.DrawRectangle(117, 130, 6, 37)
        if self.pilarEnEsquina.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(28, 10, 28, 40)
            pintor.DrawLine(28, 49, 28, 81)
            pintor.DrawLine(28, 92, 28, 123)
            pintor.DrawLine(78, 132, 78, 164)
            pintor.DrawLine(162, 10, 162, 40)
            pintor.DrawLine(162, 49, 162, 81)
            pintor.DrawLine(162, 92, 162, 123)
            pintor.DrawLine(162, 132, 162, 164)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(25, 7, 6, 37)
            pintor.DrawRectangle(25, 47, 6, 38)
            pintor.DrawRectangle(25, 89, 6, 37)
            pintor.DrawRectangle(75, 130, 6, 37)
            pintor.DrawRectangle(159, 7, 6, 37)
            pintor.DrawRectangle(159, 47, 6, 38)
            pintor.DrawRectangle(159, 89, 6, 37)
            pintor.DrawRectangle(159, 130, 6, 37)
        if self.fachadaConForjado.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(33, 45, 157, 45)
            pintor.DrawLine(33, 87, 157, 87)
            pintor.DrawLine(81, 128, 157, 128)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(30, 42, 130, 6)
            pintor.DrawRectangle(30, 84, 130, 6)
            pintor.DrawRectangle(79, 125, 81, 6)
        if self.fachadaConCubierta.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(33, 5, 157, 5)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(30, 2, 130, 6)
        if self.fachadaConSuelo.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(33, 128, 72, 128)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(30, 125, 45, 6)
        if self.fachadaConSolera.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 6, 1)
            pintor.SetPen(boli)
            pintor.DrawLine(81, 168, 157, 168)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(79, 165, 81, 6)
        if self.cajaPersiana.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 4, 1)
            brush = wx.Brush(wx.Colour(245, 185, 31), wx.TRANSPARENT)
            pintor.SetPen(boli)
            pintor.SetBrush(brush)
            pintor.DrawLine(45, 20, 63, 20)
            pintor.DrawLine(45, 61, 63, 61)
            pintor.DrawLine(45, 102, 63, 102)
            pintor.DrawLine(91, 20, 108, 20)
            pintor.DrawLine(91, 61, 108, 61)
            pintor.DrawLine(91, 102, 108, 102)
            pintor.DrawLine(132, 20, 149, 20)
            pintor.DrawLine(132, 61, 149, 61)
            pintor.DrawLine(132, 102, 149, 102)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(43, 18, 22, 5)
            pintor.DrawRectangle(43, 59, 22, 5)
            pintor.DrawRectangle(43, 100, 22, 5)
            pintor.DrawRectangle(89, 18, 21, 5)
            pintor.DrawRectangle(89, 59, 21, 5)
            pintor.DrawRectangle(89, 100, 21, 5)
            pintor.DrawRectangle(130, 18, 21, 5)
            pintor.DrawRectangle(130, 59, 21, 5)
            pintor.DrawRectangle(130, 100, 21, 5)
        if self.contornoDeHueco.GetValue() == True:
            boli = wx.Pen((245, 185, 31), 3, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(44, 24, 19, 13)
            pintor.DrawRectangle(44, 65, 19, 13)
            pintor.DrawRectangle(44, 106, 19, 13)
            pintor.DrawRectangle(90, 24, 19, 13)
            pintor.DrawRectangle(90, 65, 19, 13)
            pintor.DrawRectangle(90, 106, 19, 13)
            pintor.DrawRectangle(131, 24, 19, 13)
            pintor.DrawRectangle(131, 65, 19, 13)
            pintor.DrawRectangle(131, 106, 19, 13)
            boli = wx.Pen((150, 150, 150), 1, 1)
            pintor.SetPen(boli)
            pintor.DrawRectangle(43, 22, 22, 16)
            pintor.DrawRectangle(46, 26, 16, 9)
            pintor.DrawRectangle(43, 63, 22, 16)
            pintor.DrawRectangle(46, 67, 16, 9)
            pintor.DrawRectangle(43, 104, 22, 16)
            pintor.DrawRectangle(46, 108, 16, 9)
            pintor.DrawRectangle(89, 22, 21, 16)
            pintor.DrawRectangle(92, 26, 15, 9)
            pintor.DrawRectangle(89, 63, 21, 16)
            pintor.DrawRectangle(92, 67, 15, 9)
            pintor.DrawRectangle(89, 104, 21, 16)
            pintor.DrawRectangle(92, 108, 15, 9)
            pintor.DrawRectangle(130, 22, 21, 16)
            pintor.DrawRectangle(133, 26, 15, 9)
            pintor.DrawRectangle(130, 63, 21, 16)
            pintor.DrawRectangle(133, 67, 15, 9)
            pintor.DrawRectangle(130, 104, 21, 16)
            pintor.DrawRectangle(133, 108, 15, 9)

    def __init__(self, parent, id, pos, size, style, name):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
        """
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent
        self.clickarCheck()

    def clickarCheck(self):
        """
        Metodo: clickarCheck
        
        
        """
        valorDefecto = False
        if self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection() == 2:
            for cerr in self.parent.cerramientos:
                if cerr[1] == 'Fachada' and 'defecto' in cerr[8] and cerr[-1] == 'aire':
                    valorDefecto = True
                    break

        if self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection() == 2 and valorDefecto == True:
            self.pilarEnFachada.SetValue(False)
            self.pilarEnEsquina.SetValue(False)
            self.contornoDeHueco.SetValue(False)
            self.cajaPersiana.SetValue(False)
            self.fachadaConForjado.SetValue(True)
            self.fachadaConCubierta.SetValue(True)
            self.fachadaConSuelo.SetValue(False)
            self.fachadaConSolera.SetValue(True)
        else:
            self.pilarEnFachada.SetValue(True)
            self.pilarEnEsquina.SetValue(False)
            self.contornoDeHueco.SetValue(True)
            self.cajaPersiana.SetValue(True)
            self.fachadaConForjado.SetValue(True)
            self.fachadaConCubierta.SetValue(True)
            self.fachadaConSuelo.SetValue(False)
            self.fachadaConSolera.SetValue(True)

    def OnBorrarButton(self, event):
        """
        Metodo: OnBorrarButton
        
        
        ARGUMENTOS:
                 event:
        """
        i = 0
        longitudPT = len(self.parent.puentesTermicos)
        while i < longitudPT and self.parent.puentesTermicos != []:
            borrado = False
            if self.pilarEnFachada.GetValue() == True:
                tipoPT = 'Pilar integrado en fachada'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.pilarEnEsquina.GetValue() == True:
                tipoPT = 'Pilar en Esquina'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.contornoDeHueco.GetValue() == True:
                tipoPT = 'Contorno de hueco'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.cajaPersiana.GetValue() == True:
                tipoPT = 'Caja de Persiana'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.fachadaConForjado.GetValue() == True:
                tipoPT = 'Encuentro de fachada con forjado'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.fachadaConCubierta.GetValue() == True:
                tipoPT = 'Encuentro de fachada con cubierta'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.fachadaConSuelo.GetValue() == True:
                tipoPT = 'Encuentro de fachada con suelo en contacto con el aire'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if self.fachadaConSolera.GetValue() == True:
                tipoPT = 'Encuentro de fachada con solera'
                if self.parent.puentesTermicos[i][2] == tipoPT:
                    self.parent.puentesTermicos.pop(i)
                    borrado = True
                    if self.parent.puentesTermicos == []:
                        break
            if borrado == False:
                i = i + 1
            longitudPT = len(self.parent.puentesTermicos)

        self.parent.cargarArbol(self.parent.arbolCerramientos)

    def OnCargarButton(self, event):
        """
        Metodo: OnCargarButton
        
        
        ARGUMENTOS:
                 event:
        """
        porDefecto = False
        for PT in self.parent.puentesTermicos:
            if PT[6] == 'defecto':
                porDefecto = True
                break

        comprobacion = self.OnComprobarAlturaNumeroPlantas()
        if comprobacion == 'error':
            return
        alturaMediaLibre = comprobacion[0]
        numeroPlantas = comprobacion[1]
        if porDefecto == False:
            self.OnCargarPTDefecto(alturaMediaLibre, numeroPlantas, self.parent.cerramientos, self.parent.ventanas)
        else:
            cerramientosSinPTdefecto = self.OnComprobarCerramientosSinPTporDefecto()
            dialogo = dialogoCargarPT.Dialog1(self)
            if cerramientosSinPTdefecto == []:
                dialogo.cargarCerramientosRadioButton.Show(False)
            else:
                dialogo.cargarCerramientosRadioButton.Show(True)
            dialogo.ShowModal()
            if dialogo.dev != False:
                opcion1 = dialogo.dev[0]
                opcion2 = dialogo.dev[1]
                opcion3 = dialogo.dev[2]
            else:
                return
            if opcion1 == True:
                self.OnCargaDeNuevo(alturaMediaLibre, numeroPlantas)
            elif opcion2 == True:
                self.OnCargaFiNoModificada(alturaMediaLibre, numeroPlantas)
            elif opcion3 == True:
                self.OnCargaEnCerramientosSinPTdefecto(alturaMediaLibre, numeroPlantas, cerramientosSinPTdefecto)

    def OnComprobarAlturaNumeroPlantas(self):
        """
        Metodo: OnComprobarAlturaNumeroPlantas
        
        
        """
        alturaMediaLibre = self.parent.parent.parent.panelDatosGenerales.alturaMediaLibre.GetValue()
        numeroPlantas = self.parent.parent.parent.panelDatosGenerales.numeroPlantas.GetValue()
        if ',' in alturaMediaLibre:
            alturaMediaLibre = alturaMediaLibre.replace(',', '.')
            self.parent.parent.parent.panelDatosGenerales.alturaMediaLibre.SetValue(alturaMediaLibre)
        if ',' in numeroPlantas:
            numeroPlantas = numeroPlantas.replace(',', '.')
            self.parent.parent.parent.panelDatosGenerales.numeroPlantas.SetValue(numeroPlantas)
        errorAltura = False
        errorNumeroPlantas = False
        try:
            float(alturaMediaLibre)
            if float(alturaMediaLibre) <= 0.0:
                errorAltura = True
        except (ValueError, TypeError):
            errorAltura = True

        try:
            float(numeroPlantas)
            if float(numeroPlantas) <= 0.0:
                errorNumeroPlantas = True
        except (ValueError, TypeError):
            errorNumeroPlantas = True

        if errorAltura == True or errorNumeroPlantas == True:
            if errorAltura == True and errorNumeroPlantas == True:
                wx.MessageBox(_(u'Revise los siguientes campos del panel de datos generales: \n - Altura media libre\n- N\xfamero de Plantas'), _(u'Aviso'))
            elif errorAltura == True:
                wx.MessageBox(_(u'Revise los siguientes campos del panel de datos generales: \n  - Altura media libre'), _(u'Aviso'))
            else:
                wx.MessageBox(_(u'Revise los siguientes campos del panel de datos generales: \n  - N\xfamero de plantas'), _(u'Aviso'))
            return 'error'
        else:
            return [alturaMediaLibre, numeroPlantas]

    def OnCargarPTDefecto(self, alturaMediaLibre, numeroPlantas, listadoCerramientos, listadoVentanas):
        """
        Metodo: OnCargarPTDefecto
        
        
        ARGUMENTOS:
                 alturaMediaLibre:
                 numeroPlantas:
                 listadoCerramientos:
                 listadoVentanas:
        """
        normaVigente = self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection()
        for i in listadoCerramientos:
            subgrupo = i[-2]
            if i[1] == 'Cubierta' and i[-1] == 'aire':
                if self.fachadaConCubierta.GetValue() == True:
                    tipoPT = 'Encuentro de fachada con cubierta'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)
            elif i[1] == 'Suelo':
                if self.fachadaConSolera.GetValue() == True and i[-1] == 'terreno':
                    tipoPT = 'Encuentro de fachada con solera'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)
                elif self.fachadaConSuelo.GetValue() == True and i[-1] == 'aire':
                    tipoPT = 'Encuentro de fachada con suelo en contacto con el aire'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)
            elif i[1] == 'Fachada' and i[-1] != 'edificio' and i[-1] == 'aire':
                if self.pilarEnFachada.GetValue() == True:
                    tipoPT = 'Pilar integrado en fachada'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)
                if self.pilarEnEsquina.GetValue() == True:
                    tipoPT = 'Pilar en Esquina'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)
                if self.fachadaConForjado.GetValue() == True:
                    tipoPT = 'Encuentro de fachada con forjado'
                    self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=i)

        for i in listadoVentanas:
            subgrupo = i.subgrupo
            if self.contornoDeHueco.GetValue() == True:
                tipoPT = 'Contorno de hueco'
                for cerr in listadoCerramientos:
                    if cerr[0] == i.cerramientoAsociado:
                        cerramientoAsociado = cerr
                        break

                self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=cerramientoAsociado, huecoAsociado=i)
            if self.cajaPersiana.GetValue() == True and i.tipo != 'Lucernario':
                tipoPT = 'Caja de Persiana'
                for cerr in listadoCerramientos:
                    if cerr[0] == i.cerramientoAsociado:
                        cerramientoAsociado = cerr
                        break

                self.anadirPT(tipoPT=tipoPT, normaVigente=normaVigente, alturaMediaLibre=alturaMediaLibre, numeroPlantas=numeroPlantas, subgrupo=subgrupo, cerramientoAsociado=cerramientoAsociado, huecoAsociado=i)

        self.parent.cargarArbol(self.parent.arbolCerramientos)

    def anadirPT(self, tipoPT = '', normaVigente = 0, alturaMediaLibre = 0.0, numeroPlantas = 0.0, subgrupo = '', cerramientoAsociado = [], huecoAsociado = None):
        """
        M\xe9todo: anadirPT
        A\xf1ade array de PT a self.parent.puentesTermicos
        """
        fi = tablasValores.tablasValores('PT', None, [tipoPT, normaVigente, cerramientoAsociado], None).fi
        if fi != False:
            if tipoPT in ('Contorno de hueco', 'Caja de Persiana'):
                nombreEltoAsociadoPT = huecoAsociado.descripcion
                elementoAsociado = huecoAsociado
                deQueCuelga = huecoAsociado.cerramientoAsociado
            else:
                nombreEltoAsociadoPT = cerramientoAsociado[0]
                elementoAsociado = cerramientoAsociado
                deQueCuelga = cerramientoAsociado[0]
            longitud = tablasValores.calcularLongitudPT(elementoAsociado, tipoPT, alturaMediaLibre, numeroPlantas)
            self.parent.puentesTermicos.append(['PT %s-%s' % (tipoPT, nombreEltoAsociadoPT),
             u'PT',
             tipoPT,
             fi,
             longitud,
             'defecto_fi',
             'defecto',
             deQueCuelga,
             subgrupo])
        return

    def OnCargaDeNuevo(self, alturaMediaLibre, numeroPlantas):
        """
        Metodo: OnCargaDeNuevo
        
        
        ARGUMENTOS:
                 alturaMediaLibre:
                 numeroPlantas:
        """
        i = 0
        while i < len(self.parent.puentesTermicos) and self.parent.puentesTermicos != []:
            PT = self.parent.puentesTermicos[i]
            tipoPT = PT[2]
            if PT[6] == 'defecto':
                if tipoPT == 'Encuentro de fachada con cubierta' and self.fachadaConCubierta.GetValue() == True or tipoPT == 'Encuentro de fachada con solera' and self.fachadaConSolera.GetValue() == True or tipoPT == 'Encuentro de fachada con suelo en contacto con el aire' and self.fachadaConSuelo.GetValue() == True or tipoPT == 'Pilar integrado en fachada' and self.pilarEnFachada.GetValue() == True or tipoPT == 'Pilar en Esquina' and self.pilarEnEsquina.GetValue() == True or tipoPT == 'Encuentro de fachada con forjado' and self.fachadaConForjado.GetValue() == True or tipoPT == 'Contorno de hueco' and self.contornoDeHueco.GetValue() == True or tipoPT == 'Caja de Persiana' and self.cajaPersiana.GetValue() == True:
                    self.parent.puentesTermicos.pop(i)
                    i -= 1
            i += 1

        self.OnCargarPTDefecto(alturaMediaLibre, numeroPlantas, self.parent.cerramientos, self.parent.ventanas)

    def OnCargaFiNoModificada(self, alturaMediaLibre, numeroPlantas):
        """
        Metodo: OnCargaFiNoModificada
        
        
        ARGUMENTOS:
                 alturaMediaLibre:
                 numeroPlantas:
        """
        for PT in self.parent.puentesTermicos:
            tipoPT = PT[2]
            if PT[5] == 'defecto_fi':
                if tipoPT == 'Encuentro de fachada con cubierta' and self.fachadaConCubierta.GetValue() == True or tipoPT == 'Encuentro de fachada con solera' and self.fachadaConSolera.GetValue() == True or tipoPT == 'Encuentro de fachada con suelo en contacto con el aire' and self.fachadaConSuelo.GetValue() == True or tipoPT == 'Pilar integrado en fachada' and self.pilarEnFachada.GetValue() == True or tipoPT == 'Pilar en Esquina' and self.pilarEnEsquina.GetValue() == True or tipoPT == 'Encuentro de fachada con forjado' and self.fachadaConForjado.GetValue() == True or tipoPT == 'Contorno de hueco' and self.contornoDeHueco.GetValue() == True or tipoPT == 'Caja de Persiana' and self.cajaPersiana.GetValue() == True:
                    cerramiento = ''
                    for cerr in self.parent.cerramientos:
                        if cerr[0] == PT[7]:
                            cerramiento = cerr
                            break

                    fi = tablasValores.tablasValores('PT', None, [tipoPT, self.parent.parent.parent.panelDatosGenerales.anoConstruccionChoice.GetSelection(), cerramiento], None).fi
                    PT[3] = fi
                    PT[5] = 'defecto_fi'
                    PT[6] = 'defecto'

        self.parent.cargarArbol(self.parent.arbolCerramientos)
        return

    def OnComprobarCerramientosSinPTporDefecto(self):
        """
        Metodo: OnComprobarCerramientosSinPTporDefecto
        
        
        """
        cerramientosSinPTdefecto = []
        for cerr in self.parent.cerramientos:
            hayPTdefecto = False
            for PT in self.parent.puentesTermicos:
                if PT[7] == cerr[0] and PT[6] == 'defecto':
                    hayPTdefecto = True
                    break

            if hayPTdefecto == False:
                cerramientosSinPTdefecto.append(cerr)

        return cerramientosSinPTdefecto

    def OnCargaEnCerramientosSinPTdefecto(self, alturaMediaLibre, numeroPlantas, cerramientosSinPTdefecto):
        """
        Metodo: OnCargaEnCerramientosSinPTdefecto
        
        
        ARGUMENTOS:
                 alturaMediaLibre:
                 numeroPlantas:
                 cerramientosSinPTdefecto:
        """
        if cerramientosSinPTdefecto != []:
            nombreCerramientosSinPTdefecto = []
            for cerr in cerramientosSinPTdefecto:
                nombreCerramientosSinPTdefecto.append(cerr[0])

            ventanasSinPTdefecto = []
            for vent in self.parent.ventanas:
                if vent.cerramientoAsociado in nombreCerramientosSinPTdefecto:
                    ventanasSinPTdefecto.append(vent)

            self.OnCargarPTDefecto(alturaMediaLibre, numeroPlantas, cerramientosSinPTdefecto, ventanasSinPTdefecto)