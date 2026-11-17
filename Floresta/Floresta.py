import random
import json
import matplotlib.pyplot as plt
import os

pasta = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pasta, "perguntas.json"), "r", encoding="utf-8") as arquivo:
    banco = json.load(arquivo)

def sortearPergunta(lista):
    sorteada = random.choice(lista)
    lista.remove(sorteada)
    return sorteada

def resposta(mensagem, validas):
    resposta = input(mensagem)
    while resposta not in validas:
        print("Opção inválida! Tente de novo.")
        resposta = input(mensagem)
    return resposta


def perderEnergia(energia, minimo, maximo):
    perda = random.randint(minimo, maximo)
    energia = energia - perda
    if energia < 0:
        energia = 0
    print("Você perdeu", perda, "de energia. Sua energia atual é de", energia)
    return energia


def ganharEnergia(energia, minimo, maximo):
    ganho = random.randint(minimo, maximo)
    energia = energia + ganho
    if energia > 100:
        energia = 100
    print("Você ganhou", ganho, "de energia. Sua energia atual é de", energia)
    return energia

def pontuarFacil(acertou, pontos):
    if acertou:
        pontos = pontos + 10
    return pontos


def pontuarDificil(acertou, pontos):
    if acertou:
        pontos = pontos + 20
    else:
        pontos = pontos - 10
    return pontos


def perguntas(pergunta, respostas, respostaCerta):
    print("\nPERGUNTA:", pergunta)
    print("a)", respostas[0])
    print("b)", respostas[1])
    print("c)", respostas[2])
    print("d)", respostas[3])

    escolhida = resposta("Sua resposta (a/b/c/d): ", ["a", "b", "c", "d"])

    if escolhida == respostaCerta:
        return True
    else:
        return False


def mostrarResultado(dados, energia, pontos, dificil):
    acertou = perguntas(dados["pergunta"], dados["respostas"], dados["certa"])
    if acertou:
        print("Correto!")
        energia = ganharEnergia(energia, 3, 8)
    else:
        print("Errado!")
        energia = perderEnergia(energia, 3, 8)

    if dificil:
        pontos = pontuarDificil(acertou, pontos)
    else:
        pontos = pontuarFacil(acertou, pontos)

    print("Pontuação atual:", pontos)
    return energia, pontos


def salvarPontuacao(nome, pontos, energia):
    try:
        with open(os.path.join(pasta, "placar.json"), "r", encoding="utf-8") as f:
            placar = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        placar = {}

    # converte o formato antigo (só pontos) para o novo (pontos e energia)
    for jogador in placar:
        if not isinstance(placar[jogador], dict):
            placar[jogador] = {"pontos": placar[jogador], "energia": 0}

    if nome not in placar or pontos > placar[nome]["pontos"]:
        placar[nome] = {"pontos": pontos, "energia": energia}

    with open(os.path.join(pasta, "placar.json"), "w", encoding="utf-8") as f:
        json.dump(placar, f, ensure_ascii=False, indent=4)


def mostrarGrafico():
    with open(os.path.join(pasta, "placar.json"), "r", encoding="utf-8") as f:
        placar = json.load(f)

    nomes = list(placar.keys())
    pontuacoes = []
    energias = []
    for nome in nomes:
        pontuacoes.append(placar[nome]["pontos"])
        energias.append(placar[nome]["energia"])

    posicoes = list(range(len(nomes)))
    largura = 0.4
    posPontos = [p - largura / 2 for p in posicoes]
    posEnergia = [p + largura / 2 for p in posicoes]

    plt.figure(figsize=(8, 5))
    barrasPontos = plt.bar(posPontos, pontuacoes, width=largura, label="Pontos")
    barrasEnergia = plt.bar(posEnergia, energias, width=largura, label="Energia")
    plt.bar_label(barrasPontos)
    plt.bar_label(barrasEnergia)
    plt.xticks(posicoes, nomes)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Pontuação e energia dos jogadores - Jogo da Floresta")
    plt.xlabel("Jogador")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()


def situacao(energia, pontos, texto, decisao, textoSim, textoNao):
    print(texto)
    escolha = resposta(decisao + " (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print(textoSim + "(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print(textoNao + "(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


situacoes = [
    ("Você entra na floresta.",
     "Deseja entrar na mata fechada para procurar a saída?",
     "Você adentra a mata fechada, com pouca luz e terreno irregular.",
     "Você segue a trilha aberta."),
    ("Anoitece e você tem que procurar abrigo.",
     "Deseja procurar um acampamento abandonado?",
     "Você encontra um acampamento abandonado.",
     "Você monta um acampamento com galhos e folhas."),
    ("Você está com sede.",
     "Deseja beber água do lago?",
     "Você bebe direto do lago, com risco de contaminação.",
     "Você procura uma forma de filtrar a água."),
    ("Você encontra frutas desconhecidas.",
     "Deseja comer as frutas, que você não sabe se são tóxicas?",
     "Você come as frutas, com o risco de intoxicação.",
     "Você come apenas frutas conhecidas."),
    ("Está frio e você precisa se aquecer.",
     "Deseja acender uma fogueira sem ferramentas?",
     "Você tenta acender a fogueira sem ferramentas.",
     "Você busca outra fonte de calor."),
    ("Você ouve um rosnado de onça vindo da mata.",
     "Deseja seguir por esse caminho?",
     "Você tenta espantar o animal.",
     "Você vai por outro caminho, muito mais longo."),
    ("Há uma velha ponte que atravessa um desfiladeiro.",
     "Deseja atravessar?",
     "Você atravessa a ponte.",
     "Você procura outra forma de seguir em frente."),
    ("Você encontra uma cobra descansando em seu caminho.",
     "Deseja seguir?",
     "Você passa por ela sem acordá-la.",
     "Você vai por outro caminho, muito mais longo."),
    ("Um desfiladeiro tampa seu caminho.",
     "Deseja escalar as rochas que estão bloqueando seu caminho?",
     "Você sobe pelas pedras soltas.",
     "Você busca outro caminho, mais longo."),
    ("Você sai da floresta e encontra uma montanha (troca de cenário).",
     "Deseja escalar a montanha?",
     "Você escala a montanha.",
     "Você não segue pela montanha e perde todas as perguntas daquele caminho."),
] 


def jogar():
    nomeJogador = input("Digite seu nome de jogador: ")
    print("Bem-vindo ao jogo da Floresta,", nomeJogador + "!")

    energia = 100
    pontos = 0

    for s in situacoes:
        energia, pontos = situacao(energia, pontos, s[0], s[1], s[2], s[3])
        if energia <= 0:
            print("\nSua energia acabou. Fim de jogo!")
            print("Pontuação final:", pontos)
            salvarPontuacao(nomeJogador, pontos, energia)
            mostrarGrafico()
            return

    print("\nParabéns,", nomeJogador + ", Você saiu da floresta!")
    print("Pontuação final:", pontos)
    print("Energia final:", energia)
    salvarPontuacao(nomeJogador, pontos, energia)
    mostrarGrafico()

jogar()