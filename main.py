import tkinter as tk
from tkinter import messagebox

from interface import configurar, limpar
from Caverna import pjblCaverna2
from Floresta import Floresta
from Montanha import montanha1


class Jogo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Aventura")
        self.janela.geometry("760x560")
        self.janela.minsize(650, 500)
        self.fase_atual = None
        self.funcao_grafico_atual = None

        self.status = tk.Label(
            janela, text="AVENTURA", font=("Arial", 20, "bold")
        )
        self.status.pack(pady=(22, 8))

        self.subtitulo = tk.Label(
            janela,
            text="Escolha sua jornada!",
            font=("Arial", 12),
            wraplength=620,
            justify="center"
        )
        self.subtitulo.pack(pady=(8, 24))

        self.area = tk.Label(
            janela,
            text="",
            font=("Arial", 13),
            wraplength=590,
            justify="center",
            height=9,
            anchor="center"
        )
        self.area.pack(fill="both", expand=True, padx=30, pady=10)

        self.quadro_opcoes = tk.Frame(janela)
        self.quadro_opcoes.pack(pady=15)

        configurar(janela, self.area, self.quadro_opcoes)
        self.mostrar_menu_inicial()

    def limpar_opcoes(self):
        for widget in self.quadro_opcoes.winfo_children():
            widget.destroy()

    def criar_botao(self, texto, comando, largura=28):
        tk.Button(
            self.quadro_opcoes,
            text=texto,
            width=largura,
            height=2,
            font=("Arial", 10),
            command=comando
        ).pack(pady=6)

    def mostrar_menu_inicial(self):
        limpar()
        self.limpar_opcoes()
        self.fase_atual = None
        self.status.config(text="AVENTURA")
        self.subtitulo.config(text="Escolha por qual fase deseja começar.")
        self.area.config(text="Prepare-se para enfrentar desafios, responder perguntas e administrar sua energia!")
        self.criar_botao("Montanha", lambda: self.mostrar_intro("Montanha", self.iniciar_montanha))
        self.criar_botao("Caverna", lambda: self.mostrar_intro("Caverna", self.iniciar_caverna))
        self.criar_botao("Floresta", lambda: self.mostrar_intro("Floresta", self.iniciar_floresta))

    def mostrar_intro(self, nome, iniciar):
        limpar()
        self.limpar_opcoes()
        self.fase_atual = nome
        self.status.config(text=f"Aventura na {nome}")
        self.subtitulo.config(text=f"Você chegou à fase da {nome.lower()}!")
        self.area.config(text="Prepare-se para enfrentar os desafios desta fase. Faça suas escolhas pelos botões e tente chegar ao final com energia e pontos!")
        self.criar_botao("Começar", iniciar)
        self.criar_botao("Voltar", self.mostrar_menu_inicial)

    def preparar_fase(self, nome):
        self.fase_atual = nome
        self.limpar_opcoes()
        limpar()
        self.status.config(text=f"Aventura na {nome}")
        self.subtitulo.config(text="Energia e pontuação serão atualizadas durante a aventura.")
        self.area.config(text="")

    def iniciar_caverna(self):
        self.preparar_fase("Caverna")
        try:
            resultado = pjblCaverna2.iniciar_caverna()
            self.finalizar_fase(resultado, lambda: pjblCaverna2.mostrar_grafico(pjblCaverna2.carregar_resultados()))
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
        self.funcao_grafico_atual = funcao_grafico
        self.limpar_opcoes()
        self.status.config(text=f"Fase {self.fase_atual} concluída!")
        self.subtitulo.config(text=f"Jogador: {resultado.get('jogador', 'Jogador')} | Pontos: {resultado.get('pontos', 0)} | Energia: {resultado.get('energia', 0)}")
        self.area.config(text="Parabéns por concluir esta etapa! O que deseja fazer agora?")
        self.criar_botao("Ver gráfico desta fase", lambda: self.abrir_grafico(funcao_grafico))
        self.criar_botao("Escolher outra fase", self.mostrar_menu_inicial)
        self.criar_botao("Encerrar jogo", self.janela.destroy)

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
    janela.state("zoomed")
    jogo = Jogo(janela)
    janela.mainloop()
