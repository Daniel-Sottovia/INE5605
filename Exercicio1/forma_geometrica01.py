import math


class Forma():
    def __init__(self, forma:str, lado1:float, lado2=0):
        self.forma_geometrica = forma
        self.lado1 = lado1
        self.lado2 = lado2

    def Area(self):
        if self.forma_geometrica.lower() == 'circulo':
            self.area = math.pi*(self.lado1 ** 2)
        else:
            if self.forma_geometrica.lower() == 'quadrado':
                self.area = self.lado1 ** 2
            else:
                self.area = self.lado1 * self.lado2
        return self.area

def main():
    circulo = Forma('circulo', 2)
    circulo.Area()
    print(circulo.area)

    retangulo = Forma('retangulo', 4, 5)
    print(retangulo.Area())
    print(retangulo.area)

    quadrado = Forma('quadrado', 4)
    quadrado.Area()
    print(quadrado.area)

if __name__ == '__main__':
    main()