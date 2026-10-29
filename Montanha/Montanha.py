import random

energia = 100
pontos = 0

print(f"Energia atual: {energia}")

print("Você encontrou uma montanha!")
print("Precisa subir ela! Poderá escolher uma dessas duas opções:")
print("1- Seguir pela trilha principal, é mais longa, porém mais segura")
print("2- Subir por um caminho íngreme, é mais curto, porém mais arriscado")

escolha1 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha1 == 1:

    perda = random.randint(20,40)
    energia -= perda
    print("Você está subindo a montanha quando se depara com um deslizamento de pedras que bloqueia o caminho. Escolha entre:")
    print("1- esperar as pedras pararem de cair e seguir por um caminho alternativo mais longo.")
    print("2- atravessar rapidamente uma passagem estreita entre as pedras, exigindo agilidade e atenção.")
    opc1 = int(input("Qual caminho vai escolher? (1/2): "))

    if opc1 == 1:
        print("Você escolheu o caminho mais fácil, para continuar responda a pergunta: (+10)")
        print("Qual é a capital do Brasil?")
        resposta = input("Escreva: ").lower()

        if resposta == "brasília":
            print("Você recebeu 10 pontos")
            pontos += 10
            print(pontos)
        else:
            print("Você não recebeu nenhum ponto")
            print(pontos)

    else:
        print("Você escolheu o caminho arriscado, para continuar responda a pergunta: (+20)")
        print("Qual é o maior oceano do mundo?")
        resposta = input("Escreva: ").lower()

        if resposta == "oceano pacífico":
            print("Você recebeu 20 pontos")
            pontos += 20
            print(pontos)
        else:
            print("Você perdeu 10 pontos")
            pontos -= 10
            print(pontos)

else:
    perda = random.randint(10,30)
    energia -= perda
    print("Durante a subida, você encontra um rio que precisa atravessar para continuar a jornada. Escolha entre:")
    print("1- procurar uma ponte de madeira mais distante, mas segura.")
    print("2- atravessar o rio pulando sobre pedras escorregadias.")
    opc1 = int(input("Qual caminho vai escolher? (1/2): "))

    if opc1 == 1:
        print("Você escolheu o caminho mais fácil, para continuar responda a pergunta: (+10)")
        print("Quantos dias tem uma semana?")
        resposta = int(input("Escreva: "))

        if resposta == 7:
            print("Você recebeu 10 pontos")
            pontos += 10
            print(pontos)
        else:
            print("Você não recebeu nenhum ponto")
            print(pontos)

    else:
        print("Você escolheu o caminho arriscado, para continuar responda a pergunta: (+20)")
        print("Quantas cores tem o arco-íris?")
        resposta = int(input("Escreva: "))

        if resposta == 7:
            print("Você recebeu 20 pontos")
            pontos += 20
            print(pontos)
        else:
            print("Você perdeu 10 pontos")
            pontos -= 10
            print(pontos)

print("Você está indo muito bem!")
print(pontos)
print(energia)
print("Já está a 1/4 de chegar")

print("Ao subir, você percebeu que a trilha está bloqueada. Uma árvore caída bloqueia a trilha principal, impedindo sua passagem.")
print("Para continuar escolha:")
print("1- contornar a árvore por uma trilha lateral com pouca inclinação.")
print("2- escalar a árvore e passar por cima dela, mantendo o equilíbrio.")
escolha1 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha1 == 1:

    perda = random.randint(20,40)
    energia -= perda
    print("Você chega a uma parede de rochas que precisa superar para alcançar uma parte mais alta da montanha. Escolha entre:")
    print("1- dar a volta pela encosta, seguindo uma trilha longa e menos inclinada.")
    print("2- escalar a parede rochosa usando pequenas fendas como apoio.")
    opc1 = int(input("Qual caminho vai escolher? (1/2): "))

    if opc1 == 1:
        print("Você escolheu o caminho mais fácil, para continuar responda a pergunta: (+10)")
        print("Qual é o maior animal terrestre do mundo?")
        resposta = input("Escreva: ").lower()

        if resposta == "elefante africano" or resposta == "elefante":
            print("Você recebeu 10 pontos")
            pontos += 10
            print(pontos)
        else:
            print("Você não recebeu nenhum ponto")
            print(pontos)

    else:
        print("Você escolheu o caminho arriscado, para continuar responda a pergunta: (+20)")
        print("Qual planeta é conhecido como Planeta Vermelho?")
        resposta = input("Escreva: ").lower()

        if resposta == "marte":
            print("Você recebeu 20 pontos")
            pontos += 20
            print(pontos)
        else:
            print("Você perdeu 10 pontos")
            pontos -= 10
            print(pontos)

