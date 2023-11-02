# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: tips.pyc
# Compiled at: 2015-05-25 19:33:25
"""
Modulo: tips.py

"""
from Calculos.funcionesCalculo import coeficienteDePasoEmisiones, diccLuminarias
import wx
k_gasNatural_emisiones = coeficienteDePasoEmisiones(combustible='Gas Natural')
k_gasoil_emisiones = coeficienteDePasoEmisiones(combustible='Gasóleo-C')
k_electricidad_emisiones = coeficienteDePasoEmisiones(combustible='Electricidad')
k_glp_emisiones = coeficienteDePasoEmisiones(combustible='GLP')
k_carbon_emisiones = coeficienteDePasoEmisiones(combustible='Carbón')
k_biocarburante_emisiones = coeficienteDePasoEmisiones(combustible='Biocarburante')
k_biomasaNoDens_emisiones = coeficienteDePasoEmisiones(combustible='Biomasa/Renovable')
k_biomasaDens_emisiones = coeficienteDePasoEmisiones(combustible='BiomasaDens')
mensajeCoeficientesPaso = _('Los coeficientes de paso de kWh a kg de CO2 son:\nGas natural: %s kgCO2/kWh\nGasóleo-C: %s kgCO2/kWh\nElectricidad (peninsular): %s kgCO2/kWh\nGLP: %s kgCO2/kWh\nCarbón: %s kgCO2/kWh\nBiocarburante: %s kgCO2/kWh\nBiomasa no densificada: %s kgCO2/kWh\nBiomasa densificada (pelets): %s kgCO2/kWh') % (k_gasNatural_emisiones,
 k_gasoil_emisiones,
 k_electricidad_emisiones,
 k_glp_emisiones,
 k_carbon_emisiones,
 k_biocarburante_emisiones,
 k_biomasaNoDens_emisiones,
 k_biomasaDens_emisiones)

