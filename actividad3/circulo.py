import math

class Circulo:
    def __init__(self, centro_x, centro_y, radio):
        self.centro_x = centro_x  
        self.centro_y = centro_y  
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)  

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio  

    def pertenece_punto(self, punto_x, punto_y):
        distancia = math.sqrt((punto_x - self.centro_x) ** 2 + (punto_y - self.centro_y) ** 2)
        return distancia <= self.radio  


circulo1 = Circulo(0, 0, 5)  


area = circulo1.calcular_area()
perimetro = circulo1.calcular_perimetro()

print("Área del círculo:",area)          
print(f"Perímetro del círculo:",perimetro)  


punto_x, punto_y = 3, 4
print(f"¿El punto ({punto_x}, {punto_y}) pertenece al círculo? {circulo1.pertenece_punto(punto_x, punto_y)}")
