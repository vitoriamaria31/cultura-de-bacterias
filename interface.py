import tkinter as tk
from simulacao import Simulacao


class InterfaceGrafica:

    def __init__(self):

        # cria o objeto da simulação
        self.simulacao = Simulacao()

        # cria a janela principal da interface gráfica
        self.janela = tk.Tk()
        self.janela.title("Simulador de Cultura de Bactérias")
        self.janela.geometry("600x550")

        # cria o título da janela
        self.titulo = tk.Label(
            self.janela,
            text="Simulador de Cultura de Bactérias",
            font=("Arial", 16, "bold")
        )
        self.titulo.pack(pady=10)

        # area de texto onde os resultados da simulação aparecem
        self.resultado = tk.Text(
            self.janela,
            width=60,
            height=15
        )
        self.resultado.pack(pady=10)

        # botão para simular o crescimento bacteriano
        self.botao_ciclo = tk.Button(
            self.janela,
            text="Próximo Ciclo",
            command=self.proximo_ciclo
        )
        self.botao_ciclo.pack(pady=5)

        # botão para trocar a bactéria comum pela bactéria resistente
        self.botao_resistente = tk.Button(
            self.janela,
            text="Usar Bactéria Resistente",
            command=self.bacteria_resistente
        )
        self.botao_resistente.pack(pady=5)

        # botão para aplicar antibiótico na população bacteriana
        self.botao_antibiotico = tk.Button(
            self.janela,
            text="Aplicar Antibiótico",
            command=self.aplicar_antibiotico
        )
        self.botao_antibiotico.pack(pady=5)

        # botão para salvar os dados atuais da simulação em arquivo JSON
        self.botao_salvar = tk.Button(
            self.janela,
            text="Salvar Simulação",
            command=self.salvar_historico
        )
        self.botao_salvar.pack(pady=5)

        # mostra os dados iniciais na tela
        self.atualizar_tela()

    # atualiza as informações exibidas na área de texto
    def atualizar_tela(self):

        self.resultado.delete(1.0, tk.END)

        self.resultado.insert(
            tk.END,
            self.simulacao.mostrar_resultado()
        )

    # executa um novo ciclo da simulação
    def proximo_ciclo(self):

        self.simulacao.simular_ciclo()
        self.atualizar_tela()

    # troca a bactéria comum pela bactéria resistente
    def bacteria_resistente(self):

        self.simulacao.usar_bacteria_resistente()
        self.atualizar_tela()

    # aplica o antibiótico na população bacteriana
    def aplicar_antibiotico(self):

        self.simulacao.aplicar_antibiotico()
        self.atualizar_tela()

    # chama o método da classe Simulacao que salva os dados no JSON
    def salvar_historico(self):

        self.simulacao.salvar_historico()

    # inicia o loop principal da interface gráfica
    def executar(self):

        self.janela.mainloop()