class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

   
    def eje_x(self):
        return self.x

   
    def eje_y(self):
        return self.y

   
    def impresion(self):
        return f"Punto({self.x}, {self.y})"

    
    def opuesto(self):
        return Punto(-self.x, -self.y)

    
    def distancia_origen(self):
        return (self.x**2 + self.y**2) ** 0.5

   
    def distancia(self, otro_punto):
        return ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2) ** 0.5

   
    def sumar(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

  
    def es_igual(self, otro_punto):
        return self.x == otro_punto.x and self.y == otro_punto.y