class Frete:
  def __init__(self, d, p):
    self.__distancia = 0
    self.__peso = 0
    self.set_d(d)
    self.set_p(p)

  def set_p(self, v):
    if v > 0: self.__peso= v
    else:
      print("ERROR")
      return

  def set_d(self, v):
    if v > 0: self.__distancia  = v
    else:
      print("ERRO")
      return

  def calcfrete(self):
    return self.__distancia * self.__peso * 0.01

  def __str__(self):
    return f"Distancia: {self.__distancia} - Peso: {self.__peso} Kg."
    

class UI():
  @staticmethod
  def main():
    d = float(input("Digite a distancia em Km \n"))
    p = int(input("digite o peso do produto em Kg \n"))
    x = Frete(d,p)
    print(f"Seu frete: {x.calcfrete()}")
    print(x)
    
UI.main()