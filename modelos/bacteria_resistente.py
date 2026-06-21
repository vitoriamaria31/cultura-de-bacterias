# Importamos a classe Bacteria para que a nova classe possa herdá-la
from modelos.bacteria import Bacteria


# Classe filha
# Herda todas as características da classe Bacteria
class BacteriaResistente(Bacteria):

    # construtor da classe filha
    def __init__(self, nome, populacao, taxa_crescimento, resistencia):

        # chama o construtor da classe mãe
        super().__init__(nome, populacao, taxa_crescimento)

        # atributo exclusivo da bactéria resistente
        self.__resistencia = resistencia

    # get da resistência
    def get_resistencia(self):
        return self.__resistencia

    # POLIMORFISMO
    def crescer(self):

        # bactérias resistentes crescem mais rápido
        for _ in range(2):
            super().crescer()

    # outro método 
    def mostrar_resistencia(self):
        return f"Resistência: {self.__resistencia}%"