def tips(self):
    """
    Metodo: tips

    ARGUMENTOS:
    """
    self.panelDatosGenerales.anoConstruccionChoice.SetToolTip(wx.ToolTip(_('Seleccione la normativa vigente en el momento de proyectar del edificio.')))
    self.panelDatosGenerales.provinciaChoice.SetToolTip(wx.ToolTip(_('Seleccione la provincia o la ciudad autónoma en la que en la que se encuentra situado el edificio objeto de la certificación')))
    self.panelDatosGenerales.tipoEdificioChoice.SetToolTip(wx.ToolTip(_('Unifamiliar, vivienda en bloque o una vivienda individual dentro un bloque')))
    self.panelDatosGenerales.localidadChoice.SetToolTip(wx.ToolTip(_('Seleccione la ciudad más próxima al emplazamiento del edificio')))
    self.panelDatosGenerales.HE1.SetToolTip(wx.ToolTip(_('Seleccione la zona climática que según el CTE-HE1 le correspondería al edificio')))
    self.panelDatosGenerales.HE4.SetToolTip(wx.ToolTip(_('Seleccione la zona climática que según el CTE-HE4 le correspondería al edificio')))
    self.panelDatosGenerales.masaParticiones.SetToolTip(wx.ToolTip(_('Seleccione la opción más conveniente para describir la masa de los forjados y particiones interiores:\n - Ligera: masa inferior a 200 kg/m2\n - Media: masa entre 200 y 500 kg/m2\n - Pesada: masa superior a 500 kg/m2')))
    self.panelDatosGenerales.otroCuadro.SetToolTip(wx.ToolTip('Indique el nombre de la localidad'))
    self.panelDatosGenerales.superficie.SetToolTip(wx.ToolTip(_('Superficie total de los recintos habitables.')))
    self.panelDatosGenerales.alturaMediaLibre.SetToolTip(wx.ToolTip(_('Media ponderada por las superficies, de las distancias interiores entre el suelo y el techo')))
    self.panelDatosGenerales.numeroPlantas.SetToolTip(wx.ToolTip(_('Número de plantas en las que se distribuye la superficie total habitable.\nSe debe incluir la planta baja si cuenta con superficie habitable.')))
    self.panelDatosGenerales.ventilacion.SetToolTip(wx.ToolTip(_('Tasa de ventilación del inmueble en renovaciones a la hora.')))
    self.panelDatosGenerales.consumoACS.SetToolTip(wx.ToolTip(_('Consumo de ACS diario en edificios del sector terciario')))
    self.panelDatosGenerales.Q50Cuadro.SetToolTip(wx.ToolTip(_('Es el caudal de infiltracion cuando la diferencia de presiones es de 50 Pa')))
    self.panelDatosGenerales.NCuadro.SetToolTip(wx.ToolTip(_('Exponente de la presión en la curva que relaciona el caudal con la presión')))
    self.panelDatosGenerales.normativaHelpButton.SetToolTip(wx.ToolTip(_('Si desconoce la normativa vigente, pulsa aqui para introducir el año de construcción del edificio.')))
    self.panelDatosGenerales.imagenButton.SetToolTip(wx.ToolTip(_('Cargue una imagen del edificio.')))
    self.panelDatosGenerales.planoButton.SetToolTip(wx.ToolTip(_('Cargue el plano de situación del edificio.')))
    self.panelDatosGenerales.Extrapeninsular.SetToolTip(wx.ToolTip(_('Si la localidad se encuentra fuera de la península ibérica debe activar esta casilla.')))
    self.panelDatosGenerales.ExentoHE4.SetToolTip(wx.ToolTip(_('Si el edificio se fuese a construir hoy en día y estuviese exento de poner placas solares por razones históricos artísticas, deberá activar esta casilla.')))
    self.panelDatosGenerales.BlowerDoorCheck.SetToolTip(wx.ToolTip(_('Si ha realizado un ensayo de permeabilidad del edificio pueda activar esta casilla. \nLa estanqueidad de la envolvente se determinará en función de lo que usted indique aquí.')))
    self.panelDatosGenerales.anoConstruccionNumeroCuadro.SetToolTip(wx.ToolTip(_('Indique el año de construcción del edificio')))
    self.panelDatosGenerales.tipoEdificioTerciarioChoice.SetToolTip(wx.ToolTip(_('Indique si se certifica el bloque completo o un local del mismo')))
    tip = wx.ToolTip(_('Indique un nombre identificativo del edificio o de la parte que se certifica'))
    self.panelDatosAdministrativos.nombreEdificio.SetToolTip(tip)
    self.panelDatosAdministrativos.direccionEdificio.SetToolTip(wx.ToolTip(_('Indique el tipo y nombre de la vía, número, piso y letra del edificio o de la parte que se certifica')))
    self.panelDatosAdministrativos.provinciaChoice.SetToolTip(wx.ToolTip(_('Seleccione la provincia o ciudad autónoma en la que se sitúa el edificio a certificar')))
    self.panelDatosAdministrativos.localidadChoice.SetToolTip(wx.ToolTip(_('Seleccione la localidad en la que se sitúa el edificio a certificar')))
    self.panelDatosAdministrativos.otroCuadro.SetToolTip(wx.ToolTip(_('Indique el nombre de la localidad en la que se sitúa el edificio a certificar')))
    self.panelDatosAdministrativos.codigoPostalEdificioCuadro.SetToolTip(wx.ToolTip(_('Indique el código postal del edificio a certificar')))
    self.panelDatosAdministrativos.referenciaCatastralEdificioCuadro.SetToolTip(wx.ToolTip(_('Indique la referencia catastral del edificio o de la parte que se certifica.')))
    self.panelDatosAdministrativos.referenciaCatastralButton.SetToolTip(wx.ToolTip(_('Indicar más de una referencia catastral para el inmueble que se certifica.')))
    self.panelDatosAdministrativos.nombreCliente.SetToolTip(wx.ToolTip(_('Indique la razón social o el nombre de la persona de contacto que ha encargado la certificación')))
    self.panelDatosAdministrativos.direccionCliente.SetToolTip(wx.ToolTip(_('Indique la dirección del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.provinciaClienteChoice.SetToolTip(wx.ToolTip(_('Seleccione la provincia o ciudad autónoma del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.localidadClienteCuadro.SetToolTip(wx.ToolTip(_('Indique la localidad del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.codigoPostalClienteCuadro.SetToolTip(wx.ToolTip(_('Indique el código postal del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.telefonoCliente.SetToolTip(wx.ToolTip(_('Indique el número de teléfono de contacto del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.mailCliente.SetToolTip(wx.ToolTip(_('Indique el correo electrónico de contacto del cliente que ha encargado la certificación')))
    self.panelDatosAdministrativos.certificadorAutor.SetToolTip(wx.ToolTip(_('Indique el nombre y apellidos del técnico certificador')))
    self.panelDatosAdministrativos.nifCertificadorCuadro.SetToolTip(wx.ToolTip(_('Indique el NIF del técnico certificador')))
    self.panelDatosAdministrativos.certificadorEmpresa.SetToolTip(wx.ToolTip(_('Indique el nombre de la empresa que se encarga de realizar la certificación')))
    self.panelDatosAdministrativos.cifCertificadorCuadro.SetToolTip(wx.ToolTip(_('Indique el CIF de la empresa encargada de la certificación')))
    self.panelDatosAdministrativos.direccionCertificador.SetToolTip(wx.ToolTip(_('Indique la dirección de la empresa o del técnico certificador')))
    self.panelDatosAdministrativos.provinciaCertificadorChoice.SetToolTip(wx.ToolTip(_('Seleccione la provincia o ciudad autónoma de la empresa o del técnico certificador')))
    self.panelDatosAdministrativos.localidadCertificadorCuadro.SetToolTip(wx.ToolTip(_('Indique la localidad de la empresa o del técnico certificador')))
    self.panelDatosAdministrativos.codigoPostalCertificadorCuadro.SetToolTip(wx.ToolTip(_('Indique el código postal de la empresa o del técnico certificador')))
    self.panelDatosAdministrativos.certificadorTelefono.SetToolTip(wx.ToolTip(_('Indique el teléfono de contacto con el técnico certificador')))
    self.panelDatosAdministrativos.certificadorMail.SetToolTip(wx.ToolTip(_('Indique el correo electrónico de contacto del técnico certificador')))
    self.panelDatosAdministrativos.titulacionHabilitanteCuadro.SetToolTip(wx.ToolTip(_('Indique la titulación del técnico que le habilita para realizar la certificación energética del edificio según la normativa vigente')))
    self.panelEnvolvente.nuevoSubgrupo.SetToolTip(wx.ToolTip(_('Defina un elemento de agrupamiento en el árbol de objetos.\nEn residencial y pequeño terciario los agrupamientos no tienen efecto sobre la calificación\n y su uso se propone por razones organizativas.\nEn gran terciario, si se dispone de regulación por iluminación natural, es necesario zonificar \nlos espacios que cuenten con estos dispositivos.')))
    self.panelInstalaciones.nuevoSubgrupo.SetToolTip(wx.ToolTip(_('Defina un elemento de agrupamiento en el árbol de objetos.\nEn residencial y pequeño terciario los agrupamientos no tienen efecto sobre la calificación\n y su uso se propone por razones organizativas.\nEn gran terciario, si se dispone de regulación por iluminación natural, es necesario zonificar \nlos espacios que cuenten con estos dispositivos.')))
    self.panelEnvolvente.panelElegirObjeto.puentesTermicosDefecto.SetToolTip(wx.ToolTip(_('Genera los puentes térmicos automáticamente.\nSu valor será función de la zona climática y de la solución constructiva.\nEs conveniente repasar sus valores.')))
    self.panelEnvolvente.panelElegirObjeto.definirCubierta.SetToolTip(wx.ToolTip(_('Define una cubierta en contacto con el aire o con el terreno.')))
    self.panelEnvolvente.panelElegirObjeto.definirFachada.SetToolTip(wx.ToolTip(_('Define una fachada en contacto con el terreno o con el aire o con otro edificio.')))
    self.panelEnvolvente.panelElegirObjeto.definirSuelo.SetToolTip(wx.ToolTip(_('Define un suelo en contacto con el terreno o con el aire.')))
    self.panelEnvolvente.panelElegirObjeto.definirHueco.SetToolTip(wx.ToolTip(_('Define una puerta, ventana o lucernario.')))
    self.panelEnvolvente.panelElegirObjeto.definirParticionInterior.SetToolTip(wx.ToolTip(_('Define la partición interior que se encuentra en contacto con un espacio no habitable.\nLas opciones son: vertical, horizontal en contacto con un espacio no habitable arriba o abajo.')))
    self.panelEnvolvente.panelElegirObjeto.definirPuenteTermico.SetToolTip(wx.ToolTip(_('Define los puentes térmicos de forma automática (por defecto) o individualmente.')))
    self.panelEnvolvente.panelElegirObjeto.contactoSuelo.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panelElegirObjeto.contactoAire.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panelElegirObjeto.contactoEdificio.SetToolTip(wx.ToolTip(_('El cerramiento sólo afectará a la inercia térmica del edificio.')))
    self.panelEnvolvente.panelElegirObjeto.vertical.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panelElegirObjeto.horizontalSuperior.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panelElegirObjeto.horizontalInferior.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panelBotones.anadirBoton.SetToolTip(wx.ToolTip(_('Añadir un elemento nuevo.')))
    self.panelEnvolvente.panelBotones.modificarBoton.SetToolTip(wx.ToolTip(_('Cambia el elemento existente')))
    self.panelEnvolvente.panelBotones.borrarBoton.SetToolTip(wx.ToolTip(_('Eliminar el elemento seleccionado.')))
    self.panelEnvolvente.panelBotones.vistaClasicaBoton.SetToolTip(wx.ToolTip(_('Vista en modo listado de los cerramientos.')))
    self.panelEnvolvente.panelBotones.vistaNormalBoton.SetToolTip(wx.ToolTip(_('Vista en modo paneles de los cerramientos.')))
    self.panelInstalaciones.panelElegirObjeto.definirACS.SetToolTip(wx.ToolTip(_('Equipo dedicado exclusivamente al ACS (tipo caldera o bomba de calor)')))
    self.panelInstalaciones.panelElegirObjeto.definirCalefaccion.SetToolTip(wx.ToolTip(_('Equipo dedicado exclusivamente al servicio de calefacción.')))
    self.panelInstalaciones.panelElegirObjeto.definirRefrigeracion.SetToolTip(wx.ToolTip(_('Equipo dedicado exclusivamente al servicio de refrigeración.')))
    self.panelInstalaciones.panelElegirObjeto.definirCaleYRefri.SetToolTip(wx.ToolTip(_('Equipo dedicado a los servicios de calefacción y refrigeración (bomba de calor). ')))
    self.panelInstalaciones.panelElegirObjeto.definirSistemasMixtosCaleyACS.SetToolTip(wx.ToolTip(_('Equipo dedicado a la calefacción y a la preparación de ACS')))
    self.panelInstalaciones.panelElegirObjeto.definirSistemasMixtosClimayACS.SetToolTip(wx.ToolTip(_('Equipo dedicado a la calefacción, refrigeración y preparación de ACS (bomba de calor)')))
    self.panelInstalaciones.panelElegirObjeto.contribucionesEnergeticas.SetToolTip(wx.ToolTip(_('Energía solar, fotovoltaica, cogeneración y recuperación de calor.')))
    self.panelInstalaciones.panelElegirObjeto.iluminacion.SetToolTip(wx.ToolTip(_('Instalación de iluminación.')))
    self.panelInstalaciones.panelElegirObjeto.ventilacion.SetToolTip(wx.ToolTip(_('Demanda térmica asociada a la ventilación mecánica del edificio.')))
    self.panelInstalaciones.panelElegirObjeto.ventiladores.SetToolTip(wx.ToolTip(_('Introduzca los ventiladores de las instalaciones térmicas del edificio.\nEmplee esta opción para introducir los ventiladores de los siguientes equipos:\n- Climatizadoras\n- Fancoils y otras unidades terminales\n- Condensadores autónomos por aire\n- ...')))
    self.panelInstalaciones.panelElegirObjeto.bombas.SetToolTip(wx.ToolTip(_('Introduzca las bombas de las instalaciones térmicas del edificio.')))
    self.panelInstalaciones.panelElegirObjeto.torresRefrigeracion.SetToolTip(wx.ToolTip(_('Introduzca las torres de refrigeración.')))
    self.panelMedidasMejora.DefinirMejorasButton.SetToolTip(wx.ToolTip(_('Nuevo conjunto de medidas de mejora')))
    self.panelMedidasMejora.CompararMejorasButton.SetToolTip(wx.ToolTip(_('Comparar conjuntos de medidas de mejora definidos')))
    self.panelMedidasMejora.cargaEdificioButton.SetToolTip(wx.ToolTip(_('Cargar como un nuevo conjunto un edificio mejorado desde archivo')))


def tipsOnHorizontalInferior(self):
    """
    Metodo: tipsOnHorizontalInferior

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único para la partición interior horizontal.')))
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Defina un elemento de agrupamiento en el árbol de objetos.')))
    self.panelEnvolvente.panel2.superficieParticion.SetToolTip(wx.ToolTip(_('Superficie total de la partición interior horizontal que separa el espacio habitable y un espacio no habitable inferior.')))
    self.panelEnvolvente.panel2.tipoEspacioChoice.SetToolTip(wx.ToolTip(_('Tipo de espacio no habitable: cámara sanitaria, garaje/espacio enterrado o local en superficie. ')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorUConocida.SetToolTip(wx.ToolTip('Transmitancia térmica calculada según apartado E.1.3. del Apéndice E del CTE-HE1.'))
    self.panelEnvolvente.panel2.perimetro.SetToolTip(wx.ToolTip(_('Longitud del perímetro de la partición interior.')))
    self.panelEnvolvente.panel2.ventilacionChoice.SetToolTip(wx.ToolTip(_('Ligeramente ventilado: comprende aquellos espacios con un nivel de estanqueidad 1, 2 o 3.\nEspacio muy ventilado: comprende aquellos espacios con un nivel de estanqueidad 4 ó 5.')))
    self.panelEnvolvente.panel2.superficieCerramiento.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento que separa el espacio no habitable del exterior.')))
    self.panelEnvolvente.panel2.volumenCuadro.SetToolTip(wx.ToolTip(_('Volumen del espacio no habitable.')))
    self.panelEnvolvente.panel2.valorUEstimadaChoice.SetToolTip(wx.ToolTip(_('Modo de definición de la transmitancia térmica de la partición: por defecto o conocida.')))
    self.panelEnvolvente.panel2.UparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaUparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.valorUparticion.SetToolTip(wx.ToolTip(_('Transmitancia térmica de la partición interior según apartado E.1.3. del Apéndice E del CTE-HE1.\nSe deben incluir las resistencias térmicas superficiales en el caso de ser un garaje/espacio enterrado.\nSe deben despreciar las resistencias térmicas superficiales en el caso de ser una cámara sanitaria.')))
    self.panelEnvolvente.panel2.cerramientosUparticionChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición de cerramiento desde la base de datos.')))
    self.panelEnvolvente.panel2.libreriaBotonUparticion.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))


def tipsOnHorizontalSuperior(self):
    """
    Metodo: tipsOnHorizontalSuperior

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único para la partición interior horizontal.')))
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Defina un elemento de agrupamiento en el árbol de objetos.')))
    self.panelEnvolvente.panel2.superficieParticion.SetToolTip(wx.ToolTip(_('Superficie total de la partición interior horizontal que separa el espacio habitable y un espacio no habitable superior.')))
    self.panelEnvolvente.panel2.tipoEspacioChoice.SetToolTip(wx.ToolTip(_('Tipo de espacio no habitable: espacio bajo cubierta inclinada u otro.')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorUConocida.SetToolTip(wx.ToolTip('Transmitancia térmica calculada según apartado E.1.3. del Apéndice E del CTE-HE1.'))
    self.panelEnvolvente.panel2.ventilacionChoice.SetToolTip(wx.ToolTip(_('Ligeramente ventilado: comprende aquellos espacios con un nivel de estanqueidad 1, 2 o 3.\nEspacio muy ventilado: comprende aquellos espacios con un nivel de estanqueidad 4 ó 5.')))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(_('¿Existe aislamiento térmico en la partición, en el cerramiento o en ambos?')))
    self.panelEnvolvente.panel2.posicionAislamientoChoice.SetToolTip(wx.ToolTip(_('El aislamiento se encuentra en la partición, en el cerramiento exterior o en ambos.')))
    self.panelEnvolvente.panel2.superficieCerramiento.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento que separa el espacio no habitable del exterior.')))
    self.panelEnvolvente.panel2.valorUEstimadaChoice.SetToolTip(wx.ToolTip(_('Modo de definición de la transmitancia térmica de la partición: por defecto o conocida.')))
    self.panelEnvolvente.panel2.UparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaUparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.valorUparticion.SetToolTip(wx.ToolTip(_('Transmitancia térmica de la partición interior, incluyendo las resistencias térmicas superficiales según apartado E.1.3. del Apéndice E del CTE-HE1.')))
    self.panelEnvolvente.panel2.cerramientosUparticionChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición de cerramiento desde la base de datos.')))
    self.panelEnvolvente.panel2.libreriaBotonUparticion.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))


def tipsOnVertical(self):
    """
    Metodo: tipsOnVertical

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único para la partición interior vertical.')))
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Defina un elemento de agrupamiento en el árbol de objetos.')))
    self.panelEnvolvente.panel2.superficieParticion.SetToolTip(wx.ToolTip(_('Superficie total de la partición interior vertical que separa el espacio habitable y un espacio no habitable.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones de la partición vertical, medida en el plano que la contiene.\n Es un campo opcional. ')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Una de las dimensione de la partición vertical, medida en el plano que la contiene.\n Es un campo opcional.')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorUConocida.SetToolTip(wx.ToolTip('Transmitancia térmica calculada según apartado E.1.3. del Apéndice E del CTE-HE1.'))
    self.panelEnvolvente.panel2.ventilacionChoice.SetToolTip(wx.ToolTip(_('Ligeramente ventilado: comprende aquellos espacios con un nivel de estanqueidad 1, 2 o 3.\nEspacio muy ventilado: comprende aquellos espacios con un nivel de estanqueidad 4 ó 5.')))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(_('¿Existe aislamiento térmico en la partición, en el cerramiento o en ambos?')))
    self.panelEnvolvente.panel2.posicionAislamientoChoice.SetToolTip(wx.ToolTip(_('El aislamiento se encuentra en la partición, en el cerramiento exterior o en ambos.')))
    self.panelEnvolvente.panel2.superficieCerramiento.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento que separa el espacio no habitable del exterior.')))
    self.panelEnvolvente.panel2.valorUEstimadaChoice.SetToolTip(wx.ToolTip(_('Modo de definición de la transmitancia térmica de la partición: por defecto o conocida.')))
    self.panelEnvolvente.panel2.UparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaUparticionRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.valorUparticion.SetToolTip(wx.ToolTip(_('Transmitancia térmica de la partición interior, incluyendo las resistencias térmicas superficiales según apartado E.1.3. del Apéndice E del CTE-HE1.')))
    self.panelEnvolvente.panel2.cerramientosUparticionChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición de cerramiento desde la base de datos.')))
    self.panelEnvolvente.panel2.libreriaBotonUparticion.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))


def tipsOndefinirHueco(self):
    """
    Metodo: tipsOndefinirHueco

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.cerramientoChoice.SetToolTip(wx.ToolTip(_('Los huecos deben estar vinculados a un cerramiento. Seleccione aquí el cerramiento.')))
    self.panelEnvolvente.panel2.permeabilidadAireChoice.SetToolTip(wx.ToolTip(_('Si conoce la clase de la carpintería y se encuentra en buen estado, seleccione valor conocido.\n Si en la carpintería se observan rendijas por las que producen infiltraciones, seleccione poco estanco.\n Para las carpinterías del tipo corredera, seleccione poco estanco.')))
    self.panelEnvolvente.panel2.propiedadesTermicasChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.vidriosCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.marcosCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.tipoVidrioChoice.SetToolTip(wx.ToolTip(_('Vidrio simple:\tU: 5.7 g: 0.82\n Vidrio doble:\tU: 3.3 g: 0.75\n Doble bajo emisivo simple:\tU: 2.7 g: 0.65')))
    self.panelEnvolvente.panel2.tipoMarcoChoice.SetToolTip(wx.ToolTip(_('Metálico sin rotura de puente térmico: \tU: 5.7\n Metálico con rotura de puente térmico: \tU: 4.0\n PVC: \tU: 2.2\n Madera: \tU: 2.2')))
    self.panelEnvolvente.panel2.decripcionHueco.SetToolTip(wx.ToolTip(_('Nombre del elemento. Deber ser único.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Dimensión horizontal del hueco.\n Es recomendable introducir los huecos como base x altura porque los puentes térmicos automáticos son más exactos.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Dimensión vertical del hueco.\n Es recomendable introducir los huecos como base x altura porque los puentes térmicos automáticos son más exactos.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de huecos iguales en esta orientación.')))
    self.panelEnvolvente.panel2.superficieHueco.SetToolTip(wx.ToolTip(_('Superficie total de los huecos (vidrios y marcos) indicados.')))
    self.panelEnvolvente.panel2.orientacionHueco.SetToolTip(wx.ToolTip(_('La orientación se hereda del cerramiento opaco en el que se encuentra.')))
    self.panelEnvolvente.panel2.porcentajeMarco.SetToolTip(wx.ToolTip(_('Porcentaje del hueco ocupado por el marco.')))
    self.panelEnvolvente.panel2.permeabilidadAire.SetToolTip(wx.ToolTip(_('Permeabilidad de la carpintería, medida con una sobrepresión de 100 Pa')))
    self.panelEnvolvente.panel2.Uvidrio.SetToolTip(wx.ToolTip(_('Transmitancia térmica del vidrio (debe incluir el efecto del acoplamiento con el marco).')))
    self.panelEnvolvente.panel2.Gvidrio.SetToolTip(wx.ToolTip(_('Factor solar del vidrio.')))
    self.panelEnvolvente.panel2.Umarco.SetToolTip(wx.ToolTip(_('Transmitancia térmica del marco.')))
    self.panelEnvolvente.panel2.UvidrioTablas.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.GvidrioTablas.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.UmarcoTablas.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.absortividadBoton.SetToolTip(wx.ToolTip(_('Defina la absortividad del marco en función del color de la carpintería.')))
    self.panelEnvolvente.panel2.proteccionSolarBoton.SetToolTip(wx.ToolTip(_('Defina los elementos de protección solar.')))
    self.panelEnvolvente.panel2.UvidrioRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.libreriaMaterialesText.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.tieneContraventanaCheck.SetToolTip(wx.ToolTip(_('Seleccione esta opción si se ha instalado una ventana doble de vidrio simple.')))
    self.panelEnvolvente.panel2.libreriaBotonVidrios.SetToolTip(wx.ToolTip(_('Librería de vidrios.')))
    self.panelEnvolvente.panel2.libreriaBotonMarcos.SetToolTip(wx.ToolTip(_('Librería de marcos.')))


def tipsOnpuentesTermicosBoton(self):
    """
    Metodo: tipsOnpuentesTermicosBoton

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.tipoPuenteChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de puente térmico.')))
    self.panelEnvolvente.panel2.cerramientoChoice.SetToolTip(wx.ToolTip(_('Los puentes térmicos deben estar asociados a un cerramiento opaco.')))
    self.panelEnvolvente.panel2.nombrePuenteTermico.SetToolTip(wx.ToolTip(_('Nombre único del puente térmico.')))
    self.panelEnvolvente.panel2.fiPuente.SetToolTip(wx.ToolTip(_('Transmitancia térmica lineal del puente térmico.')))
    self.panelEnvolvente.panel2.longitudPuente.SetToolTip(wx.ToolTip(_('Longitud del puente térmico.')))


def tipsOnpuentesTermicosDefectoBoton(self):
    """
    Metodo: tipsOnpuentesTermicosDefectoBoton

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.pilarEnFachada.SetToolTip(wx.ToolTip(_('1 pilar cada 5m lineales de forjado')))
    self.panelEnvolvente.panel2.pilarEnEsquina.SetToolTip(wx.ToolTip(_('2 pilares por fachada')))
    self.panelEnvolvente.panel2.contornoDeHueco.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas o ventanas de 1m de ancho')))
    self.panelEnvolvente.panel2.cajaPersiana.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas o ventanas de 1m de ancho')))
    self.panelEnvolvente.panel2.fachadaConForjado.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas por el usuario o se supone una anchura de 7m')))
    self.panelEnvolvente.panel2.fachadaConCubierta.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas por el usuario o se supone una anchura de 7m')))
    self.panelEnvolvente.panel2.fachadaConSuelo.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas por el usuario o una se supone una anchura de 7m')))
    self.panelEnvolvente.panel2.fachadaConSolera.SetToolTip(wx.ToolTip(_('...o las longitudes indicadas por el usuario o una se supone una anchura de 7m')))


def tipsOndefinirCubiertaTerreno(self):
    """
    Metodo: tipsOndefinirCubiertaTerreno

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione un elemento del árbol de objetos.')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido')))
    self.panelEnvolvente.panel2.cerramientosChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición definida en "Elementos Constructivos"')))
    self.panelEnvolvente.panel2.tipoAislateChoice.SetToolTip(wx.ToolTip(_('EPS: Poliestireno expandido\nXPS: Poliestireno extruido\nMW: Lana mineral\nPUR: Poliuretano')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único del elemento.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del cerramiento, medida en el plano que lo contiene.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del cerramiento, medida en el plano que lo contiene.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento.')))
    self.panelEnvolvente.panel2.profundidadEnterrada.SetToolTip(wx.ToolTip(_('Profundidad a la que se encuentra enterrada la cubierta.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorU.SetToolTip(wx.ToolTip(_('Transmitancia térmica de la cubierta, calculada según el apartado E.1.2.3 del Apéndice E del CTE-HE1, \n incluyendo el efecto de las resistencias superficiales y teniendo en cuenta la capa del terreno.')))
    self.panelEnvolvente.panel2.inercia.SetToolTip(wx.ToolTip(_('Masa por m2 de cubierta, sin tener en cuenta la capa del terreno.')))
    self.panelEnvolvente.panel2.espesorAislante.SetToolTip(wx.ToolTip(_('Espesor del aislante (m).')))
    self.panelEnvolvente.panel2.landaAislante.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislante.SetToolTip(wx.ToolTip(_('Resistencia térmica sólo del aislamiento.')))
    self.panelEnvolvente.panel2.UradioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.aislanteRadioButton.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.RaislateRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.libreriaBoton.SetToolTip(wx.ToolTip(_('Librería de cerramientos..')))


def tipsOndefinirCubiertaConAire(self):
    """
    Metodo: tipsOndefinirCubiertaConAire

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione un elemento del arbol de agrupamiento al que pertenece este cerramiento.')))
    self.panelEnvolvente.panel2.obstaculoRemotoChoice.SetToolTip(wx.ToolTip(_('Seleccion el patron de sombreamiento que afecta a este cerramiento y a sus huecos.')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido.')))
    self.panelEnvolvente.panel2.cerramientosChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición definida en el menu de "Elementos Constructivos"')))
    self.panelEnvolvente.panel2.compoMuroChoice.SetToolTip(wx.ToolTip(_('Seleccione la opción más acorde.')))
    self.panelEnvolvente.panel2.tipoForjadoChoice.SetToolTip(wx.ToolTip(_('Unidireccional, reticular, casetones recuperables o losa.')))
    self.panelEnvolvente.panel2.camaraAireChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.tipoAislateChoice.SetToolTip(wx.ToolTip(_('EPS: Poliestireno expandido\nXPS: Poliestireno extruido\nMW: Lana mineral\nPUR: Poliuretano')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único para este cerramiento.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones de la cubierta, medida en el plano que la contiene.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Una de las dimensione de la cubierta, medida en el plano que la contiene.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de elementos iguales definidos en esta entrada.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.\nEsta superficie incluye el área de los huecos.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(_('Valor de la transmitancia térmica empleado en los cálculos.')))
    self.panelEnvolvente.panel2.valorU.SetToolTip(wx.ToolTip(_('Cálculado según el apartado E.1.1. del Apéndice E del CTE-HE1 (invierno).')))
    self.panelEnvolvente.panel2.inercia.SetToolTip(wx.ToolTip(_('Masa total por m2 de este cerramiento.')))
    self.panelEnvolvente.panel2.espesorAislante.SetToolTip(wx.ToolTip(_('Espesor del aislamiento.')))
    self.panelEnvolvente.panel2.landaAislante.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislante.SetToolTip(wx.ToolTip(_('Resistencia térmica sólo del aislamiento.')))
    self.panelEnvolvente.panel2.UradioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.aislanteRadioButton.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.RaislateRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.libreriaBoton.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(_('Si conoce la existencia de aislamiento active esta opción.')))


def tipsOnFachadaConEdificio(self):
    """
    Metodo: tipsOnFachadaConEdificio

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione el elemento del arbol de agrupamiento al que pertenece este elemento.')))
    self.panelEnvolvente.panel2.inerciaChoice.SetToolTip(wx.ToolTip(_('Seleccione la masa por m2 de todas las capas que componen este cerramiento.')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único de este cerramiento')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Dimensión horizontal del cerramiento.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Dimensión vertical del cerramiento.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de veces que se repite el cerramiento y que queda definido en esta entrada.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.')))


def tipsOndefinirSueloTerreno(self):
    """
    Metodo: tipsOndefinirSueloTerreno

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione el elemento del arbol de objetos al que pertenece este cerramiento.')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido.')))
    self.panelEnvolvente.panel2.posicionAislanteChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.posicionAislanteChoice.SetToolTip(wx.ToolTip(_('Posición del aislamiento: continuo o perimentral')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único de este cerramiento.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del elemento.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del elemento.\n Es un campo opcional. Si se introduce este valor se empleará para la terminación automática de los puentes térmicos.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de veces que se repite este cerramiento y que se incluye en esta definición.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.')))
    self.panelEnvolvente.panel2.profundidad.SetToolTip(wx.ToolTip(_('Profundidad a la que se encuentra enterrada esta solera.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.perimetro.SetToolTip(wx.ToolTip(_('Longitud acumulada de los bordes que dan al exterior de este suelo')))
    self.panelEnvolvente.panel2.Raislate.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.espesor.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislate2.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.espesor2.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.menor05Radio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.mayor05Radio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(''))


def tipsOnFachadaConAire(self):
    """
    Metodo: tipsOnFachadaConAire

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione el elemento del arbol de objetos al que pertenece esta fachada')))
    self.panelEnvolvente.panel2.orientacionChoice.SetToolTip(wx.ToolTip(_('Seleccione la orientación asimilada.\n Norte:\t [-22.5º a +22.5º)\nNE:\t [+22.5º a +60)\n Este:\t [+60º a +111º)\n SE:\t [+111º a +162º)\n Sur:\t [+162º a -162º)\n SO:\t [-162 a -111º)\n Oeste:\t [-111º a -60º)\n NO:\t [-60º a -22.5º)')))
    self.panelEnvolvente.panel2.obstaculoRemotoChoice.SetToolTip(wx.ToolTip(_('Seleccione el perfil sombras que afecta a esta fachada. ')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, conocido o estimado.')))
    self.panelEnvolvente.panel2.cerramientosChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición definida en "Elementos Constructivos"')))
    self.panelEnvolvente.panel2.tipoFachadaChoice.SetToolTip(wx.ToolTip(_('Una hoja, dos hojas o fachada ventilada.\nEsta decisión afecta al valor de transmitancia térmica y a los puentes térmicos asocidados al cerramiento.')))
    self.panelEnvolvente.panel2.compoMuroChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.camarAireChoice.SetToolTip(wx.ToolTip(_('No ventilada: las aberturas no permiten el flujo de aire y no exceden:\n 500 mm2 por m de longitud horizontal para cámaras horizontales\n500 mm2 por m2 se superficie para cámaras de aire horizontales\n Ligeramente ventilada: no existe un dispositivo para el flujo de aire \n limitado a través de ella desde el ambiente exterior, pero con aberturas\n dentro de los siguientes rangos: \n entre 500 y 1500 mm2 por m de longitud horizontal para cámaras horizontales \n entre 500 y 1500 mm2 por m2 de superficie para cámaras de aire horizontales \n Muy ventilada: aquella en que los valres de las aberturas exceden: \n 1500 mm2 por m de longitud horizontal para cámaras de aire verticales \n 1500 mm2 por m2 de superficie para cámaras de aire horizontales.')))
    self.panelEnvolvente.panel2.posicionAislamientoChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.tipoAislateChoice.SetToolTip(wx.ToolTip(_('EPS: Poliestireno expandido\nXPS: Poliestireno extruido\nMW: Lana mineral\nPUR: Poliuretano')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único de la fachada.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Dimensión horizontal de la fachada.\nSi se introduce, este valor será utilizado para determinar\n la longitud del puente térmico de frente de forjado.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Dimensión vertical del cerramiento.')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de veces que se repite este cerramiento.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.\nEsta superficie incluye el área de los huecos.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorU.SetToolTip(wx.ToolTip(_('Cálculado según el apartado E.1.1. del Apéndice E del CTE-HE1.')))
    self.panelEnvolvente.panel2.inercia.SetToolTip(wx.ToolTip(_('Introduzca la masa por m2 de este cerramiento.')))
    self.panelEnvolvente.panel2.espesorAislante.SetToolTip(wx.ToolTip(_('Espesor del aislamiento.')))
    self.panelEnvolvente.panel2.landaAislante.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislante.SetToolTip(wx.ToolTip(_('Resistencia térmica sólo del aislamiento.')))
    self.panelEnvolvente.panel2.UradioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.aislanteRadioButton.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.RaislateRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.libreriaBoton.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(''))


def tipsOnSueloConAire(self):
    """
    Metodo: tipsOnSueloConAire

    ARGUMENTOS:
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione el elemento del arbol de objetos al que pertenece este suelo')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.cerramientosChoice.SetToolTip(wx.ToolTip(_('Seleccione una composición definida en "Elementos Constructivos"')))
    self.panelEnvolvente.panel2.compoMuroChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.entrevigadoChoice.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.tipoAislateChoice.SetToolTip(wx.ToolTip(_('EPS: Poliestireno expandido\nXPS: Poliestireno extruido\nMW: Lana mineral\nPUR: Poliuretano')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Seleccione un nombre único para este suelo')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del elemento')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Una de las dimensiones del elemento')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de veces que se repite este cerramiento y que se incluye en esta definición.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.valorU.SetToolTip(wx.ToolTip(_('Cálculado según el apartado E.1.1 del Apéndice E del CTE-HE1.')))
    self.panelEnvolvente.panel2.inercia.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.espesorAislante.SetToolTip(wx.ToolTip(_('Espesor del aislamiento.')))
    self.panelEnvolvente.panel2.landaAislante.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislante.SetToolTip(wx.ToolTip(_('Resistencia térmica sólo del aislamiento.')))
    self.panelEnvolvente.panel2.UradioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la transmitancia térmica del cerramiento.')))
    self.panelEnvolvente.panel2.libreriaRadioButton.SetToolTip(wx.ToolTip(_('Seleccione esta opción si conoce la composición del cerramiento.')))
    self.panelEnvolvente.panel2.aislanteRadioButton.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.RaislateRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.libreriaBoton.SetToolTip(wx.ToolTip(_('Librería de cerramientos.')))


def tipsOnFachadaConTerreno(self):
    """
    Metodo: tipsOnFachadaConTerreno

    ARGUMENTOS:
                self):  :
    """
    self.panelEnvolvente.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione el elemento del arbol de objetos al que pertenece esta fachada')))
    self.panelEnvolvente.panel2.valorUChoice.SetToolTip(wx.ToolTip(_('Por defecto, estimado o conocido')))
    self.panelEnvolvente.panel2.tipoAislateChoice.SetToolTip(wx.ToolTip(_('EPS: Poliestireno expandido\nXPS: Poliestireno extruido\nMW: Lana mineral\nPUR: Poliuretano')))
    self.panelEnvolvente.panel2.nombreMuro.SetToolTip(wx.ToolTip(_('Nombre único del cerramiento.')))
    self.panelEnvolvente.panel2.longitudMuro.SetToolTip(wx.ToolTip(_('Dimensión horizontal de la fachada.')))
    self.panelEnvolvente.panel2.alturaMuro.SetToolTip(wx.ToolTip(_('Dimensión vertical de la fachada')))
    self.panelEnvolvente.panel2.multiMuro.SetToolTip(wx.ToolTip(_('Número de veces que se repite este cerramiento y que se incluye en esta definición.')))
    self.panelEnvolvente.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Superficie total del cerramiento medida desde el interior del edificio.')))
    self.panelEnvolvente.panel2.UFinalCuadro.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.profundidadEnterrada.SetToolTip(wx.ToolTip(_('Figuras E.3 y E.4 del CTE-HE1.')))
    self.panelEnvolvente.panel2.espesorAislante.SetToolTip(wx.ToolTip(_('Espesor del aislamiento.')))
    self.panelEnvolvente.panel2.landaAislante.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.Raislante.SetToolTip(wx.ToolTip(_('Resistencia térmica sólo del aislamiento.')))
    self.panelEnvolvente.panel2.aislanteRadioButton.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.RaislateRadio.SetToolTip(wx.ToolTip(''))
    self.panelEnvolvente.panel2.aislamientoCheck.SetToolTip(wx.ToolTip(''))


def Acs(self):
    """
    Metodo: Acs

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Definir un elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.aislanteCaldera.SetToolTip(wx.ToolTip(_('El técnico certificador debe realizar una estimación del aislamiento de la caldera.')))
    self.panelInstalaciones.panel2.valorUAChoice.SetToolTip(wx.ToolTip(_('Seleccione la forma de estimar las pérdidas del depósito de ACS.\nSi escoge la opción por defecto, se supondrá que el depósito no está aislado y las pérdidas serán elevadas.')))
    self.panelInstalaciones.panel2.aislamientoAcumulacionChoice.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimientoCombustion.SetToolTip(wx.ToolTip(_('Rendimiento de humos de la combustión.\nNo es ni el rendimiento nominal, ni el estacional.\nSi esta información no está disponible, se empleará el valor de 85%')))
    self.panelInstalaciones.panel2.potenciaNominal.SetToolTip(wx.ToolTip(_('Potencia nominal de la caldera.\nEn el caso de que se trate de un bloque de viviendas \n con múltiples instalaciones individuales iguales, se pueden indicar\n las características de un único equipo introduciendo el porcentaje total cubierto por todos ellos.\n \nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con una \n caldera individual de 24 kW, en este campo introduciremos la potencia de 24 kW, no 240 kW')))
    self.panelInstalaciones.panel2.cargaMedia.SetToolTip(wx.ToolTip(_('Factor de carga media estacional de la caldera.\nSi existen contadores en la instalación, su valor se puede estimar a partir de sus lecturas.\nSi no existe la posibilidad de realizar una estimación se adoptará el valor de 0.2.')))
    self.panelInstalaciones.panel2.cargaMediaHelpButton.SetToolTip(wx.ToolTip(_('Esta ayuda le permite calcular el factor de carga media estacional\npara instalaciones con varios generadores de calor trabajando simultaneamente.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador.')))
    self.panelInstalaciones.panel2.rendimientoGlobal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.temperaturaAlta.SetToolTip(wx.ToolTip(_('Consigna de paro del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.temperaturaBaja.SetToolTip(wx.ToolTip(_('Consigna de arranque del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.espesorAislamiento.SetToolTip(wx.ToolTip(_('Espesor del aislamiento que recubre el tanque de acumulación de ACS')))
    self.panelInstalaciones.panel2.UAvalor.SetToolTip(wx.ToolTip(_('Coeficiente global de pérdidas del depósito de acumulación del ACS')))
    self.panelInstalaciones.panel2.definirCalderaBoton.SetToolTip(wx.ToolTip(_('Defina las características que mejor se ajustan a la caldera considerada.')))
    self.panelInstalaciones.panel2.definirMetros2Radio.SetToolTip(wx.ToolTip(_('Defina la cobertura de este generador en función de los m2 a los que da servicio.\nEn el caso de que se trate de un bloque de viviendas con múltiples instalaciones individuales iguales, se puede indicarlas características de un único equipo introduciendo la superficie total cubierta por todos ellos.')))
    self.panelInstalaciones.panel2.definirDemandaRadio.SetToolTip(wx.ToolTip(_('Defina el porcentaje de superficie cubierto por este generador respecto a la superficie de la zona/edificio.\nEn el caso de que se trate de un bloque de viviendas con múltiples instalaciones individuales iguales, se puede indicarlas características de un único equipo introduciendo el porcentaje total cubierto por todos ellos.')))
    self.panelInstalaciones.panel2.acumulacionCheck.SetToolTip(wx.ToolTip(_('Si la preparación del ACS no es instantánea, escoja esta opción.')))
    self.panelInstalaciones.panel2.multiplicador.SetToolTip(wx.ToolTip(_('Número de depósitos de acumulación representados en esta definición.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el multiplicador 10. ')))
    self.panelInstalaciones.panel2.volumen.SetToolTip(wx.ToolTip(_('Volumen de acumulación de uno solo de los depósitos de ACS.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el valor de 100 litros e indicaremos un multiplicador de 10.')))
    self.panelInstalaciones.panel2.VariosGeneradoresCheck.SetToolTip(wx.ToolTip(_('Active esta opción si existen varios generadores que entran de forma escalonada\npara cubrir la demanda.')))
    self.panelInstalaciones.panel2.FraccionPotencia.SetToolTip(wx.ToolTip(_('Si exiten varios equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total que corresponde\nal equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW,\nse podrán definir como dos generadores independientes y cada uno de ellos \nrepresentarán respectivamente las fracciones 0.6 y 0.4 de la potencia total.')))
    self.panelInstalaciones.panel2.fraccionPotenciaEntrada.SetToolTip(wx.ToolTip(_('Si exiten varias equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total a la que\nentra en servicio el equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW, y la gestión\nde los equipos se realiza de tal manera que entra primero el de 60 kW y luego el de 40 kW, \ndiremos que la fracción de la potencia total a la que entra el generador de 60 kW es 0.0 \ny la fraccción de la potencia total a la que entra el generador de 40 kW es 0.6.')))


def Calefaccion(self):
    """
    Metodo: Calefaccion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Definir un elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.aislanteCaldera.SetToolTip(wx.ToolTip(_('El técnico certificador debe realizar una estimación del aislamiento de la caldera.')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimientoCombustion.SetToolTip(wx.ToolTip(_('Rendimiento de humos de la combustión.\nNo es ni el rendimiento nominal, ni el estacional.\nSi esta información no está disponible, se empleará el valor de 85%')))
    self.panelInstalaciones.panel2.potenciaNominal.SetToolTip(wx.ToolTip(_('Potencia nominal de la caldera.\nEn el caso de que se trate de un bloque de viviendas \n con múltiples instalaciones individuales iguales, se pueden indicar\nlas características de un único equipo introduciendo el porcentaje total cubierto por todos ellos.\n \nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con una \n caldera individual de 24 kW, en este campo introduciremos la potencia de 24 kW, no 240 kW')))
    self.panelInstalaciones.panel2.cargaMedia.SetToolTip(wx.ToolTip(_('Carga media estacional de la caldera.\nSi existen contadores en la instalación, su valor se puede estimar a partir de sus lecturas.\nSi no existe la posibilidad de realizar una estimación se adoptará el valor de 0.2.')))
    self.panelInstalaciones.panel2.cargaMediaHelpButton.SetToolTip(wx.ToolTip(_('Esta ayuda le permite calcular el factor de carga media estacional\npara instalaciones con varios generadores de calor trabajando simultaneamente.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador.')))
    self.panelInstalaciones.panel2.rendimientoGlobal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.definirCalderaBoton.SetToolTip(wx.ToolTip(_('Defina las características que mejor se ajustan a la caldera considerada.')))
    self.panelInstalaciones.panel2.definirMetros2Radio.SetToolTip(wx.ToolTip(_('Defina la cobertura de este generador en función de los m2 a los que da servicio')))
    self.panelInstalaciones.panel2.definirDemandaRadio.SetToolTip(wx.ToolTip(_('Defina la cobertura de este generador como una fracción de la demanda total del edificio')))
    self.panelInstalaciones.panel2.VariosGeneradoresCheck.SetToolTip(wx.ToolTip(_('Active esta opción si existen varios generadores que entran de forma escalonada\npara cubrir la demanda.')))
    self.panelInstalaciones.panel2.FraccionPotencia.SetToolTip(wx.ToolTip(_('Si exiten varios equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total que corresponde\nal equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW,\nse podrán definir como dos generadores independientes y cada uno de ellos \nrepresentarán respectivamente las fracciones 0.6 y 0.4 de la potencia total.')))
    self.panelInstalaciones.panel2.fraccionPotenciaEntrada.SetToolTip(wx.ToolTip(_('Si exiten varias equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total a la que\nentra en servicio el equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW, y la gestión\nde los equipos se realiza de tal manera que entra primero el de 60 kW y luego el de 40 kW, \ndiremos que la fracción de la potencia total a la que entra el generador de 60 kW es 0.0 \ny la fraccción de la potencia total a la que entra el generador de 40 kW es 0.6.')))


def Refrigeracion(self):
    """
    Metodo: Refrigeracion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Definir un elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador.')))
    self.panelInstalaciones.panel2.rendimientoGlobal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.definirMetros2Radio.SetToolTip(wx.ToolTip(_('Defina la cobertura de este generador en función de los m2 a los que da servicio')))
    self.panelInstalaciones.panel2.definirDemandaRadio.SetToolTip(wx.ToolTip(_('Defina la cobertura de este generador como una fracción de la demanda total del edificio')))
    self.panelInstalaciones.panel2.VariosGeneradoresCheck.SetToolTip(wx.ToolTip(_('Active esta opción si existen varios generadores que entran de forma escalonada\npara cubrir la demanda.')))
    self.panelInstalaciones.panel2.FraccionPotencia.SetToolTip(wx.ToolTip(_('Si exiten varios equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total que corresponde\nal equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW,\nse podrán definir como dos generadores independientes y cada uno de ellos \nrepresentarán respectivamente las fracciones 0.6 y 0.4 de la potencia total.')))
    self.panelInstalaciones.panel2.fraccionPotenciaEntrada.SetToolTip(wx.ToolTip(_('Si exiten varias equipos generadores que trabajan simultáneamente para dar la potencia total\ndemandada por la instalación, debe indicar en este campo la fracción de la potencia total a la que\nentra en servicio el equipo generador que se está introduciendo en este momento. \nPor ejemplo, si una instalación cuenta con dos equipos de 60 y 40 kW, y la gestión\nde los equipos se realiza de tal manera que entra primero el de 60 kW y luego el de 40 kW, \ndiremos que la fracción de la potencia total a la que entra el generador de 60 kW es 0.0 \ny la fraccción de la potencia total a la que entra el generador de 40 kW es 0.6.')))


def Climatizacion(self):
    """
    Metodo: Climatizacion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Definir un elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.coberturaMetros2.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje2.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador en modo calor')))
    self.panelInstalaciones.panel2.rendimietoMedio2.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal2.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador en modo frio')))
    self.panelInstalaciones.panel2.rendimientoGlobalCal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoGlobalRef.SetToolTip(wx.ToolTip(''))


def MixtosCaleyAcs(self):
    """
    Metodo: MixtosCaleyAcs

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.aislanteCaldera.SetToolTip(wx.ToolTip(_('El técnico certificador debe realizar una estimación del aislamiento de la caldera.')))
    self.panelInstalaciones.panel2.valorUAChoice.SetToolTip(wx.ToolTip(_('Seleccione la forma de estimar las pérdidas del depósito de ACS.\n Si escoge la opción por defecto, se supondrá que el depósito no está aislado y las pérdidas serán elevadas.')))
    self.panelInstalaciones.panel2.aislamientoAcumulacionChoice.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.coberturaMetros2.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje2.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimientoCombustion.SetToolTip(wx.ToolTip(_('Rendimiento de humos de la combustión.\n No es ni el rendimiento nominal, ni el estacional.\n Si esta información no está disponible, se empleará el valor de 85%')))
    self.panelInstalaciones.panel2.potenciaNominal.SetToolTip(wx.ToolTip(_('Potencia nominal de la caldera.\nEn el caso de que se trate de un bloque de viviendas \n con múltiples instalaciones individuales iguales, se pueden indicar\n las características de un único equipo introduciendo el porcentaje total cubierto por todos ellos.\n \nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con una \n caldera individual de 24 kW, en este campo introduciremos la potencia de 24 kW, no 240 kW')))
    self.panelInstalaciones.panel2.cargaMedia.SetToolTip(wx.ToolTip(_('Carga media estacional de la caldera.\n Si existen contadores en la instalación, su valor se puede estimar a partir de sus lecturas.\n Si no existe la posibilidad de realizar una estimación se adoptará el valor de 0.2.')))
    self.panelInstalaciones.panel2.cargaMediaHelpButton.SetToolTip(wx.ToolTip(_('Esta ayuda le permite calcular el factor de carga media estacional\npara instalaciones con varios generadores de calor trabajando simultaneamente.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador.')))
    self.panelInstalaciones.panel2.rendimientoGlobal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.volumen.SetToolTip(wx.ToolTip(_('Volumen de acumulación de uno solo de los depósitos de ACS.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el valor de 100 litros e indicaremos un multiplicador de 10.')))
    self.panelInstalaciones.panel2.temperaturaAlta.SetToolTip(wx.ToolTip(_('Consigna de paro del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.temperaturaBaja.SetToolTip(wx.ToolTip(_('Consigna de arranque del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.espesorAislamiento.SetToolTip(wx.ToolTip(_('Espesor del aislamiento que recubre el tanque de acumulación de ACS')))
    self.panelInstalaciones.panel2.UAvalor.SetToolTip(wx.ToolTip(_('Coeficiente global de pérdidas del depósito de acumulación del ACS')))
    self.panelInstalaciones.panel2.definirCalderaBoton.SetToolTip(wx.ToolTip(_('Defina las características que mejor se ajustan a la caldera considerada.')))
    self.panelInstalaciones.panel2.acumulacionCheck.SetToolTip(wx.ToolTip(_('Si la preparación del ACS no es instantánea, escoja esta opción.')))
    self.panelInstalaciones.panel2.multiplicador.SetToolTip(wx.ToolTip(_('Número de depósitos de acumulación representados en esta definición.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el multiplicador 10. ')))


def MixtosClimayAcs(self):
    """
    Metodo: MixtosClimayAcs

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Definir un elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.generadorChoice.SetToolTip(wx.ToolTip(_('Seleccione el tipo de generador')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.rendimientoChoice.SetToolTip(wx.ToolTip(_('Si conoce el rendimiento de la instalación indique "conocido" en caso contrario "estimado"')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.rendimietoMedio.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador en modo calor')))
    self.panelInstalaciones.panel2.rendimietoMedio2.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal2.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador en modo frio')))
    self.panelInstalaciones.panel2.coberturaMetros.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.coberturaMetros2.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje2.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.coberturaMetros3.SetToolTip(wx.ToolTip(_('Superficie útil habitable en m2 cuya demanda es cubierta por este equipo')))
    self.panelInstalaciones.panel2.coberturaPorcentaje3.SetToolTip(wx.ToolTip(_('Porcentaje de la demanda que es cubierta por este equipo.\nSi el equipo cuelga de una zona de agrupamiento, el porcentaje estará referido a la superficie asignada a la zona de agrupamiento.\nSi el equipo cuelga del "edificio objeto", el porcentaje se referirá a la superficie útil habitable total del edificio.\nSi en un mismo edificio, se han definido instalaciones que cuelgan de una zona e instalaciones que cuelgan del edificio, \nse recomienda emplear la superficie en m2 en vez del porcentaje.')))
    self.panelInstalaciones.panel2.rendimietoMedio3.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoNominal3.SetToolTip(wx.ToolTip(_('Rendimiento nominal del generador cuando prepara ACS')))
    self.panelInstalaciones.panel2.rendimientoGlobal.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoGlobal2.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.rendimientoGlobal3.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.valorUAChoice.SetToolTip(wx.ToolTip(_('Seleccione la forma de estimar las pérdidas del depósito de ACS.\n Si escoge la opción por defecto, se supondrá que el depósito no está aislado y las pérdidas serán elevadas.')))
    self.panelInstalaciones.panel2.aislamientoAcumulacionChoice.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.volumen.SetToolTip(wx.ToolTip(_('Volumen de acumulación de uno solo de los depósitos de ACS.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el valor de 100 litros e indicaremos un multiplicador de 10.')))
    self.panelInstalaciones.panel2.temperaturaAlta.SetToolTip(wx.ToolTip(_('Consigna de paro del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.temperaturaBaja.SetToolTip(wx.ToolTip(_('Consigna de arranque del aporte de calor al tanque de ACS.')))
    self.panelInstalaciones.panel2.espesorAislamiento.SetToolTip(wx.ToolTip(_('Espesor del aislamiento que recubre el tanque de acumulación de ACS')))
    self.panelInstalaciones.panel2.UAvalor.SetToolTip(wx.ToolTip(_('Coeficiente global de pérdidas del depósito de acumulación del ACS')))
    self.panelInstalaciones.panel2.acumulacionCheck.SetToolTip(wx.ToolTip(_('Si la preparación del ACS no es instantánea, escoja esta opción.')))
    self.panelInstalaciones.panel2.multiplicador.SetToolTip(wx.ToolTip(_('Número de depósitos de acumulación representados en esta definición.\nPor ejemplo, si se califica un edificio en bloque con 10 apartamentos y cada uno de ellos cuenta con un \n acumulador de 100 litros, en este campo introduciremos el multiplicador 10. ')))


def Renovables(self):
    """
    Metodo: Renovables

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.combustibleChoice.SetToolTip(wx.ToolTip(mensajeCoeficientesPaso))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.porcentajeACS.SetToolTip(wx.ToolTip(_('Indique el porcentaje de la demanda de ACS que es cubierto mediante fuentes de energía renovable o calor recuperado')))
    self.panelInstalaciones.panel2.porcentajeCalefaccion.SetToolTip(wx.ToolTip(_('Indique el porcentaje de la demanda de calefacción que es cubierto mediante fuentes de energía renovable o calor recuperado')))
    self.panelInstalaciones.panel2.porcentajeRefrigeracion.SetToolTip(wx.ToolTip(_('Indique el porcentaje de la demanda de Refrigeración que es cubierto mediante fuentes de energía renovable o calor recuperado')))
    self.panelInstalaciones.panel2.energia.SetToolTip(wx.ToolTip(_('Energía eléctrica generada para autoconsumo.')))
    self.panelInstalaciones.panel2.energiaConsumida.SetToolTip(wx.ToolTip(_('Energía consumida. En el caso de fotovoltaica, se pone 0.')))
    self.panelInstalaciones.panel2.fChartButton.SetToolTip(wx.ToolTip(''))
    self.panelInstalaciones.panel2.calorGeneradoACS.SetToolTip(wx.ToolTip(_('Reducción de la demanda de ACS, como consecuencia del empleo del equipo.')))
    self.panelInstalaciones.panel2.calorGeneradoCal.SetToolTip(wx.ToolTip(_('Reducción de la demanda de calefacción, como consecuencia del empleo de este equipo.')))
    self.panelInstalaciones.panel2.calorGeneradoRef.SetToolTip(wx.ToolTip(_('Reducción de la demanda de refrigeración como consecuencia del empleo de este equipo.\nEn el caso de una instalación de trigeneración, en este campo se debe introducir directamente \nel frío anual producido por el equipo de refrigeración.')))
    self.panelInstalaciones.panel2.fuenteRadio.SetToolTip(wx.ToolTip(_('Se introduce la reducción de las demandas producida por las renovables o la recuperación del calor.')))
    self.panelInstalaciones.panel2.generacionRadio.SetToolTip(wx.ToolTip(_('Se introduce la energía eléctrica generada.')))
    self.panelInstalaciones.panel2.captadoresCheck.SetToolTip(wx.ToolTip(''))


def Iluminacion(self):
    """
    Metodo: Iluminacion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.usoChoice.SetToolTip(wx.ToolTip(_('Para cada tipo de actividad se recomiendan unos niveles de iluminación')))
    self.panelInstalaciones.panel2.definirSegunChoice.SetToolTip(wx.ToolTip(_('Si conoce la potencia instalada y el nivel de iluminación, escoja "conocido", en caso contrario escoja "estimado".')))
    lumenWIncandescente = diccLuminarias['Incandescente'][0]
    lumenWIncandescentesHalogenas = diccLuminarias['Incandescentes halógenas'][0]
    lumenWFluorescente26 = diccLuminarias['Fluorescencia lineal de 26 mm'][0]
    lumenWFluorescente16 = diccLuminarias['Fluorescencia lineal de 16 mm'][0]
    lumenWFluorescenteCompacta = diccLuminarias['Fluorescencia compacta'][0]
    lumenWSodio = diccLuminarias['Sodio Blanco'][0]
    lumenWMercurio = diccLuminarias['Vapor de Mercurio'][0]
    lumenWHalogenuros = diccLuminarias['Halogenuros metálicos'][0]
    lumenWInduccion = diccLuminarias['Inducción'][0]
    lumenWLed = diccLuminarias['LED'][0]
    lumenWLedTube = diccLuminarias['LED Tube (lineal)'][0]
    self.panelInstalaciones.panel2.tipoEquipoChoice.SetToolTip(wx.ToolTip(_('Seleccion el tipo de luminaria más acorde a la instalación. \nDebe tener en cuenta que por la opción estimada se asignan las siguientes eficiencias luminosas:\nIncandescente:\t\t %s lm/W\nIncandescentes halógenas:\t\t %s lm/W\nFluorescencia lineal de 26 mm:\t %s lm/W\nFluorescencia lineal de 16 mm:\t %s lm/W\nFluorescencia compacta:\t\t %s lm/W\nSodio Blanco:\t\t\t %s lm/W\nVapor de Mercurio:\t\t %s lm/W\nHalogenuros metálicos:\t\t %s lm/W\nInducción:\t\t\t %s lm/W\nLED Spot (puntual, bombilla):\t %s lm/W\nLED Tube (lineal):\t\t\t %s lm/W' % (lumenWIncandescente,
     lumenWIncandescentesHalogenas,
     lumenWFluorescente26,
     lumenWFluorescente16,
     lumenWFluorescenteCompacta,
     lumenWSodio,
     lumenWMercurio,
     lumenWHalogenuros,
     lumenWInduccion,
     lumenWLed,
     lumenWLedTube))))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de la instalación debe ser único.')))
    self.panelInstalaciones.panel2.superficieMuro.SetToolTip(wx.ToolTip(_('Seleccione la superficie asociada a esta instalación.')))
    self.panelInstalaciones.panel2.potenciaInstalada.SetToolTip(wx.ToolTip(_('Seleccione la potencia eléctrica de la instalación de iluminación, incluyendo los equipos auxiliares.')))
    self.panelInstalaciones.panel2.iluminancia.SetToolTip(wx.ToolTip(_('Nivel de iluminación medido en condiciones nominales y sin aporte de iluminación natural.')))
    self.panelInstalaciones.panel2.zonaRepresentacionCheck.SetToolTip(wx.ToolTip(_('espacios donde el criterio de diseño, imagen o el estado anímico que se quiere transmitir \nal usuario con la iluminación, son preponderantes frente a los criterios de eficiencia energética. \nAfecta a la formación de la escala.')))
    self.panelInstalaciones.panel2.sinControl.SetToolTip(wx.ToolTip(_('No existen dispositivos de regulación de la iluminación por el nivel de iluminación natural.')))
    self.panelInstalaciones.panel2.conControl.SetToolTip(wx.ToolTip(_('Existen dispositivos de regulación de la iluminación por el nivel de iluminación natural.')))
    self.panelInstalaciones.panel2.superficieControl.SetToolTip(wx.ToolTip(_('Superficie útil habitable iluminada por luminarias equipas con regulación \nde la intensidad por nivel de iluminación natural.')))


def Ventilacion(self):
    """
    Metodo: Ventilacion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de la instalación debe ser único.')))
    self.panelInstalaciones.panel2.equipoVentilacion.SetToolTip(wx.ToolTip(_('Introduzca el caudal de aire primario introducido.')))
    self.panelInstalaciones.panel2.rendimiento.SetToolTip(wx.ToolTip(_('Seleccione el rendimiento estacional de recuperación sensible del equipo.')))
    self.panelInstalaciones.panel2.recuperadorCheck.SetToolTip(wx.ToolTip(_('Seleccione si existe un equipo de recuperación.')))


def TorresRefrigeracion(self):
    """
    Metodo: TorresRefrigeracion

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.torreChoice.SetToolTip(wx.ToolTip(_('Seleccione velocidad variable si el ventilador de la torre puede variar su velocidad para ajustarse al nivel de demanda.')))
    self.panelInstalaciones.panel2.EstimacionConsumoChoice.SetToolTip(wx.ToolTip(_('Conocido o estimado')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.consumo.SetToolTip(wx.ToolTip(_('Consumo eléctrico anual de la torre de refrigeración (kWh)')))
    self.panelInstalaciones.panel2.numeroHorasDemanda.SetToolTip(wx.ToolTip(_('Nº de horas al año en las que hay demanda  de refrigeración y está funcionando la torre ')))
    self.panelInstalaciones.panel2.potenciaElectricaNominal.SetToolTip(wx.ToolTip(_('Potencia consumida por la o las bombas en situación de plena carga (kW)')))
    self.panelInstalaciones.panel2.botonDefinirCurva.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante una curva.')))
    self.panelInstalaciones.panel2.botonDefinirEscalones.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante escalones.')))
    self.panelInstalaciones.panel2.numeroHorasHelpButton.SetToolTip(wx.ToolTip(_('Estimador del número de horas de funcionamiento de la torre.')))


def bombas(self):
    """
    Metodo: bombas

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.bombaChoice.SetToolTip(wx.ToolTip(_('Seleccione velocidad variable si la bomba varía su velocidad para ajustarse al nivel de demanda térmica.')))
    self.panelInstalaciones.panel2.EstimacionConsumoChoice.SetToolTip(wx.ToolTip(_('Estimado o conocido.')))
    self.panelInstalaciones.panel2.seleccionServicio.SetToolTip(wx.ToolTip(_('Si la misma bomba se emplea para calefacción y refrigeración, deberá duplicarla.')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.consumo.SetToolTip(wx.ToolTip(_('Consumo eléctrico anual de la bomba en el servicio seleccionado (kWh)')))
    self.panelInstalaciones.panel2.potenciaElectricaNominal.SetToolTip(wx.ToolTip(_('Potencia consumida por la o las bombas en situación de plena carga (kW)')))
    self.panelInstalaciones.panel2.numeroHorasDemanda.SetToolTip(wx.ToolTip(_('Nº de horas al año en las que hay demanda  de calefacción/refrigeración/ACS \n(según el servicio seleccionado) y para cubrir esta demanda está funcionando \nla o las bombas.')))
    self.panelInstalaciones.panel2.horasTemporadaAcs.SetToolTip(wx.ToolTip(_('Nº de horas de disponibilidad de la bomba destinada a ACS, aunque no exista demanda.')))
    self.panelInstalaciones.panel2.horasTemporadaCalefaccion.SetToolTip(wx.ToolTip(_('Nº de horas de disponibilidad de la bomba destinada a calefacción, aunque no exista demanda.')))
    self.panelInstalaciones.panel2.horasTemporadaRefrigeracion.SetToolTip(wx.ToolTip(_('Nº de horas de disponibilidad de la bomba destinada a refrigeración, aunque no exista demanda.')))
    self.panelInstalaciones.panel2.fraccionPotenciaNoDemanda.SetToolTip(wx.ToolTip(_('Fracción de la potencia consumida mientras no hay demanda, pero está en disponibilidad.')))
    self.panelInstalaciones.panel2.numeroHorasHelpButton.SetToolTip(wx.ToolTip(_('Estimador del número de horas de funcionamiento de la bomba.')))
    self.panelInstalaciones.panel2.funcionamientoNoDemanda.SetToolTip(wx.ToolTip(_('Si la bomba se apaga cuando cesa la demanda térmica, indique no.\nSi la bomba permanece en funcionamiento aunque la demanda térmica haya desaparecido, indique si.')))
    self.panelInstalaciones.panel2.botonDefinirCurva.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante una curva.')))
    self.panelInstalaciones.panel2.botonDefinirEscalones.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante escalones.')))


def ventiladores(self):
    """
    Metodo: ventiladores

    ARGUMENTOS:
    """
    self.panelInstalaciones.panel2.subgrupoChoice.SetToolTip(wx.ToolTip(_('Seleccione elemento del árbol de objetos al que pertenece esta instalación')))
    self.panelInstalaciones.panel2.ventiladorChoice.SetToolTip(wx.ToolTip(_('Seleccione velocidad variable si el ventilador de la climatizadora varía su velocidad para ajustarse al nivel de demanda térmica.')))
    self.panelInstalaciones.panel2.EstimacionConsumoChoice.SetToolTip(wx.ToolTip(_('Estimado o conocido')))
    self.panelInstalaciones.panel2.seleccionServicio.SetToolTip(wx.ToolTip(_('Si el mismo ventilador se emplea para calefacción y refrigeración, deberá duplicarlo.')))
    self.panelInstalaciones.panel2.nombreInstalacion.SetToolTip(wx.ToolTip(_('El nombre de esta instalación debe ser único.')))
    self.panelInstalaciones.panel2.consumo.SetToolTip(wx.ToolTip(_('Consumo eléctrico anual del ventilador en el servicio seleccionado (kWh)')))
    self.panelInstalaciones.panel2.potenciaElectricaNominal.SetToolTip(wx.ToolTip(_('Potencia consumida por el o los ventiladores en situación de plena carga (kW)')))
    self.panelInstalaciones.panel2.numeroHorasDemanda.SetToolTip(wx.ToolTip(_('Nº de horas al año en las que hay demanda  de calefacción/refrigeración \n(según el servicio seleccionado) y para cubrir esta demanda está funcionando \nel o los ventiladores.')))
    self.panelInstalaciones.panel2.horasTemporadaCalefaccion.SetToolTip(wx.ToolTip(_('Nº de horas de disponibilidad del ventilador destinado a calefacción, aunque no exista demanda.')))
    self.panelInstalaciones.panel2.horasTemporadaRefrigeracion.SetToolTip(wx.ToolTip(_('Nº de horas de disponibilidad del ventilador destinado a refrigeración, aunque no exista demanda.')))
    self.panelInstalaciones.panel2.fraccionPotenciaNoDemanda.SetToolTip(wx.ToolTip(_('Fracción de la potencia consumida mientras no hay demanda, pero está en disponibilidad.')))
    self.panelInstalaciones.panel2.numeroHorasHelpButton.SetToolTip(wx.ToolTip(_('Estimador del número de horas de demanda térmica.')))
    self.panelInstalaciones.panel2.funcionamientoNoDemanda.SetToolTip(wx.ToolTip(_('Si el ventilador se apaga cuando cesa la demanda térmica, indique no.\nSi el ventilador permanece en funcionamiento aunque la demanda térmica haya desaparecido, indique si.')))
    self.panelInstalaciones.panel2.botonDefinirCurva.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante una curva.')))
    self.panelInstalaciones.panel2.botonDefinirEscalones.SetToolTip(wx.ToolTip(_('Defina cómo se fracciona el consumo de la bomba cuando se fracciona el caudal, mediante escalones.')))