import datetime

class Recorde:
    def __init__(self, atleta, nacionalidade, data, tempo):
        self.__atleta = str()
        self.__nacionalidade = str()
        self.__data = str()
        self.__tempo = str()

        self.set_atleta(atleta)
        self.set_nacionalidade(nacionalidade)
        self.set_data(data)
        self.set_tempo(tempo)
        

    def set_atleta(self, nome):
        if nome != "": self.__atleta = nome
        else: ValueError()

    def set_nacionalidade(self, nas):
        if nas != "": self.__nacionalidade = nas
        else: ValueError()

    def set_data(self, data):
        self.__data = datetime.datetime.strptime(data, "%d/%m/%Y")

    def set_tempo(self, tempo):
        mins, secs = map(int, tempo.split(':'))
        self.__tempo = datetime.timedelta(minutes=mins, seconds=secs)

    def get_atleta(self):
        return self.__atleta
    def get_nacionalidade(self):
        return self.__nacionalidade
    def get_data(self):
        return self.__data
    def get_tempo(self):
        return self.__tempo
    
class Esporte:
    def __init__(self, nome, prova):
        self.__nomeE = str()
        self.__prova = str()
        self.__recordes = []

    def set_nomeE(self, nome):
        if nome != "": self.__nomeE = nome
        else: ValueError()

    def set_prova(self, nome):
        if nome != "": self.__prova = nome
        else: ValueError()

    def inserir(self, atleta):
        self.__recordes.append(atleta)

    def listar(self):
        list = []
        for li in self.__recordes:
            list.append(li.get_atleta())
        return list
    
    def menor_tempo(self):
        var = datetime.timedelta(minutes=10, seconds=59)
        for obj in self.__recordes:
            temp = obj.get_tempo()
            if temp < var:
                var = temp
        return f"Tempo recorde: {var}"


    def __str__(self):
        return f"Esporte: {self.__nomeE} - Prova: {self.__prova}"
    


class UI:
    @staticmethod
    def menu():
        print("1-Inserir atleta 2-listar 3-recorde 0-fim")   
        return int(input())
    @staticmethod
    def main():
        op = 5
        x = Esporte("Corrida", "100m")
        while op != 0:
            op = UI.menu()
            if op == 1:
                nome = input("nome: ")
                nacionalidade = input("nacionalidade: ")
                data = input("data do recorde: ")
                tempo = input("tempo do recorde: ")
                a = Recorde(nome,nacionalidade,data,tempo)
                x.inserir(a)

            if op == 2:
                print(x.listar())
            
            if op == 3:
                print(x.menor_tempo())
UI.main()