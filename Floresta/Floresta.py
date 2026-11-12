import random
import json
import matplotlib.pyplot as plt


with open("perguntas.json", "r", encoding="utf-8") as arquivo:
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
        with open("placar.json", "r", encoding="utf-8") as f:
            placar = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        placar = {}

    # converte o formato antigo (só pontos) para o novo (pontos e energia)
    for jogador in placar:
        if not isinstance(placar[jogador], dict):
            placar[jogador] = {"pontos": placar[jogador], "energia": 0}

    if nome not in placar or pontos > placar[nome]["pontos"]:
        placar[nome] = {"pontos": pontos, "energia": energia}

    with open("placar.json", "w", encoding="utf-8") as f:
        json.dump(placar, f, ensure_ascii=False, indent=4)


def mostrarGrafico():
    with open("placar.json", "r", encoding="utf-8") as f:
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


def situacao1(energia, pontos):
    print("Você entra na floresta.")
    escolha = resposta("Deseja entrar na mata fechada para procurar a saída? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você adentra a mata fechada, com pouca luz e terreno irregular.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você segue a trilha aberta.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao2(energia, pontos):
    print("Anoitece e você tem que procurar abrigo.")
    escolha = resposta("Deseja procurar um acampamento abandonado? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você encontra um acampamento abandonado.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você monta um acampamento com galhos e folhas.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao3(energia, pontos):
    print("Você está com sede.")
    escolha = resposta("Deseja beber água do lago? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você bebe direto do lago, com risco de contaminação.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você procura uma forma de filtrar a água.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao4(energia, pontos):
    print("Você encontra frutas desconhecidas.")
    escolha = resposta("Deseja comer as frutas, que você não sabe se são tóxicas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você come as frutas, com o risco de intoxicação.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você come apenas frutas conhecidas.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao5(energia, pontos):
    print("Está frio e você precisa se aquecer.")
    escolha = resposta("Deseja acender uma fogueira sem ferramentas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta acender a fogueira sem ferramentas.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você busca outra fonte de calor.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao6(energia, pontos):
    print("Você ouve um rosnado de onça vindo da mata.")
    escolha = resposta("Deseja seguir por esse caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta espantar o animal.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao7(energia, pontos):
    print("Há uma velha ponte que atravessa um desfiladeiro.")
    escolha = resposta("Deseja atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você atravessa a ponte.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você procura outra forma de seguir em frente.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao8(energia, pontos):
    print("Você encontra uma cobra descansando em seu caminho.")
    escolha = resposta("Deseja seguir? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você passa por ela sem acordá-la.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao9(energia, pontos):
    print("Um desfiladeiro tampa seu caminho.")
    escolha = resposta("Deseja escalar as rochas que estão bloqueando seu caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você sobe pelas pedras soltas.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você busca outro caminho, mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def situacao10(energia, pontos):
    print("Você chega à margem de um riacho (troca de cenário).")
    escolha = resposta("Deseja montar um bote improvisado para atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você monta um bote improvisado com troncos e cipós.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
        dificil = True
    else:
        print("Você não segue pelo caminho e perde todas as perguntas daquele caminho.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])
        dificil = False

    return mostrarResultado(dados, energia, pontos, dificil)


def jogar():
    nomeJogador = input("Digite seu nome de jogador: ")
    print("Bem-vindo ao jogo da Floresta,", nomeJogador + "!")

    energia = 100
    pontos = 0

    situacoes = [situacao1, situacao2, situacao3, situacao4, situacao5,
                 situacao6, situacao7, situacao8, situacao9, situacao10]

    for situacao in situacoes:
        energia, pontos = situacao(energia, pontos)
        if energia <= 0:
            print("\nSua energia acabou. Fim de jogo!")
            print("Pontuação final:", pontos)
            salvarPontuacao(nomeJogador, pontos, energia)
            mostrarGrafico()
            return

    print("\nParabéns,", nomeJogador + ", Você saiu da floresta!")
    print("Pontuação final:", pontos)
    salvarPontuacao(nomeJogador, pontos, energia)
    mostrarGrafico()

jogar()