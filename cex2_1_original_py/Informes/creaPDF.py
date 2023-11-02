# Embedded file name: Informes\creaPDF.pyc
"""
Modulo: creaPDF.py

"""
from Calculos.listados import Localizacion, programaVersion
from Calculos.listadosWeb import listadoOpcionesVentiladores, listadoOpcionesServicioVentiladores, listadoOpcionesTorreDeRefrigeracion, listadoOpcionesBombas, listadoOpcionesServicioBombas, getTraduccion, listadoCombustibles, listadoInstalaciones, listadoInstalacionesClimatizacion, listadoInstalacionesElectrico, getElementoEnListado, listadoCerramientos
from StringIO import StringIO
from reportlab.graphics.shapes import Line, Drawing
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
import DatosGenerales.trataImagenes as trataImagenes
import base64
import copy
import datetime
import directorios
import logging
import math
import operator
import os
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

def cuentaLineas(comentarios):
    """Cuenta las l\xedneas presentes en el comentario
    """
    com = comentarios.split('\n')
    nLineas = len(com)
    for c in com:
        if len(c) > 90:
            nLineas += 1

    return nLineas


def divideComentariosEnVariasPaginas(comentarios):
    nLineas = cuentaLineas(comentarios)
    com = comentarios.split('\n')
    paginas = []
    nLPDF = 0
    nLComentario = 0
    pagina = ''
    while nLComentario < nLineas & nLPDF < 58:
        pagina += com[nLComentario] + '\n'
        if len(com[nLComentario]) > 90:
            nLPDF = +1
        nLPDF = +1
        nLComentario += 1

    paginas.append(pagina)
    lineasRestantes = nLineas - 58
    if lineasRestantes <= 0:
        return paginas
    paginasRestantes = lineasRestantes // 65 + 1
    for p in range(paginasRestantes - 1):
        nLPDF = 0
        pagina = ''
        while nLPDF < 65:
            pagina += com[nLComentario] + '\n'
            if len(com[nLComentario]) > 90:
                nLPDF = +1
            nLPDF = +1
            nLComentario += 1

        paginas.append(pagina)

    nLPDF = 0
    pagina = ''
    while nLPDF < lineasRestantes % 65:
        pagina += com[nLComentario] + '\n'
        if len(com[nLComentario]) > 90:
            nLPDF = +1
        nLPDF += 1
        nLComentario += 1

    paginas.append(pagina)
    return paginas


