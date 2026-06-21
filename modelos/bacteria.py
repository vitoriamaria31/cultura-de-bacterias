# Classe Bacteria
# Esta classe representa uma bactéria comum da simulação.

class Bacteria:

    # Método construtor
    # É executado automaticamente quando criamos um objeto.
    def __init__(self, nome, populacao, taxa_crescimento):

        # Encapsulamento:
        # Os atributos são "privados" usando __
        self.__nome = nome
        self.__populacao = populacao
        self.__taxa_crescimento = taxa_crescimento

    # get para retornar o nome
    def get_nome(self):
        return self.__nome

    # get para retornar a população
    def get_populacao(self):
        return self.__populacao

    # método responsável pelo crescimento bacteriano
    def crescer(self):

        aumento = int(self.__populacao * self.__taxa_crescimento)

        self.__populacao += aumento

    # método para mostrar informações da bactéria
    def mostrar_dados(self):

        return (
            f"Espécie: {self.__nome}\n"
            f"População: {self.__populacao}"
        )