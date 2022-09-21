from Locador import Locador
from Locatario import Locatario
from Mobilia import Mobilia

class Imovel:
  def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
    if isinstance(codigo, int) and isinstance(descricao, str) and isinstance(valor, float) and isinstance(locador, Locador):
      self.__codigo = codigo
      self.__descricao = descricao
      self.__valor = valor
      self.__locador = locador
      self.__locatarios = []
      self.__mobilias = []

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self, codigo: int):
    if isinstance(codigo, int):
      self.__codigo = codigo

  @property
  def descricao(self):
    return self.__descricao

  @descricao.setter
  def descricao(self, descricao: str):
    if isinstance(descricao, str):
      self.__descricao = descricao

  @property
  def locador(self):
    return self.__locador

  @locador.setter
  def locador(self, locador: Locador):
    if isinstance(locador, Locador):
      self.__locador = locador

  @property
  def locatarios(self):
    return self.__locatarios

  def incluir_locatario(self, locatario: Locatario):
    if isinstance(locatario, Locatario):
      if locatario not in self.__locatarios:
        self.__locatarios.append(locatario)

  def excluir_locatario(self, codigo_locatario: int):
    if isinstance(codigo_locatario, int):
      for locatario in self.__locatarios:
        if locatario.codigo == codigo_locatario:
          self.__locatarios.remove(locatario)

  @property
  def mobilias(self):
    return self.__mobilias

  def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
    '''if isinstance(codigo_mobilia, int) and isinstance(descricao_mobilia, str):
      cont = 0
      tam = len(self.__mobilias)
      soma = 0
      while cont < tam:
        if self.__mobilias[cont].codigo == codigo_mobilia:
          soma += 1
        cont += 1

      if soma == 0:
        nova_mobilia = Mobilia(codigo=codigo_mobilia, descricao=descricao_mobilia)
        self.__mobilias.append(nova_mobilia)'''

    if isinstance(codigo_mobilia, int) and isinstance(descricao_mobilia, str):
      valor = True
      for mobilia in self.__mobilias:
        if mobilia.codigo == codigo_mobilia:
          valor = False

      if valor:
        self.__mobilias.append(Mobilia(codigo=codigo_mobilia, descricao=descricao_mobilia))


  def excluir_mobilia(self, codigo_mobilia: int):
    if isinstance(codigo_mobilia, int):
      for mobilia in self.__mobilias:
        if mobilia.codigo == codigo_mobilia:
          self.__mobilias.remove(mobilia)

  def find_locatario_by_codigo(self, codigo_locatario: int):
    if isinstance(codigo_locatario, int):
      for locatario in self.__locatarios:
        if locatario.codigo == codigo_locatario:
          return locatario

def main():
  daniel = Locador(4954, 'Daniel', 67999, 'floripa')
  casa = Imovel(123, 'casa grande', 2450000.00, locador=daniel)
  casa.incluir_mobilia(123, 'cama')
  casa.incluir_mobilia(234, 'cadeira')
  casa.excluir_mobilia(444)
  francesco = Locatario(222, 'Francesco', 679898)
  otavio = Locatario(111, 'Otávio', 679922)
  fimose = Locatario(555, 'Vinicius', 489333)
  casa.incluir_locatario(francesco)
  casa.incluir_locatario(otavio)
  casa.excluir_locatario(333)
  casa.excluir_locatario(222)
  casa.incluir_locatario(fimose)
  print(casa.mobilias)
  print(casa.locatarios)
  pass

if __name__ == '__main__':
  main()