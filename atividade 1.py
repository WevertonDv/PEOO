class ConcertoMusical:
    nome_conserto = ""
    horario_concerto = ""
    sala = 0
    assentos_disponiveis = 0

    def __init__ (self,nome_conserto,horario_concerto,sala,assentos_disponiveis):
        self.nome_conserto = nome_conserto
        self.horario_concerto = horario_concerto
        self.sala = sala
        self.assentos_disponiveis = assentos_disponiveis

    def vender_ingressos(self,quantidade):
        if self.assentos_disponiveis < quantidade:
            print("Infelismente a quantidade solicitada esta insdisponivel.")

        else:
            self.assentos_disponiveis = self.assentos_disponiveis - quantidade
            print(f"Concluimos sua reserva de {quantidade}.")
    def verificar_lotacao(self):
        if self.assentos_disponiveis == 0:
            print("O concerto esta lotado.")
        else:
            print(f"há {self.assentos_disponiveis} disponiveis.")

    def exibir_informacoes(self):
        print(f"O nome do concerto é:{self.nome_conserto}.")
        print(f"O horario do conserto é:{self.horario_concerto}")
        print(f"A sala será: {self.sala}")
        print(f"Ainda tem {self.assentos_disponiveis}.")  

concerto_1 = ConcertoMusical ("rock","00:00",5,800)
concerto_1.exibir_informacoes()
concerto_1.vender_ingressos(500)
concerto_1.verificar_lotacao()