class Pessoa:
    nome = ""
    idade = 0
    def __init__ (self,nome,idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f"Olá! Meu nome é {self.nome}")

p1 = Pessoa ("Weverton Antonio",20)
p1.falar()

p2 = Pessoa ("Elyabe",19)
p2.falar()
