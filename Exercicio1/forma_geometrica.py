import math


class Forma():
    def __init__(self, s:str):
        self.forma_geometrica = s
        self.Circulo()
        self.Quadrado()
        self.Retangulo()
        self.Area()


    def Circulo(self):
        if self.forma_geometrica.lower() == 'circulo':
            self.raio = float(input('Raio: '))

    def Quadrado(self):
        if self.forma_geometrica.lower() == 'quadrado':
            self.lado = float(input('Lado: '))

    def Retangulo(self):
        if self.forma_geometrica.lower() == 'retangulo':
            self.base = float(input('Base: '))
            self.altura = float(input('Altura: '))

    def Area(self):
        if self.forma_geometrica.lower() == 'circulo':
            self.area = math.pi*(self.raio**2)
        else:
            if self.forma_geometrica.lower() == 'quadrado':
                self.area = self.lado ** 2
            else:
                self.area = self.base * self.altura
        return print(f'Área: {self.area}')

objeto = Forma('retangulo')
