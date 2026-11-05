import random
import json
energia = 100   

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


def mostrarResultado(dados):
    acertou = perguntas(dados["pergunta"], dados["respostas"], dados["certa"])
    if acertou:
        print("Correto!")
    else:
        print("Errado!")

def situacao1():
    print("\nSituacao 1")
    print("Você entra na floresta.")
    escolha = resposta("Deseja entrar na mata fechada para procurar a saída? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você adentra a mata fechada, com pouca luz e terreno irregular.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você segue a trilha aberta.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia

def situacao2():
    print("\nSituacao 2")
    print("Anoitece e você tem que procurar abrigo.")
    escolha = resposta("Deseja procurar um acampamento abandonado? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você encontra um acampamento abandonado.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você monta um acampamento com galhos e folhas.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia

def situacao3():
    print("\nSituacao 3")
    print("Você está com sede.")
    escolha = resposta("Deseja beber água do lago? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você bebe direto do lago, com risco de contaminação.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você procura uma forma de filtrar a água.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao4():
    print("\nSituacao 4")
    print("Você encontra frutas desconhecidas.")
    escolha = resposta("Deseja comer as frutas, que você não sabe se são tóxicas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você come as frutas, com o risco de intoxicação.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você come apenas frutas conhecidas.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao5():
    print("\nSituacao 5")
    print("Está frio e você precisa se aquecer.")
    escolha = resposta("Deseja acender uma fogueira sem ferramentas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta acender a fogueira sem ferramentas.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você busca outra fonte de calor.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao6():
    print("\nSituacao 6")
    print("Você ouve um rosnado de onça vindo da mata.")
    escolha = resposta("Deseja seguir por esse caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta espantar o animal.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao7():
    print("\nSituacao 7")
    print("Há uma velha ponte que atravessa um desfiladeiro.")
    escolha = resposta("Deseja atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você atravessa a ponte.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você procura outra forma de seguir em frente.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao8():
    print("\nSituacao 8")
    print("Você encontra uma cobra descansando em seu caminho.")
    escolha = resposta("Deseja seguir? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você passa por ela sem acordá-la.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia

def situacao9():
    print("\nSituacao 9")
    print("Um desfiladeiro tampa seu caminho.")
    escolha = resposta("Deseja escalar as rochas que estão bloqueando seu caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você sobe pelas pedras soltas.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você busca outro caminho, mais longo.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def situacao10():
    print("\nSituacao 10")
    print("Você chega à margem de um riacho (troca de cenário).")
    escolha = resposta("Deseja montar um bote improvisado para atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você monta um bote improvisado com troncos e cipós.(Poupou energia)")
        energia = perderEnergia(energia, 0, 5)
        dados = sortearPergunta(banco["dificeis"])
    else:
        print("Você não segue pelo caminho e perde todas as perguntas daquele caminho.(Gastou energia)")
        energia = perderEnergia(energia, 5, 10)
        dados = sortearPergunta(banco["faceis"])

    mostrarResultado(dados)
    return energia


def jogar():
    nomeJogador = input("Digite seu nome de jogador: ")
    print("Bem-vindo ao jogo da Floresta,", nomeJogador + "!")

    energia = 100

    energia = situacao1(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao2(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao3(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao4(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao5(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao6(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao7(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao8(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao9(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    energia = situacao10(energia)
    if energia <= 0:
        print("\nSua energia acabou. Fim de jogo!")
        return

    print("\nParabéns,", nomeJogador + ", Você saiu da floresta!")

jogar()