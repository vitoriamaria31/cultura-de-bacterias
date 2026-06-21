import tkinter as tk
from simulacao import Simulacao


class InterfaceGrafica:

    def __init__(self):

        # cria o objeto da simulação
        self.simulacao = Simulacao()

        # janela principal
        self.janela = tk.Tk()
        self.janela.title("Simulador de Cultura de Bactérias")
        self.janela.geometry("600x500")

        # título
        self.titulo = tk.Label(
            self.janela,
            text="Simulador de Cultura de Bactérias",
            font=("Arial", 16, "bold")
        )
        self.titulo.pack(pady=10)

        # área de texto para mostrar resultados
        self.resultado = tk.Text(
            self.janela,
            width=60,
            height=15
        )
        self.resultado.pack(pady=10)

        # botão para simular crescimento
        self.botao_ciclo = tk.Button(
            self.janela,
            text="Próximo Ciclo",
            command=self.proximo_ciclo
        )
        self.botao_ciclo.pack(pady=5)

        # botão para usar bactéria resistente
        self.botao_resistente = tk.Button(
            self.janela,
            text="Usar Bactéria Resistente",
            command=self.bacteria_resistente
        )
        self.botao_resistente.pack(pady=5)

        # botão para aplicar antibiótico
        self.botao_antibiotico = tk.Button(
            self.janela,
            text="Aplicar Antibiótico",
            command=self.aplicar_antibiotico
        )
        self.botao_antibiotico.pack(pady=5)

        # mostra dados iniciais
        self.atualizar_tela()

    def atualizar_tela(self):

        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(
            tk.END,
            self.simulacao.mostrar_resultado()
        )

    def proximo_ciclo(self):

        self.simulacao.simular_ciclo()
        self.atualizar_tela()

    def bacteria_resistente(self):

        self.simulacao.usar_bacteria_resistente()
        self.atualizar_tela()

    def aplicar_antibiotico(self):

        self.simulacao.aplicar_antibiotico()
        self.atualizar_tela()

    def executar(self):

        self.janela.mainloop()