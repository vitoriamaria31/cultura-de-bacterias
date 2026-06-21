from modelos.bacteria import Bacteria
from modelos.bacteria_resistente import BacteriaResistente
from modelos.ambiente import Ambiente
from modelos.antibiotico import Antibiotico


class Simulacao:

    def __init__(self):
        self.bacteria = Bacteria("E. coli", 100, 0.25)
        self.ambiente = Ambiente(37, 80)
        self.antibiotico = Antibiotico("Penicilina", 0.30)
        self.ciclo = 0

    def simular_ciclo(self):
        self.ciclo += 1
        self.bacteria.crescer()
        return self.mostrar_resultado()

    def usar_bacteria_resistente(self):
        self.bacteria = BacteriaResistente("E. coli resistente", 100, 0.25, 70)

    def aplicar_antibiotico(self):
        populacao_atual = self.bacteria.get_populacao()
        eficacia = self.antibiotico.get_eficacia()

        reducao = int(populacao_atual * eficacia)
        nova_populacao = populacao_atual - reducao

        self.bacteria._Bacteria__populacao = nova_populacao

        return self.mostrar_resultado()

    def mostrar_resultado(self):
        resultado = f"Ciclo: {self.ciclo}\n\n"
        resultado += self.bacteria.mostrar_dados()
        resultado += "\n\n"
        resultado += self.ambiente.mostrar_dados()
        resultado += "\n\n"
        resultado += self.antibiotico.mostrar_dados()

        return resultado