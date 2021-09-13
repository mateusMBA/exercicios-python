class Triangulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        
        if (self.a == self.b == self.c):
            return 'equilátero'
        else:
            if (self.a == self.b or self.a == self.c or self.b == self.c):
                return 'isóceles'
            else:
                return 'escaleno'