class Etiqueta(Flowable):
    """
    Clase: Etiqueta del modulo creaPDF.py
    
    
    """

    def __init__(self, categoria, emisiones, Limites):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                categoria:
                emisiones:
                Limites :
        """
        Flowable.__init__(self)
        self.categoria = categoria
        self.emisiones = emisiones
        self.limites = Limites
        self.punto = 15.0
        self.scaleX = 1.0
        self.scaleY = 1.0
        self.translateX = 0.0
        self.translateY = 0.0

    def draw(self):
        """
        Metodo: draw
        
        
        """
        canv = self.canv
        canv.translate(self.translateX, self.translateY)
        canv.scale(self.scaleX, self.scaleY)
        u = cm
        canv.setLineWidth(1)
        canv.setStrokeColor(black)
        canv.setFillColorCMYK(1, 0, 1, 0)
        cmyk = [(1, 0, 1, 0),
         (0.7, 0, 1, 0),
         (0.3, 0, 1, 0),
         (0, 0, 1, 0),
         (0, 0.3, 1, 0),
         (0, 0.7, 1, 0),
         (0, 1, 1, 0)]
        letras = ['A',
         'B',
         'C',
         'D',
         'E',
         'F',
         'G']
        limites_str = ['< ' + str(round(self.limites[0], 1)),
         str(round(self.limites[0], 1)) + '-' + str(round(self.limites[1], 1)),
         str(round(self.limites[1], 1)) + '-' + str(round(self.limites[2], 1)),
         str(round(self.limites[2], 1)) + '-' + str(round(self.limites[3], 1)),
         str(round(self.limites[3], 1)) + '-' + str(round(self.limites[4], 1)),
         str(round(self.limites[4], 1)) + '-' + str(round(self.limites[5], 1)),
         u'\u2265 ' + str(round(self.limites[5], 1))]
        for contador in range(0, 7):
            c, m, y, k = cmyk[contador]
            canv.setFillColorCMYK(c, m, y, k)
            canv.setStrokeColorCMYK(c, m, y, k)
            p = canv.beginPath()
            p.moveTo(0, 0 - contador * u * 0.45)
            p.lineTo(u + contador * u * 0.3, 0 - contador * u * 0.45)
            p.lineTo(1.225 * u + contador * u * 0.3, 0.18 * u - contador * u * 0.45)
            p.lineTo(u + contador * u * 0.3, 0.36 * u - contador * u * 0.45)
            p.lineTo(0, 0.36 * u - contador * u * 0.45)
            p.lineTo(0, 0 - contador * u * 0.45)
            canv.drawPath(p, stroke=1, fill=1)
            if self.categoria == letras[contador]:
                canv.setFillColorCMYK(c, m, y, k)
                canv.setStrokeColorCMYK(c, m, y, k)
                p.moveTo(1.5 * u + self.punto * u * 0.3 + 2.7 * u, 0 - contador * u * 0.45)
                p.lineTo(1.5 * u + self.punto * u * 0.3 + 1 * u, 0 - contador * u * 0.45)
                p.lineTo(1.5 * u + self.punto * u * 0.3 + 0.7 * u, 0.18 * u - contador * u * 0.45)
                p.lineTo(1.5 * u + self.punto * u * 0.3 + 1 * u, 0.36 * u - contador * u * 0.45)
                p.lineTo(1.5 * u + self.punto * u * 0.3 + 2.7 * u, 0.36 * u - contador * u * 0.45)
                p.lineTo(1.5 * u + self.punto * u * 0.3 + 2.7 * u, 0 - contador * u * 0.45)
                canv.drawPath(p, stroke=1, fill=1)
                canv.setFont('arialbd', 9)
                canv.setFillColor(black)
                canv.drawCentredString(1.5 * u + self.punto * u * 0.3 + 1.7 * u, 0.15 * u - contador * u * 0.45 - 3, ' ' + self.emisiones + ' ' + letras[contador])
            canv.setFillColor(white)
            canv.setFont('arialbd', 10)
            canv.drawCentredString(0.95 * u + contador * u * 0.3, 0.17 * u - contador * u * 0.45 - 3.5, letras[contador])
            canv.setFont('arialbd', 6)
            canv.drawString(0.1 * u, 0.22 * u - contador * u * 0.45 - 3.5, limites_str[contador])
            canv.setFont('arialbd', 10)

    def wrap(self, aW, aH):
        """
        Metodo: wrap
        
        
        ARGUMENTOS:
                aW:
                aH):
        """
        canv = self.canv
        return (canv._leading, canv.stringWidth(self.categoria))


def ajustaTamannoImagen(im, anchoDisponible, altoDisponible):
    if im.drawHeight / altoDisponible >= im.drawWidth / anchoDisponible:
        factorAjuste = im.drawHeight / altoDisponible
    else:
        factorAjuste = im.drawWidth / anchoDisponible
    im.drawHeight /= factorAjuste
    im.drawWidth /= factorAjuste
    return im


class GeneraInforme():
    """
    Clase: generaInforme del modulo creaPDF.py
    
    
    """

    def __init__(self, filename = '', objEdificio = None, datosAdmin = [], listadoConjuntosMMUsuario = [], datosEconomicos = [], datosConfiguracionInforme = []):
        self.filename = filename
        self.objEdificio = objEdificio
        self.datosAdmin = datosAdmin
        self.datosEconomicos = datosEconomicos
        self.datosConfiguracionInforme = datosConfiguracionInforme
        conjuntosMMSeleccionados = [self.datosConfiguracionInforme[0], self.datosConfiguracionInforme[1], self.datosConfiguracionInforme[2]]
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
        self.getEstilosDocumento()
        if self.filename == None or self.filename == '':
            self.filename = DirectorioDoc + '/informeCalificacion.pdf'
        elif '.cex' in self.filename:
            self.filename = self.filename.replace('.cex', '.pdf')
        elif '.CEX' in self.filename:
            self.filename = self.filename.replace('.CEX', '.pdf')
        else:
            self.filename = DirectorioDoc + '/informeCalificacion.pdf'
        try:
            os.remove(self.filename)
        except:
            logging.info(u'Excepcion en: %s' % __name__)
            if os.path.exists(self.filename) == True:
                raise BorradoInformeCertificacion

        Story = []
        t = Paragraph(_(u'CERTIFICADO DE EFICIENCIA ENERG\xc9TICA DE EDIFICIOS'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.paginaInicial()
        Story += self.anexo1()
        Story.append(PageBreak())
        Story += self.anexo2()
        Story.append(PageBreak())
        Story += self.anexo3()
        Story += self.anexo4()
        self.pageNumber = 1
        doc = SimpleDocTemplate(self.filename.encode('iso-8859-15'))
        doc.leftMargin = 1.27 * cm
        doc.rightMargin = 1.27 * cm
        doc.topMargin = 1.0 * cm
        doc.bottomMargin = 1.27 * cm
        Story2 = copy.deepcopy(Story)
        self.totalPageNumber = 1
        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
        self.totalPageNumber = doc.page
        doc = SimpleDocTemplate(self.filename.encode('iso-8859-15'))
        doc.leftMargin = 1.27 * cm
        doc.rightMargin = 1.27 * cm
        doc.topMargin = 1.0 * cm
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
            logging.info(u'Excepcion Fuente Ausente en: %s' % __name__)
            raise FuenteAusente

        pdfmetrics.registerFontFamily('arial', normal='arial', bold='arialbd', italic='ariali', boldItalic='arialbi')
        self.titulo1 = ParagraphStyle('normal', fontName='arialbd', fontSize=13, alignment=TA_CENTER)
        self.titulo2 = ParagraphStyle('normal', fontName='arialbd', fontSize=10, alignment=TA_JUSTIFY)
        self.titulo3 = ParagraphStyle('normal', fontName='arialbd', fontSize=9, alignment=TA_CENTER)
        self.tabla1ContenidosN = ParagraphStyle('normal', fontName='arialbd', fontSize=9, leading=10.0, alignment=TA_JUSTIFY)
        self.tabla1ContenidosN_espacios = ParagraphStyle('normal', fontName='arialbd', fontSize=10, borderPadding=0.0, leading=8, spaceBefore=6, spaceAfter=6, alignment=TA_JUSTIFY)
        self.tabla1ContenidosNC = ParagraphStyle('normal', fontName='arialbd', fontSize=9, leading=8, alignment=TA_CENTER)
        self.tabla1Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=9, leading=10.0, alignment=TA_JUSTIFY)
        self.tabla2Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=8, leading=10.0, alignment=TA_CENTER)
        self.tabla4Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=6, leading=10.0, spaceBefore=0.0, spaceAfter=0.0, alignment=TA_CENTER)
        self.tabla1Contenidos_espacios = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=8, spaceBefore=0.0, spaceAfter=4, alignment=TA_JUSTIFY)
        self.tabla1Contenidos_parrafos = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=8, spaceBefore=0.0, spaceAfter=4, leftIndent=8, alignment=TA_JUSTIFY)
        self.tabla1ContenidosD = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=7, spaceBefore=0.0 * cm, alignment=TA_RIGHT)
        self.anexos = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=11, spaceBefore=0.0 * cm, alignment=TA_JUSTIFY)
        self.tabla1ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=10, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.tabla2ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=9, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.tabla3ContenidosC = ParagraphStyle('normal', fontName='arial', fontSize=7, borderPadding=0.0, leading=8, spaceBefore=0.0 * cm, alignment=TA_CENTER)
        self.tabla3Contenidos = ParagraphStyle('normal', fontName='arial', fontSize=6, borderPadding=0.1, leading=8, alignment=TA_JUSTIFY)
        self.tablaContenidosNotaPie = ParagraphStyle('normal', fontName='arial', fontSize=7, borderPadding=0.1, leading=8, alignment=TA_JUSTIFY)
        self.rosa = Color(red=0.253 / 0.255, green=0.233 / 0.255, blue=0.217 / 0.255)
        self.naranja = Color(red=0.251 / 0.255, green=0.212 / 0.255, blue=0.18 / 0.255)

    def paginaInicial(self):
        Story = []
        Story += self.tablaIdentificacionEdificio()
        Story += self.tablaTipoEdificioQueSeCertifica()
        Story += self.tablaDatosTecnicoCertificador()
        Story += self.tablaCalificacionEnergeticaObtenida()
        return Story

    def tablaIdentificacionEdificio(self):
        nombreEdificio = self.datosAdmin[0]
        direccionEdificio = self.datosAdmin[1]
        localidadEdificio = self.datosAdmin[2]
        provinciaEdificio = self.datosAdmin[3]
        otroLocalidad = self.datosAdmin[4]
        codigoPostalEdificio = self.datosAdmin[14]
        listadoRefCat = self.datosAdmin[15]
        ccaaEdificio = Localizacion().getCCAA(provinciaEdificio)
        if localidadEdificio == 'Otro':
            localidad = otroLocalidad
        else:
            localidad = localidadEdificio
        Story = []
        t = Paragraph(_(u'IDENTIFICACI\xd3N DEL EDIFICIO O DE LA PARTE QUE SE CERTIFICA:'), self.titulo2)
        Story.append(t)
        a0 = Paragraph(unicode(nombreEdificio), self.tabla1Contenidos)
        a1 = Paragraph(unicode(direccionEdificio), self.tabla1Contenidos)
        data = [[Paragraph(_(u'Nombre del edificio'), self.tabla1ContenidosN), a0], [Paragraph(_(u'Direcci\xf3n'), self.tabla1ContenidosN), a1]]
        t = Table(data, [7.69 * cm, 11.01 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'Municipio'), self.tabla1ContenidosN)
        a12 = Paragraph(unicode(localidad), self.tabla1Contenidos)
        a13 = Paragraph(_(u'C\xf3digo Postal'), self.tabla1ContenidosN)
        a14 = Paragraph(codigoPostalEdificio, self.tabla1Contenidos)
        a21 = Paragraph(_(u'Provincia'), self.tabla1ContenidosN)
        a22 = Paragraph(unicode(provinciaEdificio), self.tabla1Contenidos)
        a23 = Paragraph(_(u'Comunidad Aut\xf3noma'), self.tabla1ContenidosN)
        a24 = Paragraph(unicode(ccaaEdificio), self.tabla1Contenidos)
        a31 = Paragraph(_(u'Zona clim\xe1tica'), self.tabla1ContenidosN)
        a32 = Paragraph(unicode(self.objEdificio.datosIniciales.zonaHE1), self.tabla1Contenidos)
        a33 = Paragraph(_(u'A\xf1o construcci\xf3n'), self.tabla1ContenidosN)
        a34 = Paragraph(self.objEdificio.datosIniciales.annoConstruccion, self.tabla1Contenidos)
        data = [[a11,
          a12,
          a13,
          a14], [a21,
          a22,
          a23,
          a24], [a31,
          a32,
          a33,
          a34]]
        t = Table(data, [7.69 * cm,
         3.5 * cm,
         4.0 * cm,
         3.51 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 2),
          self.rosa),
         ('BACKGROUND',
          (2, 0),
          (2, 2),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'Normativa vigente (construcci\xf3n / rehabilitaci\xf3n)'), self.tabla1ContenidosN)
        if self.objEdificio.datosIniciales.normativaVigente == u'Anterior':
            a12 = Paragraph(_(u'Anterior a la NBE-CT-79'), self.tabla1Contenidos)
        else:
            a12 = Paragraph(unicode(self.objEdificio.datosIniciales.normativaVigente), self.tabla1Contenidos)
        a21 = Paragraph(_(u'Referencia/s catastral/es'), self.tabla1ContenidosN)
        a22 = Paragraph(unicode(listadoRefCat[0]), self.tabla1Contenidos)
        data = [[a11, a12], [a21, a22]]
        t = Table(data, [7.69 * cm, 11.01 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        return Story

    def tablaTipoEdificioQueSeCertifica(self):
        Story = []
        data = [[Paragraph(_(u'Tipo de edificio o parte del edificio que se certifica:'), self.tabla1ContenidosNC)]]
        t = Table(data, [18.7 * cm], [0.5 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = u'\u25cb ' + _(u'Edificio de nueva construcci\xf3n')
        a12 = u'\u25cb ' + _(u'Edificio Existente')
        if self.objEdificio.esEdificioExistente == False:
            a11 = u'\u25cf ' + _(u'Edificio de nueva construcci\xf3n')
        elif self.objEdificio.esEdificioExistente == True:
            a12 = u'\u25cf ' + _(u'Edificio Existente')
        data = [[a11, a12]]
        t = Table(data, [9.35 * cm, 9.35 * cm], [0.5 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('FONT',
          (0, 0),
          (-1, -1),
          'arial',
          9),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0),
         ('BOTTOMPADDING',
          (0, 0),
          (-1, -1),
          0)]))
        Story.append(t)
        data = [[Paragraph(u'', self.tabla1ContenidosNC)]]
        t = Table(data, [18.7 * cm], [0.5 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa),
         ('LEFTPADDING',
          (0, 0),
          (-1, -1),
          0.5 * cm),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = u'\u25cb ' + _(u'Vivienda')
        a12 = u'\u25cb ' + _(u'Terciario')
        a21 = u'\u25cb ' + _(u'Unifamiliar')
        a22 = u'\u25cb ' + _(u'Edificio completo')
        a31 = u'\u25cb ' + _(u'Bloque')
        a32 = u'\u25cb ' + _(u'Local')
        a41 = u'\u25cb ' + _(u'Bloque completo')
        a42 = u''
        a51 = u'\u25cb ' + _(u'Vivienda individual')
        a52 = u''
        if self.objEdificio.programa == 'Residencial':
            a11 = u'\u25cf ' + _(u'Vivienda')
            if self.objEdificio.datosIniciales.tipoEdificio == u'Bloque de Viviendas':
                a31 = u'\u25cf ' + _(u'Bloque')
                a41 = u'\u25cf ' + _(u'Bloque completo')
            elif self.objEdificio.datosIniciales.tipoEdificio == u'Unifamiliar':
                a21 = u'\u25cf ' + _(u'Unifamiliar')
            elif self.objEdificio.datosIniciales.tipoEdificio == u'Vivienda Individual':
                a31 = u'\u25cf ' + _(u'Bloque')
                a51 = u'\u25cf ' + _(u'Vivienda individual')
        else:
            a12 = u'\u25cf ' + _(u'Terciario')
            if self.objEdificio.datosIniciales.tipoUsoTerciario == u'Edificio completo':
                a22 = u'\u25cf ' + _(u'Edificio completo')
            elif self.objEdificio.datosIniciales.tipoUsoTerciario == u'Local':
                a32 = u'\u25cf ' + _(u'Local')
        data = [[a11, a12],
         [a21, a22],
         [a31, a32],
         [a41, a42],
         [a51, a52]]
        t = Table(data, [9.35 * cm, 9.35 * cm], [0.4 * cm,
         0.4 * cm,
         0.4 * cm,
         0.4 * cm,
         0.4 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('FONT',
          (0, 0),
          (-1, -1),
          'arial',
          9),
         ('BOX',
          (0, 0),
          (0, -1),
          0.5,
          colors.black),
         ('BOX',
          (1, 0),
          (1, -1),
          0.5,
          colors.black),
         ('LEFTPADDING',
          (0, 0),
          (1, 0),
          0.5 * cm),
         ('LEFTPADDING',
          (0, 1),
          (1, 2),
          1.0 * cm),
         ('LEFTPADDING',
          (0, 3),
          (1, 4),
          1.5 * cm),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0),
         ('BOTTOMPADDING',
          (0, 0),
          (-1, -1),
          0)]))
        Story.append(t)
        Story.append(Spacer(1, 0.5 * cm))
        return Story

    def tablaDatosTecnicoCertificador(self):
        nombreCertificador = self.datosAdmin[11]
        razonSocialCertificador = self.datosAdmin[10]
        telefonoCertificador = self.datosAdmin[12]
        emailCertificador = self.datosAdmin[13]
        nifCertificado = self.datosAdmin[19]
        cifCertificador = self.datosAdmin[20]
        direccionCertificador = self.datosAdmin[21]
        provinciaCertificador = self.datosAdmin[22]
        localidadCertificador = self.datosAdmin[23]
        codigoPostalCertificador = self.datosAdmin[24]
        titulacionHabilitante = self.datosAdmin[25]
        ccaaCertificador = Localizacion().getCCAA(provinciaCertificador)
        Story = []
        t = Paragraph(_(u'DATOS DEL T\xc9CNICO CERTIFICADOR:'), self.titulo2)
        Story.append(t)
        a11 = Paragraph(_(u'Nombre y Apellidos'), self.tabla1ContenidosN)
        a12 = Paragraph(nombreCertificador, self.tabla1Contenidos)
        a13 = Paragraph(_(u'NIF(NIE)'), self.tabla1ContenidosN)
        a14 = Paragraph(nifCertificado, self.tabla1Contenidos)
        a21 = Paragraph(_(u'Raz\xf3n social'), self.tabla1ContenidosN)
        a22 = Paragraph(razonSocialCertificador, self.tabla1Contenidos)
        a23 = Paragraph(_(u'NIF'), self.tabla1ContenidosN)
        a24 = Paragraph(cifCertificador, self.tabla1Contenidos)
        data = [[a11,
          a12,
          a13,
          a14], [a21,
          a22,
          a23,
          a24]]
        t = Table(data, [5.19 * cm,
         7.75 * cm,
         1.75 * cm,
         4.01 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('FONT',
          (0, 0),
          (-1, -1),
          'arial',
          10),
         ('FONT',
          (0, 0),
          (0, 1),
          'arialbd',
          10),
         ('FONT',
          (2, 0),
          (2, 1),
          'arialbd',
          10),
         ('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa),
         ('BACKGROUND',
          (2, 0),
          (2, 1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'Domicilio'), self.tabla1ContenidosN)
        a12 = Paragraph(direccionCertificador, self.tabla1Contenidos)
        data = [[a11, a12]]
        t = Table(data, [7.69 * cm, 11.01 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'Municipio'), self.tabla1ContenidosN)
        a12 = Paragraph(localidadCertificador, self.tabla1Contenidos)
        a13 = Paragraph(_(u'C\xf3digo Postal'), self.tabla1ContenidosN)
        a14 = Paragraph(codigoPostalCertificador, self.tabla1Contenidos)
        a21 = Paragraph(_(u'Provincia'), self.tabla1ContenidosN)
        a22 = Paragraph(provinciaCertificador, self.tabla1Contenidos)
        a23 = Paragraph(_(u'Comunidad Aut\xf3noma'), self.tabla1ContenidosN)
        a24 = Paragraph(ccaaCertificador, self.tabla1Contenidos)
        data = [[a11,
          a12,
          a13,
          a14], [a21,
          a22,
          a23,
          a24]]
        t = Table(data, [7.69 * cm,
         3.5 * cm,
         4.0 * cm,
         3.51 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa),
         ('BACKGROUND',
          (2, 0),
          (2, 1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'e-mail:'), self.tabla1ContenidosN)
        a12 = Paragraph(emailCertificador, self.tabla1Contenidos)
        a13 = Paragraph(_(u'Tel\xe9fono'), self.tabla1ContenidosN)
        a14 = Paragraph(telefonoCertificador, self.tabla1Contenidos)
        data = [[a11,
          a12,
          a13,
          a14]]
        t = Table(data, [7.69 * cm,
         5.25 * cm,
         2.25 * cm,
         3.51 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('FONT',
          (0, 0),
          (-1, -1),
          'arial',
          10),
         ('FONT',
          (0, 0),
          (0, -1),
          'arialbd',
          10),
         ('FONT',
          (2, 0),
          (2, -1),
          'arialbd',
          10),
         ('BACKGROUND',
          (0, 0),
          (0, -1),
          self.rosa),
         ('BACKGROUND',
          (2, 0),
          (2, -1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a21 = Paragraph(_(u'Titulaci\xf3n habilitante seg\xfan normativa vigente'), self.tabla1ContenidosN)
        a22 = Paragraph(titulacionHabilitante, self.tabla1Contenidos)
        data = [[a21, a22]]
        t = Table(data, [7.69 * cm, 11.01 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        a11 = Paragraph(_(u'Procedimiento reconocido de calificaci\xf3n energ\xe9tica  utilizado y versi\xf3n:'), self.tabla1ContenidosN)
        a12 = Paragraph(programaVersion, self.tabla1Contenidos)
        data = [[a11, a12]]
        t = Table(data, [11.19 * cm, 7.51 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        return Story

    def tablaCalificacionEnergeticaObtenida(self):
        Story = []
        t = Paragraph(_(u'CALIFICACI\xd3N ENERG\xc9TICA OBTENIDA:'), self.titulo2)
        Story.append(t)
        a11 = Paragraph(_(u'EMISIONES DE DI\xd3XIDO DE'), self.tabla1ContenidosNC)
        a21 = Paragraph(_(u'CARBONO'), self.tabla1ContenidosNC)
        a31 = Paragraph(_(u'[kgCO2/ m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'CONSUMO DE ENERG\xcdA'), self.tabla1ContenidosNC)
        a22 = Paragraph(_(u'PRIMARIA NO RENOVABLE'), self.tabla1ContenidosNC)
        a32 = Paragraph(_(u'[kWh/m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
        data = [[a12, a11], [a22, a21], [a32, a31]]
        t = Table(data, [7.08 * cm, 7.08 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (-1, -1),
          self.rosa),
         ('BOX',
          (0, 0),
          (0, -1),
          0.5,
          colors.black),
         ('BOX',
          (1, 0),
          (1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        limitesEmisionesGlobales = self.objEdificio.datosResultados.emisiones_limites
        imagenCalificacionGlobal = Etiqueta(str(self.objEdificio.datosResultados.emisiones_nota), str(round(self.objEdificio.datosResultados.emisionesMostrar, 1)), limitesEmisionesGlobales)
        imagenCalificacionGlobal.scaleX = 0.75
        imagenCalificacionGlobal.scaleY = 0.75
        imagenCalificacionGlobal.translateX = 0 * cm
        imagenCalificacionGlobal.translateY = 0.9 * cm
        limitesEnPrimNoRen = self.objEdificio.datosResultados.enPrimNoRen_limites
        imagenConsumoEnergia = Etiqueta(str(self.objEdificio.datosResultados.enPrimNoRen_nota), str(round(self.objEdificio.datosResultados.enPrimNoRenMostrar, 1)), limitesEnPrimNoRen)
        imagenConsumoEnergia.scaleX = 0.75
        imagenConsumoEnergia.scaleY = 0.75
        imagenConsumoEnergia.translateX = 0 * cm
        imagenConsumoEnergia.translateY = 0.9 * cm
        data = [[imagenConsumoEnergia,
          '',
          imagenCalificacionGlobal,
          '']]
        t = Table(data, [4.52 * cm,
         2.58 * cm,
         4.52 * cm,
         2.58 * cm], [2.52 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black), ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm), ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        p = Paragraph(_(u'El t\xe9cnico abajo firmante declara responsablemente que ha realizado\n                        la certificaci\xf3n energ\xe9tica del edificio o de la parte que se certifica\n                        de acuerdo con el procedimiento establecido por la normativa vigente\n                        y que son ciertos los datos que figuran en el presente documento, y sus anexos:\n                        '), self.tabla1Contenidos)
        Story.append(p)
        Story.append(Spacer(0, 0.4 * cm))
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
        p = Paragraph(_(u'Fecha: ') + '%s/%s/%s' % (dia, mes, anno), self.tabla1Contenidos)
        Story.append(p)
        Story.append(Spacer(0, 0.4 * cm))
        Story.append(Spacer(0, 0.4 * cm))
        Story.append(Spacer(0, 0.4 * cm))
        p = Paragraph(_(u'Firma del t\xe9cnico certificador'), self.tabla1ContenidosC)
        Story.append(p)
        Story.append(Spacer(0, 0.4 * cm))
        p = Paragraph(_(u'<i><b>Anexo I.</b> Descripci\xf3n de las caracter\xedsticas energ\xe9ticas del edificio.</i>'), self.anexos)
        Story.append(p)
        p = Paragraph(_(u'<i><b>Anexo II.</b> Calificaci\xf3n energ\xe9tica del edificio.</i>'), self.anexos)
        Story.append(p)
        p = Paragraph(_(u'<i><b>Anexo III.</b> Recomendaciones para la mejora de la eficiencia energ\xe9tica.</i>'), self.anexos)
        Story.append(p)
        p = Paragraph(_(u'<i><b>Anexo IV.</b> Pruebas, comprobaciones e inspecciones realizadas por el t\xe9cnico certificador.</i>'), self.anexos)
        Story.append(p)
        Story.append(Spacer(0, 0.4 * cm))
        p = Paragraph(_(u'Registro del \xd3rgano Territorial Competente:'), self.tabla1Contenidos)
        Story.append(p)
        Story.append(PageBreak())
        return Story

    def anexo1(self):
        Story = []
        t = Paragraph(_(u'ANEXO I'), self.titulo1)
        Story.append(t)
        t = Paragraph(_(u'DESCRIPCI\xd3N DE LAS CARACTER\xcdSTICAS ENERG\xc9TICAS DEL EDIFICIO'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        t = Paragraph(_(u'En este apartado se describen las caracter\xedsticas energ\xe9ticas del edificio,                         envolvente t\xe9rmica, instalaciones, condiciones de funcionamiento y ocupaci\xf3n y                         dem\xe1s datos utilizados para obtener la calificaci\xf3n energ\xe9tica del edificio.'), self.tabla1Contenidos)
        Story.append(t)
        Story.append(Spacer(0, 0.7 * cm))
        Story += self.tablaAnexo1Aptdo1()
        Story.append(CondPageBreak(6 * cm))
        Story += self.tablaAnexo1Aptdo2()
        Story.append(Spacer(0, 0.7 * cm))
        Story.append(CondPageBreak(6 * cm))
        Story += self.tablaAnexo1Aptdo3()
        Story.append(Spacer(0, 0.7 * cm))
        Story.append(CondPageBreak(6 * cm))
        Story += self.tablaAnexo1Aptdo4()
        Story.append(Spacer(0, 0.7 * cm))
        Story.append(CondPageBreak(6 * cm))
        if self.objEdificio.programa != 'Residencial':
            Story += self.tablaAnexo1Aptdo5()
            Story.append(Spacer(0, 0.7 * cm))
            Story.append(CondPageBreak(6 * cm))
        Story += self.tablaAnexo1Aptdo6()
        Story.append(Spacer(0, 0.7 * cm))
        return Story

    def tablaAnexo1Aptdo1(self):
        Story = []
        t = Paragraph(_(u'1.\tSUPERFICIE, IMAGEN Y SITUACI\xd3N'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        superficieInmueble = self.objEdificio.datosIniciales.area
        a11 = Paragraph(_(u'Superficie habitable [m\xb2]'), self.tabla1ContenidosN)
        a12 = Paragraph(u'%s' % superficieInmueble, self.tabla1Contenidos)
        data = [[a11, a12]]
        t = Table(data, [7.25 * cm, 10.75 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa), ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black), ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Imagen del edificio'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Plano de situaci\xf3n'), self.tabla1ContenidosNC)
        plano = Image(StringIO(base64.b64decode(self.objEdificio.datosIniciales.plano)))
        edificio = Image(StringIO(base64.b64decode(self.objEdificio.datosIniciales.imagen)))
        anchoDisponible = 250.0
        altoDisponible = 185.0
        edificio = ajustaTamannoImagen(edificio, anchoDisponible, altoDisponible)
        plano = ajustaTamannoImagen(plano, anchoDisponible, altoDisponible)
        edificio.hAlign = 'CENTER'
        edificio.vAlign = 'MIDDLE'
        plano.hAlign = 'CENTER'
        plano.vAlign = 'MIDDLE'
        a21 = edificio
        a22 = plano
        data = [[a11, a12], [a21, a22]]
        t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (1, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('VALIGN',
          (-1, -1),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.7 * cm))
        return Story

    def tablaAnexo1Aptdo2(self):
        Story = []
        t = Paragraph(_(u'2.\tENVOLVENTE T\xc9RMICA'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        Story.append(CondPageBreak(4 * cm))
        Story += self.tablaAnexo1Aptdo2Cerramientos()
        Story += self.tablaAnexo1Aptdo2Huecos()
        return Story

    def tablaAnexo1Aptdo2Cerramientos(self):
        Story = []
        t = Paragraph(_(u'Cerramientos opacos'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Superficie [m\xb2]'), self.tabla1ContenidosNC)
        a14 = Paragraph(_(u'Transmitancia [W/m\xb2\xb7K]'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'Modo de obtenci\xf3n'), self.tabla1ContenidosNC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15]]
        for i in self.objEdificio.datosIniciales.listadoCerramientos:
            if i.modoObtencion != '':
                modo = Paragraph(_(i.modoObtencion), self.tabla1ContenidosC)
            else:
                modo = Paragraph('', self.tabla1ContenidosC)
            tipoCerr = getTraduccion(listado=listadoCerramientos, elemento=i.tipo)
            tipo = Paragraph(_(tipoCerr), self.tabla1ContenidosC)
            descripcion = Paragraph(i.nombre, self.tabla1Contenidos)
            superficie = Paragraph('%s' % i.superficieNeta, self.tabla1ContenidosC)
            transmitancia = Paragraph('%0.2f' % float(i.U), self.tabla1ContenidosC)
            data.append([descripcion,
             tipo,
             superficie,
             transmitancia,
             modo])

        t = Table(data, [5.76 * cm,
         4.44 * cm,
         1.98 * cm,
         2.47 * cm,
         3.35 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black)]))
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(4 * cm))
        return Story

    def tablaAnexo1Aptdo2Huecos(self):
        Story = []
        t = Paragraph(_(u'Huecos y lucernarios'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Superficie [m\xb2]'), self.tabla1ContenidosNC)
        a14 = Paragraph(_(u'Transmitancia [W/m\xb2\xb7K]'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'Factor solar'), self.tabla1ContenidosNC)
        a16 = Paragraph(_(u'Modo de obtenci\xf3n. Transmitancia'), self.tabla1ContenidosNC)
        a17 = Paragraph(_(u'Modo de obtenci\xf3n. Factor solar'), self.tabla1ContenidosNC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16,
          a17]]
        for i in self.objEdificio.datosIniciales.listadoHuecos:
            if 'Estimad' in i.__tipo__:
                modo = Paragraph(_(u'Estimado'), self.tabla1ContenidosC)
            else:
                modo = Paragraph(_(u'Conocido'), self.tabla1ContenidosC)
            descripcion = Paragraph(i.descripcion, self.tabla1Contenidos)
            tipo = Paragraph(_(i.tipo), self.tabla1ContenidosC)
            superficie = Paragraph(i.superficie, self.tabla1ContenidosC)
            transmitancia = Paragraph('%0.2f' % i.calculoUhueco(), self.tabla1ContenidosC)
            factorSolar = Paragraph('%0.2f' % i.calculoFShueco(), self.tabla1ContenidosC)
            data.append([descripcion,
             tipo,
             superficie,
             transmitancia,
             factorSolar,
             modo,
             modo])

        t = Table(data, [4.75 * cm,
         2.08 * cm,
         1.84 * cm,
         2.45 * cm,
         1.48 * cm,
         2.71 * cm,
         2.71 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa)]))
        Story.append(t)
        return Story

    def tablaAnexo1Aptdo3(self):
        Story = []
        t = Paragraph(_(u'3.\tINSTALACIONES T\xc9RMICAS'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        Story.append(CondPageBreak(4 * cm))
        Story += self.tablaAnexo1Aptdo3Generadores()
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(4 * cm))
        Story += self.tablaAnexo1Aptdo3TorresRefrigeracion()
        Story += self.tablaAnexo1Aptdo3VentiladoresYBombas()
        return Story

    def tablaAnexo1Aptdo3Generadores(self):
        Story = []
        t = Paragraph(_(u'Generadores de calefacci\xf3n'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Potencia nominal [kW]'), self.tabla1ContenidosNC)
        a14 = Paragraph(_(u'Rendimiento Estacional[%]'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'Tipo de Energ\xeda'), self.tabla1ContenidosNC)
        a16 = Paragraph(_(u'Modo de obtenci\xf3n'), self.tabla1ContenidosNC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        for i in self.objEdificio.datosIniciales.calefaccion.listado:
            if 'Estimado' in i.modoObtencion:
                modo = Paragraph(_(u'Estimado'), self.tabla1ContenidosC)
            else:
                modo = Paragraph(_(u'Conocido'), self.tabla1ContenidosC)
            rendimiento = i.rendimiento
            descripcion = Paragraph(i.nombre, self.tabla1Contenidos)
            generador = Paragraph(_(i.generador), self.tabla1ContenidosC)
            combustibleEquipo = getTraduccion(listado=listadoCombustibles, elemento=i.combustible)
            combustible = Paragraph(combustibleEquipo, self.tabla1Contenidos)
            potencia = Paragraph(i.potencia, self.tabla1ContenidosC)
            data.append([descripcion,
             generador,
             potencia,
             rendimiento,
             combustible,
             modo])

        if len(data) > 1:
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        else:
            data.append(['',
             '',
             '',
             '',
             '',
             ''])
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        data = [a11,
         a12,
         a13,
         a14,
         a15,
         a16]
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa)]))
        Story.append(t)
        totalTipoCalefaccion = _(u'Calefacci\xf3n')
        totalPotenciaNominalCalefaccion = ''
        totalRendCalefaccion = ''
        totalEnerCalefaccion = ''
        totalModoObtencionCalefaccion = ''
        a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
        a12 = Paragraph(u'%s' % totalTipoCalefaccion, self.tabla1ContenidosC)
        a13 = Paragraph(u'%s' % totalPotenciaNominalCalefaccion, self.tabla1ContenidosC)
        a14 = Paragraph(u'%s' % totalRendCalefaccion, self.tabla1ContenidosC)
        a15 = Paragraph(u'%s ' % totalEnerCalefaccion, self.tabla1ContenidosC)
        a16 = Paragraph(u'%s' % totalModoObtencionCalefaccion, self.tabla1ContenidosC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        t = Table(data, [3.77 * cm,
         4 * cm,
         3 * cm,
         2.5 * cm,
         2.25 * cm,
         2.48 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.naranja)]))
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(4 * cm))
        t = Paragraph(_(u'Generadores de refrigeraci\xf3n'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Potencia nominal [kW]'), self.tabla1ContenidosNC)
        a14 = Paragraph(_(u'Rendimiento Estacional[%]'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'Tipo de Energ\xeda'), self.tabla1ContenidosNC)
        a16 = Paragraph(_(u'Modo de obtenci\xf3n'), self.tabla1ContenidosNC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        for i in self.objEdificio.datosIniciales.refrigeracion.listado:
            if 'Estimado' in i.modoObtencion:
                modo = Paragraph(_(u'Estimado'), self.tabla1ContenidosC)
            else:
                modo = Paragraph(_(u'Conocido'), self.tabla1ContenidosC)
            rendimiento = i.rendimiento
            descripcion = Paragraph(i.nombre, self.tabla1Contenidos)
            generador = Paragraph(_(i.generador), self.tabla1ContenidosC)
            combustibleEquipo = getTraduccion(listado=listadoCombustibles, elemento=i.combustible)
            combustible = Paragraph(combustibleEquipo, self.tabla1Contenidos)
            potencia = Paragraph(i.potencia, self.tabla1ContenidosC)
            data.append([descripcion,
             generador,
             potencia,
             rendimiento,
             combustible,
             modo])

        if len(data) > 1:
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        else:
            data.append(['',
             '',
             '',
             '',
             '',
             ''])
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa)]))
        Story.append(t)
        totalTipoRef = _(u'Refrigeraci\xf3n')
        totalPotenciaNominalRef = ''
        totalRendRef = ''
        totalEnerRef = ''
        totalModoObtencionRef = ''
        a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
        a12 = Paragraph(u'%s' % totalTipoRef, self.tabla1ContenidosC)
        a13 = Paragraph(u'%s' % totalPotenciaNominalRef, self.tabla1ContenidosC)
        a14 = Paragraph(u'%s' % totalRendRef, self.tabla1ContenidosC)
        a15 = Paragraph(u'%s' % totalEnerRef, self.tabla1ContenidosC)
        a16 = Paragraph(u'%s' % totalModoObtencionRef, self.tabla1ContenidosC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        t = Table(data, [3.77 * cm,
         4 * cm,
         3 * cm,
         2.5 * cm,
         2.25 * cm,
         2.48 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.naranja)]))
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story.append(CondPageBreak(4 * cm))
        t = Paragraph(_(u'Instalaciones de Agua Caliente Sanitaria'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Demanda diario de ACS a 60\xb0 (litros/d\xeda)'), self.tabla1ContenidosNC)
        a12 = Paragraph(u'%s' % self.objEdificio.datosIniciales.Q_ACS, self.tabla1ContenidosC)
        data = [[a11, a12]]
        t = Table(data, [7.69 * cm, 3.2 * cm], None, None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa)]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Potencia nominal [kW]'), self.tabla1ContenidosNC)
        a14 = Paragraph(_(u'Rendimiento Estacional[%]'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'Tipo de Energ\xeda'), self.tabla1ContenidosNC)
        a16 = Paragraph(_(u'Modo de obtenci\xf3n'), self.tabla1ContenidosNC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        for i in self.objEdificio.datosIniciales.ACS.listado:
            if 'Estimado' in i.modoObtencion:
                modo = Paragraph(_(u'Estimado'), self.tabla1ContenidosC)
            else:
                modo = Paragraph(_(u'Conocido'), self.tabla1ContenidosC)
            rendimiento = i.rendimiento
            descripcion = Paragraph(i.nombre, self.tabla1Contenidos)
            generador = Paragraph(_(i.generador), self.tabla1ContenidosC)
            combustibleEquipo = getTraduccion(listado=listadoCombustibles, elemento=i.combustible)
            combustible = Paragraph(combustibleEquipo, self.tabla1Contenidos)
            potencia = Paragraph(i.potencia, self.tabla1ContenidosC)
            data.append([descripcion,
             generador,
             potencia,
             rendimiento,
             combustible,
             modo])

        if len(data) > 1:
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        else:
            data.append(['',
             '',
             '',
             '',
             '',
             ''])
            t = Table(data, [3.77 * cm,
             4 * cm,
             3 * cm,
             2.5 * cm,
             2.25 * cm,
             2.48 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa)]))
        Story.append(t)
        totalTipoACS = _(u'ACS')
        totalPotenciaNominalACS = ''
        totalRendACS = ''
        totalEnerACS = ''
        totalModoObtencionACS = ''
        a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
        a12 = Paragraph(u'%s' % totalTipoACS, self.tabla1ContenidosC)
        a13 = Paragraph(u'%s' % totalPotenciaNominalACS, self.tabla1ContenidosC)
        a14 = Paragraph(u'%s' % totalRendACS, self.tabla1ContenidosC)
        a15 = Paragraph(u'%s' % totalEnerACS, self.tabla1ContenidosC)
        a16 = Paragraph(u'%s' % totalModoObtencionACS, self.tabla1ContenidosC)
        data = [[a11,
          a12,
          a13,
          a14,
          a15,
          a16]]
        t = Table(data, [3.77 * cm,
         4 * cm,
         3 * cm,
         2.5 * cm,
         2.25 * cm,
         2.48 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.naranja)]))
        Story.append(t)
        return Story

    def tablaAnexo1Aptdo3TorresRefrigeracion(self):
        Story = []
        if self.objEdificio.datosIniciales.sistemasTorresRefrigeracion != []:
            t = Paragraph(_(u'Torres de refrigeraci\xf3n (s\xf3lo edificios terciarios)'), self.titulo2)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
            a13 = Paragraph(_(u'Servicio asociado'), self.tabla1ContenidosNC)
            a14 = Paragraph(_(u'Consumo de energ\xeda [kWh/a\xf1o]'), self.tabla1ContenidosNC)
            data = [[a11,
              a12,
              a13,
              a14]]
            for i in self.objEdificio.datosIniciales.sistemasTorresRefrigeracion:
                descripcion = Paragraph(i[0], self.tabla1Contenidos)
                tipoEquipo = listadoOpcionesTorreDeRefrigeracion[i[3]][1]
                tipo = Paragraph(tipoEquipo, self.tabla1Contenidos)
                consumo = str(round(float(i[2]), 1))
                servicio = Paragraph(u'', self.tabla1ContenidosC)
                data.append([descripcion,
                 tipo,
                 servicio,
                 consumo])

            if len(data) > 1:
                t = Table(data, [4.62 * cm,
                 4.28 * cm,
                 4.45 * cm,
                 4.62 * cm], None, None, 1, 1, 1)
            else:
                data.append(['',
                 '',
                 '',
                 ''])
                t = Table(data, [4.62 * cm,
                 4.28 * cm,
                 4.45 * cm,
                 4.62 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.rosa)]))
            Story.append(t)
            consumoTotalTorres = round(self.objEdificio.datosResultados.enFinalRealTorresRef * self.objEdificio.datosIniciales.area, 2)
            a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
            a12 = Paragraph(u'', self.tabla1ContenidosC)
            a13 = Paragraph(u'', self.tabla1ContenidosC)
            a14 = Paragraph(u'%s' % consumoTotalTorres, self.tabla1ContenidosC)
            data = [[a11,
              a12,
              a13,
              a14]]
            t = Table(data, [4.62 * cm,
             4.28 * cm,
             4.45 * cm,
             4.62 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.naranja)]))
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
        return Story

    def tablaAnexo1Aptdo3VentiladoresYBombas(self):
        Story = []
        if self.objEdificio.datosIniciales.sistemasVentiladores != [] or self.objEdificio.datosIniciales.sistemasBombas != []:
            Story.append(CondPageBreak(4 * cm))
            t = Paragraph(_(u'Ventilaci\xf3n y bombeo (s\xf3lo edificios terciarios)'), self.titulo2)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'Tipo'), self.tabla1ContenidosNC)
            a13 = Paragraph(_(u'Servicio asociado'), self.tabla1ContenidosNC)
            a14 = Paragraph(_(u'Consumo de energ\xeda [kWh/a\xf1o]'), self.tabla1ContenidosNC)
            data = [[a11,
              a12,
              a13,
              a14]]
            for i in self.objEdificio.datosIniciales.sistemasVentiladores:
                descripcion = Paragraph(i[0], self.tabla1Contenidos)
                tipoEquipo = listadoOpcionesVentiladores[i[3]][1]
                tipo = Paragraph(tipoEquipo, self.tabla1Contenidos)
                servicioEquipo = listadoOpcionesServicioVentiladores[i[12]][1]
                servicio = Paragraph(servicioEquipo, self.tabla1ContenidosC)
                consumo = Paragraph(_(u'%0.2f' % float(i[2])), self.tabla1ContenidosC)
                data.append([descripcion,
                 tipo,
                 servicio,
                 consumo])

            for i in self.objEdificio.datosIniciales.sistemasBombas:
                descripcion = Paragraph(i[0], self.tabla1Contenidos)
                tipoEquipo = listadoOpcionesBombas[i[3]][1]
                tipo = Paragraph(tipoEquipo, self.tabla1Contenidos)
                servicioEquipo = listadoOpcionesServicioBombas[i[12]][1]
                servicio = Paragraph(servicioEquipo, self.tabla1ContenidosC)
                consumo = Paragraph(_(u'%0.2f' % float(i[2])), self.tabla1ContenidosC)
                data.append([descripcion,
                 tipo,
                 servicio,
                 consumo])

            if len(data) > 1:
                t = Table(data, [4.62 * cm,
                 4.28 * cm,
                 4.45 * cm,
                 4.62 * cm], None, None, 1, 1, 1)
            else:
                data.append(['',
                 '',
                 '',
                 ''])
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.rosa)]))
            Story.append(t)
            consumoTotalVentiladoresYBombas = round((self.objEdificio.datosResultados.enFinalRealVentiladores + self.objEdificio.datosResultados.enFinalRealBombas) * self.objEdificio.datosIniciales.area, 2)
            a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
            a12 = Paragraph(u'', self.tabla1ContenidosC)
            a13 = Paragraph(u'', self.tabla1ContenidosC)
            a14 = Paragraph(u'%s' % consumoTotalVentiladoresYBombas, self.tabla1ContenidosC)
            data = [[a11,
              a12,
              a13,
              a14]]
            t = Table(data, [4.62 * cm,
             4.28 * cm,
             4.45 * cm,
             4.62 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.naranja)]))
            Story.append(t)
            Story.append(Spacer(0, 0.7 * cm))
        return Story

    def tablaAnexo1Aptdo4(self):
        Story = []
        if self.objEdificio.datosIniciales.sistemasIluminacion != []:
            t = Paragraph(_(u'4.\tINSTALACI\xd3N DE ILUMINACI\xd3N (s\xf3lo edificios terciarios)'), self.titulo2)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            a11 = Paragraph(_(u'Espacio'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'Potencia instalada [W/m\xb2]'), self.tabla1ContenidosNC)
            a13 = Paragraph(_(u'VEEI [W/m\xb2\xb7100lux]'), self.tabla1ContenidosNC)
            a14 = Paragraph(_(u'Iluminaci\xf3n media [lux]'), self.tabla1ContenidosNC)
            a15 = Paragraph(_(u'Modo de obtenci\xf3n'), self.tabla1ContenidosNC)
            data = [[a11,
              a12,
              a13,
              a14,
              a15]]
            potenciaTotal = 0.0
            for i in self.objEdificio.datosIniciales.sistemasIluminacion:
                espacio = Paragraph(_(i[-1]), self.tabla1Contenidos)
                potenciaInst = float(i[2])
                potenciaTotal += potenciaInst
                potenciaInstalacionPorM2 = potenciaInst / float(i[5])
                potencia = Paragraph('%0.2f' % potenciaInstalacionPorM2, self.tabla1ContenidosC)
                veei = Paragraph('%0.2f' % float(i[3]), self.tabla1ContenidosC)
                iluminanciaMedia = Paragraph('%0.2f' % float(i[9][1]), self.tabla1ContenidosC)
                modoDefinicion = i[8]
                if modoDefinicion == u'Conocido(ensayado/justificado)':
                    modo = _(u'Conocido')
                else:
                    modo = modoDefinicion
                modo = Paragraph(modo, self.tabla1Contenidos)
                data.append([espacio,
                 potencia,
                 veei,
                 iluminanciaMedia,
                 modo])

            if len(data) > 1:
                t = Table(data, [3.6 * cm,
                 3.56 * cm,
                 3.64 * cm,
                 3.6 * cm,
                 3.6 * cm], None, None, 1, 1, 1)
            else:
                data.append(['',
                 '',
                 '',
                 '',
                 ''])
                t = Table(data, [3.6 * cm,
                 3.56 * cm,
                 3.64 * cm,
                 3.6 * cm,
                 3.6 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.rosa)]))
            Story.append(t)
            totalPotenciaIluminacion = potenciaTotal / self.objEdificio.datosIniciales.area
            totalVEEIIluminacion = ''
            totalIluminanciaIluminacion = ''
            totalModoObtencionIluminacion = ''
            a11 = Paragraph(_(u'TOTALES'), self.tabla1ContenidosNC)
            a12 = Paragraph(u'%0.2f' % totalPotenciaIluminacion, self.tabla1ContenidosC)
            a13 = Paragraph(u'%s' % totalVEEIIluminacion, self.tabla1ContenidosC)
            a14 = Paragraph(u'%s' % totalIluminanciaIluminacion, self.tabla1ContenidosC)
            a15 = Paragraph(u'%s' % totalModoObtencionIluminacion, self.tabla1ContenidosC)
            data = [[a11,
              a12,
              a13,
              a14,
              a15]]
            t = Table(data, [3.6 * cm,
             3.56 * cm,
             3.64 * cm,
             3.6 * cm,
             3.6 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('ALIGN',
              (0, 0),
              (-1, -1),
              'CENTER'),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('BACKGROUND',
              (0, 0),
              (-1, 0),
              self.naranja)]))
            Story.append(t)
        return Story

    def tablaAnexo1Aptdo5(self):
        Story = []
        t = Paragraph(_(u'5.\tCONDICIONES DE FUNCIONAMIENTO Y OCUPACI\xd3N (s\xf3lo edificios terciarios)'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'Espacio'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'Superficie [m\xb2]'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'Perfil de uso'), self.tabla1ContenidosNC)
        a21 = Paragraph(_(u'Edificio'), self.tabla1Contenidos)
        a22 = Paragraph(u'%s' % self.objEdificio.datosIniciales.area, self.tabla1ContenidosC)
        a23 = Paragraph(_(self.objEdificio.datosIniciales.tipoEdificio), self.tabla1ContenidosC)
        data = [[a11, a12, a13], [a21, a22, a23]]
        t = Table(data, [6.09 * cm, 6.24 * cm, 5.67 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 0),
          (-1, 0),
          self.rosa)]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        return Story

    def tablaAnexo1Aptdo6(self):
        Story = []
        if len(self.objEdificio.datosIniciales.contribuciones.listado) > 0:
            if self.objEdificio.programa == 'Residencial':
                t = Paragraph(_(u'5.\tENERG\xcdAS RENOVABLES '), self.titulo2)
            else:
                t = Paragraph(_(u'6.\tENERG\xcdAS RENOVABLES '), self.titulo2)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            dataSolar = []
            dataElectrica = []
            for i in self.objEdificio.datosIniciales.contribuciones.listado:
                a31 = Paragraph(u'%s' % i.nombre, self.tabla1Contenidos)
                if i.porcCal != '':
                    try:
                        porcCal = float(i.porcCal)
                    except:
                        logging.info(u'Excepcion en: %s' % __name__)
                        porcCal = 0.0

                else:
                    porcCal = 0.0
                if i.porcRef != '':
                    try:
                        porcRef = float(i.porcRef)
                    except:
                        logging.info(u'Excepcion en: %s' % __name__)
                        porcRef = 0.0

                else:
                    porcRef = 0.0
                if i.porcACS != '':
                    try:
                        porcACS = float(i.porcACS)
                    except:
                        logging.info(u'Excepcion en: %s' % __name__)
                        porcACS = 0.0

                else:
                    porcACS = 0.0
                if i.electricidadGen != '':
                    try:
                        electricidadGen = float(i.electricidadGen)
                    except:
                        logging.info(u'Excepcion en: %s' % __name__)
                        electricidadGen = 0.0

                else:
                    electricidadGen = 0.0
                if porcCal > 0.0 or porcRef > 0.0 or porcACS > 0:
                    if porcCal > 0.0:
                        a32 = Paragraph(u'%s' % porcCal, self.tabla1ContenidosC)
                    else:
                        a32 = Paragraph(u'-', self.tabla1ContenidosC)
                    if porcRef > 0.0:
                        a33 = Paragraph(u'%s' % porcRef, self.tabla1ContenidosC)
                    else:
                        a33 = Paragraph(u'-', self.tabla1ContenidosC)
                    if porcACS > 0.0:
                        a34 = Paragraph(u'%s' % porcACS, self.tabla1ContenidosC)
                    else:
                        a34 = Paragraph(u'-', self.tabla1ContenidosC)
                    demandaACS = u'-'
                    a35 = Paragraph(u'%s' % demandaACS, self.tabla1ContenidosC)
                    dataSolar.append([a31,
                     a32,
                     a33,
                     a34,
                     a35])
                if electricidadGen > 0:
                    a21 = Paragraph(u'%s' % i.nombre, self.tabla1Contenidos)
                    a22 = Paragraph(u'%s' % electricidadGen, self.tabla1ContenidosC)
                    dataElectrica.append([a21, a22])

            if len(dataSolar) > 0:
                t = Paragraph(_(u'T\xe9rmica'), self.titulo2)
                Story.append(t)
                Story.append(Spacer(0, 0.4 * cm))
                a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
                a12 = Paragraph(_(u'Consumo de Energ\xeda Final, cubierto en funci\xf3n del servicio asociado [%]'), self.tabla1ContenidosNC)
                a13 = Paragraph(_(u'Demanda de ACS cubierta [%]'), self.tabla1ContenidosNC)
                a21 = u''
                a22 = Paragraph(_(u'Calefacci\xf3n'), self.tabla1ContenidosNC)
                a23 = Paragraph(_(u'Refrigeraci\xf3n'), self.tabla1ContenidosNC)
                a24 = Paragraph(_(u'ACS'), self.tabla1ContenidosNC)
                data = [[a11,
                  a12,
                  u'',
                  u'',
                  a13], [a21,
                  a22,
                  a23,
                  a24,
                  u'']]
                t = Table(data, [5.37 * cm,
                 4.54 * cm,
                 2.82 * cm,
                 2.5 * cm,
                 2.77 * cm], None, None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'),
                 ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'),
                 ('SPAN', (0, 0), (0, -1)),
                 ('SPAN', (1, 0), (-2, 0)),
                 ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black),
                 ('BACKGROUND',
                  (0, 0),
                  (-1, -1),
                  self.rosa)]))
                Story.append(t)
                t = Table(dataSolar, [5.37 * cm,
                 4.54 * cm,
                 2.82 * cm,
                 2.5 * cm,
                 2.77 * cm], None, None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'), ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'), ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black)]))
                Story.append(t)
                totalCal = self.objEdificio.datosIniciales.contribuciones.porcCalTotal
                totalRef = self.objEdificio.datosIniciales.contribuciones.porcRefTotal
                totalACS = self.objEdificio.datosIniciales.contribuciones.porcACSTotal
                a11 = Paragraph(_(u'TOTAL'), self.tabla1ContenidosNC)
                if totalCal != u'' and totalCal > 0.0:
                    a12 = Paragraph(u'%s' % totalCal, self.tabla1ContenidosC)
                else:
                    a12 = Paragraph(u'-', self.tabla1ContenidosC)
                if totalRef != u'' and totalRef > 0.0:
                    a13 = Paragraph(u'%s' % totalRef, self.tabla1ContenidosC)
                else:
                    a13 = Paragraph(u'-', self.tabla1ContenidosC)
                if totalACS != u'' and totalACS > 0.0:
                    a14 = Paragraph(u'%s' % totalACS, self.tabla1ContenidosC)
                else:
                    a14 = Paragraph(u'-', self.tabla1ContenidosC)
                totalDemandaACS = u'-'
                a15 = Paragraph(u'%s' % totalDemandaACS, self.tabla1ContenidosC)
                data = [[a11,
                  a12,
                  a13,
                  a14,
                  a15]]
                t = Table(data, [5.37 * cm,
                 4.54 * cm,
                 2.82 * cm,
                 2.5 * cm,
                 2.77 * cm], [0.5 * cm], None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'),
                 ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'),
                 ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black),
                 ('BACKGROUND',
                  (0, 0),
                  (-1, 0),
                  self.naranja)]))
                Story.append(t)
                Story.append(Spacer(0, 0.4 * cm))
            if len(dataElectrica) > 0:
                t = Paragraph(_(u'El\xe9ctrica'), self.titulo2)
                Story.append(t)
                Story.append(Spacer(0, 0.4 * cm))
                a11 = Paragraph(_(u'Nombre'), self.tabla1ContenidosNC)
                a12 = Paragraph(_(u' Energ\xeda el\xe9ctrica generada y autoconsumida [kWh/a\xf1o]'), self.tabla1ContenidosNC)
                data = [[a11, a12]]
                t = Table(data, [6.19 * cm, 6.39 * cm], None, None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'),
                 ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'),
                 ('SPAN', (0, 0), (0, -1)),
                 ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black),
                 ('BACKGROUND',
                  (0, 0),
                  (-1, -1),
                  self.rosa)]))
                Story.append(t)
                t = Table(dataElectrica, [6.19 * cm, 6.39 * cm], None, None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'), ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'), ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black)]))
                Story.append(t)
                if len(self.objEdificio.datosIniciales.contribuciones.listado) > 0.0:
                    totalDemandaCubierto = self.objEdificio.datosIniciales.contribuciones.electricidadGenTotal
                else:
                    totalDemandaCubierto = u''
                a11 = Paragraph(_(u'TOTAL'), self.tabla1ContenidosNC)
                a12 = Paragraph(u'%s' % totalDemandaCubierto, self.tabla1ContenidosC)
                data = [[a11, a12]]
                t = Table(data, [6.19 * cm, 6.39 * cm], [0.5 * cm], None, 1, 1, 1, hAlign='LEFT')
                t.setStyle(TableStyle([('VALIGN',
                  (0, 0),
                  (-1, -1),
                  'MIDDLE'),
                 ('ALIGN',
                  (0, 0),
                  (-1, -1),
                  'CENTER'),
                 ('GRID',
                  (0, 0),
                  (-1, -1),
                  0.5,
                  colors.black),
                 ('BACKGROUND',
                  (0, 0),
                  (-1, 0),
                  self.naranja)]))
                Story.append(t)
        return Story

    def anexo2(self):
        Story = []
        t = Paragraph(_(u'ANEXO II'), self.titulo1)
        Story.append(t)
        t = Paragraph(_(u'CALIFICACI\xd3N ENERG\xc9TICA DEL EDIFICIO'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        Story += self.tablaAnexo2ZonaClimatica()
        Story.append(Spacer(0, 0.6 * cm))
        Story += self.tablaAnexo2Aptdo1()
        Story.append(Spacer(0, 0.7 * cm))
        Story += self.tablaAnexo2Aptdo2()
        Story.append(Spacer(0, 0.7 * cm))
        Story += self.tablaAnexo2Aptdo3()
        Story.append(Spacer(0, 0.2 * cm))
        d = Drawing(1, 1)
        d.add(Line(0, 0, 150, 0))
        Story.append(d)
        Story.append(Spacer(0, 0.1 * cm))
        textoPiePagina = _(u'\xb9El indicador global es resultado de la suma de los indicadores parciales \nm\xe1s el valor del indicador para consumos auxiliares, si los hubiera \n(s\xf3lo ed. terciarios, ventilaci\xf3n, bombeo, etc\u2026). La energ\xeda el\xe9ctrica autoconsumida se descuenta \n\xfanicamente del indicador global, no as\xed de los valores parciales')
        textoPiePaginaParagraph = Paragraph(textoPiePagina, self.tablaContenidosNotaPie)
        Story.append(textoPiePaginaParagraph)
        return Story

    def tablaAnexo2ZonaClimatica(self):
        Story = []
        a11 = Paragraph(_(u'Zona clim\xe1tica'), self.tabla1ContenidosN)
        a12 = Paragraph(self.objEdificio.datosIniciales.zonaHE1, self.tabla1Contenidos)
        if self.objEdificio.programa == 'Residencial':
            usoEdificio = self.objEdificio.programa
        else:
            usoEdificio = self.objEdificio.datosIniciales.tipoEdificio
        a13 = Paragraph(_(u'Uso'), self.tabla1ContenidosN)
        a14 = Paragraph(_(usoEdificio), self.tabla1Contenidos)
        data = [[a11,
          a12,
          a13,
          a14]]
        t = Table(data, [4.5 * cm,
         4.5 * cm,
         4.5 * cm,
         4.5 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (0, 0),
          self.rosa),
         ('BACKGROUND',
          (2, 0),
          (2, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        return Story

    def tablaAnexo2Aptdo1(self):
        Story = []
        t = Paragraph(_(u'1.\tCALIFICACI\xd3N ENERG\xc9TICA DEL EDIFICIO EN EMISIONES'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.3 * cm))
        a11 = Paragraph(_(u'INDICADOR GLOBAL'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'INDICADORES PARCIALES'), self.tabla1ContenidosNC)
        data = [[a11, a12]]
        t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (3, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        imagen = Etiqueta(str(self.objEdificio.datosResultados.emisiones_nota), str(round(self.objEdificio.datosResultados.emisionesMostrar, 1)), self.objEdificio.datosResultados.emisiones_limites)
        imagen.scaleX = 0.95
        imagen.scaleY = 0.95
        imagen.translateX = 0.0 * cm
        imagen.translateY = 1.15 * cm
        a12 = Paragraph(u'%0.2f %s' % (self.objEdificio.datosResultados.emisionesMostrar, self.objEdificio.datosResultados.emisiones_nota), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'CALEFACCI\xd3N'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'ACS'), self.tabla1ContenidosNC)
        a33 = Paragraph(_(u'<i>Emisiones calefacci\xf3n [kgCO2/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a351 = Paragraph(_(u'<i>Emisiones ACS</i>'), self.tabla1ContenidosC)
        a352 = Paragraph(_(u'<i>[kgCO2/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a53 = Paragraph(_(u'REFRIGERACI\xd3N'), self.tabla1ContenidosNC)
        a55 = Paragraph(_(u'ILUMINACI\xd3N'), self.tabla1ContenidosNC)
        a71 = Paragraph(_(u'<i>Emisiones globales [kgCO2/m\xb2 a\xf1o]\xb9</i>'), self.tabla1ContenidosC)
        a73 = Paragraph(_(u'<i>Emisiones refrigeraci\xf3n [kgCO2/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a75 = Paragraph(_(u'<i>Emisiones iluminaci\xf3n [kgCO2/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a24 = Paragraph(self.objEdificio.datosResultados.emisionesCal_nota, self.tabla1ContenidosNC)
        a26 = Paragraph(self.objEdificio.datosResultados.emisionesACS_nota, self.tabla1ContenidosNC)
        a43 = Paragraph('%0.2f' % self.objEdificio.datosResultados.emisionesCal, self.tabla1ContenidosNC)
        a45 = Paragraph('%0.2f' % self.objEdificio.datosResultados.emisionesACS, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            a64 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a64 = Paragraph(self.objEdificio.datosResultados.emisionesRef_nota, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial':
            a66 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a66 = Paragraph(self.objEdificio.datosResultados.emisionesIlum_nota, self.tabla1ContenidosNC)
        a81 = Paragraph('%0.2f' % self.objEdificio.datosResultados.emisionesMostrar, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            a83 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a83 = Paragraph('%0.2f' % self.objEdificio.datosResultados.emisionesRef, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial':
            a85 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a85 = Paragraph('%0.2f' % self.objEdificio.datosResultados.emisionesIlum, self.tabla1ContenidosNC)
        data = [[imagen,
          '',
          a13,
          '',
          a15,
          ''],
         ['',
          '',
          '',
          '',
          '',
          ''],
         ['',
          '',
          a33,
          a24,
          [a351, a352],
          a26],
         ['',
          '',
          a43,
          '',
          a45,
          ''],
         ['',
          '',
          a53,
          '',
          a55,
          ''],
         ['',
          '',
          '',
          '',
          '',
          ''],
         [a71,
          '',
          a73,
          a64,
          a75,
          a66],
         ['',
          '',
          a83,
          '',
          a85,
          '']]
        t = Table(data, [5.73 * cm,
         3.27 * cm,
         3.6 * cm,
         0.9 * cm,
         3.71 * cm,
         0.8 * cm], [0.5 * cm,
         0.5 * cm,
         1 * cm,
         0.5 * cm,
         0.5 * cm,
         0.5 * cm,
         1 * cm,
         0.5 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('SPAN', (0, 0), (0, 5)),
         ('SPAN', (1, 0), (1, 5)),
         ('SPAN', (2, 0), (3, 1)),
         ('SPAN', (4, 0), (5, 1)),
         ('BACKGROUND',
          (2, 0),
          (5, 1),
          self.rosa),
         ('SPAN', (3, 2), (3, 3)),
         ('SPAN', (5, 2), (5, 3)),
         ('SPAN', (3, 6), (3, 7)),
         ('SPAN', (5, 6), (5, 7)),
         ('SPAN', (2, 4), (3, 5)),
         ('SPAN', (4, 4), (5, 5)),
         ('BACKGROUND',
          (2, 4),
          (5, 5),
          self.rosa),
         ('SPAN', (0, 6), (1, 7)),
         ('SPAN', (0, 6), (1, 7))]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        t = Paragraph(_(u'La calificaci\xf3n global del edificio se expresa en t\xe9rminos de di\xf3xido de carbono liberado                         a la atm\xf3sfera como consecuencia del consumo energ\xe9tico del mismo.'), self.tabla1Contenidos)
        Story.append(t)
        Story.append(Spacer(0, 0.2 * cm))
        emisionesConsumoElectricoM2 = self.objEdificio.datosResultados.emisionesMostrar_Electricidad
        emisionesCombustiblesFosilesM2 = self.objEdificio.datosResultados.emisiones_GasNatural + self.objEdificio.datosResultados.emisiones_Gasoil + self.objEdificio.datosResultados.emisiones_GLP + self.objEdificio.datosResultados.emisiones_Carbon + self.objEdificio.datosResultados.emisiones_Biocarburante + self.objEdificio.datosResultados.emisiones_BiomasaNoDens + self.objEdificio.datosResultados.emisiones_BiomasaDens
        emisionesConsumoElectrico = emisionesConsumoElectricoM2 * self.objEdificio.datosIniciales.area
        emisionesCombustiblesFosiles = emisionesCombustiblesFosilesM2 * self.objEdificio.datosIniciales.area
        a12 = Paragraph(_(u'kgCO2/m\xb2 a\xf1o'), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u' kgCO2/a\xf1o'), self.tabla1ContenidosNC)
        a21 = Paragraph(_(u' <i>Emisiones CO2 por consumo el\xe9ctrico</i>'), self.tabla1ContenidosC)
        a22 = Paragraph('%0.2f' % emisionesConsumoElectricoM2, self.tabla1ContenidosC)
        a23 = Paragraph('%0.2f' % emisionesConsumoElectrico, self.tabla1ContenidosC)
        a31 = Paragraph(_(u' <i>Emisiones CO2 por otros combustibles</i>'), self.tabla1ContenidosC)
        a32 = Paragraph('%0.2f' % emisionesCombustiblesFosilesM2, self.tabla1ContenidosC)
        a33 = Paragraph('%0.2f' % emisionesCombustiblesFosiles, self.tabla1ContenidosC)
        data = [['', a12, a13], [a21, a22, a23], [a31, a32, a33]]
        t = Table(data, [7.8 * cm, 2.75 * cm, 2.36 * cm], None, None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('ALIGN',
          (0, 0),
          (-1, -1),
          'CENTER'),
         ('GRID',
          (0, 1),
          (2, -1),
          0.5,
          colors.black),
         ('GRID',
          (1, 0),
          (2, -1),
          0.5,
          colors.black),
         ('BACKGROUND',
          (0, 1),
          (0, 2),
          self.rosa),
         ('BACKGROUND',
          (1, 0),
          (2, 0),
          self.rosa)]))
        Story.append(t)
        return Story

    def tablaAnexo2Aptdo2(self):
        Story = []
        t = Paragraph(_(u'2.    CALIFICACI\xd3N ENERG\xc9TICA DEL EDIFICIO EN CONSUMO DE ENERG\xcdA PRIMARIA NO RENOVABLE'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.3 * cm))
        t = Paragraph(_(u'Por energ\xeda primaria no renovable se entiende la energ\xeda consumida por el                         edificio procedente de fuentes no renovables que                         no ha sufrido ning\xfan proceso de conversi\xf3n o transformaci\xf3n.'), self.tabla1Contenidos)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        a11 = Paragraph(_(u'INDICADOR GLOBAL'), self.tabla1ContenidosNC)
        a12 = Paragraph(_(u'INDICADORES PARCIALES'), self.tabla1ContenidosNC)
        data = [[a11, a12]]
        t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BACKGROUND',
          (0, 0),
          (3, 0),
          self.rosa),
         ('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        imagen = Etiqueta(str(self.objEdificio.datosResultados.enPrimNoRen_nota), str(round(self.objEdificio.datosResultados.enPrimNoRenMostrar, 1)), self.objEdificio.datosResultados.enPrimNoRen_limites)
        imagen.scaleX = 0.95
        imagen.scaleY = 0.95
        imagen.translateX = 0.3 * cm
        imagen.translateY = 1.15 * cm
        a12 = Paragraph(u'%0.2f %s' % (self.objEdificio.datosResultados.enPrimNoRenMostrar, self.objEdificio.datosResultados.enPrimNoRen_nota), self.tabla1ContenidosNC)
        a13 = Paragraph(_(u'CALEFACCI\xd3N'), self.tabla1ContenidosNC)
        a15 = Paragraph(_(u'ACS'), self.tabla1ContenidosNC)
        a33 = Paragraph(_(u'<i>Energ\xeda primaria calefacci\xf3n [kWh/m\xb2a\xf1o]</i>'), self.tabla1ContenidosC)
        a351 = Paragraph(_(u'<i>Energ\xeda primaria ACS</i>'), self.tabla1ContenidosC)
        a352 = Paragraph(_(u'<i>[kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a53 = Paragraph(_(u'REFRIGERACI\xd3N'), self.tabla1ContenidosNC)
        a55 = Paragraph(_(u'ILUMINACI\xd3N'), self.tabla1ContenidosNC)
        a71 = Paragraph(_(u'<i>Consumo global de energ\xeda primaria no renovable [kWh/m\xb2 a\xf1o]\xb9</i>'), self.tabla1ContenidosC)
        a73 = Paragraph(_(u'<i>Energ\xeda primaria refrigeraci\xf3n [kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
        a75 = Paragraph(_(u'<i>Energ\xeda primaria iluminaci\xf3n [kWh/m\xb2a\xf1o]</i>'), self.tabla1ContenidosC)
        a24 = Paragraph(self.objEdificio.datosResultados.enPrimNoRenCal_nota, self.tabla1ContenidosNC)
        a26 = Paragraph(self.objEdificio.datosResultados.enPrimNoRenACS_nota, self.tabla1ContenidosNC)
        a43 = Paragraph('%0.2f' % self.objEdificio.datosResultados.enPrimNoRenCal, self.tabla1ContenidosNC)
        a45 = Paragraph('%0.2f' % self.objEdificio.datosResultados.enPrimNoRenACS, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            a64 = Paragraph('-', self.tabla1ContenidosNC)
            a83 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a64 = Paragraph(self.objEdificio.datosResultados.enPrimNoRenRef_nota, self.tabla1ContenidosNC)
            a83 = Paragraph('%0.2f' % self.objEdificio.datosResultados.enPrimNoRenRef, self.tabla1ContenidosNC)
        if self.objEdificio.programa == 'Residencial':
            a66 = Paragraph('-', self.tabla1ContenidosNC)
            a85 = Paragraph('-', self.tabla1ContenidosNC)
        else:
            a66 = Paragraph(self.objEdificio.datosResultados.enPrimNoRenIlum_nota, self.tabla1ContenidosNC)
            a85 = Paragraph('%0.2f' % self.objEdificio.datosResultados.enPrimNoRenIlum, self.tabla1ContenidosNC)
        a81 = Paragraph('%0.2f' % self.objEdificio.datosResultados.enPrimNoRenMostrar, self.tabla1ContenidosNC)
        data = [[imagen,
          '',
          a13,
          '',
          a15,
          ''],
         ['',
          '',
          '',
          '',
          '',
          ''],
         ['',
          '',
          a33,
          a24,
          [a351, a352],
          a26],
         ['',
          '',
          a43,
          '',
          a45,
          ''],
         ['',
          '',
          a53,
          '',
          a55,
          ''],
         ['',
          '',
          '',
          '',
          '',
          ''],
         [a71,
          '',
          a73,
          a64,
          a75,
          a66],
         ['',
          '',
          a83,
          '',
          a85,
          '']]
        t = Table(data, [5.73 * cm,
         3.27 * cm,
         3.6 * cm,
         0.9 * cm,
         3.71 * cm,
         0.8 * cm], [0.5 * cm,
         0.5 * cm,
         1 * cm,
         0.5 * cm,
         0.5 * cm,
         0.5 * cm,
         1 * cm,
         0.5 * cm], None, 1, 1, 1)
        t.setStyle(TableStyle([('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('SPAN', (0, 0), (0, 5)),
         ('SPAN', (1, 0), (1, 5)),
         ('SPAN', (2, 0), (3, 1)),
         ('SPAN', (4, 0), (5, 1)),
         ('BACKGROUND',
          (2, 0),
          (5, 1),
          self.rosa),
         ('SPAN', (3, 2), (3, 3)),
         ('SPAN', (5, 2), (5, 3)),
         ('SPAN', (3, 6), (3, 7)),
         ('SPAN', (5, 6), (5, 7)),
         ('SPAN', (2, 4), (3, 5)),
         ('SPAN', (4, 4), (5, 5)),
         ('BACKGROUND',
          (2, 4),
          (5, 5),
          self.rosa),
         ('SPAN', (0, 6), (1, 7)),
         ('SPAN', (0, 6), (1, 7))]))
        Story.append(t)
        return Story

    def tablaAnexo2Aptdo3(self):
        Story = []
        t = Paragraph(_(u'3.\tCALIFICACI\xd3N PARCIAL DE LA DEMANDA ENERG\xc9TICA DE CALEFACCI\xd3N Y REFRIGERACI\xd3N'), self.titulo2)
        Story.append(t)
        Story.append(Spacer(0, 0.3 * cm))
        t = Paragraph(_(u'La demanda energ\xe9tica de calefacci\xf3n y refrigeraci\xf3n es la energ\xeda necesaria                         para mantener las condiciones internas de confort del edificio.'), self.tabla1Contenidos)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
            imagenDdaCal = Etiqueta(self.objEdificio.datosResultados.ddaBrutaCal_nota, str(round(self.objEdificio.datosResultados.ddaBrutaCal, 1)), self.objEdificio.datosResultados.ddaBrutaCal_limites)
            imagenDdaCal.scaleX = 0.95
            imagenDdaCal.scaleY = 0.95
            imagenDdaCal.translateX = 0.3 * cm
            imagenDdaCal.translateY = 1.15 * cm
            a11 = Paragraph(_(u'DEMANDA DE CALEFACCI\xd3N'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'DEMANDA DE REFRIGERACI\xd3N'), self.tabla1ContenidosNC)
            data = [[a11, a12]]
            t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (-1, -1),
              self.rosa),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            a14 = Paragraph(u'No calificable', self.tabla1ContenidosNC)
            data = [[imagenDdaCal, '', a14]]
            t = Table(data, [5.73 * cm, 3.27 * cm, 9.0 * cm], [3.2 * cm], None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            a11 = Paragraph(_(u'<i>Demanda de calefacci\xf3n [kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
            a12 = Paragraph(_(u'<i>Demanda de refrigeraci\xf3n [kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
            data = [[a11, a12]]
            t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
        else:
            imagenDdaCal = Etiqueta(self.objEdificio.datosResultados.ddaBrutaCal_nota, str(round(self.objEdificio.datosResultados.ddaBrutaCal, 1)), self.objEdificio.datosResultados.ddaBrutaCal_limites)
            imagenDdaCal.scaleX = 0.95
            imagenDdaCal.scaleY = 0.95
            imagenDdaCal.translateX = 0.3 * cm
            imagenDdaCal.translateY = 1.15 * cm
            imagenDdaRef = Etiqueta(self.objEdificio.datosResultados.ddaBrutaRef_nota, str(round(self.objEdificio.datosResultados.ddaBrutaRef, 1)), self.objEdificio.datosResultados.ddaBrutaRef_limites)
            imagenDdaRef.scaleX = 0.95
            imagenDdaRef.scaleY = 0.95
            imagenDdaRef.translateX = 0.3 * cm
            imagenDdaRef.translateY = 1.15 * cm
            a11 = Paragraph(_(u'DEMANDA DE CALEFACCI\xd3N'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'DEMANDA DE REFRIGERACI\xd3N'), self.tabla1ContenidosNC)
            data = [[a11, a12]]
            t = Table(data, [9.0 * cm, 9.0 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (-1, -1),
              self.rosa),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            data = [[imagenDdaCal,
              '',
              imagenDdaRef,
              '']]
            t = Table(data, [5.73 * cm,
             3.27 * cm,
             5.73 * cm,
             3.27 * cm], [3.2 * cm], None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            a11 = Paragraph(_(u'<i>Demanda de calefacci\xf3n [kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
            a12 = Paragraph(_(u'<i>Demanda de refrigeraci\xf3n [kWh/m\xb2 a\xf1o]</i>'), self.tabla1ContenidosC)
            data = [[a11, a12]]
            t = Table(data, [9.0 * cm, 9.0 * cm], [0.5 * cm], None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
        return Story

    def anexo3(self):
        Story = []
        t = Paragraph(_(u'ANEXO III'), self.titulo1)
        Story.append(t)
        t = Paragraph(_(u'RECOMENDACIONES PARA LA MEJORA DE LA EFICIENCIA ENERG\xc9TICA'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        if self.listadoConjuntosMMUsuario == []:
            t = Paragraph(_(u'Apartado no definido'), self.titulo1)
            Story.append(t)
            Story.append(CondPageBreak(27.2 * cm))
        for conjuntoMM in self.listadoConjuntosMMUsuario:
            a0 = Paragraph(unicode(conjuntoMM.nombre), self.tabla1ContenidosN)
            data = [[a0]]
            t = Table(data, [18 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BOX',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('BACKGROUND',
              (0, 0),
              (-1, -1),
              self.rosa)]))
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            t = Paragraph(_(u'CALIFICACI\xd3N ENERG\xc9TICA GLOBAL'), self.titulo3)
            Story.append(t)
            a11 = Paragraph(_(u'CONSUMO DE ENERG\xcdA'), self.tabla1ContenidosNC)
            a21 = Paragraph(_(u'PRIMARIA NO RENOVABLE'), self.tabla1ContenidosNC)
            a31 = Paragraph(_(u'[kWh/m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'EMISIONES DE DI\xd3XIDO DE'), self.tabla1ContenidosNC)
            a22 = Paragraph(_(u' CARBONO'), self.tabla1ContenidosNC)
            a32 = Paragraph(_(u'[kgCO2/ m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
            data = [[a11, a12], [a21, a22], [a31, a32]]
            t = Table(data, [6 * cm, 6 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (-1, -1),
              self.rosa),
             ('BOX',
              (0, 0),
              (0, -1),
              0.5,
              colors.black),
             ('BOX',
              (1, 0),
              (1, -1),
              0.5,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            imagenEmisiones = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, 1)), conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_limites)
            imagenEmisiones.scaleX = 0.95
            imagenEmisiones.scaleY = 0.95
            imagenEmisiones.translateX = 0.3 * cm
            imagenEmisiones.translateY = 1.15 * cm
            imagenEmisiones.punto = 4.5
            imagenConsumo = Etiqueta(str(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_nota), str(round(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, 1)), conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_limites)
            imagenConsumo.scaleX = 0.95
            imagenConsumo.scaleY = 0.95
            imagenConsumo.translateX = 0.3 * cm
            imagenConsumo.translateY = 1.15 * cm
            imagenConsumo.punto = 4.5
            data = [[imagenConsumo,
              '',
              imagenEmisiones,
              '']]
            t = Table(data, [3.7 * cm,
             2.3 * cm,
             3.7 * cm,
             2.3 * cm], [3.1 * cm], None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            t = Paragraph(_(u'CALIFICACIONES ENERG\xc9TICAS PARCIALES'), self.titulo3)
            Story.append(t)
            a11 = Paragraph(_(u'DEMANDA DE CALEFACCI\xd3N [kWh/m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
            a12 = Paragraph(_(u'DEMANDA DE REFRIGERACI\xd3N [kWh/m\xb2 a\xf1o]'), self.tabla1ContenidosNC)
            data = [[a11, a12]]
            t = Table(data, [6.0 * cm, 6.0 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (-1, -1),
              self.rosa),
             ('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            imagenCalefaccion = Etiqueta(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota, '%0.1f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal, conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_limites)
            imagenCalefaccion.scaleX = 0.95
            imagenCalefaccion.scaleY = 0.95
            imagenCalefaccion.translateX = 0.3 * cm
            imagenCalefaccion.translateY = 1.15 * cm
            imagenCalefaccion.punto = 4.5
            imagenRefrigeracion = Etiqueta(conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota, '%0.1f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef, conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_limites)
            imagenRefrigeracion.scaleX = 0.95
            imagenRefrigeracion.scaleY = 0.95
            imagenRefrigeracion.translateX = 0.3 * cm
            imagenRefrigeracion.translateY = 1.15 * cm
            imagenRefrigeracion.punto = 4.5
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                aref = Paragraph(u'No calificable', self.tabla1ContenidosNC)
                data = [[imagenCalefaccion, aref]]
                t = Table(data, [6.0 * cm, 6.0 * cm], [3.1 * cm], None, 1, 1, 1)
            else:
                data = [[imagenCalefaccion,
                  '',
                  imagenRefrigeracion,
                  '']]
                t = Table(data, [3.7 * cm,
                 2.3 * cm,
                 3.7 * cm,
                 2.3 * cm], [3.1 * cm], None, 1, 1, 1)
            t.setStyle(TableStyle([('GRID',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            Story.append(Spacer(0, 0.5 * cm))
            t = Paragraph(_(u'AN\xc1LISIS T\xc9CNICO'), self.titulo2)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            a11 = Paragraph(_(u'Indicador'), self.titulo3)
            a12 = Paragraph(_(u'Calefacci\xf3n'), self.titulo3)
            a13 = ''
            a14 = ''
            a15 = Paragraph(_(u'Refrigeraci\xf3n'), self.titulo3)
            a16 = ''
            a17 = ''
            a18 = Paragraph(_(u'ACS'), self.titulo3)
            a19 = ''
            a110 = ''
            a111 = Paragraph(_(u'Iluminaci\xf3n'), self.titulo3)
            a112 = ''
            a113 = ''
            a114 = Paragraph(_(u'Total'), self.titulo3)
            a115 = ''
            a116 = ''
            a21 = ''
            a22 = Paragraph(_(u'Valor'), self.tabla2Contenidos)
            a23 = ''
            a24 = Paragraph(_(u'ahorro respecto a la situaci\xf3n original'), self.tabla4Contenidos)
            a25 = Paragraph(_(u'Valor'), self.tabla2Contenidos)
            a26 = ''
            a27 = Paragraph(_(u'ahorro respecto a la situaci\xf3n original'), self.tabla4Contenidos)
            a28 = Paragraph(_(u'Valor'), self.tabla2Contenidos)
            a29 = ''
            a210 = Paragraph(_(u'ahorro respecto a la situaci\xf3n original'), self.tabla4Contenidos)
            a211 = Paragraph(_(u'Valor'), self.tabla2Contenidos)
            a212 = ''
            a213 = Paragraph(_(u'ahorro respecto a la situaci\xf3n original'), self.tabla4Contenidos)
            a214 = Paragraph(_(u'Valor'), self.tabla2Contenidos)
            a215 = ''
            a216 = Paragraph(_(u'ahorro respecto a la situaci\xf3n original'), self.tabla4Contenidos)
            porcAhorroEnPrimNoRenCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                porcAhorroEnPrimNoRenRef = '-'
            else:
                porcAhorroEnPrimNoRenRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef)
            porcAhorroEnPrimNoRenACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS)
            if self.objEdificio.programa == 'Residencial':
                porcAhorroEnPrimNoRenIlum = '-'
            else:
                porcAhorroEnPrimNoRenIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum)
            porcAhorroEnPrimNoRen = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enPrimNoRenMostrar, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar)
            a31 = Paragraph(_(u'Consumo Energ\xeda primaria no renovable [kWh/m\xb2 a\xf1o]'), self.tabla2Contenidos)
            a32 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal, self.tabla3ContenidosC)
            a33 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenCal_nota, self.tabla2ContenidosC)
            a34 = Paragraph(u'%s %s' % (porcAhorroEnPrimNoRenCal, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                a35 = Paragraph('-', self.tabla2ContenidosC)
                a36 = Paragraph('-', self.tabla2ContenidosC)
            else:
                a35 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef, self.tabla3ContenidosC)
                a36 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenRef_nota, self.tabla2ContenidosC)
            a37 = Paragraph(u'%s %s' % (porcAhorroEnPrimNoRenRef, u'%'), self.tabla3ContenidosC)
            a38 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS, self.tabla3ContenidosC)
            a39 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenACS_nota, self.tabla2ContenidosC)
            a310 = Paragraph(u'%s %s' % (porcAhorroEnPrimNoRenACS, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa != 'Residencial':
                a311 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum, self.tabla3ContenidosC)
                a312 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenIlum_nota, self.tabla2ContenidosC)
            else:
                a311 = Paragraph('-', self.tabla2ContenidosC)
                a312 = Paragraph('-', self.tabla2ContenidosC)
            a313 = Paragraph(u'%s %s' % (porcAhorroEnPrimNoRenIlum, u'%'), self.tabla3ContenidosC)
            a314 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRenMostrar, self.tabla3ContenidosC)
            a315 = Paragraph(conjuntoMM.datosNuevoEdificio.datosResultados.enPrimNoRen_nota, self.tabla2ContenidosC)
            a316 = Paragraph(u'%s %s' % (porcAhorroEnPrimNoRen, u'%'), self.tabla3ContenidosC)
            porcAhorroEnFinalCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalCal)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                porcAhorroEnFinalRef = '-'
            else:
                porcAhorroEnFinalRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRef)
            porcAhorroEnFinalACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalACS)
            if self.objEdificio.programa == 'Residencial':
                porcAhorroEnFinalIlum = '-'
            else:
                porcAhorroEnFinalIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinalIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinalIlum)
            porcAhorroEnFinal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.enFinal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.enFinal)
            a41 = Paragraph(_(u'Consumo Energ\xeda final [kWh/m\xb2 a\xf1o]'), self.tabla2Contenidos)
            a42 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalCal, self.tabla3ContenidosC)
            a43 = u''
            a44 = Paragraph('%s %s' % (porcAhorroEnFinalCal, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                a45 = Paragraph('-', self.tabla2ContenidosC)
                a46 = u''
            else:
                a45 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalRef, self.tabla3ContenidosC)
                a46 = u''
            a47 = Paragraph('%s %s' % (porcAhorroEnFinalRef, u'%'), self.tabla3ContenidosC)
            a48 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalACS, self.tabla3ContenidosC)
            a49 = u''
            a410 = Paragraph('%s %s' % (porcAhorroEnFinalACS, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial':
                a411 = Paragraph('-', self.tabla2ContenidosC)
                a412 = u''
            else:
                a411 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinalIlum, self.tabla3ContenidosC)
                a412 = u''
            a413 = Paragraph('%s %s' % (porcAhorroEnFinalIlum, u'%'), self.tabla3ContenidosC)
            a414 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.enFinal, self.tabla3ContenidosC)
            a415 = u''
            a416 = Paragraph('%s %s' % (porcAhorroEnFinal, u'%'), self.tabla3ContenidosC)
            porcAhorroEmisionesCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                porcAhorroEmisionesRef = '-'
            else:
                porcAhorroEmisionesRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef)
            porcAhorroEmisionesACS = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesACS, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS)
            if self.objEdificio.programa == 'Residencial':
                porcAhorroEmisionesIlum = '-'
            else:
                porcAhorroEmisionesIlum = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesIlum, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum)
            porcAhorroEmisiones = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.emisionesMostrar, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar)
            a51 = Paragraph(_(u'Emisiones de CO2 [kgCO2/m\xb2 a\xf1o]'), self.tabla2Contenidos)
            a52 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal, self.tabla3ContenidosC)
            a53 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesCal_nota, self.tabla2ContenidosC)
            a54 = Paragraph(u'%s %s' % (porcAhorroEmisionesCal, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                a55 = Paragraph('-', self.tabla2ContenidosC)
                a56 = Paragraph('-', self.tabla2ContenidosC)
            else:
                a55 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef, self.tabla3ContenidosC)
                a56 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesRef_nota, self.tabla2ContenidosC)
            a57 = Paragraph(u'%s %s' % (porcAhorroEmisionesRef, u'%'), self.tabla3ContenidosC)
            a58 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS, self.tabla3ContenidosC)
            a59 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesACS_nota, self.tabla2ContenidosC)
            a510 = Paragraph(u'%s %s' % (porcAhorroEmisionesACS, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial':
                a511 = Paragraph('-', self.tabla2ContenidosC)
                a512 = Paragraph('-', self.tabla2ContenidosC)
            else:
                a511 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum, self.tabla3ContenidosC)
                a512 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesIlum_nota, self.tabla2ContenidosC)
            a513 = Paragraph(u'%s %s' % (porcAhorroEmisionesIlum, u'%'), self.tabla3ContenidosC)
            a514 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.emisionesMostrar, self.tabla3ContenidosC)
            a515 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.emisiones_nota, self.tabla2ContenidosC)
            a516 = Paragraph(u'%s %s' % (porcAhorroEmisiones, u'%'), self.tabla3ContenidosC)
            porcAhorroDdaCal = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.ddaBrutaCal, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                porcAhorroDdaRef = '-'
            else:
                porcAhorroDdaRef = calculoPorcAhorro(valorEdificioObjeto=self.objEdificio.datosResultados.ddaBrutaRef, valorConjuntoMM=conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef)
            a61 = Paragraph(_(u'Demanda [kWh/m\xb2 a\xf1o]'), self.tabla2Contenidos)
            a62 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal, self.tabla3ContenidosC)
            a63 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaCal_nota, self.tabla2ContenidosC)
            a64 = Paragraph(u'%s %s' % (porcAhorroDdaCal, u'%'), self.tabla3ContenidosC)
            if self.objEdificio.programa == 'Residencial' and self.objEdificio.datosIniciales.zonaHE1 in ('alpha1', 'A1', 'B1', 'C1', 'D1', 'E1'):
                a65 = Paragraph('-', self.tabla2ContenidosC)
                a66 = Paragraph('-', self.tabla2ContenidosC)
            else:
                a65 = Paragraph('%0.2f' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef, self.tabla3ContenidosC)
                a66 = Paragraph(u'%s' % conjuntoMM.datosNuevoEdificio.datosResultados.ddaBrutaRef_nota, self.tabla2ContenidosC)
            a67 = Paragraph(u'%s %s' % (porcAhorroDdaRef, u'%'), self.tabla3ContenidosC)
            a68 = ''
            a69 = ''
            a610 = ''
            a611 = ''
            a612 = ''
            a613 = ''
            a614 = ''
            a615 = ''
            a616 = ''
            data = [[a11,
              a12,
              a13,
              a14,
              a15,
              a16,
              a17,
              a18,
              a19,
              a110,
              a111,
              a112,
              a113,
              a114,
              a115,
              a116],
             [a21,
              a22,
              a23,
              a24,
              a25,
              a26,
              a27,
              a28,
              a29,
              a210,
              a211,
              a212,
              a213,
              a214,
              a215,
              a216],
             [a41,
              a42,
              a43,
              a44,
              a45,
              a46,
              a47,
              a48,
              a49,
              a410,
              a411,
              a412,
              a413,
              a414,
              a415,
              a416],
             [a31,
              a32,
              a33,
              a34,
              a35,
              a36,
              a37,
              a38,
              a39,
              a310,
              a311,
              a312,
              a313,
              a314,
              a315,
              a316],
             [a51,
              a52,
              a53,
              a54,
              a55,
              a56,
              a57,
              a58,
              a59,
              a510,
              a511,
              a512,
              a513,
              a514,
              a515,
              a516],
             [a61,
              a62,
              a63,
              a64,
              a65,
              a66,
              a67,
              a68,
              a69,
              a610,
              a611,
              a612,
              a613,
              a614,
              a615,
              a616]]
            t = Table(data, [3.5 * cm,
             0.85 * cm,
             0.5 * cm,
             1.55 * cm,
             0.85 * cm,
             0.5 * cm,
             1.55 * cm,
             0.85 * cm,
             0.5 * cm,
             1.55 * cm,
             0.85 * cm,
             0.5 * cm,
             1.55 * cm,
             0.85 * cm,
             0.5 * cm,
             1.55 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (-1, 1),
              self.rosa),
             ('BACKGROUND',
              (0, 2),
              (0, 5),
              self.rosa),
             ('BACKGROUND',
              (3, 2),
              (3, 5),
              self.naranja),
             ('BACKGROUND',
              (6, 2),
              (6, 5),
              self.naranja),
             ('BACKGROUND',
              (9, 2),
              (9, 4),
              self.naranja),
             ('BACKGROUND',
              (12, 2),
              (12, 4),
              self.naranja),
             ('BACKGROUND',
              (15, 2),
              (15, 4),
              self.naranja),
             ('BACKGROUND',
              (7, 5),
              (-1, 5),
              colors.grey),
             ('SPAN', (1, 0), (3, 0)),
             ('SPAN', (4, 0), (6, 0)),
             ('SPAN', (7, 0), (9, 0)),
             ('SPAN', (10, 0), (12, 0)),
             ('SPAN', (13, 0), (15, 0)),
             ('GRID',
              (0, 0),
              (-1, -2),
              0.5,
              colors.black),
             ('GRID',
              (0, -1),
              (6, -1),
              0.5,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE'),
             ('SPAN', (0, 0), (0, 1)),
             ('SPAN', (1, 1), (2, 1)),
             ('SPAN', (4, 1), (5, 1)),
             ('SPAN', (7, 1), (8, 1)),
             ('SPAN', (10, 1), (11, 1)),
             ('SPAN', (13, 1), (14, 1)),
             ('SPAN', (1, 2), (2, 2)),
             ('SPAN', (4, 2), (5, 2)),
             ('SPAN', (7, 2), (8, 2)),
             ('SPAN', (10, 2), (11, 2)),
             ('SPAN', (13, 2), (14, 2)),
             ('BOX',
              (7, -1),
              (-1, 5),
              0.5,
              colors.black),
             ('SPAN', (7, -1), (-1, 5))]))
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            t = Paragraph(_(u'Nota: Los indicadores energ\xe9ticos anteriores est\xe1n calculados en base a coeficientes est\xe1ndar de operaci\xf3n y funcionamiento del edificio, por lo que solo son v\xe1lidos a efectos de su calificaci\xf3n energ\xe9tica. Para el an\xe1lisis econ\xf3mico de las medidas de ahorro y eficiencia energ\xe9tica, el t\xe9cnico certificador deber\xe1 utilizar las condiciones reales y datos hist\xf3ricos de consumo del edificio.'), self.tabla1Contenidos)
            Story.append(t)
            Story.append(Spacer(0, 0.4 * cm))
            Story.append(CondPageBreak(5 * cm))
            a0 = Paragraph(_(u'DESCRIPCI\xd3N DE LA MEDIDA DE MEJORA'), self.titulo2)
            a1 = Paragraph(_(u'Caracter\xedsticas de la medida (modelo de equipos, materiales, par\xe1metros caracter\xedsticos )'), self.tabla1ContenidosN)
            a2 = Paragraph(unicode(conjuntoMM.caracteristicas), self.tabla1Contenidos)
            Story.append(CondPageBreak(5 * cm))
            costeInversionInicial = conjuntoMM.calculoInversionInicial()
            if costeInversionInicial != '-':
                costeMM = u'%s \u20ac' % costeInversionInicial
            else:
                costeMM = costeInversionInicial
            a3 = Paragraph(_(u'Coste estimado de la medida'), self.tabla1ContenidosN)
            a4 = Paragraph(costeMM, self.tabla1Contenidos)
            Story.append(CondPageBreak(5 * cm))
            a5 = Paragraph(_(u'Otros datos de inter\xe9s'), self.tabla1ContenidosN)
            a6 = Paragraph(unicode(conjuntoMM.otrosDatos), self.tabla1Contenidos)
            data = [[a0],
             [a1],
             [a2],
             [a3],
             [a4],
             [a5],
             [a6]]
            t = Table(data, None, None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BACKGROUND',
              (0, 0),
              (0, 0),
              self.rosa),
             ('BOX',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black),
             ('LINEABOVE',
              (0, 1),
              (0, 1),
              1,
              colors.black),
             ('LINEABOVE',
              (0, 3),
              (0, 3),
              1,
              colors.black),
             ('LINEABOVE',
              (0, 5),
              (0, 5),
              1,
              colors.black),
             ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm),
             ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
            Story.append(t)
            Story.append(PageBreak())

        return Story

    def anexo4(self):
        Story = []
        t = Paragraph(_(u'ANEXO IV'), self.titulo1)
        Story.append(t)
        t = Paragraph(_(u'PRUEBAS, COMPROBACIONES E INSPECCIONES REALIZADAS POR EL T\xc9CNICO CERTIFICADOR'), self.titulo1)
        Story.append(t)
        Story.append(Spacer(0, 0.5 * cm))
        t = Paragraph(_(u'Se describen a continuaci\xf3n las pruebas, comprobaciones e inspecciones                         llevadas a cabo por el t\xe9cnico certificador durante el proceso de toma de                         datos y   de calificaci\xf3n de la eficiencia energ\xe9tica del edificio, con la                         finalidad de establecer la conformidad de la informaci\xf3n de partida contenida                         en el certificado de eficiencia energ\xe9tica.'), self.tabla1Contenidos)
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        Story += self.tablaAnexo4FechaRealizacion()
        Story += self.tablaAnexo4ComentariosTecnico()
        Story += self.tablaAnexo4DocumentacionAdjunta()
        return Story

    def tablaAnexo4FechaRealizacion(self):
        Story = []
        a11 = Paragraph(_(u'Fecha de realizaci\xf3n de la visita del t\xe9cnico certificador'), self.tabla1ContenidosNC)
        if len(self.datosConfiguracionInforme) >= 7:
            fechaVisitaDia = self.datosConfiguracionInforme[6][0]
            fechaVisitaMes = self.datosConfiguracionInforme[6][1]
            fechaVisitaAnno = self.datosConfiguracionInforme[6][2]
        else:
            fechaVisitaDia = ''
            fechaVisitaMes = ''
            fechaVisitaAnno = ''
        if fechaVisitaDia == '' and fechaVisitaMes == '' and fechaVisitaAnno == '':
            a12 = Paragraph('', self.tabla1ContenidosC)
        else:
            a12 = Paragraph('%s/%s/%s' % (fechaVisitaDia, fechaVisitaMes, fechaVisitaAnno), self.tabla1ContenidosC)
        data = [[a11, a12]]
        t = Table(data, [9.74 * cm, 3 * cm], [0.5 * cm], None, 1, 1, 1, hAlign='LEFT')
        t.setStyle(TableStyle([('GRID',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black),
         ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm),
         ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE'),
         ('BACKGROUND',
          (0, 0),
          (0, 1),
          self.rosa)]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        return Story

    def tablaAnexo4ComentariosTecnico(self):
        Story = []
        data = []
        comentariosTecnico = self.datosConfiguracionInforme[3]
        data.append([Paragraph(_(u'COMENTARIOS DEL T\xc9CNICO CERTIFICADOR'), self.tabla1ContenidosC)])
        comentariosTecnico = comentariosTecnico.replace('\n', '<br/>\n')
        if comentariosTecnico == '':
            comentariosTecnico = '-\n\n'
        else:
            com = comentariosTecnico.split('\n')
            for l in com:
                data.append([Paragraph(l, self.tabla1Contenidos)])

        t = Table(data, [18.0 * cm], None, None, 1, 1, 1)
        t.setStyle(TableStyle([('BOX',
          (0, 0),
          (-1, -1),
          0.5,
          colors.black), ('TOPPADDING',
          (0, 0),
          (-1, -1),
          0.0 * cm), ('VALIGN',
          (0, 0),
          (-1, -1),
          'MIDDLE')]))
        Story.append(t)
        Story.append(Spacer(0, 0.4 * cm))
        return Story

    def tablaAnexo4DocumentacionAdjunta(self):
        Story = []
        data = []
        documentacionAdjunta = self.datosConfiguracionInforme[4]
        documentacionAdjunta = documentacionAdjunta.replace('\n', '<br/>\n')
        if documentacionAdjunta != '':
            data.append([Paragraph(_(u'DOCUMENTACION ADJUNTA'), self.tabla1ContenidosC)])
            doc = documentacionAdjunta.split('\n')
            for l in doc:
                data.append([Paragraph(l, self.tabla1Contenidos)])

            t = Table(data, [18.0 * cm], None, None, 1, 1, 1)
            t.setStyle(TableStyle([('BOX',
              (0, 0),
              (-1, -1),
              0.5,
              colors.black), ('TOPPADDING',
              (0, 0),
              (-1, -1),
              0.0 * cm), ('VALIGN',
              (0, 0),
              (-1, -1),
              'MIDDLE')]))
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
        pieDePagina = ParagraphStyle('normal', fontName='arial', fontSize=8, borderPadding=0.0, leading=4, spaceBefore=0.0 * cm, alignment=TA_JUSTIFY)
        pieDePagina2 = ParagraphStyle('normal', fontName='arial', fontSize=8, borderPadding=0.0, leading=4, spaceBefore=0.0 * cm, alignment=TA_RIGHT)
        a11 = Paragraph(_(u'Fecha'), pieDePagina)
        a12 = Paragraph('%i/%i/%i' % (self.fechaImpresionCertificado.day, self.fechaImpresionCertificado.month, self.fechaImpresionCertificado.year), pieDePagina2)
        a13 = u''
        a21 = Paragraph(_(u'Ref. Catastral'), pieDePagina)
        listadoRefCat = self.datosAdmin[15]
        a22 = Paragraph(u'%s' % listadoRefCat[0], pieDePagina2)
        a23 = Paragraph(_(u'P\xe1gina %i de %i') % (self.pageNumber, self.totalPageNumber), pieDePagina2)
        data = [[a11, a12, a13], [a21, a22, a23]]
        t = Table(data, [2.94 * cm, 5.75 * cm, 9.75 * cm], None, None, 1, 1, 1)
        w, h = t.wrapOn(canv, 20 * cm, 5 * cm)
        t.drawOn(canv, 1.27 * cm, bottom_margin - 0.25 * inch)
        return


class EtiquetaMedidas(Flowable):
    """
    Clase: EtiquetaMedidas del modulo creaPDF.py
    
    
    """

    def __init__(self, categoria, emisiones, Limites):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                categoria:
                emisiones:
                Limites :
        """
        Flowable.__init__(self)
        self.categoria = categoria
        self.emisiones = emisiones
        self.limites = Limites

    def draw(self):
        """
        Metodo: draw
        
        
        """
        canv = self.canv
        u = cm
        canv.setLineWidth(1)
        canv.setStrokeColor(black)
        canv.setFillColorRGB(255, 255, 1)
        rgb = [(0.25, 0.25, 0.25),
         (0.4, 0.4, 0.4),
         (0.55, 0.55, 0.55),
         (0.7, 0.7, 0.7),
         (0.6, 0.6, 0.6),
         (0.4, 0.4, 0.4),
         (0.2, 0.2, 0.2)]
        letras = ['A',
         'B',
         'C',
         'D',
         'E',
         'F',
         'G']
        limites_str = ['< ' + str(self.limites[0]),
         str(self.limites[0]) + '-' + str(self.limites[1]),
         str(self.limites[1]) + '-' + str(self.limites[2]),
         str(self.limites[2]) + '-' + str(self.limites[3]),
         str(self.limites[3]) + '-' + str(self.limites[4]),
         str(self.limites[4]) + '-' + str(self.limites[5]),
         '>= ' + str(self.limites[5])]
        for contador in range(0, 7):
            r, g, b = rgb[contador]
            canv.setFillColorRGB(r, g, b)
            canv.setStrokeColorRGB(r, g, b)
            p = canv.beginPath()
            p.moveTo(0, 0 - contador * u * 0.35)
            p.lineTo(u + contador * u * 0.3, 0 - contador * u * 0.35)
            p.lineTo(1.175 * u + contador * u * 0.3, 0.14 * u - contador * u * 0.35)
            p.lineTo(u + contador * u * 0.3, 0.28 * u - contador * u * 0.35)
            p.lineTo(0, 0.28 * u - contador * u * 0.35)
            p.lineTo(0, 0 - contador * u * 0.35)
            canv.drawPath(p, stroke=1, fill=1)
            if self.categoria == letras[contador]:
                canv.setFillColorRGB(r, g, b)
                canv.setStrokeColorRGB(r, g, b)
                p.moveTo(u + contador * u * 0.3 + 2 * u, 0 - contador * u * 0.35)
                p.lineTo(u + contador * u * 0.3 + 1 * u, 0 - contador * u * 0.35)
                p.lineTo(u + contador * u * 0.3 + 0.7 * u, 0.14 * u - contador * u * 0.35)
                p.lineTo(u + contador * u * 0.3 + 1 * u, 0.28 * u - contador * u * 0.35)
                p.lineTo(u + contador * u * 0.3 + 2 * u, 0.28 * u - contador * u * 0.35)
                p.lineTo(u + contador * u * 0.3 + 2 * u, 0 - contador * u * 0.35)
                canv.drawPath(p, stroke=1, fill=1)
                canv.setFont('Verdana', 6)
                canv.setFillColor(white)
                canv.drawCentredString(u + contador * u * 0.3 + 1.5 * u, 0.15 * u - contador * u * 0.35 - 3.5, self.emisiones + ' ' + letras[contador])
            canv.setFillColor(white)
            canv.setFont('arial', 9)
            canv.drawCentredString(u + contador * u * 0.3, 0.14 * u - contador * u * 0.35 - 3.5, letras[contador])
            canv.setFont('arial', 4)
            canv.drawString(0.1 * u, 0.15 * u - contador * u * 0.35 - 3.5, limites_str[contador])
            canv.setFont('arial', 10)

    def wrap(self, aW, aH):
        """
        Metodo: wrap
        
        
        ARGUMENTOS:
                aW:
                aH):
        """
        canv = self.canv
        return (canv._leading, canv.stringWidth(self.categoria))


def calculoPorcAhorro(valorEdificioObjeto, valorConjuntoMM):
    try:
        ahorro = round((valorEdificioObjeto - valorConjuntoMM) / valorEdificioObjeto * 100.0, 1)
    except:
        logging.info(u'Excepcion en: %s' % __name__)
        ahorro = '-'

    return ahorro


class FuenteAusente(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return _(u'Falta la fuente Arial. Debe instalarla en su ordenador para obtener el informe de certificaci\xf3n.')


class BorradoInformeCertificacion(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return _(u'No se ha podido generar el informe de certificaci\xf3n. Si hay alg\xfan documento abierto con el mismo nombre debe cerrarlo.')


if __name__ == '__main__':
    informe = GeneraInforme()