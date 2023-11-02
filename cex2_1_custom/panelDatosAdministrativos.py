# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: panelDatosAdministrativos.pyc
# Compiled at: 2015-02-17 10:49:19
"""
Modulo: panelDatosAdministrativos.py

"""
from Calculos.listados import Localizacion
from Instalaciones.comprobarCampos import Comprueba3
from miChoice import MiChoice
from undo import eventoUndo
import DatosAdministrativos.ayudaReferenciasCatastrales as ayudaReferenciasCatastrales, copy, decoradores, wx
wxID_PANEL1, wxID_PANEL1CERTIFICADORAUOTORTEXT, wxID_PANEL1CERTIFICADORAUTOR, wxID_PANEL1CERTIFICADOREMPRESA, wxID_PANEL1CERTIFICADOREMPRESATEXT, wxID_PANEL1CERTIFICADORMAIL, wxID_PANEL1CERTIFICADORMAILTEXT, wxID_PANEL1CERTIFICADORTELEFONO, wxID_PANEL1CERTIFICADORTELEFONOTEXT, wxID_PANEL1COMUNIDADEDIFICIO, wxID_PANEL1COMUNIDADEDIFICO, wxID_PANEL1CONTACTOCLIENTE, wxID_PANEL1CONTACTOCLIENTETEXT, wxID_PANEL1DATOSCERTIFICADORTEXT, wxID_PANEL1DATOSCLIENTETEXT, wxID_PANEL1DIRECCIONCLIENTE, wxID_PANEL1DIRECCIONCLIENTETEXT, wxID_PANEL1DIRECCIONEDIFICIO, wxID_PANEL1DIRECCIONTEXT, wxID_PANEL1DATOSADMINISTRATIVOSTXT, wxID_PANEL1LOCALIDADEDIFICIO, wxID_PANEL1LOCALIDADTEXT, wxID_PANEL1MAILCLIENTE, wxID_PANEL1MAILCLIENTETEXT, wxID_PANEL1NOMBRECLIENTE, wxID_PANEL1NOMBRECLIENTETEXT, wxID_PANEL1NOMBREEDIFICIO, wxID_PANEL1NOMBREEDIFICIOTEXT, wxID_PANEL1PROVINCIACHOICE, wxID_PANEL1PROVINCIATEXT, wxID_PANEL1TELEFONOCLIENTE, wxID_PANEL1TELEFONOCLIENTETEXT, wxID_PANEL1OTROCUADRO, wxID_PANEL1DIRECCIONCERTIFICADORTEXT, wxID_PANEL1DIRECCIONCERTIFICADOR, wxID_PANEL1PROVINCIACERTIFICADORTEXT, wxID_PANEL1PROVINCIACERTIFICADORCHOICE, wxID_PANEL1LOCALIDADCERTIFICADORTEXT, wxID_PANEL1LOCALIDADCERTIFICADORCUADRO, wxID_PANEL1CODIGOPOSTALCERTIFICADORTEXT, wxID_PANEL1CODIGOPOSTALCERTIFICADORCUADRO, wxID_PANEL1NIFCERTIFICADORTEXT, wxID_PANEL1NIFCERTIFICADORCUADRO, wxID_PANEL1CIFCERTIFICADORTEXT, wxID_PANEL1CIFCERTIFICADORCUADRO, wxID_PANEL1TITULACIONHABILITANTECERTIFICADORTEXT, wxID_PANEL1TITULACIONHABILITANTECERTIFICADORCUADRO, wxID_PANEL1CODIGOPOSTALEDIFICIOTEXT, wxID_PANEL1CODIGOPOSTALEDIFICIOCUADRO, wxID_PANEL1REFERENCIACATASTRALEDIFICIOTEXT, wxID_PANEL1REFERENCIACATASTRALEDIFICIOCUADRO, wxID_PANEL1PROVINCIACLIENTETEXT, wxID_PANEL1PROVINCIACLIENTECHOICE, wxID_PANEL1LOCALIDADCLIENTETEXT, wxID_PANEL1LOCALIDADCLIENTECUADRO, wxID_PANEL1CODIGOPOSTALCLIENTETEXT, wxID_PANEL1CODIGOPOSTALCLIENTECUADRO, wxID_PANEL1REFERENCIACATASTRALBOTON = [ wx.NewId() for _init_ctrls in range(58) ]

