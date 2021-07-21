class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        return (max(self.a, self.b, self.c))**2 ==((self.a**2 + self.b**2 + self.c**2)-(max(self.a, self.b, self.c))**2)

    
    def semelhantes(self, outroself):
        tria = outroself
        tri1 = sorted([int(self.a), int(self.b), int(self.c)])
        tri2 = sorted([int(tria.a), int(tria.b), int(tria.c)])
        for lado in range(len(tri1)):
            if (tri1[lado]>= tri2[lado]) and  (tri1[lado]% tri2[lado])== 0:
                semelhante = True
            elif tri2[lado] > tri1[lado] and tri2[lado]%tri1[lado]==0:
                semelhante = True
            else:
                semelhante = False
                break
        return semelhante

        
        
