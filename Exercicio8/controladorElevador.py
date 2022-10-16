from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException

from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        pass

    def subir(self) -> str:
        self.__elevador.subir()

    def descer(self) -> str:
        self.__elevador.descer()

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializar_elevador(self,
                             andar_atual: int,
                             total_andares_predio: int,
                             capacidade: int,
                             total_pessoas: int):
        if not(isinstance(andar_atual, int)
            and isinstance(total_andares_predio, int)
            and isinstance(capacidade, int)
            and isinstance(total_pessoas, int)):
            return None
        self.__elevador = Elevador(capacidade=capacidade,
                                   total_pessoas= total_pessoas,
                                   total_andares= total_andares_predio,
                                   andar_atual= andar_atual)