else:
    perda = random.randint(10,30)
    energia -= perda
    print("Uma neblina densa cobre a montanha, dificultando a visão e tornando o caminho perigoso. Escolha entre:")
    print("1- parar e esperar a neblina diminuir antes de continuar pela trilha sinalizada.")
    print("2- seguir por um caminho estreito usando um mapa e uma bússola para se orientar.")
    opc1 = int(input("Qual caminho vai escolher? (1/2): "))

    if opc1 == 1:
        print("Você escolheu o caminho mais fácil, para continuar responda a pergunta: (+10)")
        print("Quantos lados tem um hexágono?")
        resposta = int(input("Escreva: "))

        if resposta == 6:
            print("Você recebeu 10 pontos")
            pontos += 10
            print(pontos)
        else:
            print("Você não recebeu nenhum ponto")
            print(pontos)

    else:
        print("Você escolheu o caminho arriscado, para continuar responda a pergunta: (+20)")
        print("Qual é o menor país do mundo?")
        resposta = input("Escreva: ").lower()

        if resposta == "vaticano" or resposta == "cidade do vaticano":
            print("Você recebeu 20 pontos")
            pontos += 20
            print(pontos)
        else:
            print("Você perdeu 10 pontos")
            pontos -= 10
            print(pontos)

print("Você já vê o topo da montanha. Durante a subida, você encontra uma ponte de cordas antiga que atravessa um precipício. Algumas tábuas estão quebradas e as cordas estão desgastadas. Você escolhe:")
print("1- procurar uma passagem alternativa pela encosta, mesmo que seja mais longa.")
print("2- atravessar a ponte cuidadosamente, equilibrando-se nas tábuas e segurando as cordas.")
escolha1 = int(input("Qual caminho vai escolher? (1/2): "))

if escolha1 == 1:
    perda = random.randint(20,40)
    energia -= perda
    print(energia)
    print("Você escolheu o caminho mais fácil, para continuar responda a pergunta: (+10)")
    print("Quem pintou a Mona Lisa?")
    resposta = input("Escreva: ").lower()

    if resposta == "leonardo da vinci":
        print("Você recebeu 10 pontos")
        pontos += 10
        print(pontos)
    else:
        print("Você não recebeu nenhum ponto")
        print(pontos)

else:
    perda = random.randint(10,30)
    energia -= perda
    print(energia)
    print("Você escolheu o caminho arriscado, para continuar responda a pergunta: (+20)")
    print("Qual é o símbolo químico da água?")
    resposta = input("Escreva: ").lower()

    if resposta == "h2o":
        print("Você recebeu 20 pontos")
        pontos += 20
        print(pontos)
    else:
        print("Você perdeu 10 pontos")
        pontos -= 10
        print(pontos)

print("Você chegou ao topo da montanha")

if energia > 70:
    print(f"FINAL ALEGRE - Você terminou com {energia} de energia e está ótimo(a).")
elif energia >= 30 and energia <= 69:
    print(f"FINAL IRÔNICO - Você terminou com {energia} de energia e está tão fraco que não consegue nem fazer piadas. Além de estar parecendo um zumbi")
else:
    print(f"FINAL SURREAL - Você terminou com {energia} de energia e está quase sem forças e vai precisar de suporte para voltar a como vivia antes")