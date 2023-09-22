class Esporte:
  def __init__(self, nomeE, horarios, mensalidade):
    self.__nomeE = str()
    self.__horarios = str()
    self.__mensalidade = float()

    self.set_nomeE(nomeE)
    self.set_horarios(horarios)
    self.set_mensalidade(mensalidade)

  def set_nomeE(self, nomeE):
    if nomeE != "":
      self.__nomeE = nomeE
    else: raise ValueError()

  def get_nomeE(self):
    return self.__nomeE

  def set_horarios(self, horarios):
    if horarios != "": self.__horarios = horarios
    else: raise ValueError()

  def set_mensalidade(self, mensalidade):
    if mensalidade > 0: self.__mensalidade = mensalidade
    else: raise ValueError()

  def get_mensalidade(self):
    return self.__mensalidade
      
  def __str__(self):
    return f"{self.__nomeE} - {self.__horarios} - {self.__mensalidade}"


class Academia:
  def __init__(self, nomeA, endereco):
    self.__nomeA = str()
    self.__esdereco = str()
    self.__esportes = []

    self.set_nomeA(nomeA)
    self.set_endereco(endereco)
    

  def set_nomeA(self, nomeA):  
    if nomeA != "": self.__nomeA = nomeA
    else: raise ValueError()

  def set_endereco(self, endereco):
    if endereco != "": self.__endereco = endereco
    else: raise ValueError()
      
  def inserir(self, e):
    self.__esportes.append(e)
    
  def listar(self):
    list = []
    for li in self.__esportes:
      list.append(li.get_nomeE())
    return list
    
  def media_mens(self):
    media = 0
    for med in self.__esportes:
      media =+ med.get_mensalidade()

    return media / len(self.__esportes)

  def __str__(self):
    return f"{self.__nomeA} - {self.__endereco} - {self.listar()}"
    #return f"{self.__nomeA} - {self.__endereco} - {self.listar()}"
  

class UI:
  @staticmethod
  def main():
    x = Esporte("Legpress", "14hs ás 21hrs", 220.00)
    y = Esporte("Barra fixa", "7hrs ás 21hrs", 100.00)
    z = Esporte("Esteira", "10hrs ás 21hrs", 160.00)
    t = Esporte(volei,"54 a 354364h", 300.33)
    
    a = Academia("Totalsaude", "Rua Monte Rei, 23253")
    
    a.inserir(x)
    a.inserir(y)
    a.inserir(z)

    print(x)
    print(y)
    print(z)
    print(t)

    print("-", end="\n")
    
    print(a)
    print(*a.listar())
    print("-", end="\n")
    
    print(f'Media: {a.media_mens():.2f} Reais')

UI.main()