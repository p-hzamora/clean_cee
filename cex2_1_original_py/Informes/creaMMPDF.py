# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Informes\creaMMPDF.pyc
# Compiled at: 2015-02-23 11:23:36
"""
Modulo: creaMMPDF.py

"""
from Calculos.listados import programaVersion
from Calculos.listadosWeb import listadoOpcionesTorreDeRefrigeracion, listadoOpcionesVentiladores, listadoOpcionesBombas, listadoOpcionesServicioVentiladores, listadoOpcionesServicioBombas, listadoInstalaciones, listadoInstalacionesClimatizacion, listadoInstalacionesElectrico, getTraduccion, getElementoEnListado
from Informes.creaPDF import FuenteAusente, Etiqueta, calculoPorcAhorro
from StringIO import StringIO
from reportlab.lib import colors
from reportlab.lib.colors import black, white, Color
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, CondPageBreak, Image, XPreformatted, Preformatted, Table, TableStyle
from reportlab.platypus.flowables import Flowable
from reportlab.rl_config import defaultPageSize
import DatosGenerales.trataImagenes as trataImagenes, base64, copy, datetime, directorios, math, operator, os, logging
DirectorioDoc = directorios.BuscaDirectorios().DirectorioDoc
Directorio = directorios.BuscaDirectorios().Directorio
PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()
top_margin = A4[1] - 0.75 * inch
bottom_margin = 0.5 * inch
left_margin = inch
right_margin = A4[0] - inch
frame_width = right_margin - left_margin

