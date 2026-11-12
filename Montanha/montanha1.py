import random
import json
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def grafico_energia():
    
    if os.path.exists("dados_montanha.json"):
        with open("dados_montanha.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []
    
    dados.sort(key = lambda jogador: jogador["pontos"], reverse = True)

    nomes = []
    energia = []
    
    for jogador in dados:
        nomes.append(jogador["nome"])
        energia.append(jogador["energia"])

    plt.bar(nomes, energia)

    plt.title("Ranking Geral Energia - Montanha")
    plt.xlabel("jogadores")
    plt.ylabel("Energia")

    plt.show()

def grafico_pontos():

    if os.path.exists("dados_montanha.json"):
        with open("dados_montanha.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []
    

    dados.sort(key = lambda jogador: jogador["pontos"], reverse = True)

    nomes = []
    pontuacao = []

    for jogador in dados:
        nomes.append(jogador["nome"])
        pontuacao.append(jogador["pontos"])

    plt.bar(nomes, pontuacao)

    plt.title("Ranking Geral Pontuação - Montanha")
    plt.xlabel("Jogadores")
    plt.ylabel("Pontuação")

    plt.show()

def salvar_dados(nome, pontos, energia):

    jogador = {
        "nome": nome,
        "pontos": pontos,
        "energia": energia
    }

    if os.path.exists("dados_montanha.json"):
        with open("dados_montanha.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    dados.append(jogador)

    with open("dados_montanha.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def atualizar_status():
    status.config(text=f"Energia: {energia} | Pontos: {pontos}")


def limpar_tela():
    for widget in conteudo.winfo_children():
        widget.destroy()


def escolher_caminho(descricao, caminho1, caminho2):

    limpar_tela()
    atualizar_status()

    tk.Label(conteudo, text=descricao, wraplength=550,
             font=("Arial", 12)).pack(pady=20)

    escolha = tk.IntVar()

    tk.Label(conteudo, text="1 - " + caminho1,
             wraplength=550).pack(pady=10)

    tk.Button(conteudo, text="1", width=15,
              command=lambda: escolha.set(1)).pack()

    tk.Label(conteudo, text="2 - " + caminho2,
             wraplength=550).pack(pady=10)

    tk.Button(conteudo, text="2", width=15,
              command=lambda: escolha.set(2)).pack()

    janela.wait_variable(escolha)

    print("Caminho escolhido:", escolha.get())

    return escolha.get()


def inserir_nome():

    limpar_tela()
    atualizar_status()

    tk.Label(conteudo, text="Você chegou ao topo da montanha!",
             font=("Arial", 14)).pack(pady=20)

    tk.Label(conteudo, text="Digite seu nome:").pack()

    entrada = tk.Entry(conteudo)
    entrada.pack(pady=10)

    nome = tk.StringVar()

    def confirmar():
        if entrada.get().strip():
            nome.set(entrada.get().strip())
            print("Nome do jogador:", nome.get())
        else:
            messagebox.showwarning("Atenção", "Digite seu nome!")

    tk.Button(conteudo, text="Confirmar",
              command=confirmar).pack(pady=10)

    entrada.bind("<Return>", lambda evento: confirmar())

    janela.wait_variable(nome)

    return nome.get()

def pergunta(pergunta, resposta_correta, pontos_ganhos, pontos_perdidos):

    limpar_tela()
    atualizar_status()

    tk.Label(conteudo, text=pergunta,
             font=("Arial", 14), wraplength=550).pack(pady=25)

    entrada = tk.Entry(conteudo, width=35)
    entrada.pack(pady=10)
    entrada.focus_set()

    resultado = tk.IntVar()

    def enviar_resposta():

        resposta = entrada.get().strip().lower()
        print("Resposta recebida:", resposta)

        if resposta == resposta_correta:
            print("Você acertou!")
            messagebox.showinfo("Resultado", "Você acertou!")
            resultado.set(pontos_ganhos)

        else:
            print("Você errou!")
            messagebox.showinfo("Resultado", "Você errou!")
            resultado.set(pontos_perdidos)

    tk.Button(conteudo, text="Enviar",
              command=enviar_resposta).pack(pady=10)

    entrada.bind("<Return>", lambda evento: enviar_resposta())

    janela.wait_variable(resultado)

    return resultado.get()

energia = 100
pontos = 0
janela = tk.Tk()
janela.title("Aventura na Montanha")
janela.geometry("650x500")
janela.resizable(False, False)

status = tk.Label(janela, text="", font=("Arial", 13, "bold"))
status.pack(pady=15)

conteudo = tk.Frame(janela)
conteudo.pack(expand=True, fill="both", padx=20, pady=10)

atualizar_status()

escolha1 = escolher_caminho(
    "Você encontrou uma montanha! Precisa subir ela! Você se depara com um deslizamento de pedras.",
    "Esperar as pedras pararem de cair e seguir por um caminho alternativo mais longo. (Seguro)",
    "Atravessar rapidamente uma passagem estreita entre as pedras. (Arriscado)"
)

escolha1 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha1 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Quantos dias tem uma semana?",
        "7",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é a capital do Brasil?",
        "brasília",
        20,
        -10
    )
    atualizar_status()

escolha2 = escolher_caminho(
    "Você encontrou uma grande fenda entre duas partes da montanha.",
    "Descer um pouco pela encosta e atravessar por um caminho mais estreito e seguro. (Seguro)",
    "Saltar sobre a fenda, calculando a distância e o impulso necessários. (Arriscado)"
)

escolha2 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha2 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Qual é a cor do céu em um dia ensolarado?",
        "azul",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Quantos lados tem um triângulo? ",
        "3",
        20,
        -10
    )
    atualizar_status()

escolha3 = escolher_caminho(
    "Uma árvore caída bloqueia a trilha principal.",
    "Contornar a árvore por uma trilha lateral com pouca inclinação. (Seguro)",
    "Escalar a árvore e passar por cima dela, mantendo o equilíbrio. (Arriscado)"
)

escolha3 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha3 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Quantas pernas tem uma aranha?",
        "8",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o maior oceano do mundo?",
        "oceano pacífico",
        20,
        -10
    )
    atualizar_status()

escolha4 = escolher_caminho(
    "Você chega a uma parede de rochas que precisa superar.",
    "Dar a volta pela encosta, seguindo uma trilha longa e menos inclinada. (Seguro)",
    "Escalar a parede rochosa usando pequenas fendas como apoio. (Arriscado)"
)

escolha4 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha4 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Qual animal é conhecido como rei da selva?",
        "leão",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 9 × 8?",
        "72",
        20,
        -10
    )
    atualizar_status()

