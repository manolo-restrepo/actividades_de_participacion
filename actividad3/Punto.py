import math
class punto:
    def __init__(self,coordenada_x,coordenada_y):
        self.coordenada_x=coordenada_x
        self.coordenada_y=coordenada_y
    def mostrar (self):
            print(self.coordenada_x,",",self.coordenada_y)
    def mover(self,nueva_x,nueva_y):
            self.coordenada_x=nueva_x
            self.coordenada_y=nueva_y
    def calcular_distancia(self,punto):
             distancia=math.sqrt((self.coordenada_x - punto.coordenada_x) ** 2 + (self.coordenada_y - punto.coordenada_y) ** 2)
             return distancia
punto1=punto(2,2)
punto2=punto(3,3)
punto.mostrar(punto2)
print(punto.calcular_distancia(punto1,punto2))
