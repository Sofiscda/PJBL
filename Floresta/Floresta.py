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
    ganho = random.randint(minimo, maximo)
    energia = energia + ganho
    if energia > 100:
        energia = 100
    print("Você ganhou", ganho, "de energia. Sua energia atual é de", energia)
    return energia