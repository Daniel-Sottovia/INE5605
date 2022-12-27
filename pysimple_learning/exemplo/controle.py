import random


class Brincando():

    def __init__(self):
        self.__votos = []

    def gerar_votos(self):
        for i in range(0, 50):
            self.__votos.append(random.randrange(1, 11))



if __name__ == '__main__':
    for i in range(0, 20):
        print(random.randrange(1,11))