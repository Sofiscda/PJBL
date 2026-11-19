import tkinter as tk
from tkinter import messagebox

janela = None
area_texto = None
entrada = None
botao_enviar = None
quadro_opcoes = None
variavel_resposta = None


def configurar(janela_principal, texto, campo, botao, quadro):
    global janela, area_texto, entrada, botao_enviar, quadro_opcoes
    janela = janela_principal
    area_texto = texto
    entrada = campo
    botao_enviar = botao
    quadro_opcoes = quadro


def escrever(mensagem):
    area_texto.configure(state="normal")
    area_texto.insert("end", str(mensagem) + "\n")
    area_texto.see("end")
    area_texto.configure(state="disabled")
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
    """Mostra uma opção por botão e devolve o valor escolhido."""
    global variavel_resposta

    limpar_opcoes()
    entrada.configure(state="disabled")
    botao_enviar.configure(state="disabled")

    if mensagem:
        escrever(mensagem)

    variavel_resposta = tk.StringVar(master=janela)

    for opcao in opcoes:
        if isinstance(opcao, tuple):
            texto_botao, valor = opcao
        else:
            texto_botao, valor = str(opcao), str(opcao)

        tk.Button(
            quadro_opcoes,
            text=texto_botao,
            width=35,
            height=2,
            command=lambda resposta=valor: variavel_resposta.set(str(resposta))
        ).pack(pady=3)

    janela.wait_variable(variavel_resposta)
    resposta = variavel_resposta.get()
    limpar_opcoes()
    escrever("> " + resposta)
    return resposta


def input(mensagem=""):
    global variavel_resposta

    limpar_opcoes()
    if mensagem:
        escrever(mensagem)

    variavel_resposta = tk.StringVar(master=janela, value="__aguardando__")
    entrada.configure(state="normal")
    entrada.delete(0, "end")
    entrada.focus_set()
    botao_enviar.configure(state="normal")

    def enviar(event=None):
        if variavel_resposta.get() != "__aguardando__":
            return
        variavel_resposta.set(entrada.get())
        entrada.configure(state="disabled")
        botao_enviar.configure(state="disabled")

    botao_enviar.configure(command=enviar)
    entrada.bind("<Return>", enviar)
    janela.wait_variable(variavel_resposta)
    resposta = variavel_resposta.get()
    escrever("> " + resposta)
    entrada.unbind("<Return>")
    return resposta


def limpar():
    area_texto.configure(state="normal")
    area_texto.delete("1.0", "end")
    area_texto.configure(state="disabled")
    limpar_opcoes()


def aviso(titulo, mensagem):
    messagebox.showinfo(titulo, mensagem, parent=janela)