class GeneraInforme():
    """
    Clase: generaInforme del modulo creaPDF.py

    """

    def __init__(self, filename='', objEdificio=None, datosAdmin=[], listadoConjuntosMMUsuario=[], datosConfiguracionInforme=[]):
        self.filename = filename
        self.objEdificio = objEdificio
        self.datosAdmin = datosAdmin
        self.datosConfiguracionInforme = datosConfiguracionInforme
        conjuntosMMSeleccionados = [
         self.datosConfiguracionInforme[0],
         self.datosConfiguracionInforme[1],
         self.datosConfiguracionInforme[2]]
        self.listadoConjuntosMMUsuario = []
        for conjuntoMM in listadoConjuntosMMUsuario:
            if conjuntoMM.nombre in conjuntosMMSeleccionados:
                self.listadoConjuntosMMUsuario.append(conjuntoMM)

        self.fechaImpresionCertificado = datetime.date.today()
        self.pageNumber = 1
        self.generaInforme()

    def generaInforme(self):
        """
        Metodo: generaInforme

        """
        if self.listadoConjuntosMMUsuario == []:
            return
        self.getEstilosDocumento()
        if self.filename == None or self.filename == '':
            self.filename = DirectorioDoc + '/informeMedidasMejora.pdf'
        else:
            if '.cex' in self.filename:
                self.filename = self.filename.replace('.cex', '_informeMedidasMejora.pdf')
            else:
                if '.CEX' in self.filename:
                    self.filename = self.filename.replace('.CEX', '_informeMedidasMejora.pdf')
                else:
                    self.filename = DirectorioDoc + '/informeMedidasMejora.pdf'
                try:
                    os.remove(self.filename)
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    if os.path.exists(self.filename) == True:
                        raise BorradoInformeMM

            Story = []
            for conjuntoMM in self.listadoConjuntosMMUsuario:
                Story += self.paginaInicialMM(conjuntoMM)
                Story += self.siguientesPaginasMM(conjuntoMM)
                Story.append(PageBreak())

        self.pageNumber = 1
        doc = SimpleDocTemplate(self.filename.encode('iso-8859-15'))
        doc.leftMargin = 1.27 * cm
        doc.rightMargin = 1.27 * cm
        doc.topMargin = 4.5 * cm
        doc.bottomMargin = 1.27 * cm
        Story2 = copy.deepcopy(Story)
        self.totalPageNumber = 1
        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
        self.totalPageNumber = doc.page
        doc = SimpleDocTemplate(self.filename.encode('iso-8859-15'))
        doc.leftMargin = 1.27 * cm
        doc.rightMargin = 1.27 * cm
        doc.topMargin = 4.5 * cm
        doc.bottomMargin = 1.27 * cm
        self.pageNumber = 1
        doc.build(Story2, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
        return

    def getEstilosDocumento(self):
        try:
            pdfmetrics.registerFont(TTFont('arialbd', 'arialbd.ttf'))
            pdfmetrics.registerFont(TTFont('arialbi', 'arialbi.ttf'))
            pdfmetrics.registerFont(TTFont('ariali', 'ariali.ttf'))
            pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
        except:
            logging.info('Excepcion Fuente Ausente en: %s' % __name__)
            raise FuenteAusente

        pdfmetrics.registerFontFamily('arial', normal='arial', bold='arialbd', italic='ariali', boldItalic='arialbi')
        self.titulo1 = ParagraphStyle('normal', fontName='arialbd', fontSize=16, alignment=TA_CENTER)
        self.titulo2 = ParagraphStyle('normal', fontName='arialbd', fontSize=10, alignment=TA_CENTER)
        self.titulo3 = ParagraphStyle('normal', fontName='arialbd', fontSize=9, alignment=TA_CENTER)
        self.titulo4 = ParagraphStyle('normal', fontName='arialbd', fontSize=9, alignment=TA_CENTER)
        self.titulo5 = ParagraphStyle('normal', fontName='arialbd', fontSize=9, alignment=TA_JUSTIFY)
        self.titulo6 = ParagraphStyle('normal', fontName='arialbd', fontSize=7, alignment=TA_CENTER)
        self.titulo7 = ParagraphStyle('normal', fontName='arialbd', fontSize=6.7, alignment=TA_CENTER)
        self.tabla1ContenidosN = ParagraphStyle('normal', fontName='arialbd', fontSize=9, leading=10.0, alignment=TA_JUSTIFY)
        self.tabla1ContenidosNC = ParagraphStyle('normal', fontName='arialbd', fontSize=9, leading=8, alignment=TA_CENTER)
        self.tabla1ContenidosNC2 = ParagraphStyle('normal', fontName='arialbi', fontSize=9, leading=8, alignment=TA_CENTER)
        self.tabla1Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=8, leading=10.0, alignment=TA_CENTER)
        self.tabla4Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=9, leading=10.0, alignment=TA_JUSTIFY)
        self.tabla2Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=9, leading=10.0, alignment=TA_CENTER)
        self.tabla5Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=6, leading=10.0, spaceBefore=0.0, spaceAfter=0.0, alignment=TA_CENTER)
        self.tabla2ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=9, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.tabla3ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=7, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.tabla2ContenidosBis = ParagraphStyle('normal', fontName='arial', fontSize=7, leading=10.0, alignment=TA_CENTER)
        self.tabla1ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=9, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.grisEncabezado = Color(red=0.209 / 0.255, green=0.209 / 0.255, blue=0.209 / 0.255)
        self.gris = Color(red=0.217 / 0.255, green=0.217 / 0.255, blue=0.217 / 0.255)
        self.morado = Color(red=0.218 / 0.255, green=0.15 / 0.255, blue=0.148 / 0.255)
        self.rosa = Color(red=0.253 / 0.255, green=0.233 / 0.255, blue=0.217 / 0.255)
        self.naranja = Color(red=0.251 / 0.255, green=0.212 / 0.255, blue=0.18 / 0.255)
        self.moradoFuerte = Color(red=0.192 / 0.255, green=0.08 / 0.255, blue=0.077 / 0.255)

    def paginaInicialMM(self, conjuntoMM):
        Story = []
        Story += self.denominacionYDescripcionMM(conjuntoMM)
        Story += self.tablaCalificacionEnergeticaGlobalMM(conjuntoMM)
        Story += self.tablaCalificacionEnergeticaParcialMM(conjuntoMM)
        Story.append(PageBreak())
        return Story

    def denominacionYDescripcionMM(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Informe descriptivo de la medida de mejora'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 2 * cm))
        a0 = Paragraph(_('DENOMINACIÓN DE LA MEDIDA DE MEJORA'), self.titulo2)
        a1 = Paragraph(unicode(conjuntoMM.nombre), self.tabla4Contenidos)
        data = [[a0],
         [
          a1]]
        t = Table(data, None, [1 * cm, 1 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 1.5 * cm))
        a0 = Paragraph(_('DESCRIPCIÓN DE LA MEDIDA DE MEJORA'), self.titulo2)
        a1 = Paragraph(_('Características de la medida (modelo de equipos, materiales, parámetros característicos )'), self.tabla1ContenidosN)
        a2 = Paragraph(unicode(conjuntoMM.caracteristicas), self.tabla4Contenidos)
        costeInversionInicial = conjuntoMM.calculoInversionInicial()
        if costeInversionInicial != '-':
            costeMM = '%s €' % costeInversionInicial
        else:
            costeMM = costeInversionInicial
        a3 = Paragraph(_('Coste estimado de la medida'), self.tabla1ContenidosN)
        a4 = Paragraph(unicode(costeMM), self.tabla4Contenidos)
        a5 = Paragraph(_('Otros datos de interés'), self.tabla1ContenidosN)
        a6 = Paragraph(unicode(conjuntoMM.otrosDatos), self.tabla4Contenidos)
        data = [
         [
          a0],
         [
          a1],
         [
          a2],
         [
          a3],
         [
          a4],
         [
          a5],
         [
          a6]]
        t = Table(data, None, [1.0 * cm, 0.5 * cm, None, 0.5 * cm, None, 0.5 * cm, None], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), self.rosa),
         (
          'BOX', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'LINEABOVE', (0, 1), (0, 1), 1, colors.black),
         (
          'LINEABOVE', (0, 3), (0, 3), 1, colors.black),
         (
          'LINEABOVE', (0, 5), (0, 5), 1, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 1 * cm))
        return Story

    def tablaCalificacionEnergeticaGlobalMM(self, conjuntoMM):
        Story = []
        t = Paragraph(_('CALIFICACIÓN ENERGÉTICA GLOBAL'), self.titulo3)
        Story.append(t)
        a11 = Paragraph(_('CONSUMO DE ENERGÍA'), self.tabla1ContenidosNC)
        a21 = Paragraph(_('PRIMARIA NO RENOVABLE'), self.tabla1ContenidosNC)
        a31 = Paragraph(_('[kWh/m² año]'), self.tabla1ContenidosNC2)
        a12 = Paragraph(_('EMISIONES DE DIÓXIDO DE'), self.tabla1ContenidosNC)
        a22 = Paragraph(_(' CARBONO'), self.tabla1ContenidosNC)
        a32 = Paragraph(_('[kgCO2/ m² año]'), self.tabla1ContenidosNC2)
        data = [[a11, a12],
         [
          a21, a22],
         [
          a31, a32]]
        t = Table(data, [7.08 * cm, 7.08 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), self.rosa),
         (
          'BOX', (0, 0), (0, -1), 0.5, colors.black),
         (
          'BOX', (1, 0), (1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        imagenEmisionesCO2 = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 2)), conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_limites)
        imagenEmisionesCO2.scaleX = 0.75
        imagenEmisionesCO2.scaleY = 0.75
        imagenEmisionesCO2.translateX = 0 * cm
        imagenEmisionesCO2.translateY = 0.9 * cm
        imagenEnPrimNoREn = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 2)), conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_limites)
        imagenEnPrimNoREn.scaleX = 0.75
        imagenEnPrimNoREn.scaleY = 0.75
        imagenEnPrimNoREn.translateX = 0 * cm
        imagenEnPrimNoREn.translateY = 0.9 * cm
        data = [
         [
          imagenEnPrimNoREn, '', imagenEmisionesCO2, '']]
        t = Table(data, [4.52 * cm, 2.58 * cm, 4.52 * cm, 2.58 * cm], [2.52 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 1 * cm))
        return Story

    def tablaCalificacionEnergeticaParcialMM(self, conjuntoMM):
        Story = []
        t = Paragraph(_('CALIFICACIONES ENERGÉTICAS PARCIALES'), self.titulo3)
        Story.append(t)
        a11 = Paragraph(_('DEMANDA DE CALEFACCIÓN'), self.tabla1ContenidosNC)
        a21 = Paragraph(_('[kWh/ m² año]'), self.tabla1ContenidosNC2)
        a12 = Paragraph(_('DEMANDA DE REFRIGERACIÓN'), self.tabla1ContenidosNC)
        a22 = Paragraph(_('[kWh/m² año]'), self.tabla1ContenidosNC2)
        data = [[a11, a12],
         [
          a21, a22]]
        t = Table(data, [7.08 * cm, 7.08 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), self.rosa),
         (
          'BOX', (0, 0), (0, -1), 0.5, colors.black),
         (
          'BOX', (1, 0), (1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        imagenDdaCal = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal, 2)), conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_limites)
        imagenDdaCal.scaleX = 0.75
        imagenDdaCal.scaleY = 0.75
        imagenDdaCal.translateX = 0 * cm
        imagenDdaCal.translateY = 0.9 * cm
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            textoDdaRef = Paragraph('No calificable', self.tabla1ContenidosNC)
            data = [[imagenDdaCal, '', textoDdaRef, '']]
        else:
            imagenDdaRef = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef, 2)), conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_limites)
            imagenDdaRef.scaleX = 0.75
            imagenDdaRef.scaleY = 0.75
            imagenDdaRef.translateX = 0 * cm
            imagenDdaRef.translateY = 0.9 * cm
            data = [
             [
              imagenDdaCal, '', imagenDdaRef, '']]
        t = Table(data, [4.52 * cm, 2.58 * cm, 4.52 * cm, 2.58 * cm], [2.52 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def siguientesPaginasMM(self, conjuntoMM):
        Story = []
        Story += self.analisisTecnico(conjuntoMM)
        Story += self.envolventeTermica(conjuntoMM)
        Story += self.instalacionesTermicas(conjuntoMM)
        if conjuntoMM.datosNuevoEdificio.programa != 'Residencial':
            Story += self.torresRef(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
            Story.append(CondPageBreak(6 * cm))
            Story += self.ventilacionBombeo(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
            Story.append(CondPageBreak(10 * cm))
            Story += self.instalacionIluminacion(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
            Story.append(CondPageBreak(6 * cm))
            Story += self.condicionesFuncionamientoOcupacion(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
            Story.append(CondPageBreak(6 * cm))
        Story += self.energiasRenovables(conjuntoMM)
        return Story

    def envolventeTermica(self, conjuntoMM):
        Story = []
        t = Paragraph(_('ENVOLVENTE TÉRMICA'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.cerramientosOpacos(conjuntoMM)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        Story += self.huecosLucernarios(conjuntoMM)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        return Story

    def instalacionesTermicas(self, conjuntoMM):
        Story = []
        Story.append(CondPageBreak(6 * cm))
        t = Paragraph(_('INSTALACIONES TÉRMICAS'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.generadoresCalefaccion(conjuntoMM)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        Story += self.generadoresRefrigeracion(conjuntoMM)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        Story += self.instalacionesACS(conjuntoMM)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        return Story

    def analisisTecnico(self, conjuntoMM):
        Story = []
        t = Paragraph(_('ANALISÍS TÉCNICO'), self.titulo5)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        a11 = Paragraph(_('Indicador'), self.titulo3)
        a12 = Paragraph(_('Calefacción'), self.titulo3)
        a13 = ''
        a14 = ''
        a15 = Paragraph(_('Refrigeración'), self.titulo3)
        a16 = ''
        a17 = ''
        a18 = Paragraph(_('ACS'), self.titulo3)
        a19 = ''
        a110 = ''
        a111 = Paragraph(_('Iluminación'), self.titulo3)
        a112 = ''
        a113 = ''
        a114 = Paragraph(_('Total'), self.titulo3)
        a115 = ''
        a116 = ''
        a21 = ''
        a22 = Paragraph(_('Valor'), self.tabla2Contenidos)
        a23 = ''
        a24 = Paragraph(_('ahorro respecto a la situación original'), self.tabla5Contenidos)
        a25 = Paragraph(_('Valor'), self.tabla2Contenidos)
        a26 = ''
        a27 = Paragraph(_('ahorro respecto a la situación original'), self.tabla5Contenidos)
        a28 = Paragraph(_('Valor'), self.tabla2Contenidos)
        a29 = ''
        a210 = Paragraph(_('ahorro respecto a la situación original'), self.tabla5Contenidos)
        a211 = Paragraph(_('Valor'), self.tabla2Contenidos)
        a212 = ''
        a213 = Paragraph(_('ahorro respecto a la situación original'), self.tabla5Contenidos)
        a214 = Paragraph(_('Valor'), self.tabla2Contenidos)
        a215 = ''
        a216 = Paragraph(_('ahorro respecto a la situación original'), self.tabla5Contenidos)
        porcAhorroEnPrimNoRenCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            porcAhorroEnPrimNoRenRef = '-'
        else:
            porcAhorroEnPrimNoRenRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef)
        porcAhorroEnPrimNoRenACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS)
        if self.objEdificio.programa == 'Residencial':
            porcAhorroEnPrimNoRenIlum = '-'
        else:
            porcAhorroEnPrimNoRenIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum)
        porcAhorroEnPrimNoRen = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenMostrar, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar)
        a31 = Paragraph(_('Consumo Energía primaria no renovable [kWh/m² año]'), self.tabla2Contenidos)
        a32 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal, self.tabla3ContenidosC)
        a33 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal_nota, self.tabla2ContenidosC)
        a34 = Paragraph('%s %s' % (porcAhorroEnPrimNoRenCal, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            a35 = Paragraph('-', self.tabla2ContenidosC)
            a36 = Paragraph('-', self.tabla2ContenidosC)
        else:
            a35 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef, self.tabla3ContenidosC)
            a36 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef_nota, self.tabla2ContenidosC)
        a37 = Paragraph('%s %s' % (porcAhorroEnPrimNoRenRef, '%'), self.tabla3ContenidosC)
        a38 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS, self.tabla3ContenidosC)
        a39 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS_nota, self.tabla2ContenidosC)
        a310 = Paragraph('%s %s' % (porcAhorroEnPrimNoRenACS, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa != 'Residencial':
            a311 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum, self.tabla3ContenidosC)
            a312 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum_nota, self.tabla2ContenidosC)
        else:
            a311 = Paragraph('-', self.tabla3ContenidosC)
            a312 = Paragraph('-', self.tabla3ContenidosC)
        a313 = Paragraph('%s %s' % (porcAhorroEnPrimNoRenIlum, '%'), self.tabla3ContenidosC)
        a314 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, self.tabla3ContenidosC)
        a315 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_nota, self.tabla2ContenidosC)
        a316 = Paragraph('%s %s' % (porcAhorroEnPrimNoRen, '%'), self.tabla3ContenidosC)
        porcAhorroEnFinalCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalCal)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            porcAhorroEnFinalRef = '-'
        else:
            porcAhorroEnFinalRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRef)
        porcAhorroEnFinalACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalACS)
        if self.objEdificio.programa == 'Residencial':
            porcAhorroEnFinalIlum = '-'
        else:
            porcAhorroEnFinalIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalIlum)
        porcAhorroEnFinal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinal)
        a41 = Paragraph(_('Consumo Energía final [kWh/m² año]'), self.tabla2Contenidos)
        a42 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalCal, self.tabla3ContenidosC)
        a43 = ''
        a44 = Paragraph('%s %s' % (porcAhorroEnFinalCal, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            a45 = Paragraph('-', self.tabla3ContenidosC)
            a46 = ''
        else:
            a45 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRef, self.tabla3ContenidosC)
            a46 = ''
        a47 = Paragraph('%s %s' % (porcAhorroEnFinalRef, '%'), self.tabla3ContenidosC)
        a48 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalACS, self.tabla3ContenidosC)
        a49 = ''
        a410 = Paragraph('%s %s' % (porcAhorroEnFinalACS, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial':
            a411 = Paragraph('-', self.tabla3ContenidosC)
            a412 = ''
        else:
            a411 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalIlum, self.tabla3ContenidosC)
            a412 = ''
        a413 = Paragraph('%s %s' % (porcAhorroEnFinalIlum, '%'), self.tabla3ContenidosC)
        a414 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinal, self.tabla3ContenidosC)
        a415 = ''
        a416 = Paragraph('%s %s' % (porcAhorroEnFinal, '%'), self.tabla3ContenidosC)
        porcAhorroEmisionesCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            porcAhorroEmisionesRef = '-'
        else:
            porcAhorroEmisionesRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef)
        porcAhorroEmisionesACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS)
        if self.objEdificio.programa == 'Residencial':
            porcAhorroEmisionesIlum = '-'
        else:
            porcAhorroEmisionesIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum)
        porcAhorroEmisiones = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesMostrar, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar)
        a51 = Paragraph(_('Emisiones de CO2 [kgCO2/m² año]'), self.tabla2Contenidos)
        a52 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal, self.tabla3ContenidosC)
        a53 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal_nota, self.tabla2ContenidosC)
        a54 = Paragraph('%s %s' % (porcAhorroEmisionesCal, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            a55 = Paragraph('-', self.tabla3ContenidosC)
            a56 = Paragraph('-', self.tabla3ContenidosC)
        else:
            a55 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef, self.tabla3ContenidosC)
            a56 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef_nota, self.tabla2ContenidosC)
        a57 = Paragraph('%s %s' % (porcAhorroEmisionesRef, '%'), self.tabla3ContenidosC)
        a58 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS, self.tabla3ContenidosC)
        a59 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS_nota, self.tabla2ContenidosC)
        a510 = Paragraph('%s %s' % (porcAhorroEmisionesACS, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial':
            a511 = Paragraph('-', self.tabla3ContenidosC)
            a512 = Paragraph('-', self.tabla3ContenidosC)
        else:
            a511 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum, self.tabla3ContenidosC)
            a512 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum_nota, self.tabla2ContenidosC)
        a513 = Paragraph('%s %s' % (porcAhorroEmisionesIlum, '%'), self.tabla3ContenidosC)
        a514 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, self.tabla3ContenidosC)
        a515 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota, self.tabla2ContenidosC)
        a516 = Paragraph('%s %s' % (porcAhorroEmisiones, '%'), self.tabla3ContenidosC)
        porcAhorroDdaCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.ddaBrutaCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            porcAhorroDdaRef = '-'
        else:
            porcAhorroDdaRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.ddaBrutaRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef)
        a61 = Paragraph(_('Demanda [kWh/m² año]'), self.tabla2Contenidos)
        a62 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal, self.tabla3ContenidosC)
        a63 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota, self.tabla2ContenidosC)
        a64 = Paragraph('%s %s' % (porcAhorroDdaCal, '%'), self.tabla3ContenidosC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1',
                                                                                                      'A1',
                                                                                                      'B1',
                                                                                                      'C1',
                                                                                                      'D1',
                                                                                                      'E1'):
            a65 = Paragraph('-', self.tabla3ContenidosC)
            a66 = Paragraph('-', self.tabla3ContenidosC)
        else:
            a65 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef, self.tabla3ContenidosC)
            a66 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota, self.tabla2ContenidosC)
        a67 = Paragraph('%s %s' % (porcAhorroDdaRef, '%'), self.tabla3ContenidosC)
        a68 = ''
        a69 = ''
        a610 = ''
        a611 = ''
        a612 = ''
        a613 = ''
        a614 = ''
        a615 = ''
        a616 = ''
        data = [
         [
          a11, a12, a13, a14, a15, a16, a17, a18, a19, 
          a110, a111, a112, a113, a114, a115, a116],
         [
          a21, a22, a23, a24, a25, a26, a27, a28, a29, 
          a210, a211, a212, a213, a214, a215, a216],
         [
          a41, a42, a43, a44, a45, a46, a47, a48, a49, 
          a410, a411, a412, a413, a414, a415, a416],
         [
          a31, a32, a33, a34, a35, a36, a37, a38, a39, 
          a310, a311, a312, a313, a314, a315, a316],
         [
          a51, a52, a53, a54, a55, a56, a57, a58, a59, 
          a510, a511, a512, a513, a514, a515, a516],
         [
          a61, a62, a63, a64, a65, a66, a67, a68, a69, 
          a610, a611, a612, a613, a614, a615, a616]]
        t = Table(data, [3.5 * cm, 0.85 * cm, 0.5 * cm, 1.55 * cm, 0.85 * cm, 0.5 * cm, 1.55 * cm, 0.85 * cm, 0.5 * cm, 1.55 * cm, 0.85 * cm, 0.5 * cm, 1.55 * cm, 0.85 * cm, 0.5 * cm, 1.55 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 1), self.rosa),
         (
          'BACKGROUND', (0, 2), (0, 5), self.rosa),
         (
          'BACKGROUND', (3, 2), (3, 5), self.naranja),
         (
          'BACKGROUND', (6, 2), (6, 5), self.naranja),
         (
          'BACKGROUND', (9, 2), (9, 4), self.naranja),
         (
          'BACKGROUND', (12, 2), (12, 4), self.naranja),
         (
          'BACKGROUND', (15, 2), (15, 4), self.naranja),
         (
          'BACKGROUND', (7, 5), (-1, 5), colors.grey),
         (
          'SPAN', (1, 0), (3, 0)),
         (
          'SPAN', (4, 0), (6, 0)),
         (
          'SPAN', (7, 0), (9, 0)),
         (
          'SPAN', (10, 0), (12, 0)),
         (
          'SPAN', (13, 0), (15, 0)),
         (
          'GRID', (0, 0), (-1, -2), 0.5, colors.black),
         (
          'GRID', (0, -1), (6, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
         (
          'SPAN', (0, 0), (0, 1)),
         (
          'SPAN', (1, 1), (2, 1)),
         (
          'SPAN', (4, 1), (5, 1)),
         (
          'SPAN', (7, 1), (8, 1)),
         (
          'SPAN', (10, 1), (11, 1)),
         (
          'SPAN', (13, 1), (14, 1)),
         (
          'SPAN', (1, 2), (2, 2)),
         (
          'SPAN', (4, 2), (5, 2)),
         (
          'SPAN', (7, 2), (8, 2)),
         (
          'SPAN', (10, 2), (11, 2)),
         (
          'SPAN', (13, 2), (14, 2)),
         (
          'BOX', (7, -1), (-1, 5), 0.5, colors.black),
         (
          'SPAN', (7, -1), (-1, 5))]))
        Story.append(t)
        Story.append(Spacer(0, 1 * cm))
        return Story

    def primeraFilaCerramientos(self):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo4)
        a12 = Paragraph(_('Tipo'), self.titulo4)
        a13 = Paragraph(_('Superficie actual [m²]'), self.titulo4)
        a14 = Paragraph(_('Transmitancia actual [W/m² K]'), self.titulo4)
        a15 = Paragraph(_('Superficie post mejora [m²]'), self.titulo4)
        a16 = Paragraph(_('Transmitancia post mejora [W/m² K]'), self.titulo4)
        data = [
         [
          a11, a12, a13, a14, a15, a16]]
        t = Table(data, [4.75 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2 * cm, 2.5 * cm], [
         2.25 * cm], None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 1), self.morado),
         (
          'BACKGROUND', (0, 0), (3, 1), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def primeraFilaHuecos(self):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo4)
        a12 = Paragraph(_('Tipo'), self.titulo4)
        a13 = Paragraph(_('Superficie actual [m²]'), self.titulo4)
        a14 = Paragraph(_('Transmitancia actual del hueco[W/m² K]'), self.titulo4)
        a17 = Paragraph(_('Transmitancia actual del vidrio[W/m² K]'), self.titulo4)
        a15 = Paragraph(_('Superficie post mejora [m²]'), self.titulo4)
        a16 = Paragraph(_('Transmitancia post mejora [W/m² K]'), self.titulo4)
        a18 = Paragraph(_('Transmitancia post mejora del vidrio [W/m² K]'), self.titulo4)
        data = [
         [
          a11, a12, a13, a14, a17, a15, a16, a18]]
        t = Table(data, [2.25 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2.5 * cm, 2 * cm, 2.5 * cm, 2.5 * cm], [
         2.25 * cm], None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.morado),
         (
          'BACKGROUND', (0, 0), (4, 1), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def cerramientosOpacos(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Cerramientos opacos'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primeraFilaCerramientos()
        cerrConjuntoMMYametidosEnInforme = []
        for cerr in self.objEdificio.datosIniciales.listadoCerramientos:
            a0 = Paragraph('%s' % cerr.nombre, self.tabla1ContenidosC)
            a1 = Paragraph('%s' % _(cerr.tipo), self.tabla1ContenidosC)
            a2 = Paragraph('%0.2f' % cerr.superficieNeta, self.tabla1ContenidosC)
            a3 = Paragraph('%0.2f' % cerr.U, self.tabla1ContenidosC)
            cerrEncontrado = False
            for cerrConjuntoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.listadoCerramientos:
                if cerrConjuntoMM.nombre == cerr.nombre:
                    a4 = Paragraph('%0.2f' % cerrConjuntoMM.superficieNeta, self.tabla1ContenidosC)
                    a5 = Paragraph('%0.2f' % cerrConjuntoMM.U, self.tabla1ContenidosC)
                    cerrEncontrado = True
                    cerrConjuntoMMYametidosEnInforme.append(cerrConjuntoMM)
                    break

            if cerrEncontrado == False:
                a4 = Paragraph('-', self.tabla1ContenidosC)
                a5 = Paragraph('-', self.tabla1ContenidosC)
            data = [
             [
              a0, a1, a2, a3, a4, a5]]
            t = Table(data, [4.75 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2 * cm, 2.5 * cm], None, None, 1, 1, 1, hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)

        for cerrConjuntoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.listadoCerramientos:
            if cerrConjuntoMM not in cerrConjuntoMMYametidosEnInforme:
                a0 = Paragraph('%s' % conjuntoMM.nombre, self.tabla1ContenidosC)
                a1 = Paragraph('-', self.tabla1ContenidosC)
                a2 = Paragraph('-', self.tabla1ContenidosC)
                a3 = Paragraph('-', self.tabla1ContenidosC)
                a4 = Paragraph('%0.2f' % cerrConjuntoMM.superficieBruta, self.tabla1ContenidosC)
                a5 = Paragraph('%0.2f' % cerrConjuntoMM.U, self.tabla1ContenidosC)
                data = [
                 [
                  a0, a1, a2, a3, a4, a5]]
                t = Table(data, [4.75 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2 * cm, 2.5 * cm], None, None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 1), self.gris),
                 (
                  'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                 (
                  'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                 (
                  'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                Story.append(t)

        return Story

    def huecosLucernarios(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Huecos y lucernarios'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primeraFilaHuecos()
        huecosConjuntoMMYametidosEnInforme = []
        for h in self.objEdificio.datosIniciales.listadoHuecos:
            a0 = Paragraph('%s' % h.descripcion, self.tabla1ContenidosC)
            a1 = Paragraph('%s' % h.tipo, self.tabla1ContenidosC)
            a2 = Paragraph('%s' % h.superficie, self.tabla1ContenidosC)
            a3 = Paragraph('%0.2f' % h.calculoUhueco(), self.tabla1ContenidosC)
            a7 = Paragraph('%0.2f' % h.Uvidrio, self.tabla1ContenidosC)
            huecoEncontrado = False
            for hConjuntoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.listadoHuecos:
                if h.descripcion == hConjuntoMM.descripcion:
                    a4 = Paragraph('%s' % hConjuntoMM.superficie, self.tabla1ContenidosC)
                    a5 = Paragraph('%0.2f' % hConjuntoMM.calculoUhueco(), self.tabla1ContenidosC)
                    a8 = Paragraph('%0.2f' % hConjuntoMM.Uvidrio, self.tabla1ContenidosC)
                    huecoEncontrado = True
                    huecosConjuntoMMYametidosEnInforme.append(hConjuntoMM)
                    break

            if huecoEncontrado == False:
                a4 = Paragraph('-', self.tabla1ContenidosC)
                a5 = Paragraph('-', self.tabla1ContenidosC)
                a8 = Paragraph('-', self.tabla1ContenidosC)
            data = [
             [
              a0, a1, a2, a3, a7, a4, a5, a8]]
            t = Table(data, [2.25 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2.5 * cm, 2 * cm, 2.5 * cm, 2.5 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)

        for hConjuntoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.listadoHuecos:
            if hConjuntoMM not in huecosConjuntoMMYametidosEnInforme:
                a0 = Paragraph('%s' % hConjuntoMM.descripcion, self.tabla1ContenidosC)
                a1 = Paragraph('%s' % hConjuntoMM.tipo, self.tabla1ContenidosC)
                a2 = Paragraph('-', self.tabla1ContenidosC)
                a3 = Paragraph('-', self.tabla1ContenidosC)
                a7 = Paragraph('-', self.tabla1ContenidosC)
                a4 = Paragraph('%s' % hConjuntoMM.superficie, self.tabla1ContenidosC)
                a5 = Paragraph('%0.2f' % hConjuntoMM.calculoUhueco(), self.tabla1ContenidosC)
                a8 = Paragraph('%0.2f' % hConjuntoMM.Uvidrio, self.tabla1ContenidosC)
                data = [
                 [
                  a0, a1, a2, a3, a7, a4, 
                  a5, a8]]
                t = Table(data, [2.25 * cm, 2.25 * cm, 1.75 * cm, 2.25 * cm, 2.5 * cm, 2 * cm, 2.5 * cm, 2.5 * cm], None, None, 1, 1, 1)
                t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 1), self.gris),
                 (
                  'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                 (
                  'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                 (
                  'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                Story.append(t)

        return Story

    def primerasFilaACSRefCalTablas(self):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo6)
        a12 = Paragraph(_('Tipo'), self.titulo6)
        a13 = Paragraph(_('Potencia nominal'), self.titulo6)
        a14 = Paragraph(_('Rendi- miento Estacional'), self.titulo6)
        a15 = Paragraph(_('Estimación Energía Consumida anual'), self.titulo6)
        a16 = Paragraph(_('Tipo post mejora '), self.titulo6)
        a17 = Paragraph(_('Potencia nominal post mejora'), self.titulo6)
        a18 = Paragraph(_('Rendimiento estacional post mejora'), self.titulo6)
        a19 = Paragraph(_('Estimación Energía Consumida anual Post mejora'), self.titulo6)
        a110 = Paragraph(_('Energía anual ahorrada'), self.titulo6)
        a21 = ''
        a22 = ''
        a23 = Paragraph(_('[kW]'), self.titulo7)
        a24 = Paragraph(_('[%]'), self.titulo7)
        a25 = Paragraph(_('[kWh/m²año]'), self.titulo7)
        a26 = ''
        a27 = Paragraph(_('[kW]'), self.titulo7)
        a28 = Paragraph(_('[%]'), self.titulo7)
        a29 = Paragraph(_('[kWh/m²año]'), self.titulo7)
        a210 = Paragraph(_('[kWh/m²año]'), self.titulo7)
        data = [
         [
          a11, a12, a13, a14, a15, a16, a17, a18, a19, 
          a110],
         [
          a21, a22, a23, a24, a25, a26, a27, a28, a29, 
          a210]]
        t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], [
         2.25 * cm, 0.75 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.morado),
         (
          'BACKGROUND', (0, 0), (4, 1), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'SPAN', (0, 0), (0, 1)),
         (
          'SPAN', (1, 0), (1, 1)),
         (
          'SPAN', (5, 0), (5, 1)),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def tablaComparacionEquipos(self, equiposEdificioObjeto=[], equiposEdificioMejorado=[]):
        Story = []
        equiposConjuntoMMYaMetidosEnInforme = []
        for i in equiposEdificioObjeto:
            a0 = Paragraph('%s' % i.nombre, self.tabla2ContenidosBis)
            if getElementoEnListado(listado=listadoInstalaciones, elemento=i.generador) == True:
                listado = listadoInstalaciones
            elif getElementoEnListado(listado=listadoInstalacionesClimatizacion, elemento=i.generador) == True:
                listado = listadoInstalacionesClimatizacion
            elif getElementoEnListado(listado=listadoInstalacionesElectrico, elemento=i.generador) == True:
                listado = listadoInstalacionesElectrico
            a1 = Paragraph('%s' % _(i.generador), self.tabla2ContenidosBis)
            a2 = Paragraph('%s' % i.potencia, self.tabla2ContenidosBis)
            a3 = Paragraph('%s %s' % (i.rendimiento, '%'), self.tabla2ContenidosBis)
            a4 = Paragraph('-', self.tabla2ContenidosBis)
            equipoEncontrado = False
            for iEquipoMM in equiposEdificioMejorado:
                if i.nombre == iEquipoMM.nombre:
                    if getElementoEnListado(listado=listadoInstalaciones, elemento=iEquipoMM.generador) == True:
                        listado = listadoInstalaciones
                    elif getElementoEnListado(listado=listadoInstalacionesClimatizacion, elemento=iEquipoMM.generador) == True:
                        listado = listadoInstalacionesClimatizacion
                    elif getElementoEnListado(listado=listadoInstalacionesElectrico, elemento=iEquipoMM.generador) == True:
                        listado = listadoInstalacionesElectrico
                    a5 = Paragraph(_(i.generador), self.tabla2ContenidosBis)
                    a6 = Paragraph('%s' % iEquipoMM.potencia, self.tabla2ContenidosBis)
                    a7 = Paragraph('%s %s' % (iEquipoMM.rendimiento, '%'), self.tabla2ContenidosBis)
                    a8 = Paragraph('-', self.tabla2ContenidosBis)
                    a9 = Paragraph('-', self.tabla2ContenidosBis)
                    equipoEncontrado = True
                    equiposConjuntoMMYaMetidosEnInforme.append(iEquipoMM)
                    break

            if equipoEncontrado == False:
                a5 = Paragraph('-', self.tabla2ContenidosBis)
                a6 = Paragraph('-', self.tabla2ContenidosBis)
                a7 = Paragraph('-', self.tabla2ContenidosBis)
                a8 = Paragraph('-', self.tabla2ContenidosBis)
                a9 = Paragraph('-', self.tabla2ContenidosBis)
            data = [[a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]]
            t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)

        for iEquipoMM in equiposEdificioMejorado:
            if iEquipoMM not in equiposConjuntoMMYaMetidosEnInforme:
                a0 = Paragraph('%s' % iEquipoMM.nombre, self.tabla2ContenidosBis)
                a1 = Paragraph('-', self.tabla2ContenidosBis)
                a2 = Paragraph('-', self.tabla2ContenidosBis)
                a3 = Paragraph('-', self.tabla2ContenidosBis)
                a4 = Paragraph('-', self.tabla2ContenidosBis)
                if getElementoEnListado(listado=listadoInstalaciones, elemento=iEquipoMM.generador) == True:
                    listado = listadoInstalaciones
                elif getElementoEnListado(listado=listadoInstalacionesClimatizacion, elemento=iEquipoMM.generador) == True:
                    listado = listadoInstalacionesClimatizacion
                elif getElementoEnListado(listado=listadoInstalacionesElectrico, elemento=iEquipoMM.generador) == True:
                    listado = listadoInstalacionesElectrico
                a5 = Paragraph(_(iEquipoMM.generador), self.tabla2ContenidosBis)
                a6 = Paragraph('%s' % iEquipoMM.potencia, self.tabla2ContenidosBis)
                a7 = Paragraph('%s %s' % (iEquipoMM.rendimiento, '%'), self.tabla2ContenidosBis)
                a8 = Paragraph('-', self.tabla2ContenidosBis)
                a9 = Paragraph('-', self.tabla2ContenidosBis)
                data = [
                 [
                  a0, a1, a2, a3, a4, a5, 
                  a6, a7, a8, a9]]
                t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
                t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
                 (
                  'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                 (
                  'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                 (
                  'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                Story.append(t)

        if len(equiposEdificioObjeto) == 0 and len(equiposEdificioMejorado) == 0:
            data = [
             [
              '', '', '', '', '', '', '', '', 
              '', '']]
            t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)
        return Story

    def generadoresCalefaccion(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Generadores de calefacción'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primerasFilaACSRefCalTablas()
        Story += self.tablaComparacionEquipos(equiposEdificioObjeto=self.objEdificio.datosIniciales.calefaccion.listado, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.calefaccion.listado)
        potNominaltotalCal = ''
        estimacionEnerConsumidaTotalCal = ''
        potNominalPostMejoraTotalCal = ''
        estimacionEnerConsumidaPostMejoraTotalCal = ''
        enerAhorradoTotalCal = ''
        a0 = Paragraph(_('TOTALES'), self.titulo4)
        a1 = ''
        a2 = Paragraph('%s' % potNominaltotalCal, self.tabla1Contenidos)
        a3 = ''
        a4 = Paragraph('%s' % estimacionEnerConsumidaTotalCal, self.tabla1Contenidos)
        a5 = ''
        a6 = Paragraph('%s' % potNominalPostMejoraTotalCal, self.tabla1Contenidos)
        a7 = ''
        a8 = Paragraph('%s' % estimacionEnerConsumidaPostMejoraTotalCal, self.tabla1Contenidos)
        a9 = Paragraph('%s' % enerAhorradoTotalCal, self.tabla1Contenidos)
        data = [
         [
          a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]]
        t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 1), self.naranja),
         (
          'BACKGROUND', (2, 0), (2, 1), self.naranja),
         (
          'BACKGROUND', (4, 0), (4, 1), self.naranja),
         (
          'BACKGROUND', (6, 0), (6, 1), self.moradoFuerte),
         (
          'BACKGROUND', (8, 0), (8, 1), self.moradoFuerte),
         (
          'BACKGROUND', (9, 0), (9, 1), self.moradoFuerte),
         (
          'BACKGROUND', (1, 0), (1, 0), colors.grey),
         (
          'BACKGROUND', (3, 0), (3, 0), colors.grey),
         (
          'BACKGROUND', (5, 0), (5, 0), colors.grey),
         (
          'BACKGROUND', (7, 0), (7, 0), colors.grey),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def generadoresRefrigeracion(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Generadores de refrigeración'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primerasFilaACSRefCalTablas()
        Story += self.tablaComparacionEquipos(equiposEdificioObjeto=self.objEdificio.datosIniciales.refrigeracion.listado, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.refrigeracion.listado)
        potNominaltotalRef = ''
        estimacionEnerConsumidaTotalRef = ''
        potNominalPostMejoraTotalRef = ''
        estimacionEnerConsumidaPostMejoraTotalRef = ''
        enerAhorradoTotalRef = ''
        a0 = Paragraph(_('TOTALES'), self.titulo4)
        a1 = ''
        a2 = Paragraph('-', self.tabla1Contenidos)
        a3 = ''
        a4 = Paragraph('-', self.tabla1Contenidos)
        a5 = ''
        a6 = Paragraph('-', self.tabla1Contenidos)
        a7 = ''
        a8 = Paragraph('-', self.tabla1Contenidos)
        a9 = Paragraph('-', self.tabla1Contenidos)
        data = [
         [
          a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]]
        t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 1), self.naranja),
         (
          'BACKGROUND', (2, 0), (2, 1), self.naranja),
         (
          'BACKGROUND', (4, 0), (4, 1), self.naranja),
         (
          'BACKGROUND', (6, 0), (6, 1), self.moradoFuerte),
         (
          'BACKGROUND', (8, 0), (8, 1), self.moradoFuerte),
         (
          'BACKGROUND', (9, 0), (9, 1), self.moradoFuerte),
         (
          'BACKGROUND', (1, 0), (1, 0), colors.grey),
         (
          'BACKGROUND', (3, 0), (3, 0), colors.grey),
         (
          'BACKGROUND', (5, 0), (5, 0), colors.grey),
         (
          'BACKGROUND', (7, 0), (7, 0), colors.grey),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def instalacionesACS(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Instalaciones de Agua Caliente Sanitaria'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primerasFilaACSRefCalTablas()
        Story += self.tablaComparacionEquipos(equiposEdificioObjeto=self.objEdificio.datosIniciales.ACS.listado, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.ACS.listado)
        potNominaltotalACS = ''
        estimacionEnerConsumidaTotalACS = ''
        potNominalPostMejoraTotalACS = ''
        estimacionEnerConsumidaPostMejoraTotalACS = ''
        enerAhorradoTotalACS = ''
        a0 = Paragraph(_('TOTALES'), self.titulo4)
        a1 = ''
        a2 = Paragraph('-', self.tabla1Contenidos)
        a3 = ''
        a4 = Paragraph('-', self.tabla1Contenidos)
        a5 = ''
        a6 = Paragraph('-', self.tabla1Contenidos)
        a7 = ''
        a8 = Paragraph('-', self.tabla1Contenidos)
        a9 = Paragraph('-', self.tabla1Contenidos)
        data = [
         [
          a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]]
        t = Table(data, [3.12 * cm, 1.98 * cm, 1.49 * cm, 1.51 * cm, 1.49 * cm, 1.98 * cm, 1.51 * cm, 1.98 * cm, 1.75 * cm, 1.49 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 1), self.naranja),
         (
          'BACKGROUND', (2, 0), (2, 1), self.naranja),
         (
          'BACKGROUND', (4, 0), (4, 1), self.naranja),
         (
          'BACKGROUND', (6, 0), (6, 1), self.moradoFuerte),
         (
          'BACKGROUND', (8, 0), (8, 1), self.moradoFuerte),
         (
          'BACKGROUND', (9, 0), (9, 1), self.moradoFuerte),
         (
          'BACKGROUND', (1, 0), (1, 0), colors.grey),
         (
          'BACKGROUND', (3, 0), (3, 0), colors.grey),
         (
          'BACKGROUND', (5, 0), (5, 0), colors.grey),
         (
          'BACKGROUND', (7, 0), (7, 0), colors.grey),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def primeraFilaTorresRefVentilacion(self):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo4)
        a12 = Paragraph(_('Tipo'), self.titulo4)
        a13 = Paragraph(_('Servicio asociado'), self.titulo4)
        a14 = Paragraph(_('Consumo de energía [kWh/año]'), self.titulo4)
        a15 = Paragraph(_('Tipo post mejora'), self.titulo4)
        a16 = Paragraph(_('Servicio asociado post mejora'), self.titulo4)
        a17 = Paragraph(_('Consumo de energía post mejora'), self.titulo4)
        data = [
         [
          a11, a12, a13, a14, a15, a16, a17]]
        t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], [
         1.75 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (3, 0), self.rosa),
         (
          'BACKGROUND', (4, 0), (-1, 0), self.morado),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def tablaComparacionEquiposGranTerciario(self, equiposEdificioObjeto=[], equiposEdificioMejorado=[], tipoEquipo=''):
        Story = []
        equiposConjuntoMMYaMetidosEnInforme = []
        for i in equiposEdificioObjeto:
            nombre = i[0]
            if tipoEquipo == 'Ventiladores':
                tipo = listadoOpcionesVentiladores[i[3]][1]
            elif tipoEquipo == 'Bombas':
                tipo = listadoOpcionesBombas[i[3]][1]
            else:
                tipo = listadoOpcionesTorreDeRefrigeracion[i[3]][1]
            consumo = str(round(float(i[2]), 1))
            if tipoEquipo == 'Ventiladores':
                servicio = listadoOpcionesServicioVentiladores[i[12]][1]
            elif tipoEquipo == 'Bombas':
                servicio = listadoOpcionesServicioBombas[i[12]][1]
            else:
                servicio = '-'
            a0 = Paragraph('%s' % nombre, self.tabla2Contenidos)
            a1 = Paragraph('%s' % tipo, self.tabla2Contenidos)
            a2 = Paragraph('%s' % servicio, self.tabla2Contenidos)
            a3 = Paragraph('%s' % consumo, self.tabla2Contenidos)
            equipoEncontrado = False
            for iEquipoMM in equiposEdificioMejorado:
                nombreEquipoMM = iEquipoMM[0]
                if tipoEquipo == 'Ventiladores':
                    tipoMM = listadoOpcionesVentiladores[iEquipoMM[3]][1]
                elif tipoEquipo == 'Bombas':
                    tipoMM = listadoOpcionesBombas[iEquipoMM[3]][1]
                else:
                    tipoMM = listadoOpcionesTorreDeRefrigeracion[iEquipoMM[3]][1]
                consumoEquipoMM = str(round(float(iEquipoMM[2]), 1))
                if tipoEquipo == 'Ventiladores':
                    servicioMM = listadoOpcionesServicioVentiladores[iEquipoMM[12]][1]
                elif tipoEquipo == 'Bombas':
                    servicioMM = listadoOpcionesServicioBombas[iEquipoMM[12]][1]
                else:
                    servicioMM = '-'
                if nombre == nombreEquipoMM:
                    a4 = Paragraph('%s' % tipoMM, self.tabla2Contenidos)
                    a5 = Paragraph('%s' % servicioMM, self.tabla2Contenidos)
                    a6 = Paragraph('%s' % consumoEquipoMM, self.tabla2Contenidos)
                    equipoEncontrado = True
                    equiposConjuntoMMYaMetidosEnInforme.append(iEquipoMM)
                    break

            if equipoEncontrado == False:
                a4 = Paragraph('-', self.tabla2Contenidos)
                a5 = Paragraph('-', self.tabla2Contenidos)
                a6 = Paragraph('-', self.tabla2Contenidos)
            data = [[a0, a1, a2, a3, a4, a5, a6]]
            t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)

        for iEquipoMM in equiposEdificioMejorado:
            nombreEquipoMM = iEquipoMM[0]
            if tipoEquipo == 'Ventiladores':
                tipoMM = listadoOpcionesVentiladores[iEquipoMM[3]][1]
            elif tipoEquipo == 'Bombas':
                tipoMM = listadoOpcionesBombas[iEquipoMM[3]][1]
            else:
                tipoMM = listadoOpcionesTorreDeRefrigeracion[iEquipoMM[3]][1]
            consumoEquipoMM = str(round(float(iEquipoMM[2]), 1))
            if tipoEquipo == 'Ventiladores':
                servicioMM = listadoOpcionesServicioVentiladores[iEquipoMM[12]][1]
            elif tipoEquipo == 'Bombas':
                servicioMM = listadoOpcionesServicioBombas[iEquipoMM[12]][1]
            else:
                servicioMM = '-'
            if iEquipoMM not in equiposConjuntoMMYaMetidosEnInforme:
                a0 = Paragraph('%s' % nombreEquipoMM, self.tabla2Contenidos)
                a1 = Paragraph('-', self.tabla2Contenidos)
                a2 = Paragraph('-', self.tabla2Contenidos)
                a3 = Paragraph('-', self.tabla2Contenidos)
                a4 = Paragraph('%s' % tipoMM, self.tabla2ContenidosBis)
                a5 = Paragraph('%s' % servicioMM, self.tabla2Contenidos)
                a6 = Paragraph('%s' % consumoEquipoMM, self.tabla2Contenidos)
                data = [
                 [
                  a0, a1, a2, a3, a4, a5, 
                  a6]]
                t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
                t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
                 (
                  'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                 (
                  'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                 (
                  'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                Story.append(t)

        if len(equiposEdificioObjeto) == 0 and len(equiposEdificioMejorado) == 0:
            data = [
             [
              '', '', '', '', '', '', '']]
            t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (5, 0), (-1, 1), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)
        return Story

    def torresRef(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Torres de refrigeración (sólo edificios terciarios)'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primeraFilaTorresRefVentilacion()
        Story += self.tablaComparacionEquiposGranTerciario(equiposEdificioObjeto=self.objEdificio.datosIniciales.sistemasTorresRefrigeracion, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.sistemasTorresRefrigeracion, tipoEquipo='TorresRefrigeracion')
        energiaAhorrada = self.objEdificio.datosResultados.enFinalTorresRef - conjuntoMM.datosNuevoEdificio.datosResultados.enFinalTorresRef
        Story.append(Spacer(0, 0.15 * cm))
        return Story

    def ventilacionBombeo(self, conjuntoMM):
        Story = []
        t = Paragraph(_('Ventilación y bombeo (sólo edificios terciarios)'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.primeraFilaTorresRefVentilacion()
        Story += self.tablaComparacionEquiposGranTerciario(equiposEdificioObjeto=self.objEdificio.datosIniciales.sistemasVentiladores, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.sistemasVentiladores, tipoEquipo='Ventiladores')
        Story += self.tablaComparacionEquiposGranTerciario(equiposEdificioObjeto=self.objEdificio.datosIniciales.sistemasBombas, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.sistemasBombas, tipoEquipo='Bombas')
        energiaConsumidaEdificioObjeto = self.objEdificio.datosResultados.enFinalVentiladores + self.objEdificio.datosResultados.enFinalBombas
        energiaConsumidaConjuntoMM = conjuntoMM.datosNuevoEdificio.datosResultados.enFinalVentiladores + conjuntoMM.datosNuevoEdificio.datosResultados.enFinalBombas
        energiaAhorrada = energiaConsumidaEdificioObjeto - energiaConsumidaConjuntoMM
        Story.append(Spacer(0, 0.15 * cm))
        return Story

    def energiaAnualAhorrada(self, energiaAhorrada):
        Story = []
        a11 = Paragraph(_('Energía anual ahorrada'), self.titulo4)
        a12 = Paragraph('%0.1f' % energiaAhorrada, self.tabla2Contenidos)
        a21 = Paragraph(_('[kWh/m² año]'), self.titulo4)
        a22 = ''
        data = [
         [
          a11, a12],
         [
          a21, a22]]
        t = Table(data, [5.81 * cm, 2.11 * cm], [
         0.5 * cm, 0.5 * cm], None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 1), self.morado),
         (
          'BACKGROUND', (1, 0), (1, 0), self.gris),
         (
          'SPAN', (1, 0), (1, 1)),
         (
          'BOX', (0, 0), (1, -1), 0.5, colors.black),
         (
          'LINEBEFORE', (1, 0), (1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def tablaComparacionEquiposIluminacion(self, equiposEdificioObjeto=[], equiposEdificioMejorado=[]):
        Story = []
        equiposConjuntoMMYaMetidosEnInforme = []
        for i in equiposEdificioObjeto:
            nombre = i[0]
            zona = i[-1]
            potencia = i[2]
            superficie = i[5]
            try:
                potenciaM2 = round(float(potencia) / float(superficie), 2)
            except:
                logging.info('Excepcion en: %s' % __name__)
                potenciaM2 = '-'

            veei = i[3]
            iluminancia = i[9][1]
            a0 = Paragraph('%s' % zona, self.tabla2Contenidos)
            a1 = Paragraph('%s' % potenciaM2, self.tabla2Contenidos)
            a2 = Paragraph('%0.1f' % float(veei), self.tabla2Contenidos)
            a3 = Paragraph('%s' % iluminancia, self.tabla2Contenidos)
            equipoEncontrado = False
            for iEquipoMM in equiposEdificioMejorado:
                nombreMM = iEquipoMM[0]
                if nombre == nombreMM:
                    potenciaMM = iEquipoMM[2]
                    superficieMM = iEquipoMM[5]
                    try:
                        potenciaM2MM = round(float(potenciaMM) / float(superficieMM), 2)
                    except:
                        logging.info('Excepcion en: %s' % __name__)
                        potenciaM2MM = '-'

                    veeiMM = iEquipoMM[3]
                    iluminanciaMM = iEquipoMM[9][1]
                    a4 = Paragraph('%s' % potenciaM2MM, self.tabla2Contenidos)
                    a5 = Paragraph('%0.1f' % float(veeiMM), self.tabla2Contenidos)
                    a6 = Paragraph('%s' % iluminanciaMM, self.tabla2Contenidos)
                    equipoEncontrado = True
                    equiposConjuntoMMYaMetidosEnInforme.append(iEquipoMM)
                    break

            if equipoEncontrado == False:
                a4 = Paragraph('-', self.tabla2Contenidos)
                a5 = Paragraph('-', self.tabla2Contenidos)
                a6 = Paragraph('-', self.tabla2Contenidos)
            data = [[a0, a1, a2, a3, a4, a5, a6]]
            t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 0), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)

        for iEquipoMM in equiposEdificioMejorado:
            if iEquipoMM not in equiposConjuntoMMYaMetidosEnInforme:
                nombreMM = iEquipoMM[0]
                potenciaMM = iEquipoMM[2]
                superficieMM = iEquipoMM[5]
                try:
                    potenciaM2MM = round(float(potenciaMM) / float(superficieMM), 2)
                except:
                    logging.info('Excepcion en: %s' % __name__)
                    potenciaM2MM = '-'

                veeiMM = iEquipoMM[3]
                iluminanciaMM = iEquipoMM[9][1]
                a0 = Paragraph('%s' % zona, self.tabla2Contenidos)
                a1 = Paragraph('-', self.tabla2Contenidos)
                a2 = Paragraph('-', self.tabla2Contenidos)
                a3 = Paragraph('-', self.tabla2Contenidos)
                a4 = Paragraph('%s' % potenciaM2MM, self.tabla2Contenidos)
                a5 = Paragraph('%0.1f' % float(veeiMM), self.tabla2Contenidos)
                a6 = Paragraph('%s' % iluminanciaMM, self.tabla2Contenidos)
                data = [
                 [
                  a0, a1, a2, a3, a4, a5, 
                  a6]]
                t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
                t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 0), self.gris),
                 (
                  'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                 (
                  'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                 (
                  'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                Story.append(t)

        if len(equiposEdificioObjeto) == 0 and len(equiposEdificioMejorado) == 0:
            data = [
             [
              '', '', '', '', '', '', '']]
            t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (4, 0), (-1, 0), self.gris),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)
        return Story

    def instalacionIluminacion(self, conjuntoMM):
        Story = []
        t = Paragraph(_('INSTALACIÓN DE ILUMINACIÓN (sólo edificios terciarios)'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        a11 = Paragraph(_('Espacio'), self.titulo4)
        a12 = Paragraph(_('Potencia instalada [W/m²]'), self.titulo4)
        a13 = Paragraph(_('VEEI [W/m²100lux]'), self.titulo4)
        a14 = Paragraph(_('Iluminancia media [lux]'), self.titulo4)
        a15 = Paragraph(_('Potencia instalada post mejora [W/m²]'), self.titulo4)
        a16 = Paragraph(_('VEEI post mejora [W/m²100lux]'), self.titulo4)
        a17 = Paragraph(_('Iluminancia media post mejora [lux]'), self.titulo4)
        data = [
         [
          a11, a12, a13, a14, a15, a16, a17]]
        t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], [
         1.75 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (3, 0), self.rosa),
         (
          'BACKGROUND', (4, 0), (-1, 0), self.morado),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        Story += self.tablaComparacionEquiposIluminacion(equiposEdificioObjeto=self.objEdificio.datosIniciales.sistemasIluminacion, equiposEdificioMejorado=conjuntoMM.datosNuevoEdificio.datosIniciales.sistemasIluminacion)
        potenciaM2Total = round(sum(float(i[2]) for i in self.objEdificio.datosIniciales.sistemasIluminacion) / self.objEdificio.datosIniciales.area, 2)
        potenciaM2TotalMM = round(sum(float(i[2]) for i in conjuntoMM.datosNuevoEdificio.datosIniciales.sistemasIluminacion) / conjuntoMM.datosNuevoEdificio.datosIniciales.area, 2)
        a21 = Paragraph(_('TOTALES'), self.titulo4)
        a22 = Paragraph('%s' % potenciaM2Total, self.tabla2Contenidos)
        a23 = Paragraph('-', self.tabla2Contenidos)
        a24 = Paragraph('-', self.tabla2Contenidos)
        a25 = Paragraph('%s' % potenciaM2TotalMM, self.tabla2Contenidos)
        a26 = Paragraph('-', self.tabla2Contenidos)
        a27 = Paragraph('-', self.tabla2Contenidos)
        data = [
         [
          a21, a22, a23, a24, a25, a26, a27]]
        t = Table(data, [3.7 * cm, 2.1 * cm, 2.1 * cm, 2.1 * cm, 2.66 * cm, 2.66 * cm, 2.66 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (3, 0), self.naranja),
         (
          'BACKGROUND', (4, 0), (-1, 0), self.moradoFuerte),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        energiaAhorrada = self.objEdificio.datosResultados.enFinalIlum - conjuntoMM.datosNuevoEdificio.datosResultados.enFinalIlum
        Story.append(Spacer(0, 0.15 * cm))
        return Story

    def condicionesFuncionamientoOcupacion(self, conjuntoMM):
        Story = []
        t = Paragraph(_('CONDICIONES DE FUNCIONAMIENTO Y OCUPACIÓN (sólo edificios terciarios)'), self.tabla1ContenidosN)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(6 * cm))
        a11 = Paragraph(_('Espacio'), self.titulo4)
        a12 = Paragraph(_('Superficie [m²]'), self.titulo4)
        a13 = Paragraph(_('Perfil de uso'), self.titulo4)
        data = [[a11, a12, a13]]
        superficieTotalZonas = 0
        for zona in conjuntoMM.datosNuevoEdificio.subgrupos:
            a21 = Paragraph('%s' % zona.nombre, self.tabla2Contenidos)
            a22 = Paragraph('%s' % zona.superficie, self.tabla2Contenidos)
            a23 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosIniciales.tipoEdificio, self.tabla2Contenidos)
            superficieTotalZonas += float(zona.superficie)
            data.append([a21, a22, a23])

        superficieEdificioObjeto = round(conjuntoMM.datosNuevoEdificio.datosIniciales.area - superficieTotalZonas, 2)
        if superficieEdificioObjeto > 0.1:
            superficieEdificioObjeto = round(conjuntoMM.datosNuevoEdificio.datosIniciales.area - superficieTotalZonas, 2)
            a21 = Paragraph('Edificio Objeto', self.tabla2Contenidos)
            a22 = Paragraph('%s' % superficieEdificioObjeto, self.tabla2Contenidos)
            a23 = Paragraph('%s' % conjuntoMM.datosNuevoEdificio.datosIniciales.tipoEdificio, self.tabla2Contenidos)
            data.append([a21, a22, a23])
        t = Table(data, [6.09 * cm, 6.24 * cm, 5.67 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def energiasRenovables(self, conjuntoMM):
        Story = []
        if len(self.objEdificio.datosIniciales.contribuciones.listado) > 0 or len(conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado) > 0:
            t = Paragraph(_('ENERGÍAS RENOVABLES'), self.tabla1ContenidosN)
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            Story += self.termica(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
            Story.append(CondPageBreak(6 * cm))
            Story += self.electrica(conjuntoMM)
            Story.append(Spacer(0, 0.5 * cm))
        return Story

    def termica(self, conjuntoMM):
        Story = []
        if self.objEdificio.datosIniciales.contribuciones.porcACSTotal > 0 or self.objEdificio.datosIniciales.contribuciones.porcCalTotal > 0 or self.objEdificio.datosIniciales.contribuciones.porcRefTotal > 0 or conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcACSTotal > 0 or conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcCalTotal > 0 or conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcRefTotal > 0:
            t = Paragraph(_('Térmica'), self.tabla1ContenidosN)
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            Story += self.primeraTablaTermica()
            Story.append(Spacer(0, 0.5 * cm))
            t = Paragraph(_('Post mejora'), self.tabla1ContenidosN)
            Story.append(t)
            Story.append(CondPageBreak(6 * cm))
            Story += self.segundaTablaTermica(conjuntoMM)
        return Story

    def primeraTablaTermica(self):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo4)
        a13 = Paragraph(_('Consumo de Energía Final, cubierto en función del servicio asociado [%]'), self.titulo4)
        a14 = ''
        a15 = ''
        a12 = Paragraph(_('Demanda de ACS cubierta [%]'), self.titulo4)
        a21 = ''
        a22 = ''
        a23 = Paragraph(_('Calefacción'), self.titulo4)
        a24 = Paragraph(_('Refrigeración'), self.titulo4)
        a25 = Paragraph(_('ACS'), self.titulo4)
        data = [
         [
          a11, a13, a14, a15, a12],
         [
          a21, a23, a24, a25, a22]]
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
         (
          'ALIGN', (0, 0), (-1, -1), 'CENTER'),
         (
          'SPAN', (0, 0), (0, -1)),
         (
          'SPAN', (1, 0), (-2, 0)),
         (
          'BACKGROUND', (0, 0), (-1, 1), self.rosa),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black)]))
        Story.append(t)
        data = []
        for i in self.objEdificio.datosIniciales.contribuciones.listado:
            if i.porcCal != '' and i.porcCal > 0.0 or i.porcRef != '' and i.porcRef > 0.0 or i.porcACS != '' and i.porcACS > 0.0:
                a11 = Paragraph('%s' % i.nombre, self.tabla2Contenidos)
                a12 = Paragraph('-', self.tabla2Contenidos)
                if i.porcCal != '' and i.porcCal > 0.0:
                    a13 = Paragraph('%s' % i.porcCal, self.tabla2Contenidos)
                else:
                    a13 = Paragraph('-', self.tabla2Contenidos)
                if i.porcRef != '' and i.porcRef > 0.0:
                    a14 = Paragraph('%s' % i.porcRef, self.tabla2Contenidos)
                else:
                    a14 = Paragraph('-', self.tabla2Contenidos)
                if i.porcACS != '' and i.porcACS > 0.0:
                    a15 = Paragraph('%s' % i.porcACS, self.tabla2Contenidos)
                else:
                    a15 = Paragraph('-', self.tabla2Contenidos)
                data.append([a11, a13, a14, a15, a12])

        if len(data) == 0:
            data.append([Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos)])
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        if len(self.objEdificio.datosIniciales.contribuciones.listado) > 0:
            totalCal = self.objEdificio.datosIniciales.contribuciones.porcCalTotal
            totalRef = self.objEdificio.datosIniciales.contribuciones.porcRefTotal
            totalACS = self.objEdificio.datosIniciales.contribuciones.porcACSTotal
        else:
            totalCal = '-'
            totalRef = '-'
            totalACS = '-'
        a11 = Paragraph(_('TOTALES'), self.titulo4)
        a12 = Paragraph('-', self.tabla2Contenidos)
        if totalCal != '' and totalCal > 0.0:
            a13 = Paragraph('%s' % totalCal, self.tabla2Contenidos)
        else:
            a13 = Paragraph('-', self.tabla1ContenidosC)
        if totalRef != '' and totalRef > 0.0:
            a14 = Paragraph('%s' % totalRef, self.tabla2Contenidos)
        else:
            a14 = Paragraph('-', self.tabla1ContenidosC)
        if totalACS != '' and totalACS > 0.0:
            a15 = Paragraph('%s' % totalACS, self.tabla2Contenidos)
        else:
            a15 = Paragraph('-', self.tabla1ContenidosC)
        data = [[a11, a13, a14, a15, a12]]
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), self.naranja),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
         (
          'ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        Story.append(t)
        return Story

    def segundaTablaTermica(self, conjuntoMM):
        Story = []
        a11 = Paragraph(_('Nombre'), self.titulo4)
        a12 = Paragraph(_('Demanda de ACS cubierta [%]'), self.titulo4)
        a13 = Paragraph(_('Consumo de Energía Final, cubierto en función del servicio asociado [%]'), self.titulo4)
        a14 = ''
        a15 = ''
        a21 = ''
        a22 = ''
        a23 = Paragraph(_('Calefacción'), self.titulo4)
        a24 = Paragraph(_('Refrigeración'), self.titulo4)
        a25 = Paragraph(_('ACS'), self.titulo4)
        data = [
         [
          a11, a13, a14, a15, a12],
         [
          a21, a23, a24, a25, a22]]
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
         (
          'ALIGN', (0, 0), (-1, -1), 'CENTER'),
         (
          'SPAN', (0, 0), (0, -1)),
         (
          'SPAN', (1, 0), (-2, 0)),
         (
          'BACKGROUND', (0, 0), (-1, 1), self.morado),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black)]))
        Story.append(t)
        data = []
        for i in conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado:
            if i.porcCal != '' and i.porcCal > 0.0 or i.porcRef != '' and i.porcRef > 0.0 or i.porcACS != '' and i.porcACS > 0.0:
                a11 = Paragraph('%s' % i.nombre, self.tabla2Contenidos)
                a12 = Paragraph('-', self.tabla2Contenidos)
                if i.porcCal != '' and i.porcCal > 0.0:
                    a13 = Paragraph('%s' % i.porcCal, self.tabla2Contenidos)
                else:
                    a13 = Paragraph('-', self.tabla2Contenidos)
                if i.porcRef != '' and i.porcRef > 0.0:
                    a14 = Paragraph('%s' % i.porcRef, self.tabla2Contenidos)
                else:
                    a14 = Paragraph('-', self.tabla2Contenidos)
                if i.porcACS != '' and i.porcACS > 0.0:
                    a15 = Paragraph('%s' % i.porcACS, self.tabla2Contenidos)
                else:
                    a15 = Paragraph('-', self.tabla2Contenidos)
                data.append([a11, a13, a14, a15, a12])

        if len(data) == 0:
            data.append([Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos),
             Paragraph('-', self.tabla2Contenidos)])
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        if len(conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado) > 0:
            totalCal = conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcCalTotal
            totalRef = conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcRefTotal
            totalACS = conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.porcACSTotal
        else:
            totalCal = '-'
            totalRef = '-'
            totalACS = '-'
        a11 = Paragraph(_('TOTALES'), self.titulo4)
        a12 = Paragraph('-', self.tabla2Contenidos)
        if totalCal != '' and totalCal > 0.0:
            a13 = Paragraph('%s' % totalCal, self.tabla2Contenidos)
        else:
            a13 = Paragraph('-', self.tabla1ContenidosC)
        if totalRef != '' and totalRef > 0.0:
            a14 = Paragraph('%s' % totalRef, self.tabla2Contenidos)
        else:
            a14 = Paragraph('-', self.tabla1ContenidosC)
        if totalACS != '' and totalACS > 0.0:
            a15 = Paragraph('%s' % totalACS, self.tabla2Contenidos)
        else:
            a15 = Paragraph('-', self.tabla1ContenidosC)
        data = [[a11, a13, a14, a15, a12]]
        t = Table(data, [6.28 * cm, 2.61 * cm, 2.54 * cm, 2.65 * cm, 3.92 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), self.moradoFuerte),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        Story.append(t)
        return Story

    def electrica(self, conjuntoMM):
        Story = []
        if self.objEdificio.datosIniciales.contribuciones.electricidadGenTotal > 0 or conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.electricidadGenTotal > 0:
            t = Paragraph(_('Eléctrica'), self.tabla1ContenidosN)
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            a11 = Paragraph(_('Nombre'), self.titulo4)
            a12 = Paragraph(_('Energía eléctrica generada y autoconsumida [kWh/año]'), self.titulo4)
            a13 = Paragraph(_('Energía eléctrica generada y autoconsumida post mejora [kWh/año]'), self.titulo4)
            data = [
             [
              a11, a12, a13]]
            t = Table(data, [7 * cm, 5.5 * cm, 5.5 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (2, 0), (2, 0), self.morado),
             (
              'BACKGROUND', (0, 0), (1, 0), self.rosa),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)
            equiposConjuntoMMYaMetidosEnInforme = []
            for i in self.objEdificio.datosIniciales.contribuciones.listado:
                if i.electricidadGen != '' and i.electricidadGen > 0.0:
                    a11 = Paragraph('%s' % i.nombre, self.tabla2Contenidos)
                    a12 = Paragraph('%s' % i.electricidadGen, self.tabla2Contenidos)
                    equipoEncontrado = False
                    for iEquipoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado:
                        if i.nombre == iEquipoMM.nombre:
                            a13 = Paragraph('%s' % iEquipoMM.electricidadGen, self.tabla2Contenidos)
                            equipoEncontrado = True
                            equiposConjuntoMMYaMetidosEnInforme.append(iEquipoMM)
                            break

                    if equipoEncontrado == False:
                        a13 = Paragraph('-', self.tabla2Contenidos)
                    data = [[a11, a12, a13]]
                    t = Table(data, [7 * cm, 5.5 * cm, 5.5 * cm], None, None, 1, 1, 1)
                    t.setStyle(TableStyle([('BACKGROUND', (2, 0), (2, 0), self.gris),
                     (
                      'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                     (
                      'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                     (
                      'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                    Story.append(t)

            for iEquipoMM in conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado:
                if iEquipoMM not in equiposConjuntoMMYaMetidosEnInforme:
                    if iEquipoMM.electricidadGen != '' and iEquipoMM.electricidadGen > 0.0:
                        a11 = Paragraph('%s' % iEquipoMM.nombre, self.tabla2Contenidos)
                        a12 = Paragraph('-', self.tabla2Contenidos)
                        a13 = Paragraph('%s' % iEquipoMM.electricidadGen, self.tabla2Contenidos)
                        data = [[a11, a12, a13]]
                        t = Table(data, [7 * cm, 5.5 * cm, 5.5 * cm], None, None, 1, 1, 1)
                        t.setStyle(TableStyle([('BACKGROUND', (2, 0), (2, 0), self.gris),
                         (
                          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
                         (
                          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
                         (
                          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
                        Story.append(t)

            if len(self.objEdificio.datosIniciales.contribuciones.listado) > 0:
                totalDemandaCubiertoEdificioObjeto = self.objEdificio.datosIniciales.contribuciones.electricidadGenTotal
            else:
                totalDemandaCubiertoEdificioObjeto = '-'
            if len(conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.listado) > 0.0:
                totalDemandaCubiertoConjuntoMM = conjuntoMM.datosNuevoEdificio.datosIniciales.contribuciones.electricidadGenTotal
            else:
                totalDemandaCubiertoConjuntoMM = '-'
            a11 = Paragraph(_('TOTALES'), self.titulo4)
            a12 = Paragraph('%s' % totalDemandaCubiertoEdificioObjeto, self.tabla2Contenidos)
            a13 = Paragraph('%s' % totalDemandaCubiertoConjuntoMM, self.tabla2Contenidos)
            data = [
             [
              a11, a12, a13]]
            t = Table(data, [7 * cm, 5.5 * cm, 5.5 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), self.moradoFuerte),
             (
              'BACKGROUND', (0, 0), (1, 0), self.naranja),
             (
              'GRID', (0, 0), (-1, -1), 0.5, colors.black),
             (
              'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
             (
              'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
            Story.append(t)
        return Story

    def myFirstPage(self, canvas, doc):
        """
        Metodo: myFirstPage

        ARGUMENTOS:
                canvas:
                doc:
        """
        canvas.saveState()
        self.drawPageFrame(canvas)
        self.pageNumber += 1
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        """
        Metodo: myLaterPages

        ARGUMENTOS:
                canvas:
                doc)::
        """
        canvas.saveState()
        self.drawPageFrame(canvas)
        self.pageNumber += 1
        canvas.setFont('arial', 7)
        canvas.restoreState()

    def drawPageFrame(self, canv):
        """
        Metodo: drawPageFrame

        ARGUMENTOS:
                canv:
        """
        encabezado1 = ParagraphStyle('normal', fontName='arialbd', fontSize=16, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        encabezado2 = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=12, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        encabezado3 = ParagraphStyle('normal', fontName='arial', fontSize=8, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        encabezadoRefCatastral = ParagraphStyle('normal', fontName='arial', fontSize=7, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        imagenEncabezadoFile = Directorio + '/Imagenes/logoEncabezado.png'
        imagenEncabezado = trataImagenes.trataImagen(imagenEncabezadoFile)
        imagen = Image(StringIO(base64.b64decode(imagenEncabezado)), width=1.5 * cm, height=2.25 * cm)
        imagen.hAlign = 'CENTER'
        a11 = imagen
        a12 = Paragraph(_('IDENTIFICACIÓN'), encabezado1)
        a121 = ''
        listadoRefCat = self.datosAdmin[15]
        a13 = Paragraph(_('Ref. Catastral'), encabezado3)
        a14 = Paragraph('%s' % listadoRefCat[0], encabezadoRefCatastral)
        fecha = self.datosConfiguracionInforme[5]
        if fecha != ['', '', '']:
            dia = fecha[0]
            mes = fecha[1]
            anno = fecha[2]
        else:
            fecha = datetime.date.today()
            dia = fecha.day
            mes = fecha.month
            anno = fecha.year
        a15 = Paragraph(_('Versión informe asociado'), encabezado3)
        a16 = Paragraph('%s/%s/%s' % (dia, mes, anno), encabezado3)
        a21 = ''
        a221 = Paragraph(_('Id. Mejora'), encabezado2)
        a222 = Paragraph('', encabezado3)
        a23 = Paragraph(_('Programa y versión'), encabezado3)
        a24 = Paragraph('%s' % programaVersion, encabezado3)
        a25 = Paragraph(_('Fecha'), encabezado3)
        a26 = Paragraph('%i/%i/%i' % (self.fechaImpresionCertificado.day,
         self.fechaImpresionCertificado.month,
         self.fechaImpresionCertificado.year), encabezado3)
        data = [
         [
          a11, a12, a121, a13, a14, a15, a16],
         [
          a21, a221, a222, a23, a24, a25, a26]]
        t = Table(data, [1.76 * cm, 1.93 * cm, 3.08 * cm, 1.66 * cm, 3.5 * cm, 1.78 * cm, 1.7 * cm], [1 * cm, 1.25 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND', (1, 0), (2, 0), self.grisEncabezado),
         (
          'BACKGROUND', (3, 0), (3, -1), self.grisEncabezado),
         (
          'BACKGROUND', (5, 0), (5, -1), self.grisEncabezado),
         (
          'BACKGROUND', (1, 1), (1, 1), self.grisEncabezado),
         (
          'BOX', (0, 0), (0, 2), 0.5, colors.black),
         (
          'GRID', (0, 0), (-1, -1), 0.5, colors.black),
         (
          'TOPPADDING', (0, 0), (-1, -1), 0.0 * cm),
         (
          'SPAN', (0, 0), (0, -1)),
         (
          'SPAN', (1, 0), (2, 0)),
         (
          'VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        w, h = t.wrapOn(canv, 2 * cm, 5 * cm)
        t.drawOn(canv, 3 * cm, top_margin - 0.7 * inch)
        return


class BorradoInformeMM(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return _('No se ha podido generar el informe de medidas de mejora. Si hay algún documento abierto con el mismo nombre debe cerrarlo.')


if __name__ == '__main__':
    informe = GeneraInforme()
    informe.generaInforme('C:\\Users\\amaia\\Desktop\\CE3X\\tempMM.cex')