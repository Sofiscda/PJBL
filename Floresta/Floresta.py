import random


def resposta(mensagem, validas):
    resposta = input(mensagem)
    while resposta not in validas:
        print("Opção inválida! Tente de novo.")
        resposta = input(mensagem)
    return resposta


def perderEnergia(energia, minimo, maximo):
    perda = random.randint(0, 5)
    energia = energia - perda
    if energia < 0:
        energia = 0
    print("Você perdeu", perda, "de energia. Sua energia atual é de", energia)
    return energia


def ganharEnergia(energia, minimo, maximo):
    ganho = random.randint(0, 5)
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

def situacao1():
    print("\nSituacao 1")
    print("Você entra na floresta.")
    escolha = resposta("Deseja entrar na mata fechada para procurar a saída? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você adentra a mata fechada, com pouca luz e terreno irregular.(Poupou energia)")
        #perguntas
    else:
        print("Você segue a trilha aberta.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao2():
    print("\nSituacao 2")
    print("Anoitece e você tem que procurar abrigo.")
    escolha = resposta("Deseja procurar um acampamento abandonado? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você encontra um acampamento abandonado.(Poupou energia)")
        #perguntas
    else:
        print("Você monta um acampamento com galhos e folhas.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao3():
    print("\nSituacao 3")
    print("Você está com sede.")
    escolha = resposta("Deseja beber água do lago? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você bebe direto do lago, com risco de contaminação.(Poupou energia)")
        #perguntas
    else:
        print("Você procura uma forma de filtrar a água.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao4():
    print("\nSituacao 4")
    print("Você encontra frutas desconhecidas.")
    escolha = resposta("Deseja comer as frutas, que você não sabe se são tóxicas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você come as frutas, com o risco de intoxicação.(Poupou energia)")
        #perguntas
    else:
        print("Você come apenas frutas conhecidas.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao5():
    print("\nSituacao 5")
    print("Está frio e você precisa se aquecer.")
    escolha = resposta("Deseja acender uma fogueira sem ferramentas? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta acender a fogueira sem ferramentas.(Poupou energia)")
        #perguntas
    else:
        print("Você busca outra fonte de calor.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao6():
    print("\nSituacao 6")
    print("Você ouve um rosnado de onça vindo da mata.")
    escolha = resposta("Deseja seguir por esse caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você tenta espantar o animal.(Poupou energia)")
        #perguntas
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao7():
    print("\nSituacao 7")
    print("Há uma velha ponte que atravessa um desfiladeiro.")
    escolha = resposta("Deseja atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você atravessa a ponte.(Poupou energia)")
        #perguntas
    else:
        print("Você procura outra forma de seguir em frente.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao8():
    print("\nSituacao 8")
    print("Você encontra uma cobra descansando em seu caminho.")
    escolha = resposta("Deseja seguir? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você passa por ela sem acordá-la.(Poupou energia)")
        #perguntas
    else:
        print("Você vai por outro caminho, muito mais longo.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao9():
    print("\nSituacao 9")
    print("Um desfiladeiro tampa seu caminho.")
    escolha = resposta("Deseja escalar as rochas que estão bloqueando seu caminho? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você sobe pelas pedras soltas.(Poupou energia)")
        #perguntas
    else:
        print("Você busca outro caminho, mais longo.(Gastou energia)")
        #perguntas

    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")


def situacao10():
    print("\nSituacao 10")
    print("Você chega à margem de um riacho (troca de cenário).")
    escolha = resposta("Deseja montar um bote improvisado para atravessar? (sim/nao): ", ["sim", "nao"])

    if escolha == "sim":
        print("Você monta um bote improvisado com troncos e cipós.(Poupou energia)")
        #perguntas
    else:
        print("Você não segue pelo caminho e perde todas as perguntas daquele caminho.(Gastou energia)")
        
    #if acertou:
    #    print("Correto!")
    #else:
    #    print("Errado!")
