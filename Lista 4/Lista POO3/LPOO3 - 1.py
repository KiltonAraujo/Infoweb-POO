class Retangulo:
  def __init__(self, b, h):
    self.__base = 0
    self.__altura = 0
    self.set_base(b)
    self.set_altura(h)
  def set_base(self, v):
    if v > 0:
      self.__base = v
    else: raise ValueError()

  def set_altura(self, v):
    if v > 0:
      self.__altura = v
    else: raise ValueError()

  def get_base(self):
    return self.__base

  def get_altura(self):
    return self.__altura

  def calc_area(self):
    return self.__base * self.__altura

  def calc_diag(self):
    return (self.__base**2 + self.__altura**2)**0.5

  def __str__(self):
    return f"Base = {self.__base} - Altura = {self.__altura}"

class UI:
  @staticmethod
  def main():
  b = float(input())
  h = float(input())
  x = Retangulo(b,h)
  print(f'Area: {x.calc_area(}') print(f'Diagonal={x.calc_diagonal()}')
UI.main()