escolha5 = escolher_caminho(
    "Uma neblina densa cobre a montanha, dificultando a visão.",
    "Esperar a neblina diminuir antes de continuar pela trilha sinalizada. (Seguro)",
    "Seguir por um caminho estreito usando um mapa e uma bússola. (Arriscado)"
)

escolha5 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha5 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Qual é o maior planeta do Sistema Solar?",
        "júpiter",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Quantos jogadores de cada equipe ficam em campo em uma partida de futebol?",
        "11",
        20,
        -10
    )
    atualizar_status()

escolha6 = escolher_caminho(
    "Você encontra uma ponte de cordas antiga que atravessa um precipício.",
    "Procurar uma passagem alternativa pela encosta, mesmo que seja mais longa. (Seguro)",
    "Atravessar a ponte cuidadosamente, equilibrando-se nas tábuas. (Arriscado)"
)

escolha6 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha6 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Quantos meses tem um ano?",
        "12",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 8 x 8?",
        "64",
        20,
        -10
    )
    atualizar_status()

escolha7 = escolher_caminho(
    "Uma grande quantidade de neve está deslizando pela encosta em sua direção.",
    "Esconder-se atrás de grandes rochas até que a avalanche passe. (Seguro)",
    "Correr por uma trilha íngreme para alcançar uma área segura. (Arriscado)"
)

escolha7 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha7 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Qual é o nome do satélite natural da Terra?",
        "lua",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 9 x 9? ",
        "81",
        20,
        -10
    )
    atualizar_status()

escolha8 = escolher_caminho(
    "Você encontra uma grande fenda entre duas partes da montanha.",
    "Descer um pouco pela encosta e atravessar por um caminho mais estreito e seguro. (Seguro)",
    "Saltar sobre a fenda, calculando a distância e o impulso necessários. (Arriscado)"
)

escolha8 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha8 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Qual fruta é conhecida por ser amarela e curvada?",
        "banana",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 72 / 4 ?",
        "18",
        20,
        -10
    )
    atualizar_status()

escolha9 = escolher_caminho(
    "Você encontra um enxame de abelhas que bloqueia a trilha.",
    "Fazer um desvio pela floresta, evitando se aproximar do enxame. (Seguro)",
    "Atravessar rapidamente uma área aberta próxima ao enxame. (Arriscado)"
)

escolha9 = int(input("Qual caminho vai escolher? (1/2): "))


if escolha9 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Em qual planeta vivemos?",
        "terra",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 24 x 4?",
        "96",
        20,
        -10
    )
    atualizar_status()

escolha10 = escolher_caminho(
    "Depois de uma forte chuva, parte da montanha fica coberta de lama.",
    "Seguir por um caminho rochoso mais longo e firme. (Seguro)",
    "Subir diretamente pela encosta lamacenta, usando raízes e pedras como apoio. (Arriscado)"
)

escolha10 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha10 == 1:
    perda = random.randint(20,40)
    energia -= perda
    pontos += pergunta(
        "Quantas horas tem um dia?",
        "24",
        10,
        0
    )
    atualizar_status()

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 21 / 3?",
        "7",
        20,
        -10
    )
    atualizar_status()

print("Você chegou ao topo da montanha")

nome = inserir_nome()

salvar_dados(nome,pontos,energia)

if energia > 70:

    messagebox.showinfo("FINAL ALEGRE", f"Você terminou com {energia} de energia e está ótimo(a).")

elif energia >= 30 and energia <= 69:

    messagebox.showinfo("FINAL IRÔNICO", f"Você terminou com {energia} de energia e está tão fraco que não consegue nem fazer piadas. Além de estar parecendo um zumbi")

else:

    messagebox.showinfo("FINAL SURREAL", f"Você terminou com {energia} de energia e está quase sem forças e vai precisar de suporte para voltar a como vivia antes")

grafico_pontos()
grafico_energia()

janela.destroy()