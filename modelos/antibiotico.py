# Classe Antibiotico
# Representa um antibiótico utilizado no experimento

class Antibiotico:

    def __init__(self, nome, eficacia):

        # nome do antibiótico
        self.__nome = nome

        # eficácia (0 a 1)
        self.__eficacia = eficacia

    # get do nome
    def get_nome(self):
        return self.__nome

    # get da eficácia
    def get_eficacia(self):
        return self.__eficacia

    # método que exibe os dados do antibiótico
    def mostrar_dados(self):

        return (
            f"Antibiótico: {self.__nome}\n"
            f"Eficácia: {self.__eficacia * 100}%"
        )