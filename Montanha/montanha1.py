import random
import json
import os
import matplotlib.pyplot as plt

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

def pergunta(pergunta, resposta_correta, pontos_ganhos, pontos_perdidos):

    print(pergunta)
    resposta = input("Escreva: ").lower()

    if resposta == resposta_correta:
        print("Você acertou!")
        return pontos_ganhos

    else:
        print("Você errou!")
        return pontos_perdidos


energia = 100
pontos = 0


print(f"Energia atual: {energia}")

print("Você encontrou uma montanha!")
print("Precisa subir ela!")
print("Você está subindo a montanha quando se depara com um deslizamento de pedras que bloqueia o caminho, escolha:")
print("1- esperar as pedras pararem de cair e seguir por um caminho alternativo mais longo. (Segura)")
print("2- atravessar rapidamente uma passagem estreita entre as pedras, exigindo agilidade e atenção. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é a capital do Brasil?",
        "brasília",
        20,
        -10
    )

print("Você encontrou uma grande fenda entre duas partes da montanha, impedindo a passagem pela trilha principal. Escolha:")
print("1- Descer um pouco pela encosta e atravessar por um caminho mais estreito e seguro. (Seguro)")
print("2- Saltar sobre a fenda, calculando a distância e o impulso necessários para alcançar o outro lado. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Quantos lados tem um triângulo? ",
        "3",
        20,
        -10
    )

print("Uma árvore caída bloqueia a trilha principal, impedindo sua passagem. Escolha")
print("1- contornar a árvore por uma trilha lateral com pouca inclinação. (Seguro)")
print("2- escalar a árvore e passar por cima dela, mantendo o equilíbrio. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o maior oceano do mundo?",
        "oceano pacífico",
        20,
        -10
    )

print("Você chega a uma parede de rochas que precisa superar para alcançar uma parte mais alta da montanha. Escolha:")
print("1- dar a volta pela encosta, seguindo uma trilha longa e menos inclinada. (Segura)")
print("2- escalar a parede rochosa usando pequenas fendas como apoio. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 9 × 8?",
        "72",
        20,
        -10
    )

print("Uma neblina densa cobre a montanha, dificultando a visão e tornando o caminho perigoso. Escolha:")
print("1- parar e esperar a neblina diminuir antes de continuar pela trilha sinalizada. (Segura)")
print("2- seguir por um caminho estreito usando um mapa e uma bússola para se orientar. (Arriscada)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Quantos jogadores de cada equipe ficam em campo em uma partida de futebol?",
        "11",
        20,
        -10
    )

print("Durante a subida, você encontra uma ponte de cordas antiga que atravessa um precipício. Algumas tábuas estão quebradas e as cordas estão desgastadas. Escolha:")
print("1- procurar uma passagem alternativa pela encosta, mesmo que seja mais longa. (Segura)")
print("2- atravessar a ponte cuidadosamente, equilibrando-se nas tábuas e segurando as cordas.(Arriscada)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 8 x 8?",
        "64",
        20,
        -10
    )

print("Durante a subida, o jogador percebe que uma grande quantidade de neve está deslizando pela encosta em sua direção. Escolha:")
print("1- esconder-se atrás de grandes rochas até que a avalanche passe. (Segura)")
print("2- correr por uma trilha íngreme para alcançar uma área segura antes que a neve chegue. (Arriscada)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 9 x 9? ",
        "81",
        20,
        -10
    )

print("O jogador encontra uma grande fenda entre duas partes da montanha, impedindo a passagem pela trilha principal. Escolha:")
print("1- descer um pouco pela encosta e atravessar por um caminho mais estreito e seguro. (Seguro)")
print("2- saltar sobre a fenda, calculando a distância e o impulso necessários para alcançar o outro lado. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 72 / 4 ?",
        "18",
        20,
        -10
    )

print("Perto de algumas árvores e flores da montanha, o jogador encontra um enxame de abelhas que bloqueia a trilha. Escolha:")
print("1- fazer um desvio pela floresta, evitando se aproximar do enxame. (Seguro)")
print("2- atravessar rapidamente uma área aberta próxima ao enxame, desviando das abelhas. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 24 x 4?",
        "96",
        20,
        -10
    )

print("Depois de uma forte chuva, parte da montanha fica coberta de lama, tornando a subida instável e perigosa. Escolha:")
print("1- seguir por um caminho rochoso mais longo, onde há maior firmeza para caminhar. (Seguro)")
print("2- subir diretamente pela encosta lamacenta, mantendo o equilíbrio e usando raízes e pedras como apoio. (Arriscado)")

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

else:
    perda = random.randint(10,25)
    energia -= perda
    pontos += pergunta(
        "Qual é o resultado de 21 / 3?",
        "7",
        20,
        -10
    )

print("Você chegou ao topo da montanha")

nome = input("Digite seu nome:")

salvar_dados(nome,pontos,energia)

if energia > 70:
    print(f"FINAL ALEGRE - Você terminou com {energia} de energia e está ótimo(a).")
elif energia >= 30 and energia <= 69:
    print(f"FINAL IRÔNICO - Você terminou com {energia} de energia e está tão fraco que não consegue nem fazer piadas. Além de estar parecendo um zumbi")
else:
    print(f"FINAL SURREAL - Você terminou com {energia} de energia e está quase sem forças e vai precisar de suporte para voltar a como vivia antes")

grafico_pontos()
grafico_energia()