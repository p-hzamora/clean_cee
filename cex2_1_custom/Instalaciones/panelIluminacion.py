# Embedded file name: Instalaciones\panelIluminacion.pyc
from Instalaciones.comprobarCampos import Comprueba
from miChoice import MiChoice
import Calculos.listadosWeb as listadosWeb
from Calculos.funcionesCalculo import diccLuminarias
import logging

class Panel1(wx.Panel):

    def _init_ctrls(self, prnt, id, posi, siz, styles, named):
        self.nombreInstalacion = 'Iluminaci\xf3n'
        self.subgrupoChoice = MiChoice(choices=[])
        self.superficieMuro = u''
        self.sinControl = False # or True, era un CheckBox que debia elegir el usuario
        self.sinControl= True
        self.conControl = False # or True, era un CheckBox que debia elegir el usuario
        self.superficieControl = u''
        # self.zonaRepresentacionCheckZona de representaci\xf3n
        self.zonaRepresentacionCheck= False
        self.usoChoice = MiChoice(choices=listadosWeb.tablaZona1)
        self.usoChoice.SetSelection(0)
        self.definirSegunChoice = MiChoice(choices=listadosWeb.listadoOpcionesIluminacion)
        self.definirSegunChoice.SetSelection(0)
        self.potenciaInstalada = u''
        self.tipoEquipoChoice = MiChoice(choices=listadosWeb.listaTipoEquipo)
        self.iluminancia = u''

    def OnNombreInstalacion(self, event):
        if self.nombreInstalacion == 'Iluminaci\xf3n':
        else:

    def __init__(self, parent, id, pos, size, style, name, real_parent = None, instalacionIluminacion = None):
        if real_parent == None:
            self.parent = parent
        else:
            self.parent = real_parent
        if instalacionIluminacion != None:
            instalacionIluminacionAntigua = instalacionIluminacion
        self.potencia = 0
        self.veei = 0
        self.cambiandoIluminancia = False
        self._init_ctrls(parent, id, pos, size, style, name)
        self.tipoSistema = 'iluminacion'
        if self.parent.parent.parent.programa == 'GranTerciario':
            self.onControlIluminacion(True)
            self.superficieMuro.Enable(False)
        else:
        self.subgrupoChoice.SetItems(self.cargarRaices(instalacionIluminacionAntigua))
        self.elegirRaiz()
        self.valoresPorDefectoIluminancia(None)
        self.onSeleccionarSubgrupo(None)
        return

    def elegirRaiz(self):
        try:
            sel = self.parent.arbolInstalaciones.GetSelection()
            aux = self.subgrupoChoice.GetItems()
            if aux == []:
                return
            self.subgrupoChoice.SetSelection(0)
            raiz = self.parent.arbolInstalaciones.GetRootItem()
            while sel != raiz:
                for i in range(len(self.parent.parent.subgrupos)):
                    if self.parent.arbolInstalaciones.GetItemText(sel) == '%s' % self.parent.parent.subgrupos[i].nombre:
                        self.subgrupoChoice.SetStringSelection(self.parent.arbolInstalaciones.GetItemText(sel))
                        return

                sel = self.parent.arbolInstalaciones.GetItemParent(sel)

        except:
            logging.info(u'Excepcion en: %s' % __name__)

    def onSeleccionarSubgrupo(self, event):
        seleccionado = self.subgrupoChoice.GetStringSelection()
        if seleccionado == '':
            seleccionado = u'Edificio Objeto'
        superficieSubZonas = 0
        for sub in self.parent.parent.subgrupos:
            if seleccionado == sub.raiz:
                superficieSubZonas += float(sub.superficie)
            if seleccionado == sub.nombre:
                superficieZona = float(sub.superficie)

        if seleccionado == u'Edificio Objeto':
            superficieZona = self.parent.parent.parent.panelDatosGenerales.superficie
            try:
                if ',' in superficieZona:
                    superficieZona = superficieZona.replace(',', '.')
                    self.parent.parent.parent.superficie= superficieZona
                superficieZona = float(self.parent.parent.parent.panelDatosGenerales.superficie)
            except (ValueError, TypeError):
                raise Exception('Revise la superficie del edificio en el panel de datos generales')
                return

        superficie = superficieZona - superficieSubZonas
        if superficie < 0:
            raise Exception('La superficie de las zonas del edificio es mayor que la superficie del edificio,  revise los valores')
            return
        self.superficieMuro= str(superficie)

    def cargarRaices(self, instalacionIluminacionAntigua):
        raices = []
        if self.parent.parent.parent.programa == 'GranTerciario':
            raicesUtilizadas = []
            for ilum in instalacionIluminacionAntigua:
                raicesUtilizadas.append((ilum[-1], ilum[-1]))

            if u'Edificio Objeto' not in raicesUtilizadas:
                raices.append((u'Edificio Objeto', 'Edificio Objeto'))
            for i in range(len(self.parent.parent.subgrupos)):
                tuplaRaiz = ('%s' % self.parent.parent.subgrupos[i].nombre, '%s' % self.parent.parent.subgrupos[i].nombre)
                if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto' and tuplaRaiz not in raicesUtilizadas:
                    raices.append(tuplaRaiz)

        else:
            raices.append((u'Edificio Objeto', 'Edificio Objeto'))
            for i in range(len(self.parent.parent.subgrupos)):
                if self.parent.parent.subgrupos[i].nombre != u'Edificio Objeto':
                    raices.append(('%s' % self.parent.parent.subgrupos[i].nombre, '%s' % self.parent.parent.subgrupos[i].nombre))

        return raices

    def onControlIluminacion(self, event):
        if self.sinControl == True and self.parent.parent.parent.programa == 'GranTerciario':
        elif self.sinControl == False and self.parent.parent.parent.programa == 'GranTerciario':

    def onDefinirSegunChoice(self, event):
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
        else:

    def onZonasRadio(self, event):
        antes = self.usoChoice.GetStringSelection()
        if self.zonaRepresentacionCheck == False:
            tabla = listadosWeb.tablaZona1
        else:
            tabla = listadosWeb.tablaZona2
        self.usoChoice.SetItems(tabla)
        if antes in tabla:
            self.usoChoice.SetStringSelection(antes)
        else:
            self.usoChoice.SetSelection(0)
        self.valoresPorDefectoIluminancia(None)
        return

    def comprobarDatos(self):
        superficie = self.superficieMuro
        iluminancia = self.iluminancia
        if ',' in superficie:
            superficie = superficie.replace(',', '.')
            self.superficieMuro= superficie
        if ',' in iluminancia:
            iluminancia = iluminancia.replace(',', '.')
            self.iluminancia= iluminancia
        self.listaErrores = u''
        self.listaErrores += Comprueba(self.nombreInstalacion, 1, self.listaErrores, 'nombre').ErrorDevuelto
        self.listaErrores += Comprueba(self.subgrupoChoice.GetStringSelection(), 0, self.listaErrores, 'zona').ErrorDevuelto
        self.listaErrores += Comprueba(self.superficieMuro, 2, self.listaErrores, 'superficie', 0).ErrorDevuelto
        self.listaErrores += Comprueba(self.usoChoice.GetStringSelection(), 0, self.listaErrores, 'uso').ErrorDevuelto
        self.listaErrores += Comprueba(self.definirSegunChoice.GetStringSelection(), 0, self.listaErrores, 'definir seg\xfan').ErrorDevuelto
        if self.parent.parent.parent.programa == 'GranTerciario' and self.conControl == True:
            superficieControl = self.superficieControl
            if ',' in superficieControl:
                superficieControl = superficieControl.replace(',', '.')
                self.superficieControl= superficieControl
            self.listaErrores += Comprueba(self.superficieControl, 2, self.listaErrores, 'superficie con control de la iluminaci\xf3n', 0.0).ErrorDevuelto
            try:
                if float(self.superficieMuro) < float(self.superficieControl):
                    if self.listaErrores != '':
                        self.listaErrores += ', '
                    self.listaErrores += 'la superficie con control de la iluminaci\xf3n es mayor que la superficie total de la zona'
            except (ValueError, TypeError):
                pass

        if 'Conocido' in self.definirSegunChoice.GetStringSelection():
            potencia = self.potenciaInstalada
            if ',' in potencia:
                potencia = potencia.replace(',', '.')
                self.potenciaInstalada= potencia
            self.listaErrores += Comprueba(self.potenciaInstalada, 2, self.listaErrores, 'potencia instalada', 0).ErrorDevuelto
        elif 'Estimado' in self.definirSegunChoice.GetStringSelection():
            self.listaErrores += Comprueba(self.tipoEquipoChoice.GetStringSelection(), 0, self.listaErrores, 'tipo de equipo').ErrorDevuelto
        self.listaErrores += Comprueba(self.iluminancia, 2, self.listaErrores, 'iluminancia media horizontal', 0).ErrorDevuelto

    def valoresPorDefectoIluminancia(self, event):
        if self.cambiandoIluminancia == False:
            iluminanciaZona1 = [500,
             500,
             300,
             500,
             100,
             100,
             300,
             700,
             500]
            iluminanciaZona2 = [500,
             300,
             200,
             200,
             100,
             200,
             200,
             200,
             300,
             300,
             100,
             200,
             500]
            if self.zonaRepresentacionCheck == False:
                tabla = iluminanciaZona1
            else:
                tabla = iluminanciaZona2
            valorPorDefecto = tabla[self.usoChoice.GetSelection()]
            antes = self.cambiandoIluminancia
            self.iluminancia= str(valorPorDefecto)
            self.cambiandoIluminancia = antes

    def OnCambioIluminancia(self, event):
        self.cambiandoIluminancia = True

    def obtenerValoresIluminacion(self):
        S = float(self.superficieMuro)
        Em = float(self.iluminancia)
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
            datosLuminaria = diccLuminarias[self.tipoEquipoChoice.GetStringSelection()]
            lumen_Watio = datosLuminaria[0]
            rendimientoLuminaria = datosLuminaria[1]
            lumen_Watio = lumen_Watio * rendimientoLuminaria
            self.potencia = Em * S / lumen_Watio
        else:
            self.potencia = float(self.potenciaInstalada)
        self.veei = self.potencia * 100 / S / Em

    def cogerDatos(self):
        if self.parent.parent.parent.programa == 'GranTerciario':
            if self.subgrupoChoice.GetItems() == []:
                return []
            zonaElegida = self.subgrupoChoice.GetStringSelection()
            raicesUtilizadas = []
            for ilum in self.parent.iluminacion:
                raicesUtilizadas.append(ilum[-1])

            if zonaElegida in raicesUtilizadas:
                raise Exception('La zona seleccionada ya tiene una instalaci\xf3n de iluminaci\xf3n')
                return []
        self.comprobarDatos()
        if self.listaErrores != u'':
            return self.listaErrores
        self.obtenerValoresIluminacion()
        datos = self.cogerDatosDelPanel()
        return datos

    def cogerDatosMM(self):
        self.comprobarDatos()
        if self.listaErrores != u'':
            return self.listaErrores
        self.obtenerValoresIluminacion()
        datos = self.cogerDatosDelPanel()
        return datos

    def cogerDatosDelPanel(self):
        datos = []
        datos.append(self.nombreInstalacion)
        datos.append('iluminacion')
        datos.append(self.potencia)
        datos.append(self.veei)
        datos.append('')
        datos.append(self.superficieMuro)
        datos.append(self.zonaRepresentacionCheck)
        datos.append(self.usoChoice.GetStringSelection())
        datos.append(self.definirSegunChoice.GetStringSelection())
        if 'Estimado' in self.definirSegunChoice.GetStringSelection():
            aux = [self.tipoEquipoChoice.GetStringSelection(), self.iluminancia]
        else:
            aux = [self.potenciaInstalada, self.iluminancia]
        datos.append(aux)
        aux = [self.conControl, self.superficieControl]
        datos.append(aux)
        datos.append(self.subgrupoChoice.GetStringSelection())
        return datos

    def cargarDatos(self, datos = [], instalacionIluminacion = []):
        self.nombreInstalacion= datos[0]
        self.superficieMuro= datos[5]
        self.zonaRepresentacionCheck= datos[6]
        self.onZonasRadio(None)
        self.usoChoice.SetStringSelection(datos[7])
        self.definirSegunChoice.SetStringSelection(datos[8])
        aux = datos[9]
        if 'Estimado' in datos[8]:
            self.tipoEquipoChoice.SetStringSelection(aux[0])
            self.iluminancia= aux[1]
        else:
            self.potenciaInstalada= aux[0]
            self.iluminancia= aux[1]
        self.cambiandoIluminancia = False
        aux = datos[10]
        self.conControl= aux[0]
        self.superficieControl= aux[1]
        self.onControlIluminacion(None)
        if self.parent.parent.parent.programa == 'GranTerciario':
            tuplaZonas = self.cargarRaices(instalacionIluminacion)
            zonaElegida = datos[11]
            if zonaElegida != u'Edificio Objeto':
                tuplaRaizInstalacionCargada = (zonaElegida, zonaElegida)
                tuplaZonas.append(tuplaRaizInstalacionCargada)
                self.subgrupoChoice.SetItems(tuplaZonas)
                self.subgrupoChoice.SetStringSelection(zonaElegida)
        else:
            self.subgrupoChoice.SetStringSelection(datos[11])
        self.onDefinirSegunChoice(None)
        return