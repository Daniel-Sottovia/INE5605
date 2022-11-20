from cliente import Cliente


class ClienteFidelidade(Cliente):

    def __init__(self, codigo_fidelidade: int, desconto: float, cpf: str,
                 nome: str, endereco: str, telefone: str):
        super().__init__(cpf, nome, endereco, telefone)
        self.__codigo_fidelidade = codigo_fidelidade
        self.__desconto = desconto

    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade

    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade: int):
        if isinstance(codigo_fidelidade, int):
            self.__codigo_fidelidade = codigo_fidelidade

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto: float):
        if isinstance(desconto, float):
            self.__desconto = desconto