class panelDatosAdministrativos(wx.Panel):
    """
    Clase: panelDatosAdministrativos del modulo panelDatosAdministrativos.py

    """

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
        self.datosAdministrativosTxt = wx.StaticBox(id=wxID_PANEL1DATOSADMINISTRATIVOSTXT, label=_('Localización e identificación del edificio'), name='datosAdministrativosTxt', parent=self, pos=wx.Point(32, 32), size=wx.Size(896, 151), style=0)
        self.datosAdministrativosTxt.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.datosAdministrativosTxt.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nombreEdificioText = wx.StaticText(id=wxID_PANEL1NOMBREEDIFICIOTEXT, label=_('Nombre del edificio'), name='nombreEdificioText', parent=self, pos=wx.Point(56, 72), size=wx.Size(149, 13), style=0)
        self.nombreEdificio = wx.TextCtrl(id=wxID_PANEL1NOMBREEDIFICIO, name='nombreEdificio', parent=self, pos=wx.Point(216, 68), size=wx.Size(688, 21), style=0, value='')
        self.nombreEdificio.Bind(wx.EVT_KILL_FOCUS, self.onCambioNombreEdificio, id=wxID_PANEL1NOMBREEDIFICIO)
        self.direccionText = wx.StaticText(id=wxID_PANEL1DIRECCIONTEXT, label=_('Dirección '), name='direccionText', parent=self, pos=wx.Point(56, 100), size=wx.Size(50, 13), style=0)
        self.direccionEdificio = wx.TextCtrl(id=wxID_PANEL1DIRECCIONEDIFICIO, name='direccionEdificio', parent=self, pos=wx.Point(216, 96), size=wx.Size(688, 21), style=0, value='')
        self.direccionEdificio.Bind(wx.EVT_KILL_FOCUS, self.onCambioDireccionEdificio, id=wxID_PANEL1DIRECCIONEDIFICIO)
        self.provinciaText = wx.StaticText(id=wxID_PANEL1PROVINCIATEXT, label=_('Provincia/Ciudad autónoma'), name='provinciaText', parent=self, pos=wx.Point(56, 128), size=wx.Size(150, 13), style=0)
        self.provinciaChoice = MiChoice(choices=[], id=wxID_PANEL1PROVINCIACHOICE, name='provinciaChoice', parent=self, pos=wx.Point(216, 124), size=wx.Size(158, 21), style=0)
        self.provinciaChoice.Bind(wx.EVT_CHOICE, self.OnProvinciaChoice, id=wxID_PANEL1PROVINCIACHOICE)
        self.localidadText = wx.StaticText(id=wxID_PANEL1LOCALIDADTEXT, label=_('Localidad'), name='localidadText', parent=self, pos=wx.Point(430, 128), size=wx.Size(50, 13), style=0)
        self.localidadChoice = MiChoice(choices=[], id=wxID_PANEL1LOCALIDADEDIFICIO, name='choice1', parent=self, pos=wx.Point(507, 124), size=wx.Size(165, 21), style=0)
        self.localidadChoice.Bind(wx.EVT_CHOICE, self.OnLocalidadChoice, id=wxID_PANEL1LOCALIDADEDIFICIO)
        self.otroCuadro = wx.TextCtrl(id=wxID_PANEL1OTROCUADRO, name='otroCuadro', parent=self, pos=wx.Point(507, 152), size=wx.Size(165, 21), style=0, value='')
        self.otroCuadro.Show(False)
        self.otroCuadro.Bind(wx.EVT_KILL_FOCUS, self.OnOtroCuadro, id=wxID_PANEL1OTROCUADRO)
        self.codigoPostalEdificioText = wx.StaticText(id=wxID_PANEL1CODIGOPOSTALEDIFICIOTEXT, label=_('Código Postal'), name='codigoPostalEdificioText', parent=self, pos=wx.Point(728, 128), size=wx.Size(74, 13), style=0)
        self.codigoPostalEdificioCuadro = wx.TextCtrl(id=wxID_PANEL1CODIGOPOSTALEDIFICIOCUADRO, name='codigoPostalEdificioCuadro', parent=self, pos=wx.Point(804, 124), size=wx.Size(100, 21), style=0, value='')
        self.referenciaCatastralEdificioText = wx.StaticText(id=wxID_PANEL1REFERENCIACATASTRALEDIFICIOTEXT, label=_('Referencia Catastral'), name='codigoPostalEdificioText', parent=self, pos=wx.Point(56, 156), size=wx.Size(150, 13), style=0)
        self.referenciaCatastralEdificioCuadro = wx.TextCtrl(id=wxID_PANEL1REFERENCIACATASTRALEDIFICIOCUADRO, name='referenciaCatastralEdificioCuadro', parent=self, pos=wx.Point(216, 152), size=wx.Size(158, 21), style=0, value='')
        self.referenciaCatastralEdificioCuadro.Bind(wx.EVT_KILL_FOCUS, self.onCambioReferenciaCatastral, id=wxID_PANEL1REFERENCIACATASTRALEDIFICIOCUADRO)
        self.referenciaCatastralButton = wx.Button(id=wxID_PANEL1REFERENCIACATASTRALBOTON, label=_(' +'), name='referenciaCatastralButton', parent=self, pos=wx.Point(376, 152), size=wx.Size(21, 21), style=0)
        self.referenciaCatastralButton.Bind(wx.EVT_BUTTON, self.onReferenciaCatastralButton, id=wxID_PANEL1REFERENCIACATASTRALBOTON)
        self.datosClienteText = wx.StaticBox(id=wxID_PANEL1DATOSCLIENTETEXT, label=_('Datos del cliente'), name='datosClienteText', parent=self, pos=wx.Point(32, 201), size=wx.Size(896, 150), style=0)
        self.datosClienteText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.datosClienteText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.nombreClienteText = wx.StaticText(id=wxID_PANEL1NOMBRECLIENTETEXT, label=_('Nombre o razón social'), name='nombreClienteText', parent=self, pos=wx.Point(56, 240), size=wx.Size(109, 13), style=0)
        self.nombreCliente = wx.TextCtrl(id=wxID_PANEL1NOMBRECLIENTE, name='nombreCliente', parent=self, pos=wx.Point(216, 236), size=wx.Size(688, 21), style=0, value='')
        self.nombreCliente.Bind(wx.EVT_KILL_FOCUS, self.onCambioNombreCliente, id=wxID_PANEL1NOMBRECLIENTE)
        self.contactoClienteText = wx.StaticText(id=wxID_PANEL1CONTACTOCLIENTETEXT, label=_('Persona de contacto'), name='contactoClienteText', parent=self, pos=wx.Point(56, 268), size=wx.Size(105, 13), style=0)
        self.contactoClienteText.Show(False)
        self.contactoCliente = wx.TextCtrl(id=wxID_PANEL1CONTACTOCLIENTE, name='contactoCliente', parent=self, pos=wx.Point(216, 264), size=wx.Size(688, 21), style=0, value='')
        self.contactoCliente.Bind(wx.EVT_KILL_FOCUS, self.onCambioContactoCliente, id=wxID_PANEL1CONTACTOCLIENTE)
        self.contactoCliente.Show(False)
        self.direccionClienteText = wx.StaticText(id=wxID_PANEL1DIRECCIONCLIENTETEXT, label=_('Dirección '), name='direccionClienteText', parent=self, pos=wx.Point(56, 268), size=wx.Size(50, 13), style=0)
        self.direccionCliente = wx.TextCtrl(id=wxID_PANEL1DIRECCIONCLIENTE, name='direccionCliente', parent=self, pos=wx.Point(216, 264), size=wx.Size(688, 21), style=0, value='')
        self.direccionCliente.Bind(wx.EVT_KILL_FOCUS, self.onCambioDireccionCliente, id=wxID_PANEL1DIRECCIONCLIENTE)
        self.provinciaClienteText = wx.StaticText(id=wxID_PANEL1PROVINCIACLIENTETEXT, label=_('Provincia/Ciudad autónoma'), name='provinciaText', parent=self, pos=wx.Point(56, 296), size=wx.Size(150, 13), style=0)
        self.provinciaClienteChoice = MiChoice(choices=Localizacion().getListadoProvincias(), id=wxID_PANEL1PROVINCIACLIENTECHOICE, name='provinciaChoice', parent=self, pos=wx.Point(216, 294), size=wx.Size(158, 21), style=0)
        self.localidadClienteText = wx.StaticText(id=wxID_PANEL1LOCALIDADCLIENTETEXT, label=_('Localidad'), name='localidadText', parent=self, pos=wx.Point(430, 296), size=wx.Size(50, 13), style=0)
        self.localidadClienteCuadro = wx.TextCtrl(id=wxID_PANEL1LOCALIDADCLIENTECUADRO, name='localidadClienteCuadro', parent=self, pos=wx.Point(507, 294), size=wx.Size(158, 21), style=0, value='')
        self.codigoPostalClienteText = wx.StaticText(id=wxID_PANEL1CODIGOPOSTALCLIENTETEXT, label=_('Código Postal'), name='localidadText', parent=self, pos=wx.Point(728, 296), size=wx.Size(74, 13), style=0)
        self.codigoPostalClienteCuadro = wx.TextCtrl(id=wxID_PANEL1CODIGOPOSTALCLIENTECUADRO, name='codigoPostalCertificadorCuadro', parent=self, pos=wx.Point(804, 294), size=wx.Size(100, 21), style=0, value='')
        self.telefonoClienteText = wx.StaticText(id=wxID_PANEL1TELEFONOCLIENTETEXT, label=_('Teléfono '), name='telefonoClienteText', parent=self, pos=wx.Point(56, 324), size=wx.Size(49, 13), style=0)
        self.telefonoCliente = wx.TextCtrl(id=wxID_PANEL1TELEFONOCLIENTE, name='telefonoCliente', parent=self, pos=wx.Point(216, 320), size=wx.Size(158, 21), style=0, value='')
        self.telefonoCliente.Bind(wx.EVT_KILL_FOCUS, self.onCambioTelefonoCliente, id=wxID_PANEL1TELEFONOCLIENTE)
        self.mailClienteText = wx.StaticText(id=wxID_PANEL1MAILCLIENTETEXT, label=_('E-mail'), name='mailClienteText', parent=self, pos=wx.Point(430, 324), size=wx.Size(35, 13), style=0)
        self.mailCliente = wx.TextCtrl(id=wxID_PANEL1MAILCLIENTE, name='mailCliente', parent=self, pos=wx.Point(507, 320), size=wx.Size(397, 21), style=0, value='')
        self.mailCliente.Bind(wx.EVT_KILL_FOCUS, self.onCambioMailCliente, id=wxID_PANEL1MAILCLIENTE)
        self.datosCertificadorText = wx.StaticBox(id=wxID_PANEL1DATOSCERTIFICADORTEXT, label=_('Datos del técnico certificador '), name='datosCertificadorText', parent=self, pos=wx.Point(32, 368), size=wx.Size(896, 207), style=0)
        self.datosCertificadorText.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False, ''))
        self.datosCertificadorText.SetForegroundColour(wx.Colour(0, 64, 128))
        self.certificadorAuotorText = wx.StaticText(id=wxID_PANEL1CERTIFICADORAUOTORTEXT, label=_('Nombre y Apellidos'), name='certificadorAuotorText', parent=self, pos=wx.Point(56, 408), size=wx.Size(150, 13), style=0)
        self.certificadorAutor = wx.TextCtrl(id=wxID_PANEL1CERTIFICADORAUTOR, name='certificadorAutor', parent=self, pos=wx.Point(216, 404), size=wx.Size(449, 21), style=0, value='')
        self.certificadorAutor.Bind(wx.EVT_KILL_FOCUS, self.onCambioCertificadorAutor, id=wxID_PANEL1CERTIFICADORAUTOR)
        self.nifCertificadorText = wx.StaticText(id=wxID_PANEL1NIFCERTIFICADORTEXT, label=_('NIF'), name='localidadText', parent=self, pos=wx.Point(728, 406), size=wx.Size(74, 13), style=0)
        self.nifCertificadorCuadro = wx.TextCtrl(id=wxID_PANEL1NIFCERTIFICADORCUADRO, name='nifCertificadorCuadro', parent=self, pos=wx.Point(804, 406), size=wx.Size(100, 21), style=0, value='')
        self.certificadorEmpresaText = wx.StaticText(id=wxID_PANEL1CERTIFICADOREMPRESATEXT, label=_('Razón social'), name='certificadorEmpresaText', parent=self, pos=wx.Point(56, 436), size=wx.Size(150, 13), style=0)
        self.certificadorEmpresa = wx.TextCtrl(id=wxID_PANEL1CERTIFICADOREMPRESA, name='certificadorEmpresa', parent=self, pos=wx.Point(216, 432), size=wx.Size(449, 21), style=0, value='')
        self.certificadorEmpresa.Bind(wx.EVT_KILL_FOCUS, self.onCambioCertificadorEmpresa, id=wxID_PANEL1CERTIFICADOREMPRESA)
        self.cifCertificadorText = wx.StaticText(id=wxID_PANEL1CIFCERTIFICADORTEXT, label=_('CIF'), name='cifCertificadorText', parent=self, pos=wx.Point(728, 436), size=wx.Size(74, 13), style=0)
        self.cifCertificadorCuadro = wx.TextCtrl(id=wxID_PANEL1CIFCERTIFICADORCUADRO, name='cifCertificadorCuadro', parent=self, pos=wx.Point(804, 432), size=wx.Size(100, 21), style=0, value='')
        self.direccionCertificadorText = wx.StaticText(id=wxID_PANEL1DIRECCIONCERTIFICADORTEXT, label=_('Dirección '), name='direccionText', parent=self, pos=wx.Point(56, 464), size=wx.Size(150, 13), style=0)
        self.direccionCertificador = wx.TextCtrl(id=wxID_PANEL1DIRECCIONCERTIFICADOR, name='direccionEdificio', parent=self, pos=wx.Point(216, 460), size=wx.Size(688, 21), style=0, value='')
        self.provinciaCertificadorText = wx.StaticText(id=wxID_PANEL1PROVINCIACERTIFICADORTEXT, label=_('Provincia/Ciudad autónoma'), name='provinciaText', parent=self, pos=wx.Point(56, 492), size=wx.Size(150, 13), style=0)
        self.provinciaCertificadorChoice = MiChoice(choices=Localizacion().getListadoProvincias(), id=wxID_PANEL1PROVINCIACERTIFICADORCHOICE, name='provinciaChoice', parent=self, pos=wx.Point(216, 488), size=wx.Size(158, 21), style=0)
        self.localidadCertificadorText = wx.StaticText(id=wxID_PANEL1LOCALIDADCERTIFICADORTEXT, label=_('Localidad'), name='localidadText', parent=self, pos=wx.Point(430, 492), size=wx.Size(50, 13), style=0)
        self.localidadCertificadorCuadro = wx.TextCtrl(id=wxID_PANEL1LOCALIDADCERTIFICADORCUADRO, name='localidadCertificadorCuadro', parent=self, pos=wx.Point(507, 488), size=wx.Size(158, 21), style=0, value='')
        self.codigoPostalCertificadorText = wx.StaticText(id=wxID_PANEL1CODIGOPOSTALCERTIFICADORTEXT, label=_('Código Postal'), name='localidadText', parent=self, pos=wx.Point(728, 492), size=wx.Size(74, 13), style=0)
        self.codigoPostalCertificadorCuadro = wx.TextCtrl(id=wxID_PANEL1CODIGOPOSTALCERTIFICADORCUADRO, name='codigoPostalCertificadorCuadro', parent=self, pos=wx.Point(804, 488), size=wx.Size(100, 21), style=0, value='')
        self.certificadorTelefonoText = wx.StaticText(id=wxID_PANEL1CERTIFICADORTELEFONOTEXT, label=_('Teléfono '), name='certificadorTelefonoText', parent=self, pos=wx.Point(56, 520), size=wx.Size(49, 13), style=0)
        self.certificadorTelefono = wx.TextCtrl(id=wxID_PANEL1CERTIFICADORTELEFONO, name='certificadorTelefono', parent=self, pos=wx.Point(216, 516), size=wx.Size(158, 21), style=0, value='')
        self.certificadorTelefono.Bind(wx.EVT_KILL_FOCUS, self.onCambioCertificadorTelefono, id=wxID_PANEL1CERTIFICADORTELEFONO)
        self.certificadorMailText = wx.StaticText(id=wxID_PANEL1CERTIFICADORMAILTEXT, label=_('E-mail'), name='certificadorMailText', parent=self, pos=wx.Point(430, 520), size=wx.Size(32, 16), style=0)
        self.certificadorMail = wx.TextCtrl(id=wxID_PANEL1CERTIFICADORMAIL, name='certificadorMail', parent=self, pos=wx.Point(507, 516), size=wx.Size(397, 21), style=0, value='')
        self.certificadorMail.Bind(wx.EVT_KILL_FOCUS, self.onCambioCertificadorMail, id=wxID_PANEL1CERTIFICADORMAIL)
        self.titulacionHabilitanteCertificadorText = wx.StaticText(id=wxID_PANEL1TITULACIONHABILITANTECERTIFICADORTEXT, label=_('Titulación habilitante según normativa vigente'), name='direccionText', parent=self, pos=wx.Point(56, 541), size=wx.Size(150, 27), style=0)
        self.titulacionHabilitanteCuadro = wx.TextCtrl(id=wxID_PANEL1TITULACIONHABILITANTECERTIFICADORCUADRO, name='titulacionHabilitanteCuadro', parent=self, pos=wx.Point(216, 544), size=wx.Size(688, 21), style=0, value='')

    def onCambioNombreEdificio(self, event):
        """
        Metodo: onCambioNombreEdificio

        ARGUMENTOS:
                event:
        """
        if self.diccionario['nombreEdificio'] != self.nombreEdificio.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'nombreEdificio', copy.deepcopy(self.diccionario['nombreEdificio'])))
            self.diccionario['nombreEdificio'] = self.nombreEdificio.GetValue()

    def onCambioReferenciaCatastral(self, event):
        if self.diccionario['referenciaCatastral'] != self.referenciaCatastralEdificioCuadro.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'referenciaCatastral', copy.deepcopy(self.diccionario['referenciaCatastral'])))
            self.diccionario['referenciaCatastral'] = self.referenciaCatastralEdificioCuadro.GetValue()
        if self.referenciaCatastralEdificioCuadro.GetValue() != '':
            if len(self.listadoRefCat) == 0:
                self.listadoRefCat.append(self.referenciaCatastralEdificioCuadro.GetValue())
            else:
                self.listadoRefCat[0] = self.referenciaCatastralEdificioCuadro.GetValue()
        elif len(self.listadoRefCat) > 0:
            self.listadoRefCat.pop(0)
            if len(self.listadoRefCat) > 0:
                self.referenciaCatastralEdificioCuadro.SetValue(self.listadoRefCat[0])

    def onCambioDireccionEdificio(self, event):
        """
        Metodo: onCambioDireccionEdificio

        ARGUMENTOS:
                event:
        """
        if self.diccionario['direccionEdificio'] != self.direccionEdificio.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'direccionEdificio', copy.deepcopy(self.diccionario['direccionEdificio'])))
            self.diccionario['direccionEdificio'] = self.direccionEdificio.GetValue()

    def onCambioNombreCliente(self, event):
        """
        Metodo: onCambioNombreCliente

        ARGUMENTOS:
                event:
        """
        if self.diccionario['nombreCliente'] != self.nombreCliente.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'nombreCliente', copy.deepcopy(self.diccionario['nombreCliente'])))
            self.diccionario['nombreCliente'] = self.nombreCliente.GetValue()

    def onCambioContactoCliente(self, event):
        """
        Metodo: onCambioContactoCliente

        ARGUMENTOS:
                event:
        """
        if self.diccionario['contactoCliente'] != self.contactoCliente.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'contactoCliente', copy.deepcopy(self.diccionario['contactoCliente'])))
            self.diccionario['contactoCliente'] = self.contactoCliente.GetValue()

    def onCambioDireccionCliente(self, event):
        """
        Metodo: onCambioDireccionCliente

        ARGUMENTOS:
                event:
        """
        if self.diccionario['direccionCliente'] != self.direccionCliente.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'direccionCliente', copy.deepcopy(self.diccionario['direccionCliente'])))
            self.diccionario['direccionCliente'] = self.direccionCliente.GetValue()

    def onCambioTelefonoCliente(self, event):
        """
        Metodo: onCambioTelefonoCliente

        ARGUMENTOS:
                event:
        """
        if self.diccionario['telefonoCliente'] != self.telefonoCliente.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'telefonoCliente', copy.deepcopy(self.diccionario['telefonoCliente'])))
            self.diccionario['telefonoCliente'] = self.telefonoCliente.GetValue()

    def onCambioMailCliente(self, event):
        """
        Metodo: onCambioMailCliente

        ARGUMENTOS:
                event:
        """
        if self.diccionario['mailCliente'] != self.mailCliente.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'mailCliente', copy.deepcopy(self.diccionario['mailCliente'])))
            self.diccionario['mailCliente'] = self.mailCliente.GetValue()

    def onCambioCertificadorEmpresa(self, event):
        """
        Metodo: onCambioCertificadorEmpresa

        ARGUMENTOS:
                event:
        """
        if self.diccionario['certificadorEmpresa'] != self.certificadorEmpresa.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'certificadorEmpresa', copy.deepcopy(self.diccionario['certificadorEmpresa'])))
            self.diccionario['certificadorEmpresa'] = self.certificadorEmpresa.GetValue()

    def onCambioCertificadorAutor(self, event):
        """
        Metodo: onCambioCertificadorAutor

        ARGUMENTOS:
                event:
        """
        if self.diccionario['certificadorAutor'] != self.certificadorAutor.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'certificadorAutor', copy.deepcopy(self.diccionario['certificadorAutor'])))
            self.diccionario['certificadorAutor'] = self.certificadorAutor.GetValue()

    def onCambioCertificadorTelefono(self, event):
        """
        Metodo: onCambioCertificadorTelefono

        ARGUMENTOS:
                event:
        """
        if self.diccionario['certificadorTelefono'] != self.certificadorTelefono.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'certificadorTelefono', copy.deepcopy(self.diccionario['certificadorTelefono'])))
            self.diccionario['certificadorTelefono'] = self.certificadorTelefono.GetValue()

    def onCambioCertificadorMail(self, event):
        """
        Metodo: onCambioCertificadorMail

        ARGUMENTOS:
                event:
        """
        if self.diccionario['certificadorMail'] != self.certificadorMail.GetValue():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self, 'certificadorMail', copy.deepcopy(self.diccionario['certificadorMail'])))
            self.diccionario['certificadorMail'] = self.certificadorMail.GetValue()

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
        self.parent = parent
        self.listadoRefCat = []
        self._init_ctrls(parent, id, pos, size, style, name)
        self.nombre = _('Datos administrativos')
        self.actualizaDiccionario()

    def actualizaDiccionario(self):
        """
        Metodo: actualizaDiccionario

        """
        self.diccionario = {}
        self.diccionario['nombreEdificio'] = self.nombreEdificio.GetValue()
        self.diccionario['direccionEdificio'] = self.direccionEdificio.GetValue()
        self.diccionario['otroCuadro'] = self.otroCuadro.GetValue()
        self.diccionario['nombreCliente'] = self.nombreCliente.GetValue()
        self.diccionario['contactoCliente'] = self.contactoCliente.GetValue()
        self.diccionario['direccionCliente'] = self.direccionCliente.GetValue()
        self.diccionario['telefonoCliente'] = self.telefonoCliente.GetValue()
        self.diccionario['mailCliente'] = self.mailCliente.GetValue()
        self.diccionario['certificadorEmpresa'] = self.certificadorEmpresa.GetValue()
        self.diccionario['certificadorAutor'] = self.certificadorAutor.GetValue()
        self.diccionario['certificadorTelefono'] = self.certificadorTelefono.GetValue()
        self.diccionario['certificadorMail'] = self.certificadorMail.GetValue()
        self.diccionario['referenciaCatastral'] = self.referenciaCatastralEdificioCuadro.GetValue()

    @decoradores.deco(5)
    def OnProvinciaChoice(self, event):
        """
        Metodo: OnProvinciaChoice

        ARGUMENTOS:
                event:
        """
        if self.parent.parent.panelDatosGenerales.diccionario['provinciaChoice'] != self.provinciaChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self.parent.parent.panelDatosGenerales, 'provinciaChoice', copy.deepcopy(self.parent.parent.panelDatosGenerales.diccionario['provinciaChoice'])))
            self.parent.parent.panelDatosGenerales.diccionario['provinciaChoice'] = self.provinciaChoice.GetSelection()
        listadoCiudades = []
        listadoCiudades = Localizacion().getLocalidadesDeProvincia(self.provinciaChoice.GetStringSelection())
        self.localidadChoice.SetItems(listadoCiudades)
        self.otroCuadro.Show(False)
        self.parent.parent.panelDatosGenerales.provinciaChoice.SetStringSelection(self.provinciaChoice.GetStringSelection())
        self.parent.parent.panelDatosGenerales.OnProvinciaChoiceRecargar()

    def OnProvinciaChoiceRecargar(self):
        """
        Metodo: OnProvinciaChoiceRecargar

        """
        listadoCiudades = []
        listadoCiudades = Localizacion().getLocalidadesDeProvincia(self.provinciaChoice.GetStringSelection())
        self.localidadChoice.SetItems(listadoCiudades)
        self.otroCuadro.Show(False)

    def OnLocalidadChoice(self, event):
        """
        Metodo: OnLocalidadChoice

        ARGUMENTOS:
                event:
        """
        if self.parent.parent.panelDatosGenerales.diccionario['choice1'] != self.localidadChoice.GetSelection():
            self.parent.parent.pilaUndo.apilar(eventoUndo(self.parent.parent.panelDatosGenerales, 'choice1', copy.deepcopy(self.parent.parent.panelDatosGenerales.diccionario['choice1'])))
            self.parent.parent.panelDatosGenerales.diccionario['choice1'] = self.localidadChoice.GetSelection()
        if self.localidadChoice.GetStringSelection() != 'Otro':
            self.otroCuadro.Show(False)
        else:
            self.otroCuadro.Show(True)
        self.parent.parent.panelDatosGenerales.localidadChoice.SetStringSelection(self.localidadChoice.GetStringSelection())
        self.parent.parent.panelDatosGenerales.OnLocalidadChoiceRecargar()

    def OnLocalidadChoiceRecargar(self):
        """
        Metodo: OnLocalidadChoiceRecargar

        """
        if self.localidadChoice.GetStringSelection() != 'Otro':
            self.otroCuadro.Show(False)
        else:
            self.otroCuadro.Show(True)

    def OnOtroCuadro(self, event):
        """
        Metodo: OnOtroCuadro

        ARGUMENTOS:
                event:
        """
        self.parent.parent.panelDatosGenerales.otroCuadro.SetValue(self.otroCuadro.GetValue())

    def onReferenciaCatastralButton(self, event):
        """
        Metodo: onReferenciaCatastralButton

        ARGUMENTOS:
            event:
        """
        dialog = ayudaReferenciasCatastrales.Dialog1(self, self.listadoRefCat)
        dialog.ShowModal()
        if len(self.listadoRefCat) > 0:
            self.referenciaCatastralEdificioCuadro.SetValue(self.listadoRefCat[0])
        else:
            self.referenciaCatastralEdificioCuadro.SetValue('')

    def cogerDatos(self):
        """
        Metodo: cogerDatos

        """
        datos = []
        datos.append(self.nombreEdificio.GetValue())
        datos.append(self.direccionEdificio.GetValue())
        datos.append(self.localidadChoice.GetStringSelection())
        datos.append(self.provinciaChoice.GetStringSelection())
        datos.append(self.otroCuadro.GetValue())
        datos.append(self.nombreCliente.GetValue())
        datos.append(self.contactoCliente.GetValue())
        datos.append(self.direccionCliente.GetValue())
        datos.append(self.telefonoCliente.GetValue())
        datos.append(self.mailCliente.GetValue())
        datos.append(self.certificadorEmpresa.GetValue())
        datos.append(self.certificadorAutor.GetValue())
        datos.append(self.certificadorTelefono.GetValue())
        datos.append(self.certificadorMail.GetValue())
        datos.append(self.codigoPostalEdificioCuadro.GetValue())
        datos.append(self.listadoRefCat)
        datos.append(self.localidadClienteCuadro.GetValue())
        datos.append(self.provinciaClienteChoice.GetStringSelection())
        datos.append(self.codigoPostalClienteCuadro.GetValue())
        datos.append(self.nifCertificadorCuadro.GetValue())
        datos.append(self.cifCertificadorCuadro.GetValue())
        datos.append(self.direccionCertificador.GetValue())
        datos.append(self.provinciaCertificadorChoice.GetStringSelection())
        datos.append(self.localidadCertificadorCuadro.GetValue())
        datos.append(self.codigoPostalCertificadorCuadro.GetValue())
        datos.append(self.titulacionHabilitanteCuadro.GetValue())
        return datos

    def cargarDatos(self, datos):
        """
        Metodo: cargarDatos

        ARGUMENTOS:
                datos:
        """
        self.nombreEdificio.SetValue(datos[0])
        self.direccionEdificio.SetValue(datos[1])
        if datos[3] == '':
            self.provinciaChoice.SetSelection(-1)
            self.localidadChoice.SetItems([])
        else:
            self.provinciaChoice.SetStringSelection(datos[3])
            self.OnProvinciaChoiceRecargar()
        if datos[2] == '':
            self.localidadChoice.SetSelection(-1)
        else:
            self.localidadChoice.SetStringSelection(datos[2])
        if datos[2] == 'Otro':
            self.otroCuadro.SetValue(datos[4])
            self.otroCuadro.Show(True)
        else:
            self.otroCuadro.Show(False)
        self.nombreCliente.SetValue(datos[5])
        self.contactoCliente.SetValue(datos[6])
        self.direccionCliente.SetValue(datos[7])
        self.telefonoCliente.SetValue(datos[8])
        self.mailCliente.SetValue(datos[9])
        self.certificadorEmpresa.SetValue(datos[10])
        self.certificadorAutor.SetValue(datos[11])
        self.certificadorTelefono.SetValue(datos[12])
        self.certificadorMail.SetValue(datos[13])
        self.codigoPostalEdificioCuadro.SetValue(datos[14])
        datosReferenciaCatastral = datos[15]
        self.listadoRefCat = []
        if type(datosReferenciaCatastral) == type([]):
            self.listadoRefCat = datosReferenciaCatastral
        elif datosReferenciaCatastral != '':
            self.listadoRefCat.append(datosReferenciaCatastral)
        if len(self.listadoRefCat) > 0:
            self.referenciaCatastralEdificioCuadro.SetValue(self.listadoRefCat[0])
        else:
            self.referenciaCatastralEdificioCuadro.SetValue('')
        self.localidadClienteCuadro.SetValue(datos[16])
        if datos[17] == '':
            self.provinciaClienteChoice.SetSelection(-1)
        else:
            self.provinciaClienteChoice.SetStringSelection(datos[17])
        self.codigoPostalClienteCuadro.SetValue(datos[18])
        self.nifCertificadorCuadro.SetValue(datos[19])
        self.cifCertificadorCuadro.SetValue(datos[20])
        self.direccionCertificador.SetValue(datos[21])
        if datos[22] == '':
            self.provinciaCertificadorChoice.SetSelection(-1)
        else:
            self.provinciaCertificadorChoice.SetStringSelection(datos[22])
        self.localidadCertificadorCuadro.SetValue(datos[23])
        self.codigoPostalCertificadorCuadro.SetValue(datos[24])
        self.titulacionHabilitanteCuadro.SetValue(datos[25])
        self.actualizaDiccionario()

    def exportarDatos(self):
        """
        Metodo: exportarDatos

        """
        listaErrores = ''
        listaErrores += Comprueba3(self.nombreEdificio.GetValue(), 0, listaErrores, _('Nombre del edificio a certificar')).ErrorDevuelto
        listaErrores += Comprueba3(self.direccionEdificio.GetValue(), 0, listaErrores, _('Dirección del edificio')).ErrorDevuelto
        listaErrores += Comprueba3(self.localidadChoice.GetStringSelection(), 0, listaErrores, _('Localidad del edificio')).ErrorDevuelto
        listaErrores += Comprueba3(self.provinciaChoice.GetStringSelection(), 0, listaErrores, _('Provincia del edificio')).ErrorDevuelto
        if self.localidadChoice.GetStringSelection() == 'Otro':
            listaErrores += Comprueba3(self.otroCuadro.GetValue(), 0, listaErrores, _('Localidad del edificio')).ErrorDevuelto
        listaErrores += Comprueba3(self.codigoPostalEdificioCuadro.GetValue(), 0, listaErrores, _('Código postal de la localidad donde está situado el edificio')).ErrorDevuelto
        listaErrores += Comprueba3(self.referenciaCatastralEdificioCuadro.GetValue(), 0, listaErrores, _('Referencia catastral')).ErrorDevuelto
        listaErrores += Comprueba3(self.certificadorAutor.GetValue(), 0, listaErrores, _('Nombre y apellidos del técnico certificador')).ErrorDevuelto
        listaErrores += Comprueba3(self.nifCertificadorCuadro.GetValue(), 0, listaErrores, _('NIF del técnico certificador')).ErrorDevuelto
        listaErrores += Comprueba3(self.certificadorEmpresa.GetValue(), 0, listaErrores, _('Razón social de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.cifCertificadorCuadro.GetValue(), 0, listaErrores, _('CIF de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.direccionCertificador.GetValue(), 0, listaErrores, _('Dirección de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.provinciaCertificadorChoice.GetStringSelection(), 0, listaErrores, _('Provincia de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.localidadCertificadorCuadro.GetValue(), 0, listaErrores, _('Localidad de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.codigoPostalCertificadorCuadro.GetValue(), 0, listaErrores, _('Código postal de la empresa certificadora')).ErrorDevuelto
        listaErrores += Comprueba3(self.certificadorTelefono.GetValue(), 0, listaErrores, _('teléfono del técnico certificador')).ErrorDevuelto
        listaErrores += Comprueba3(self.certificadorMail.GetValue(), 0, listaErrores, _('Correo electrónico de contacto')).ErrorDevuelto
        listaErrores += Comprueba3(self.titulacionHabilitanteCuadro.GetValue(), 0, listaErrores, _('Titulación del técnico certificador habilitante según la normativa vigente para realizar la certificación energética')).ErrorDevuelto
        if listaErrores != '':
            wx.MessageBox(_('Revise los siguientes campos de la pestaña de Datos Admnistrativos:\n') + listaErrores, _('Aviso'))
            datosPanelDatosAdministrativos = []
            return datosPanelDatosAdministrativos
        datosPanelDatosAdministrativos = self.cogerDatos()
        return datosPanelDatosAdministrativos