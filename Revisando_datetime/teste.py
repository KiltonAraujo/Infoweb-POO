import datetime

class Cliente:
    def __init__(self, nome, nascimento, numero):
        self.__nome = nome
        self.__nascimento = str()
        self.__numero = numero

        self.set_nascimento(nascimento)

    def set_nascimento(self, nas):
        self.set_nascimento = datetime.datetime.strptime(nas, "%d/%m/%Y")

    def get_nas(self):
        return self.__nascimento

    def __str__(self):
        return f"Nome: {self.__nome} - Data de nascimento: {self.__nascimento}"

a = Cliente("kilton", "24/05/2006", "87791398")
print(a)
