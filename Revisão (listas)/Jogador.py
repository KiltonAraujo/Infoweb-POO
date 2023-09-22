class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome = str()
    self.__camisa = int()
    self.__gols = 0
    self.set_nome(nome)
    self.set_camisa(camisa)
    self.set_gols(gols)

  def set_nome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()

  def set_gols(self, gols):
    if gols > 0:
      self.__gols = gols
    else: raise ValueError()
      
  def set_camisa(self, camisa):
    if camisa > 0 and camisa < 100:
      self.__camisa = camisa

  def get_gols(self):
    return self.__gols
    
  def __str__(self):
    return f"{self.__nome} - Camisa: {self.__camisa} - gols totais: {self.__gols}"


class Time:
  def __init__(self, nomeT, estado):
    self.__nomeT = str()
    self.__estado = str()
    self.__jogadores = []

    self.set_nomeT(nomeT)
    self.set_estado(estado)
    
  def set_nomeT(self, nomeT):
    if nomeT != "": self.__nomeT = nomeT
    else: raise ValueError()

  def set_estado(self, estado):
    if estado != "": self.__estado = estado
    else: raise ValueError()

  def inserir(self, jogador):
    self.__jogadores.append(jogador)

  def listar(self):
    return self.__jogadores

  def artilheiro(self):
    if len(self.__jogadores) == 0: return None
    artilheiro = self.__jogadores[0]
    for j in self.__jogadores:
      if j.get_gols() > artilheiro.get_gols():
        artilheiro = j
    return artilheiro

  

class UI:
  @staticmethod
  def main():
    p1 = Jogador("andre",23, 4)
    p2 = Jogador("kill", 10, 15)
    p3 = Jogador("bungas", 3, 10)
    t = Time("ifrn", "RN")
    t.inserir(p1)
    t.inserir(p2)
    t.inserir(p3)
    print(*t.listar())
    print(t.artilheiro())
    
UI.main()