# Embedded file name: Calculos\calculoPoligonosPatronesSombra.pyc
"""
Modulo: calculoPoligonosPatronesSombra.py

"""
import copy
from Polygon import Polygon

class compruebaPuntos:
    """
    Clase: compruebaPuntos del modulo calculoPoligonosPatronesSombra.py
    
    
    """

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """
        Constructor de la clase
        
        
        ARGUMENTOS:
                x1:
                y1:
                x2:
                y2:
                x3:
                y3:
                x4:
                y4:
        """
        if self.fueraDeRango(x1, y1) or self.fueraDeRango(x2, y2) or self.fueraDeRango(x3, y3) or self.fueraDeRango(x4, y4):
            a = Polygon(((x1, y1),
             (x2, y2),
             (x3, y3),
             (x4, y4)))
            self.puntosAuxiliares = self.interseccion(a)
        else:
            self.puntosAuxiliares = [[[x1, y1],
              [x2, y2],
              [x3, y3],
              [x4, y4]]]

    def devuelvePuntos(self):
        """
        Metodo: devuelvePuntos
        
        
        """
        return self.puntosAuxiliares

    def interseccion(self, poly):
        """
        Metodo: interseccion: Calcula la intersecci\xf3n del pol\xedgono introducido
        por el usuario con el cuadro +/-120 azimuth y 0-80\xba elevaci\xf3n
        
        
        ARGUMENTOS:
                poly: Polygon definido con las coordenadas introducidas por el usuario
        """
        cuadro = Polygon(((-120, 0),
         (120, 0),
         (120, 80),
         (-120, 80)))
        interseccion = cuadro & poly
        if interseccion.area() == 0.0:
            return 'poligono fuera de limites'
        else:
            listadoPoligonosCuadrilateros = []
            for inter in interseccion:
                puntos = copy.deepcopy(inter)
                if len(puntos) == 3:
                    listadoPoligonosCuadrilateros.append([puntos[0],
                     puntos[1],
                     puntos[2],
                     puntos[2]])
                elif len(puntos) == 4:
                    listadoPoligonosCuadrilateros.append(puntos)
                elif len(puntos) == 5:
                    listadoPoligonosCuadrilateros.append([puntos[0],
                     puntos[1],
                     puntos[2],
                     puntos[3]])
                    listadoPoligonosCuadrilateros.append([puntos[3],
                     puntos[4],
                     puntos[4],
                     puntos[0]])
                elif len(puntos) == 6:
                    listadoPoligonosCuadrilateros.append([puntos[0],
                     puntos[1],
                     puntos[2],
                     puntos[5]])
                    listadoPoligonosCuadrilateros.append([puntos[2],
                     puntos[3],
                     puntos[4],
                     puntos[5]])
                elif len(puntos) == 7:
                    listadoPoligonosCuadrilateros.append([puntos[0],
                     puntos[1],
                     puntos[2],
                     puntos[6]])
                    listadoPoligonosCuadrilateros.append([puntos[2],
                     puntos[3],
                     puntos[4],
                     puntos[6]])
                    listadoPoligonosCuadrilateros.append([puntos[4],
                     puntos[5],
                     puntos[5],
                     puntos[6]])
                elif len(puntos) == 8:
                    listadoPoligonosCuadrilateros.append([puntos[0],
                     puntos[1],
                     puntos[2],
                     puntos[7]])
                    listadoPoligonosCuadrilateros.append([puntos[2],
                     puntos[3],
                     puntos[6],
                     puntos[7]])
                    listadoPoligonosCuadrilateros.append([puntos[3],
                     puntos[4],
                     puntos[5],
                     puntos[6]])

            return listadoPoligonosCuadrilateros

    def fueraDeRango(self, x, y):
        """
        Metodo: fueraDeRango
        
        
        ARGUMENTOS:
                x:
                y:
        """
        if x < -120.0 or x > 120.0:
            return True
        if y > 80.0:
            return True
        return False