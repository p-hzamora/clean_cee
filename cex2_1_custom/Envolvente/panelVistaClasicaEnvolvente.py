# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Envolvente\panelVistaClasicaEnvolvente.pyc
# Compiled at: 2015-02-23 10:04:45
"""
Modulo: panelVistaClasicaEnvolvente.py

"""
from Calculos.listadosWeb import getTraduccion, listadoOpcionesPropiedadesTermicasHuecos, listadoOpcionesPuentesTermicos, listadoPosicionCerramientos, listadoCerramientos
from Envolvente.comprobarCampos import Comprueba
from miChoiceGrid import MiChoiceGrid
import Envolvente.dialogoConfirma as dialogoConfirma, wx, wx.grid
from miGrid import MyGrid
import logging
wxID_PANEL1CERRAMIESTOSRADIO, wxID_PANEL1HUECOSRADIO, wxID_PANEL1GRID1, wxID_PANEL1PTERMICOSRADIO, wxID_PANEL1GRID2, wxID_PANEL1GRID3, wxID_PANEL1ANADIRBOTON, wxID_PANEL1DEFINIR, wxID_WXPANEL1STATICLINE = [ wx.NewId() for _init_ctrls in range(9) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelVistaClasicaEnvolvente.py

    """

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                prnt:
                id:
                 posi:
                 siz:
                 styles:
                 named:
        """
        wx.Panel.__init__(self, id=id, name=named, parent=prnt, pos=posi, size=siz, style=styles)
        self.SetBackgroundColour('white')
        self.definirText = wx.StaticText(id=wxID_PANEL1DEFINIR, label=_('Envolvente térmica del edificio'), name='definirText', parent=self, pos=wx.Point(0, 0), size=wx.Size(167, 18), style=0)
        self.definirText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.definirText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.cerramiestosRadio = wx.RadioButton(id=wxID_PANEL1CERRAMIESTOSRADIO, label=_('Cerramientos'), name='cerramiestosRadio', parent=self, pos=wx.Point(20, 40), size=wx.Size(81, 13), style=wx.RB_GROUP)
        self.cerramiestosRadio.SetValue(True)
        self.cerramiestosRadio.Bind(wx.EVT_RADIOBUTTON, self.OnCerramiestosRadioRadiobutton, id=wxID_PANEL1CERRAMIESTOSRADIO)
        self.huecosRadio = wx.RadioButton(id=wxID_PANEL1HUECOSRADIO, label=_('Huecos'), name='huecosRadio', parent=self, pos=wx.Point(20, 100), size=wx.Size(81, 13), style=0)
        self.huecosRadio.SetValue(False)
        self.huecosRadio.Bind(wx.EVT_RADIOBUTTON, self.OnHuecosRadioRadiobutton, id=wxID_PANEL1HUECOSRADIO)
        self.pTermicosRadio = wx.RadioButton(id=wxID_PANEL1PTERMICOSRADIO, label=_('Puentes térmicos'), name='pTermicosRadio', parent=self, pos=wx.Point(20, 160), size=wx.Size(112, 13), style=0)
        self.pTermicosRadio.SetValue(False)
        self.pTermicosRadio.Bind(wx.EVT_RADIOBUTTON, self.OnPTermicosRadioRadiobutton, id=wxID_PANEL1PTERMICOSRADIO)
        self.staticLine = wx.StaticLine(id=wxID_WXPANEL1STATICLINE, name='staticLine', parent=self, pos=wx.Point(0, 202), size=wx.Size(710, 3), style=0)
        self.staticLine.SetBackgroundColour(wx.Colour(0, 64, 128))
        self.listaCerramientos = MyGrid(id=wxID_PANEL1GRID1, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaCerramientos.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnListaCerramientos, id=wxID_PANEL1GRID1)
        self._init_coll_listaCerramientos_Columns(self.listaCerramientos)
        self.listaHuecos = MyGrid(id=wxID_PANEL1GRID3, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self._init_coll_listaHuecos_Columns(self.listaHuecos)
        self.listaHuecos.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnListaHuecos, id=wxID_PANEL1GRID3)
        self.listaPuentesTermicos = MyGrid(id=wxID_PANEL1GRID2, parent=self, pos=wx.Point(0, 232), size=wx.Size(710, 308), style=wx.RAISED_BORDER)
        self.listaPuentesTermicos.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnListaPTermicos, id=wxID_PANEL1GRID2)
        self._init_coll_listaPuentesTermicos_Columns(self.listaPuentesTermicos)
        self.guardarBoton = wx.Button(id=wxID_PANEL1ANADIRBOTON, label=_('Guardar cambios'), name='anadirBoton', parent=self, pos=wx.Point(610, 555), size=wx.Size(100, 23), style=0)
        self.guardarBoton.Bind(wx.EVT_BUTTON, self.onGuardarBoton, id=wxID_PANEL1ANADIRBOTON)

    def onGuardarBoton(self, event):
        """
        Metodo: onGuardarBoton

        ARGUMENTOS:
                event:
        """
        devuelto = self.realizaCambios(None, self.listaActual)
        if devuelto != 1:
            wx.MessageBox(_('Revise los siguientes campos:\n') + devuelto, _('Aviso'))
        return

    def _init_coll_listaPuentesTermicos_Columns(self, parent):
        """
        Metodo: _init_coll_listaPuentesTermicos_Columns

        ARGUMENTOS:
                 parent:
        """
        parent.CreateGrid(0, 5)
        parent.SetColLabelValue(0, _('Nombre'))
        parent.SetColLabelValue(1, _('Cerramiento asociado'))
        parent.SetColLabelValue(2, _('Tipo de puente térmico'))
        parent.SetColLabelValue(3, _('φ\n(W/mK)'))
        parent.SetColLabelValue(4, _('Longitud\n(m)'))

    def _init_coll_listaCerramientos_Columns(self, parent):
        """
        Metodo: _init_coll_listaCerramientos_Columns

        ARGUMENTOS:
                 parent:
        """
        parent.CreateGrid(0, 8)
        parent.SetColLabelValue(0, _('Nombre'))
        parent.SetColLabelValue(1, _('Tipo de\ncerramiento'))
        parent.SetColLabelValue(2, _('Superficie\n(m2)'))
        parent.SetColLabelValue(3, _('U\n(W/m2K)'))
        parent.SetColLabelValue(4, _('Peso/m2\n(kg/m2)'))
        parent.SetColLabelValue(5, _('Posición'))
        parent.SetColLabelValue(6, _('Modo definición'))
        parent.SetColLabelValue(7, _('Patrón de sombras'))

    def _init_coll_listaHuecos_Columns(self, parent):
        """
        Metodo: _init_coll_listaHuecos_Columns

        ARGUMENTOS:
                 parent:
        """
        parent.CreateGrid(0, 15)
        parent.SetColLabelValue(0, _('Nombre'))
        parent.SetColLabelValue(1, _('Cerramiento\nasociado'))
        parent.SetColLabelValue(2, _('Longitud\n(m)'))
        parent.SetColLabelValue(3, _('Altura\n(m)'))
        parent.SetColLabelValue(4, _('Multiplicador'))
        parent.SetColLabelValue(5, _('Superficie\n(m2)'))
        parent.SetColLabelValue(6, _('U vidrio\n(W/m2K)'))
        parent.SetColLabelValue(7, _('g vidrio'))
        parent.SetColLabelValue(8, _('U marco\n(W/m2K)'))
        parent.SetColLabelValue(9, _('% Marco'))
        parent.SetColLabelValue(10, _('Absortividad marco'))
        parent.SetColLabelValue(11, _('Modo definición'))
        parent.SetColLabelValue(12, _('Permeabilidad\n(m3/hm2)'))
        parent.SetColLabelValue(13, _('Orientación'))
        parent.SetColLabelValue(14, _('Patrón de sombras'))

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
        self.cambios = False
        self._init_ctrls(parent, id, pos, size, style, name)
        self.parent = parent
        self.OnCerramiestosRadioRadiobutton(None)
        self.listaActual = 'Cerramientos'
        return

    def OnListaPTermicos(self, event):
        """
        Metodo: OnListaPTermicos

        ARGUMENTOS:
                event:
        """
        self.cambios = True

    def OnListaHuecos(self, event):
        """
        Metodo: OnListaHuecos

        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 5:
            self.listaHuecos.SetCellValue(event.GetRow(), 2, '')
            self.listaHuecos.SetCellValue(event.GetRow(), 3, '')
            self.listaHuecos.SetCellValue(event.GetRow(), 4, '')
        elif event.GetCol() == 2 or event.GetCol() == 3 or event.GetCol() == 4:
            try:
                lon = float(self.listaHuecos.GetCellValue(event.GetRow(), 2))
                alt = float(self.listaHuecos.GetCellValue(event.GetRow(), 3))
                mul = float(self.listaHuecos.GetCellValue(event.GetRow(), 4))
                self.listaHuecos.SetCellValue(event.GetRow(), 5, str(lon * alt * mul))
            except (ValueError, TypeError):
                pass
            except IndexError:
                pass

        elif event.GetCol() == 6 or event.GetCol() == 7 or event.GetCol() == 8:
            self.listaHuecos.SetCellValue(event.GetRow(), 11, 'Conocidas')

    def OnListaCerramientos(self, event):
        """
        Metodo: OnListaCerramientos

        ARGUMENTOS:
                event:
        """
        self.cambios = True
        if event.GetCol() == 3 or event.GetCol() == 4:
            self.listaCerramientos.SetCellValue(event.GetRow(), 6, 'Conocido')
            self.listaCerramientos.SetReadOnly(event.GetRow(), 4, False)

    def OnCerramiestosRadioRadiobutton(self, event):
        """
        Metodo: OnCerramiestosRadioRadiobutton

        ARGUMENTOS:
                 event:
        """
        if self.cambios == True:
            DeseaReemplazar = dialogoConfirma.Dialog1(self, _('¿Desea guardar los cambios?'))
            DeseaReemplazar.ShowModal()
            if DeseaReemplazar.dev == True:
                devuelto = self.realizaCambios(None, self.listaActual)
                if devuelto != 1:
                    if self.listaActual == 'Cerramientos':
                        self.cerramiestosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(True)
                        self.listaPuentesTermicos.Show(False)
                    elif self.listaActual == 'Huecos':
                        self.huecosRadio.SetValue(True)
                        self.listaHuecos.Show(True)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(False)
                    else:
                        self.pTermicosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(True)
                    wx.MessageBox(_('Revise los siguientes campos:\n') + devuelto, _('Aviso'))
                    return
        self.cambios = False
        self.listaActual = 'Cerramientos'
        self.listaHuecos.Show(False)
        self.listaCerramientos.Show(True)
        self.listaPuentesTermicos.Show(False)
        return

    def OnHuecosRadioRadiobutton(self, event):
        """
        Metodo: OnHuecosRadioRadiobutton

        ARGUMENTOS:
                 event:
        """
        if self.cambios == True:
            DeseaReemplazar = dialogoConfirma.Dialog1(self, _('¿Desea guardar los cambios?'))
            DeseaReemplazar.ShowModal()
            if DeseaReemplazar.dev == True:
                devuelto = self.realizaCambios(None, self.listaActual)
                if devuelto != 1:
                    if self.listaActual == 'Cerramientos':
                        self.cerramiestosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(True)
                        self.listaPuentesTermicos.Show(False)
                    elif self.listaActual == 'Huecos':
                        self.huecosRadio.SetValue(True)
                        self.listaHuecos.Show(True)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(False)
                    else:
                        self.pTermicosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(True)
                    wx.MessageBox(_('Revise los siguientes campos:\n') + devuelto, _('Aviso'))
                    return
        self.cambios = False
        self.listaActual = 'Huecos'
        self.listaHuecos.Show(True)
        self.listaCerramientos.Show(False)
        self.listaPuentesTermicos.Show(False)
        return

    def OnPTermicosRadioRadiobutton(self, event):
        """
        Metodo: OnPTermicosRadioRadiobutton

        ARGUMENTOS:
                 event:
        """
        if self.cambios == True:
            DeseaReemplazar = dialogoConfirma.Dialog1(self, _('¿Desea guardar los cambios?'))
            DeseaReemplazar.ShowModal()
            if DeseaReemplazar.dev == True:
                devuelto = self.realizaCambios(None, self.listaActual)
                if devuelto != 1:
                    if self.listaActual == 'Cerramientos':
                        self.cerramiestosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(True)
                        self.listaPuentesTermicos.Show(False)
                    elif self.listaActual == 'Huecos':
                        self.huecosRadio.SetValue(True)
                        self.listaHuecos.Show(True)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(False)
                    else:
                        self.pTermicosRadio.SetValue(True)
                        self.listaHuecos.Show(False)
                        self.listaCerramientos.Show(False)
                        self.listaPuentesTermicos.Show(True)
                    wx.MessageBox(_('Revise los siguientes campos:\n') + devuelto, _('Aviso'))
                    return
        self.cambios = False
        self.listaActual = 'Puentes'
        self.listaHuecos.Show(False)
        self.listaCerramientos.Show(False)
        self.listaPuentesTermicos.Show(True)
        return

    def cargaCerramientos(self):
        """
        Metodo: cargaCerramientos
        """
        try:
            self.listaCerramientos.DeleteRows(0, self.listaCerramientos.GetNumberRows())
        except:
            logging.info('Excepcion en: %s' % __name__)

        listadoPatronesSombra = []
        for i in self.parent.parent.parent.nuevoListadoSombras:
            listadoPatronesSombra.append((i[0], _(i[0])))

        opcionesPatronesSombra = MiChoiceGrid(choices=listadoPatronesSombra)
        self.listaCerramientos.ampliaDiccionarioTraduccion(opcionesPatronesSombra.traduccion)
        opcionesOrientacion = MiChoiceGrid(choices=listadoPosicionCerramientos)
        self.listaCerramientos.ampliaDiccionarioTraduccion(opcionesOrientacion.traduccion)
        opcionesTipoCerramiento = MiChoiceGrid(choices=listadoCerramientos)
        self.listaCerramientos.ampliaDiccionarioTraduccion(opcionesTipoCerramiento.traduccion)
        for i in range(len(self.parent.cerramientos)):
            self.listaCerramientos.AppendRows(1)
            self.listaCerramientos.SetCellValue(i, 0, self.parent.cerramientos[i][0])
            self.listaCerramientos.SetReadOnly(i, 0)
            self.listaCerramientos.SetCellEditor(i, 1, opcionesTipoCerramiento)
            self.listaCerramientos.SetCellValue(i, 1, self.parent.cerramientos[i][1])
            self.listaCerramientos.SetReadOnly(i, 1)
            self.listaCerramientos.SetCellValue(i, 2, str(self.parent.cerramientos[i][2]))
            self.listaCerramientos.SetReadOnly(i, 2)
            self.listaCerramientos.SetCellValue(i, 3, str(self.parent.cerramientos[i][3]))
            self.listaCerramientos.SetReadOnly(i, 3)
            self.listaCerramientos.SetCellValue(i, 4, str(self.parent.cerramientos[i][4]))
            self.listaCerramientos.SetReadOnly(i, 4)
            self.listaCerramientos.SetCellEditor(i, 5, opcionesOrientacion)
            self.listaCerramientos.SetCellValue(i, 5, self.parent.cerramientos[i][5])
            self.listaCerramientos.SetReadOnly(i, 5)
            if self.parent.cerramientos[i][1] == 'Fachada' and self.parent.cerramientos[i][-1] == 'edificio':
                self.listaCerramientos.SetCellValue(i, 6, '')
            else:
                self.listaCerramientos.ampliaDiccionarioTraduccion({_(self.parent.cerramientos[i][8]): self.parent.cerramientos[i][8]})
                self.listaCerramientos.SetCellValue(i, 6, self.parent.cerramientos[i][8])
            self.listaCerramientos.SetReadOnly(i, 6)
            self.listaCerramientos.SetCellEditor(i, 7, opcionesPatronesSombra)
            self.listaCerramientos.SetCellValue(i, 7, self.parent.cerramientos[i][7])
            if (self.parent.cerramientos[i][1] == 'Fachada' or self.parent.cerramientos[i][1] == 'Cubierta') and self.parent.cerramientos[i][-1] == 'aire':
                pass
            else:
                self.listaCerramientos.SetReadOnly(i, 7)

        self.listaCerramientos.AutoSizeColumns()

    def cargaHuecos(self):
        """
        Metodo: cargaHuecos

        """
        try:
            self.listaHuecos.DeleteRows(0, self.listaHuecos.GetNumberRows())
        except:
            logging.info('Excepcion en: %s' % __name__)

        listadoCerramientos = []
        for i in self.parent.cerramientos:
            if i[len(i) - 1] == 'aire' and i[1] != 'Suelo':
                listadoCerramientos.append((i[0], i[0]))

        opcionesCerramientos = MiChoiceGrid(choices=listadoCerramientos)
        self.listaHuecos.ampliaDiccionarioTraduccion(opcionesCerramientos.traduccion)
        listadoPatronesSombra = []
        for i in self.parent.parent.parent.nuevoListadoSombras:
            listadoPatronesSombra.append((i[0], _(i[0])))

        opcionesPatronesSombra = MiChoiceGrid(choices=listadoPatronesSombra)
        self.listaHuecos.ampliaDiccionarioTraduccion(opcionesPatronesSombra.traduccion)
        for i in range(len(self.parent.ventanas)):
            self.listaHuecos.AppendRows(1)
            self.listaHuecos.SetCellValue(i, 0, self.parent.ventanas[i].descripcion)
            self.listaHuecos.SetReadOnly(i, 0)
            self.listaHuecos.SetCellEditor(i, 1, opcionesCerramientos)
            self.listaHuecos.SetCellValue(i, 1, self.parent.ventanas[i].cerramientoAsociado)
            self.listaHuecos.SetReadOnly(i, 1)
            self.listaHuecos.SetCellValue(i, 2, str(self.parent.ventanas[i].longitud))
            self.listaHuecos.SetCellValue(i, 3, str(self.parent.ventanas[i].altura))
            self.listaHuecos.SetCellValue(i, 4, str(self.parent.ventanas[i].multiplicador))
            self.listaHuecos.SetCellValue(i, 5, str(self.parent.ventanas[i].superficie))
            if 'Estimad' in self.parent.ventanas[i].__tipo__:
                self.listaHuecos.SetCellValue(i, 6, str(self.parent.ventanas[i].Uvidrio))
                self.listaHuecos.SetCellValue(i, 7, str(self.parent.ventanas[i].Gvidrio))
                self.listaHuecos.SetCellValue(i, 8, str(self.parent.ventanas[i].Umarco))
            else:
                self.listaHuecos.SetCellValue(i, 6, str(self.parent.ventanas[i].UvidrioConocido))
                self.listaHuecos.SetCellValue(i, 7, str(self.parent.ventanas[i].GvidrioConocido))
                self.listaHuecos.SetCellValue(i, 8, str(self.parent.ventanas[i].UmarcoConocido))
            self.listaHuecos.SetCellValue(i, 9, str(self.parent.ventanas[i].porcMarco))
            self.listaHuecos.SetCellValue(i, 10, str(self.parent.ventanas[i].absortividadValor))
            self.listaHuecos.SetReadOnly(i, 11)
            if 'Estimad' in self.parent.ventanas[i].__tipo__:
                modoDefinicion = getTraduccion(listado=listadoOpcionesPropiedadesTermicasHuecos, elemento='Estimadas')
                self.listaHuecos.ampliaDiccionarioTraduccion({modoDefinicion: 'Estimadas'})
                self.listaHuecos.SetCellValue(i, 11, modoDefinicion)
                self.listaHuecos.SetReadOnly(i, 6)
                self.listaHuecos.SetReadOnly(i, 7)
                self.listaHuecos.SetReadOnly(i, 8)
            else:
                modoDefinicion = getTraduccion(listado=listadoOpcionesPropiedadesTermicasHuecos, elemento='Conocidas')
                self.listaHuecos.ampliaDiccionarioTraduccion({modoDefinicion: 'Conocidas'})
                self.listaHuecos.SetCellValue(i, 11, modoDefinicion)
            self.listaHuecos.SetCellValue(i, 12, str(self.parent.ventanas[i].permeabilidadValor))
            self.listaHuecos.SetReadOnly(i, 12)
            self.listaHuecos.ampliaDiccionarioTraduccion({_(self.parent.ventanas[i].orientacion): self.parent.ventanas[i].orientacion})
            self.listaHuecos.SetCellValue(i, 13, str(self.parent.ventanas[i].orientacion))
            self.listaHuecos.SetReadOnly(i, 13)
            self.listaHuecos.SetCellEditor(i, 14, opcionesPatronesSombra)
            self.listaHuecos.SetCellValue(i, 14, self.parent.ventanas[i].patronSombras)

        self.listaHuecos.AutoSizeColumns()

    def cargaPTermicos(self):
        """
        Metodo: cargaPTermicos

        """
        try:
            self.listaPuentesTermicos.DeleteRows(0, self.listaPuentesTermicos.GetNumberRows())
        except:
            logging.info('Excepcion en: %s' % __name__)

        opcionesPuentes = MiChoiceGrid(choices=listadoOpcionesPuentesTermicos)
        self.listaPuentesTermicos.ampliaDiccionarioTraduccion(opcionesPuentes.traduccion)
        listadoCerramientos = []
        for i in self.parent.cerramientos:
            listadoCerramientos.append((i[0], i[0]))

        opcionesCerramientos = MiChoiceGrid(choices=listadoCerramientos)
        self.listaPuentesTermicos.ampliaDiccionarioTraduccion(opcionesCerramientos.traduccion)
        for i in range(len(self.parent.puentesTermicos)):
            self.listaPuentesTermicos.AppendRows(1)
            self.listaPuentesTermicos.SetCellValue(i, 0, self.parent.puentesTermicos[i][0])
            self.listaPuentesTermicos.SetReadOnly(i, 0)
            self.listaPuentesTermicos.SetCellEditor(i, 1, opcionesCerramientos)
            self.listaPuentesTermicos.SetCellValue(i, 1, self.parent.puentesTermicos[i][7])
            self.listaPuentesTermicos.SetCellEditor(i, 2, opcionesPuentes)
            self.listaPuentesTermicos.SetCellValue(i, 2, self.parent.puentesTermicos[i][2])
            self.listaPuentesTermicos.SetCellValue(i, 3, str(self.parent.puentesTermicos[i][3]))
            self.listaPuentesTermicos.SetCellValue(i, 4, str(self.parent.puentesTermicos[i][4]))

        self.listaPuentesTermicos.AutoSizeColumns()

    def realizaCambios(self, event, listaModifica):
        """
        Metodo: realizaCambios

        ARGUMENTOS:
                event:
                listaModifica:
        """
        listaErrores = ''
        if listaModifica == 'Cerramientos':
            for i in range(len(self.parent.cerramientos)):
                listaErrores += Comprueba(self.listaCerramientos.GetCellValue(i, 7), 1, listaErrores, _('patrón de sombras %s') % (i + 1)).ErrorDevuelto
                if listaErrores != '':
                    return listaErrores

            for i in range(len(self.parent.cerramientos)):
                patronSombras = self.listaCerramientos.GetCellValue(i, 7)
                if isinstance(patronSombras, unicode):
                    patronSombrasTraducido = patronSombras
                else:
                    patronSombrasTraducido = patronSombras.decode('cp1252')
                self.parent.cerramientos[i][7] = patronSombrasTraducido

        elif listaModifica == 'Huecos':
            for i in range(len(self.parent.ventanas)):
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 5), 2, listaErrores, _('superficie (m2) %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 6), 2, listaErrores, _('U vidrio %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 7), 2, listaErrores, _('g vidrio %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 8), 2, listaErrores, _('U marco %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 9), 2, listaErrores, _('porcentaje marco %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaHuecos.GetCellValue(i, 10), 2, listaErrores, _('absortividad marco %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != '':
                return listaErrores
            for i in range(len(self.parent.ventanas)):
                self.parent.ventanas[i].longitud = self.listaHuecos.GetCellValue(i, 2)
                self.parent.ventanas[i].altura = self.listaHuecos.GetCellValue(i, 3)
                self.parent.ventanas[i].multiplicador = self.listaHuecos.GetCellValue(i, 4)
                self.parent.ventanas[i].superficie = self.listaHuecos.GetCellValue(i, 5)
                if self.listaHuecos.GetCellValue(i, 11) == 'Conocidas':
                    self.parent.ventanas[i].UvidrioConocido = self.listaHuecos.GetCellValue(i, 6)
                    self.parent.ventanas[i].GvidrioConocido = self.listaHuecos.GetCellValue(i, 7)
                    self.parent.ventanas[i].UmarcoConocido = self.listaHuecos.GetCellValue(i, 8)
                    self.parent.ventanas[i].calculoPropiedadesTermicas()
                self.parent.ventanas[i].porcMarco = self.listaHuecos.GetCellValue(i, 9)
                self.parent.ventanas[i].absortividadValor = self.listaHuecos.GetCellValue(i, 10)
                self.parent.ventanas[i].patronSombras = unicode(self.listaHuecos.GetCellValue(i, 14))

        else:
            for i in range(len(self.parent.puentesTermicos)):
                listaErrores += Comprueba(self.listaPuentesTermicos.GetCellValue(i, 1), 1, listaErrores, _('cerramiento asociado %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaPuentesTermicos.GetCellValue(i, 2), 1, listaErrores, _('tipo de puente térmico %s') % (i + 1)).ErrorDevuelto
                listaErrores += Comprueba(self.listaPuentesTermicos.GetCellValue(i, 3), 2, listaErrores, _('φ %s') % (i + 1), 0).ErrorDevuelto
                listaErrores += Comprueba(self.listaPuentesTermicos.GetCellValue(i, 4), 2, listaErrores, _('longitud %s') % (i + 1), 0).ErrorDevuelto

            if listaErrores != '':
                return listaErrores
            for i in range(len(self.parent.puentesTermicos)):
                self.parent.puentesTermicos[i][2] = self.listaPuentesTermicos.GetCellValue(i, 2)
                fi_previa = self.parent.puentesTermicos[i][3]
                self.parent.puentesTermicos[i][3] = self.listaPuentesTermicos.GetCellValue(i, 3)
                self.parent.puentesTermicos[i][4] = self.listaPuentesTermicos.GetCellValue(i, 4)
                fi_nueva = float(self.listaPuentesTermicos.GetCellValue(i, 3))
                if fi_nueva != float(fi_previa):
                    self.parent.puentesTermicos[i][5] = 'usuario_fi'
                self.parent.puentesTermicos[i][7] = unicode(self.listaPuentesTermicos.GetCellValue(i, 1))

        self.parent.cargarArbol(self.parent.arbolCerramientos)
        self.cambios = False
        self.cargaCerramientos()
        self.cargaHuecos()
        self.cargaPTermicos()
        return 1