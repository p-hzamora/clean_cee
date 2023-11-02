# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: AnalisisEconomico\panelResultadoAnalisis.pyc
# Compiled at: 2015-02-17 11:40:42
"""
Modulo: panelResultadoAnalisis.py

"""
from AnalisisEconomico.funcionesCalculoAnalisisEconomico import getDiccConsumosCBFacturasSgServicioYCombustible, comprobarEstanTodasFacturas, comprobarQueNoHayFacturasExtra, calculoDdaNetaCBFact, calculoCMfacturas, getDiccConsumosCMFacturasSgServicio, comprobarPreciosEnergia, getDiccConsumosContribuciones, calculoPrecioCombustibleConsumido, calculoPrecioCombustibleConsumidoPorServicio, guardarCostesConjuntosMM
from AnalisisEconomico.miGridAnalisisEconomico import MyGrid
from Calculos.funcionesCalculo import coeficienteDePasoEmisiones, calculoDdaBruta, calculoDdaNeta
from MedidasDeMejora.objetoGrupoMejoras import ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM
import AnalisisEconomico.analisisFinanciero as analisisFinanciero, datosEdificio, wx
wxID_PANEL1, wxID_PANEL1GRID1, wxID_PANEL1TITULOTEXT, wxID_PANEL1CALCULARBOTON = [ wx.NewId() for _init_ctrls in range(4) ]

