# Classe Ambiente
# Responsável por armazenar as condições do cultivo

class Ambiente:

    def __init__(self, temperatura, nutrientes):

        # temperatura do ambiente
        self.__temperatura = temperatura

        # quantidade de nutrientes disponível
        self.__nutrientes = nutrientes

    # get da temperatura
    def get_temperatura(self):
        return self.__temperatura

    # get dos nutrientes
    def get_nutrientes(self):
        return self.__nutrientes

    # set da temperatura
    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    # set dos nutrientes
    def set_nutrientes(self, nutrientes):
        self.__nutrientes = nutrientes

    # exibe informações do ambiente
    def mostrar_dados(self):

        return (
            f"Temperatura: {self.__temperatura} °C\n"
            f"Nutrientes: {self.__nutrientes}%"
        )