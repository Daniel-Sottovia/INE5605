class Locador():
  def __init__(self, cpf: int, nome: str, telefone: int, endereco: str):
    self.__cpf = cpf
    self.__nome = nome
    self.__telefone = telefone
    self.__endereco = endereco

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf: int):
    if isinstance(cpf, int):
      self.__cpf = cpf

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
  def telefone(self, telefone: int):
    if isinstance(telefone, int):
      self.__telefone = telefone

  @property
  def endereco(self):
    return self.__endereco

  @endereco.setter
  def endereco(self, endereco:str):
    if isinstance(endereco, str):
      self.__endereco = endereco

