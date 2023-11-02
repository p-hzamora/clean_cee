# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: DatosGenerales\trataImagenes.pyc
# Compiled at: 2014-02-18 15:21:04
import Image, StringIO, base64
cm = 28.346456692913385

def trataImagen(nombreArchivo):
    width = 8.75 * cm
    height = 4.75 * cm
    im = Image.open(nombreArchivo)
    if im.size[0] / width < 1.0 and im.size[1] / height < 1.0:
        factorAjuste = 1
    elif im.size[0] / width > im.size[1] / height < 1.0:
        factorAjuste = width / im.size[0]
    else:
        factorAjuste = height / im.size[1]
    im = im.resize((int(im.size[0] * factorAjuste), int(im.size[1] * factorAjuste)), Image.ANTIALIAS)
    output = StringIO.StringIO()
    im.save(output, format='PNG')
    contents = output.getvalue()
    output.close()
    return base64.b64encode(contents)