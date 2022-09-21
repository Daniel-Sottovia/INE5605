class Cliente:
    def __init__(self, cpf: int, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    '''def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome'''

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    '''def set_cpf(self, cpf: int):
        self.__cpf = cpf
        
    def set_nome(self, nome: str):
        self.__nome = nome'''

    @cpf.setter
    def cpf(self, cpf: int):
        print("ALTERANDO O CPF")
        if cpf is not None and cpf > 0:
            self.__cpf = cpf
        else:
            print('VALOR INVALIDO PARA O CPF')

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

cliente1 = Cliente(123, "Jean")
cliente1.cpf = 999
# cliente1.set_cpf(999)

print(f"CPF CLIENTE 1 {cliente1.cpf}")
print(f"NOME CLIENTE 1 {cliente1.nome}")
# print(f"CPF CLIENTE 1 {cliente1.get_cpf()}")
# print(f"NOME CLIENTE 1 {cliente1.get_nome()}")

cliente2 = Cliente(456, 'Antonio')
# cliente2.cpf = 456
# cliente2.nome = 'Antonio'

print()

'''print(f"CPF CLIENTE 2 {cliente2.get_cpf()}")
print(f"NOME CLIENTE 2 {cliente2.get_nome()}")

print()

print('OBJETO 1', cliente1)
print('OBJETO 2', cliente2)'''