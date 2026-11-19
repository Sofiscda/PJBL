import tkinter as tk
from tkinter import messagebox

from interface import configurar, limpar
from Caverna import pjblCaverna2
from Floresta import Floresta
from Montanha import montanha1


class Jogo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Aventura - Escolha sua fase")
        self.janela.geometry("760x600")
        self.janela.minsize(650, 500)
        self.fase_atual = None

        titulo = tk.Label(janela, text="AVENTURA", font=("Arial", 22, "bold"))
        titulo.pack(pady=(15, 5))

        self.subtitulo = tk.Label(
            janela,
            text="Escolha por qual fase deseja começar.",
            font=("Arial", 11)
        )
        self.subtitulo.pack(pady=(0, 10))

        self.area = tk.Text(janela, height=20, wrap="word", state="disabled", font=("Arial", 10))
        self.area.pack(fill="both", expand=True, padx=20, pady=8)

        quadro_entrada = tk.Frame(janela)
        quadro_entrada.pack(fill="x", padx=20, pady=5)
        self.entrada = tk.Entry(quadro_entrada, state="disabled")
        self.entrada.pack(side="left", fill="x", expand=True, ipady=6)
        self.botao_enviar = tk.Button(quadro_entrada, text="Enviar", state="disabled")
        self.botao_enviar.pack(side="left", padx=(8, 0))
        configurar(janela, self.area, self.entrada, self.botao_enviar)

        self.menu = tk.Frame(janela)
        self.menu.pack(pady=12)
        self.mostrar_menu_inicial()

    def limpar_menu(self):
        for widget in self.menu.winfo_children():
            widget.destroy()

    def mostrar_menu_inicial(self):
        self.limpar_menu()
        self.subtitulo.config(text="Escolha por qual fase deseja começar.")
        opcoes = [
            ("Montanha", self.iniciar_montanha),
            ("Caverna", self.iniciar_caverna),
            ("Floresta", self.iniciar_floresta),
        ]
        for texto, comando in opcoes:
            tk.Button(self.menu, text=texto, width=18, command=comando).pack(side="left", padx=7)

    def preparar_fase(self, nome):
        self.fase_atual = nome
        self.limpar_menu()
        limpar()
        self.subtitulo.config(text=f"Fase atual: {nome}")
        self.entrada.configure(state="disabled")
        self.botao_enviar.configure(state="disabled")

    def iniciar_caverna(self):
        self.preparar_fase("Caverna")
        try:
            resultado = pjblCaverna2.iniciar_caverna()
            self.finalizar_fase(resultado, pjblCaverna2.mostrar_grafico)
        except Exception as erro:
            self.tratar_erro(erro)

    def iniciar_floresta(self):
        self.preparar_fase("Floresta")
        try:
            resultado = Floresta.jogar()
            self.finalizar_fase(resultado, Floresta.mostrarGrafico)
        except Exception as erro:
            self.tratar_erro(erro)

    def iniciar_montanha(self):
        self.preparar_fase("Montanha")
        self.janela.withdraw()
        try:
            resultado = montanha1.iniciar_montanha(self.janela)
            self.janela.deiconify()
            self.finalizar_fase(resultado, self.grafico_montanha)
        except Exception as erro:
            self.janela.deiconify()
            self.tratar_erro(erro)

    @staticmethod
    def grafico_montanha():
        montanha1.grafico_pontos()
        montanha1.grafico_energia()

    def finalizar_fase(self, resultado, funcao_grafico):
        if not resultado:
            resultado = {"jogador": "Jogador", "pontos": 0, "energia": 0}
        self.subtitulo.config(
            text=f"{self.fase_atual} concluída | Pontos: {resultado['pontos']} | Energia: {resultado['energia']}"
        )
        self.entrada.configure(state="disabled")
        self.botao_enviar.configure(state="disabled")
        self.limpar_menu()
        tk.Label(self.menu, text="O que deseja fazer agora?", font=("Arial", 11, "bold")).pack(pady=5)
        tk.Button(self.menu, text="Ver gráfico desta fase", width=24,
                  command=lambda: self.abrir_grafico(funcao_grafico)).pack(pady=4)
        tk.Button(self.menu, text="Escolher outra fase", width=24,
                  command=self.mostrar_menu_inicial).pack(pady=4)
        tk.Button(self.menu, text="Encerrar jogo", width=24,
                  command=self.janela.destroy).pack(pady=4)

    def abrir_grafico(self, funcao):
        try:
            funcao()
        except Exception as erro:
            self.tratar_erro(erro)

    def tratar_erro(self, erro):
        messagebox.showerror("Erro na fase", f"Ocorreu um erro:\n{erro}", parent=self.janela)
        self.janela.deiconify()
        self.mostrar_menu_inicial()


if __name__ == "__main__":
    janela = tk.Tk()
    jogo = Jogo(janela)
    janela.mainloop()
