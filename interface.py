import tkinter as tk
from tkinter import messagebox, simpledialog

janela = None
area_texto = None
quadro_opcoes = None
variavel_resposta = None
_historico = []


def configurar(janela_principal, texto, quadro):
    global janela, area_texto, quadro_opcoes, _historico
    janela = janela_principal
    area_texto = texto
    quadro_opcoes = quadro
    _historico = []


def escrever(mensagem):
    global _historico
    _historico.append(str(mensagem))
    # Mantém a tela legível, mostrando as mensagens mais recentes.
    _historico = _historico[-7:]
    area_texto.configure(text="\n\n".join(_historico))
    janela.update_idletasks()


def print(*valores, sep=" ", end="\n", **kwargs):
    mensagem = sep.join(str(valor) for valor in valores)
    if end != "\n":
        mensagem += end
    escrever(mensagem.rstrip("\n"))


def limpar_opcoes():
    for widget in quadro_opcoes.winfo_children():
        widget.destroy()


def escolher_opcao(mensagem, opcoes):
    global variavel_resposta
    limpar_opcoes()
    if mensagem:
        escrever(mensagem)

    variavel_resposta = tk.StringVar(master=janela)

    for indice, opcao in enumerate(opcoes, start=1):
        if isinstance(opcao, tuple):
            texto_botao, valor = opcao
        else:
            texto_botao, valor = f"{indice} - {opcao}", str(opcao)

        tk.Button(
            quadro_opcoes,
            text=texto_botao,
            font=("Arial", 10),
            width=48,
            height=2,
            command=lambda resposta=valor: variavel_resposta.set(str(resposta))
        ).pack(pady=5)

    janela.wait_variable(variavel_resposta)
    resposta = variavel_resposta.get()
    limpar_opcoes()
    escrever("Você escolheu: " + resposta)
    return resposta


def input(mensagem=""):
    if mensagem:
        escrever(mensagem)
    resposta = simpledialog.askstring("Aventura", mensagem or "Digite sua resposta:", parent=janela)
    return resposta or ""


def limpar():
    global _historico
    _historico = []
    area_texto.configure(text="")
    limpar_opcoes()


def aviso(titulo, mensagem):
    messagebox.showinfo(titulo, mensagem, parent=janela)