class Panel1(wx.Panel):
    """
    Clase: Panel1 del modulo panelResultadoAnalisis.py

    """

    def _init_coll_tablaResultados_Columns(self, parent):
        """
        Metodo: _init_coll_tablaResultados_Columns

        ARGUMENTOS:
                 parent:
        """
        parent.CreateGrid(0, 5)
        parent.SetColLabelValue(0, _(' Conjunto de mejoras '))
        parent.SetColLabelValue(1, _('Años - Amortización simple\n (Análisis facturas) '))
        parent.SetColLabelValue(2, _('  VAN (€) \n (Facturas) '))
        parent.SetColLabelValue(3, _('Años - Amortización simple\n (Análisis teórico) '))
        parent.SetColLabelValue(4, _('  VAN (€) \n (Teórico) '))
        parent.AutoSizeColumns()

    def _init_ctrls(self, prnt, id_prnt, pos_prnt, size_prnt, style_prnt, name_prnt):
        """
        Metodo: _init_ctrls

        ARGUMENTOS:
                  prnt:
                 id_prnt:
                 pos_prnt:
                 size_prnt:
                 style_prnt:
                 name_prnt:
        """
        wx.Panel.__init__(self, id=id_prnt, name=name_prnt, parent=prnt, pos=pos_prnt, size=size_prnt, style=style_prnt | wx.TAB_TRAVERSAL)
        self.SetBackgroundColour('white')
        self.tituloText = wx.StaticText(id=wxID_PANEL1TITULOTEXT, label=_('Resultado del análisis económico'), name='tituloText', parent=self, pos=wx.Point(15, 24), size=wx.Size(281, 18), style=0)
        self.tituloText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.tituloText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.tablaResultados = MyGrid(id=wxID_PANEL1GRID1, parent=self, pos=wx.Point(15, 70), size=wx.Size(695, 400), style=wx.RAISED_BORDER | wx.TAB_TRAVERSAL)
        self._init_coll_tablaResultados_Columns(self.tablaResultados)
        self.calcularBoton = wx.Button(id=wxID_PANEL1CALCULARBOTON, label=_('Calcular'), name='calcularBoton', parent=self, pos=wx.Point(628, 530), size=wx.Size(80, 23), style=0)
        self.calcularBoton.Bind(wx.EVT_BUTTON, self.OnCalcularButton, id=wxID_PANEL1CALCULARBOTON)
        self.incluirConjuntosMedidas()

    def incluirConjuntosMedidas(self):
        """
        Metodo: incluirConjuntosMedidas

        """
        if self.tablaResultados.GetNumberRows() != 0:
            self.tablaResultados.DeleteRows(0, self.tablaResultados.GetNumberRows())
        listadoConjuntosMMUsuario = self.parent.parent.parent.listadoConjuntosMMUsuario
        cont = 0
        for i in range(len(listadoConjuntosMMUsuario)):
            conjuntoMM = listadoConjuntosMMUsuario[i]
            self.tablaResultados.AppendRows(1)
            try:
                payBackFacturas = str(round(float(conjuntoMM.analisisEconomico.analisisFacturas.payBack), 1))
            except:
                payBackFacturas = conjuntoMM.analisisEconomico.analisisFacturas.payBack

            try:
                vanFacturas = str(round(float(conjuntoMM.analisisEconomico.analisisFacturas.van), 1))
            except:
                vanFacturas = conjuntoMM.analisisEconomico.analisisFacturas.van

            try:
                payBackTeorico = str(round(float(conjuntoMM.analisisEconomico.analisisTeorico.payBack), 1))
            except:
                payBackTeorico = conjuntoMM.analisisEconomico.analisisTeorico.payBack

            try:
                vanTeorico = str(round(float(conjuntoMM.analisisEconomico.analisisTeorico.van), 1))
            except:
                vanTeorico = conjuntoMM.analisisEconomico.analisisTeorico.van

            self.tablaResultados.SetCellValue(cont, 0, conjuntoMM.nombre)
            self.tablaResultados.SetCellValue(cont, 1, payBackFacturas)
            self.tablaResultados.SetCellValue(cont, 2, vanFacturas)
            self.tablaResultados.SetCellValue(cont, 3, payBackTeorico)
            self.tablaResultados.SetCellValue(cont, 4, vanTeorico)
            self.tablaResultados.SetReadOnly(cont, 0)
            self.tablaResultados.SetReadOnly(cont, 1)
            self.tablaResultados.SetReadOnly(cont, 2)
            self.tablaResultados.SetReadOnly(cont, 3)
            self.tablaResultados.SetReadOnly(cont, 4)
            cont = cont + 1

        self.tablaResultados.AutoSizeColumns()

    def cogerDatos(self):
        """
        Metodo: cogerDatos
        no se utiliza esta funcion. Estaba antiguamente
        """
        pass

    def cargarDatos(self):
        """
        Metodo: cargarDatos

        """
        self.recargaTablaResultados()

    def OnCalcularButton(self, event):
        """
        Metodo: OnCalcularButton

        flag: indica si se deben mostrar los mensajes o no. Por defecto esta a 1, cuando le doy a calcular desde el analisis economico, muestra los errores.
        Si se llama desde el frame, esta a 0, y no muestra los mensajes de error.
    
        ARGUMENTOS:
                event:
        """
        self.parent.parent.parent.calculoAnalisisEconomico(flag=1)

    def recargaTablaResultados(self):
        if self.parent.parent.parent.objEdificio.casoValido == False:
            for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
                conjuntoMM.analisisEconomico.inicializar()

        i = 0
        for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
            try:
                self.tablaResultados.SetCellValue(i, 1, str(round(conjuntoMM.analisisEconomico.analisisFacturas.payBack, 1)))
                self.tablaResultados.SetCellValue(i, 2, str(round(conjuntoMM.analisisEconomico.analisisFacturas.van, 1)))
            except TypeError:
                self.tablaResultados.SetCellValue(i, 1, str(conjuntoMM.analisisEconomico.analisisFacturas.payBack))
                self.tablaResultados.SetCellValue(i, 2, str(conjuntoMM.analisisEconomico.analisisFacturas.van))

            try:
                self.tablaResultados.SetCellValue(i, 3, str(round(conjuntoMM.analisisEconomico.analisisTeorico.payBack, 1)))
                self.tablaResultados.SetCellValue(i, 4, str(round(conjuntoMM.analisisEconomico.analisisTeorico.van, 1)))
            except TypeError:
                self.tablaResultados.SetCellValue(i, 3, str(conjuntoMM.analisisEconomico.analisisTeorico.payBack))
                self.tablaResultados.SetCellValue(i, 4, str(conjuntoMM.analisisEconomico.analisisTeorico.van))

            i += 1

    def calculoAnalisisEconomico(self, flag=1):
        """
        flag: indica si se deben mostrar los mensajes o no. Por defecto esta a 1, cuando le doy a calcular desde el analisis economico, muestra los errores.
        Si se llama desde el frame, esta a 0, y no muestra los mensajes de error.
        
        La funcion devuelve True si se ha realizado correctamente el analisis economico o False si no se ha realizado
        """
        datosEconomicos = self.parent.panelDatosEconomicos.cogerDatos()
        faltanDatos, listaErrores, self.diccPreciosCombustibles, self.incrementoPrecioEnergia, self.tipoInteres = comprobarPreciosEnergia(datosEconomicos=datosEconomicos, objEdificio=self.parent.parent.parent.objEdificio, listadoConjuntosMMUsuario=self.parent.parent.parent.listadoConjuntosMMUsuario)
        if faltanDatos == True:
            for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
                conjuntoMM.analisisEconomico.inicializar()

            if flag:
                wx.MessageBox(_('Revise los siguientes campos:\n') + listaErrores + _('.'), _('Aviso'))
            return
        faltanDatos, listaErrores = self.cogerCostesMedidas()
        if faltanDatos == True:
            if flag:
                wx.MessageBox(_('Revise los datos del coste de las medidas para realizar el análisis económico de los siguientes conjuntos de medidas de mejora: \n') + listaErrores, _('Aviso'))
        analisisValido, listaErrores = self.calculoTeorico(flag)
        if analisisValido == False:
            if flag:
                wx.MessageBox(listaErrores, _('Aviso'))
        analisisValido, listaErrores = self.calculoFacturas(flag)
        if listaErrores != '':
            if flag:
                wx.MessageBox(listaErrores, _('Aviso'))

    def cogerCostesMedidas(self):
        """
        Para cada conjunto tomo datos de vidaUtil, inversionInicial y costeMantenimiento
        Son arrays con valores para cada medida
        """
        faltanDatos, listaErrores = guardarCostesConjuntosMM(listadoCosteMedidas=self.parent.panelCosteMedidas.cogerDatos(), listadoConjuntosMMUsuario=self.parent.parent.parent.listadoConjuntosMMUsuario)
        return (
         faltanDatos, listaErrores)

    def calculoTeorico(self, flag=1):
        """
        Metodo: calculoTeorico

        """
        analisisValido = True
        listaErrores = ''
        objEdificio = self.parent.parent.parent.objEdificio
        area = objEdificio.datosIniciales.area
        precio_CB_teor = calculoPrecioCombustibleConsumido(diccConsumoCombustible=objEdificio.datosResultados.calculoConsumoEnFinalSegunCombustible(), diccPreciosCombustibles=self.diccPreciosCombustibles, area=area)
        encabezadoError = _('No se ha podido calcular el análisis económico teórico de los siguientes conjuntos de medida de mejora:\n')
        for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
            numeroMedidasConjunto = conjuntoMM.getNumeroMedidasConjunto()
            if conjuntoMM.datosNuevoEdificio.casoValido == False or conjuntoMM.datosEdificioOriginal.casoValido == False:
                if analisisValido == True:
                    listaErrores += encabezadoError
                conjuntoMM.analisisEconomico.inicializar()
                auxNombre = conjuntoMM.nombre.encode('cp1252')
                errorMedida = '   - %s\n' % auxNombre
                listaErrores += errorMedida
                analisisValido = False
            elif len(conjuntoMM.analisisEconomico.vidaUtil) != numeroMedidasConjunto or len(conjuntoMM.analisisEconomico.inversionInicial) != numeroMedidasConjunto or len(conjuntoMM.analisisEconomico.costeMantenimiento) != numeroMedidasConjunto:
                conjuntoMM.analisisEconomico.inicializar()
            else:
                try:
                    precio_CM_teor = calculoPrecioCombustibleConsumido(diccConsumoCombustible=conjuntoMM.datosNuevoEdificio.datosResultados.calculoConsumoEnFinalSegunCombustible(), diccPreciosCombustibles=self.diccPreciosCombustibles, area=area)
                    ahorroEconomicoAnual = precio_CB_teor - precio_CM_teor
                    payBackTeorico = analisisFinanciero.payBack(inversionInicial=conjuntoMM.analisisEconomico.inversionInicial, ahorroEconomicoAnual=ahorroEconomicoAnual, costesMantenimientoAnual=sum(conjuntoMM.analisisEconomico.costeMantenimiento), vidaUtil=conjuntoMM.analisisEconomico.vidaUtil)
                    vanTeorico = analisisFinanciero.van(inversionInicial=conjuntoMM.analisisEconomico.inversionInicial, ahorroEconomicoAnual=ahorroEconomicoAnual, tasaIncrementoPrecioEnergia=float(self.incrementoPrecioEnergia) / 100.0, costesMantenimientoAnual=sum(conjuntoMM.analisisEconomico.costeMantenimiento), tasaRetornoInversion=float(self.tipoInteres) / 100.0, vidaUtil=conjuntoMM.analisisEconomico.vidaUtil)
                    conjuntoMM.analisisEconomico.analisisTeorico.guardarResultados(van=vanTeorico, payBack=payBackTeorico, precioAnual_CB=precio_CB_teor, precioAnual_CM=precio_CM_teor, ahorroEconomico=ahorroEconomicoAnual)
                except:
                    if analisisValido == True:
                        listaErrores += encabezadoError
                    conjuntoMM.analisisEconomico.inicializar()
                    auxNombre = conjuntoMM.nombre.encode('cp1252')
                    errorMedida = '   - %s\n' % auxNombre
                    listaErrores += errorMedida
                    analisisValido = False

        return (
         analisisValido, listaErrores)

    def calculoFacturas(self, flag=1):
        """
        Metodo: calculoFacturas
    
        Devuelve listadoErrores que puede ser '' o str

        """
        analisisValido = True
        listaErrores = ''
        objEdificio = self.parent.parent.parent.objEdificio
        area = objEdificio.datosIniciales.area
        extrapeninsular = objEdificio.datosIniciales.extrapeninsular
        if self.parent.objetosFactura == []:
            listaErrores = _('Sólo se va a realizar el análisis económico teórico ya que no se han definido las facturas y por lo tanto no hay datos suficientes para hacer el análisis económico según facturas.')
            analisisValido = False
            return (analisisValido, listaErrores)
        diccCal_CB_fact, diccRef_CB_fact, diccACS_CB_fact, diccIlum_CB_fact, diccVentiladores_CB_fact, diccBombas_CB_fact, diccTorresRef_CB_fact = getDiccConsumosCBFacturasSgServicioYCombustible(listadoFacturas=self.parent.objetosFactura, area=area, programa=objEdificio.programa)
        arrayErrores = comprobarEstanTodasFacturas(listadoACS_CB=objEdificio.datosIniciales.ACS.listado, listadoCal_CB=objEdificio.datosIniciales.calefaccion.listado, listadoRef_CB=objEdificio.datosIniciales.refrigeracion.listado, listadoIlum_CB=objEdificio.datosIniciales.sistemasIluminacion, listadoVentiladores_CB=objEdificio.datosIniciales.sistemasVentiladores, listadoBombas_CB=objEdificio.datosIniciales.sistemasBombas, listadoTorresRef_CB=objEdificio.datosIniciales.sistemasTorresRefrigeracion, diccCal_CB_fact=diccCal_CB_fact, diccRef_CB_fact=diccRef_CB_fact, diccACS_CB_fact=diccACS_CB_fact, diccIlum_CB_fact=diccIlum_CB_fact, diccVentiladores_CB_fact=diccVentiladores_CB_fact, diccBombas_CB_fact=diccBombas_CB_fact, diccTorresRef_CB_fact=diccTorresRef_CB_fact)
        if arrayErrores != []:
            listaErrores += _('Para realizar el análisis económico a partir de los datos de las facturas debe indicar: \n')
            for i in arrayErrores:
                listaErrores += i

            analisisValido = False
            for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
                conjuntoMM.analisisEconomico.inicializarAnalisisFacturas()

            return (
             analisisValido, listaErrores)
        arrayErrores = comprobarQueNoHayFacturasExtra(listadoACS_CB=objEdificio.datosIniciales.ACS.listado, listadoCal_CB=objEdificio.datosIniciales.calefaccion.listado, listadoRef_CB=objEdificio.datosIniciales.refrigeracion.listado, listadoIlum_CB=objEdificio.datosIniciales.sistemasIluminacion, listadoVentiladores_CB=objEdificio.datosIniciales.sistemasVentiladores, listadoBombas_CB=objEdificio.datosIniciales.sistemasBombas, listadoTorresRef_CB=objEdificio.datosIniciales.sistemasTorresRefrigeracion, diccCal_CB_fact=diccCal_CB_fact, diccRef_CB_fact=diccRef_CB_fact, diccACS_CB_fact=diccACS_CB_fact, diccIlum_CB_fact=diccIlum_CB_fact, diccVentiladores_CB_fact=diccVentiladores_CB_fact, diccBombas_CB_fact=diccBombas_CB_fact, diccTorresRef_CB_fact=diccTorresRef_CB_fact)
        if arrayErrores != []:
            listaErrores += _('No se puede realizar el análisis económico porque se han definido las siguientes facturas cuyo consumo no se ha definido en el edificio objeto de la certificación: \n')
            for i in arrayErrores:
                listaErrores += i

            analisisValido = False
            for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
                conjuntoMM.analisisEconomico.inicializarAnalisisFacturas()

            return (
             analisisValido, listaErrores)
        diccContribuciones_CB_fact = getDiccConsumosContribuciones(listadoContribuciones=objEdificio.datosIniciales.contribuciones, area=area)
        precio_CB_fact = calculoPrecioCombustibleConsumidoPorServicio(diccCal=diccCal_CB_fact, diccRef=diccRef_CB_fact, diccACS=diccACS_CB_fact, diccIlum=diccIlum_CB_fact, diccVentiladores=diccVentiladores_CB_fact, diccBombas=diccBombas_CB_fact, diccTorresRef=diccTorresRef_CB_fact, diccContribuciones=diccContribuciones_CB_fact, diccPreciosCombustibles=self.diccPreciosCombustibles, area=area)
        ddaNetaACS_CB_fact = calculoDdaNetaCBFact(instServicio=objEdificio.datosIniciales.ACS, dicc_CB_fact=diccACS_CB_fact)
        ddaNetaCal_CB_fact = calculoDdaNetaCBFact(instServicio=objEdificio.datosIniciales.calefaccion, dicc_CB_fact=diccCal_CB_fact)
        ddaNetaRef_CB_fact = calculoDdaNetaCBFact(instServicio=objEdificio.datosIniciales.refrigeracion, dicc_CB_fact=diccRef_CB_fact)
        contribGeneracionACS = objEdificio.datosIniciales.contribuciones.calorRecupACSTotal / objEdificio.datosIniciales.area
        contribGeneracionCal = objEdificio.datosIniciales.contribuciones.calorRecupACSTotal / objEdificio.datosIniciales.area
        contribGeneracionRef = objEdificio.datosIniciales.contribuciones.calorRecupACSTotal / objEdificio.datosIniciales.area
        ddaBrutaACS_CB_fact = calculoDdaBruta(ddaNeta=ddaNetaACS_CB_fact, porcTermica=objEdificio.datosIniciales.contribuciones.porcACSTotal, contribGeneracion=contribGeneracionACS)
        ddaBrutaCal_CB_fact = calculoDdaBruta(ddaNeta=ddaNetaCal_CB_fact, porcTermica=objEdificio.datosIniciales.contribuciones.porcCalTotal, contribGeneracion=contribGeneracionCal)
        ddaBrutaRef_CB_fact = calculoDdaBruta(ddaNeta=ddaNetaRef_CB_fact, porcTermica=objEdificio.datosIniciales.contribuciones.porcRefTotal, contribGeneracion=contribGeneracionRef)
        encabezadoError = _('No se ha podido calcular el análisis económico según facturas de los siguientes conjuntos de medidas de mejora:\n')
        for conjuntoMM in self.parent.parent.parent.listadoConjuntosMMUsuario:
            numeroMedidasConjunto = conjuntoMM.getNumeroMedidasConjunto()
            if conjuntoMM.datosNuevoEdificio.casoValido == False or conjuntoMM.datosEdificioOriginal.casoValido == False:
                if analisisValido == True:
                    listaErrores += encabezadoError
                conjuntoMM.analisisEconomico.inicializar()
                auxNombre = conjuntoMM.nombre.encode('cp1252')
                errorMedida = '   - %s\n' % auxNombre
                listaErrores += errorMedida
                analisisValido = False
            elif len(conjuntoMM.analisisEconomico.vidaUtil) != numeroMedidasConjunto or len(conjuntoMM.analisisEconomico.inversionInicial) != numeroMedidasConjunto or len(conjuntoMM.analisisEconomico.costeMantenimiento) != numeroMedidasConjunto:
                conjuntoMM.analisisEconomico.inicializar()
            else:
                try:
                    ddaBrutaACS_CB_teor = objEdificio.datosResultados.ddaBrutaACS
                    ddaBrutaACS_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaACS
                    ddaBrutaACS_CM_fact = calculoCMfacturas(valor_CB_teor=ddaBrutaACS_CB_teor, valor_CM_teor=ddaBrutaACS_CM_teor, valor_CB_fact=ddaBrutaACS_CB_fact)
                    ddaBrutaCal_CB_teor = objEdificio.datosResultados.ddaBrutaCal
                    ddaBrutaCal_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal
                    ddaBrutaCal_CM_fact = calculoCMfacturas(valor_CB_teor=ddaBrutaCal_CB_teor, valor_CM_teor=ddaBrutaCal_CM_teor, valor_CB_fact=ddaBrutaCal_CB_fact)
                    ddaBrutaRef_CB_teor = objEdificio.datosResultados.ddaBrutaRef
                    ddaBrutaRef_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef
                    ddaBrutaRef_CM_fact = calculoCMfacturas(valor_CB_teor=ddaBrutaRef_CB_teor, valor_CM_teor=ddaBrutaRef_CM_teor, valor_CB_fact=ddaBrutaRef_CB_fact)
                    if conjuntoMM.datosNuevoEdificio.programa != 'Residencial':
                        enFinalIlum_CB_teor = objEdificio.datosResultados.enFinalRealIlum
                        enFinalIlum_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRealIlum
                        enFinalIlum_CB_fact = diccIlum_CB_fact['Electricidad']
                        enFinalIlum_CM_fact = calculoCMfacturas(valor_CB_teor=enFinalIlum_CB_teor, valor_CM_teor=enFinalIlum_CM_teor, valor_CB_fact=enFinalIlum_CB_fact)
                        if conjuntoMM.datosNuevoEdificio.programa == 'GranTerciario':
                            enFinalVentiladores_CB_teor = objEdificio.datosResultados.enFinalRealVentiladores
                            enFinalVentiladores_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRealVentiladores
                            enFinalVentiladores_CB_fact = diccVentiladores_CB_fact['Electricidad']
                            enFinalVentiladores_CM_fact = calculoCMfacturas(valor_CB_teor=enFinalVentiladores_CB_teor, valor_CM_teor=enFinalVentiladores_CM_teor, valor_CB_fact=enFinalVentiladores_CB_fact)
                            enFinalBombas_CB_teor = objEdificio.datosResultados.enFinalRealBombas
                            enFinalBombas_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRealBombas
                            enFinalBombas_CB_fact = diccBombas_CB_fact['Electricidad']
                            enFinalBombas_CM_fact = calculoCMfacturas(valor_CB_teor=enFinalBombas_CB_teor, valor_CM_teor=enFinalBombas_CM_teor, valor_CB_fact=enFinalBombas_CB_fact)
                            enFinalTorresRef_CB_teor = objEdificio.datosResultados.enFinalRealTorresRef
                            enFinalTorresRef_CM_teor = conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRealTorresRef
                            enFinalTorresRef_CB_fact = diccTorresRef_CB_fact['Electricidad']
                            enFinalTorresRef_CM_fact = calculoCMfacturas(valor_CB_teor=enFinalTorresRef_CB_teor, valor_CM_teor=enFinalTorresRef_CM_teor, valor_CB_fact=enFinalTorresRef_CB_fact)
                        else:
                            enFinalVentiladores_CM_fact = 0
                            enFinalBombas_CM_fact = 0
                            enFinalTorresRef_CM_fact = 0
                    else:
                        enFinalIlum_CM_fact = 0
                        enFinalVentiladores_CM_fact = 0
                        enFinalBombas_CM_fact = 0
                        enFinalTorresRef_CM_fact = 0
                    ddaNetaACS_CM_fact = calculoDdaNeta(ddaBruta=ddaBrutaACS_CM_fact, porcTermica=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcACSTotal, contribGeneracion=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.calorRecupACSTotal / area)
                    ddaNetaCal_CM_fact = calculoDdaNeta(ddaBruta=ddaBrutaCal_CM_fact, porcTermica=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcCalTotal, contribGeneracion=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.calorRecupCalTotal / area)
                    ddaNetaRef_CM_fact = calculoDdaNeta(ddaBruta=ddaBrutaRef_CM_fact, porcTermica=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcRefTotal, contribGeneracion=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.calorRecupRefTotal / area)
                    diccCal_CM_fact = getDiccConsumosCMFacturasSgServicio(ddaNeta=ddaNetaCal_CM_fact, instServicio=conjuntoMM.datosNuevoEdificio.datosIniciales.calefaccion)
                    diccRef_CM_fact = getDiccConsumosCMFacturasSgServicio(ddaNeta=ddaNetaRef_CM_fact, instServicio=conjuntoMM.datosNuevoEdificio.datosIniciales.refrigeracion)
                    diccACS_CM_fact = getDiccConsumosCMFacturasSgServicio(ddaNeta=ddaNetaACS_CM_fact, instServicio=conjuntoMM.datosNuevoEdificio.datosIniciales.ACS)
                    diccIlum_CM_fact = {'Electricidad': enFinalIlum_CM_fact}
                    diccVentiladores_CM_fact = {'Electricidad': enFinalVentiladores_CM_fact}
                    diccBombas_CM_fact = {'Electricidad': enFinalBombas_CM_fact}
                    diccTorresRef_CM_fact = {'Electricidad': enFinalTorresRef_CM_fact}
                    diccContribuciones_CM_fact = getDiccConsumosContribuciones(listadoContribuciones=conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones, area=area)
                    precio_CM_fact = calculoPrecioCombustibleConsumidoPorServicio(diccCal=diccCal_CM_fact, diccRef=diccRef_CM_fact, diccACS=diccACS_CM_fact, diccIlum=diccIlum_CM_fact, diccVentiladores=diccVentiladores_CM_fact, diccBombas=diccBombas_CM_fact, diccTorresRef=diccTorresRef_CM_fact, diccContribuciones=diccContribuciones_CM_fact, diccPreciosCombustibles=self.diccPreciosCombustibles, area=area)
                    ahorroEconomicoAnual = precio_CB_fact - precio_CM_fact
                    payBackFacturas = analisisFinanciero.payBack(inversionInicial=conjuntoMM.analisisEconomico.inversionInicial, ahorroEconomicoAnual=ahorroEconomicoAnual, costesMantenimientoAnual=sum(conjuntoMM.analisisEconomico.costeMantenimiento), vidaUtil=conjuntoMM.analisisEconomico.vidaUtil)
                    vanFacturas = analisisFinanciero.van(inversionInicial=conjuntoMM.analisisEconomico.inversionInicial, ahorroEconomicoAnual=ahorroEconomicoAnual, tasaIncrementoPrecioEnergia=float(self.incrementoPrecioEnergia) / 100.0, costesMantenimientoAnual=sum(conjuntoMM.analisisEconomico.costeMantenimiento), tasaRetornoInversion=float(self.tipoInteres) / 100.0, vidaUtil=conjuntoMM.analisisEconomico.vidaUtil)
                    conjuntoMM.analisisEconomico.analisisFacturas.guardarResultados(van=vanFacturas, payBack=payBackFacturas, precioAnual_CB=precio_CB_fact, precioAnual_CM=precio_CM_fact, ahorroEconomico=ahorroEconomicoAnual)
                    conjuntoMM.analisisEconomico.analisisFacturas.resultadosCB = ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM(diccCal=diccCal_CB_fact, diccRef=diccRef_CB_fact, diccACS=diccACS_CB_fact, diccIlum=diccIlum_CB_fact, diccVentiladores=diccVentiladores_CB_fact, diccBombas=diccBombas_CB_fact, diccTorresRef=diccTorresRef_CB_fact, diccContribuciones=diccContribuciones_CB_fact, ddaBrutaCal=ddaBrutaCal_CB_fact, ddaBrutaRef=ddaBrutaRef_CB_fact, ddaBrutaACS=ddaBrutaACS_CB_fact, ddaNetaCal=ddaNetaCal_CB_fact, ddaNetaRef=ddaNetaRef_CB_fact, ddaNetaACS=ddaNetaACS_CB_fact)
                    conjuntoMM.analisisEconomico.analisisFacturas.resultadosCM = ResultadoDemandasyConsumosAnalisisEconomicoConjuntoMM(diccCal=diccCal_CM_fact, diccRef=diccRef_CM_fact, diccACS=diccACS_CM_fact, diccIlum=diccIlum_CB_fact, diccVentiladores=diccVentiladores_CM_fact, diccBombas=diccBombas_CM_fact, diccTorresRef=diccTorresRef_CM_fact, diccContribuciones=diccContribuciones_CM_fact, ddaBrutaCal=ddaBrutaCal_CM_fact, ddaBrutaRef=ddaBrutaRef_CM_fact, ddaBrutaACS=ddaBrutaACS_CM_fact, ddaNetaCal=ddaNetaCal_CM_fact, ddaNetaRef=ddaNetaRef_CM_fact, ddaNetaACS=ddaNetaACS_CM_fact)
                except:
                    if analisisValido == True:
                        listaErrores += encabezadoError
                    conjuntoMM.analisisEconomico.inicializarAnalisisFacturas()
                    auxNombre = conjuntoMM.nombre.encode('cp1252')
                    errorMedida = '   - %s\n' % auxNombre
                    listaErrores += errorMedida
                    analisisValido = False

        return (
         analisisValido, listaErrores)

    def __init__(self, parent, id, pos, size, style, name, real_parent):
        """
        Constructor de la clase

        ARGUMENTOS:
                 parent:
                 id:
                 pos:
                 size:
                 style:
                 name:
                real_parent:
        """
        self.parent = real_parent
        self.diccPreciosCombustibles = []
        self._init_ctrls(parent, id, pos, size, style, name)


class resultadoEconomicoTeorico():
    pass


class resultadoEconomicoFacturas():
    pass