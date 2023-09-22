import datetime

class Paciente:
  def __init__(self, nome, cpf, telefone, nascimento):
    self.__nome = nome
    self.__cpf = cpf 
    self.__telefone = telefone
    self.__nascimento = str() #xx/xx/xxxx

    self.set_nascimento(nascimento)
    
  def set_nascimento(self, nascimento):
    dia, mes, ano = map(int, nascimento.split("/"))
    self.__nascimento = datetime.datetime(ano,mes,dia)
    

  def calc_idade(self):
    hoje = datetime.datetime.today()
    
    idade = hoje - self.__nascimento
    dias = idade.days
    anos = dias // 365
    meses = (dias%365) // 30
    return f"Idade: {anos} ano(s) e {meses} meses"

  def __str__(self):
    return f"Nome do paciente: {self.__nome} - cpf: {self.__cpf} - telefone: {self.__telefone} - idade: {self.calc_idade()}"


class UI:
  main():
  prrint("1 - inserir paciente | 0 - fim")
