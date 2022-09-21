class Locatario:
  def __init__(self, codigo: int, nome: str, telefone: int):
    if isinstance(codigo, int) and isinstance(nome, str) and isinstance(telefone, int):
      self.__codigo = codigo
      self.__nome = nome
      self.__telefone = telefone

  @property
  def codigo(self):
    return self.__codigo

  @codigo.setter
  def codigo(self, codigo: int):
    if isinstance(codigo, int):
      self.__codigo = codigo

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    if isinstance(nome, str):
      self.__nome = nome

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone:int):
    if isinstance(telefone, int):
      self.__telefone = telefone

