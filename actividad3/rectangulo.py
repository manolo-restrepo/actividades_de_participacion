import math
class rectangulo:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def calcular_perimetro(self):
        perimetro=2*abs((self.x2-self.x1)+(self.y2-self.y1))
        return perimetro
    def calcular_area(self):
        area= abs((self.x2-self.x1)*(self.y2-self.y1))
        return area
    def cuadrado(self):
        if (self.x2-self.x1) == (self.y2-self.y1):
            return ("es cuadrado")
        else:
            return("no es cuadrado hermano")
rectangulo1=rectangulo(2,3,4,6)
print("perimetro:", rectangulo1.calcular_perimetro())
print("area:", rectangulo1.calcular_area())
print(rectangulo1.cuadrado())