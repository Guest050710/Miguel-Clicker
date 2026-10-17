version = "Super Alpha Beta Limited"

class Jogador():
    def __init__(self, nome):
        self.nome = nome

        self.dinheiro = 0
        self.dps = 0

    def adicionarDinheiro(self):
        self.dinheiro += 1

jogador = Jogador(nome="Miguel")