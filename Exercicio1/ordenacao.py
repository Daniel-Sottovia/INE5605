class Ordenacao():

    def __init__(self, array_para_ordenar: []):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar


    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        """Método de ordenação Bolha (Bubble Sort)"""
        tam = len(self.array_para_ordenar)
        cont = 0
        while cont < tam:
            i = cont
            while i < tam:
                if self.array_para_ordenar[cont] > self.array_para_ordenar[i]:
                    self.array_para_ordenar[cont], self.array_para_ordenar[i] = self.array_para_ordenar[i], self.array_para_ordenar[cont]
                i += 1
            cont += 1

        return self.array_para_ordenar

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo:
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        tam = len(self.array_para_ordenar)
        cont = 0
        final = ''
        while cont < tam:
            if cont == tam - 1:
                final = final + f'{self.array_para_ordenar[cont]}'
            else:
                final = final + f'{self.array_para_ordenar[cont]},'
            cont += 1

        return final


lista = [5,4,3,2,1]
c = Ordenacao(lista)
c.ordena()
print(c.array_para_ordenar)
print(c.toString())

