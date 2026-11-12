import json
import random
import matplotlib.pyplot as plt

PONTOS_INICIAIS = 0
# dificuldade: (pontos ganhos por acerto, pontos perdidos por erro)
PONTOS = {
    "facil": (10, 5),
    "media": (20, 10),
    "dificil": (30, 15),
}
DIFICULDADES = {"facil": "facil", "media": "media", "dificil": "dificil"}

ENERGIA = {
    "ar_livre": (5, 15),
    "esquerda": (5, 10),
    "meio_pontas": (5, 15),
    "meio_rapido": (5, 10),
    "meio_morcegos": (10, 20),
    "fundo_descanso": (10, 20),
    "urso_fuga": (15, 30),
    "item_comida": (5, 15),
    "item_agua": (10, 20),
    "mina_1_erro": (10, 20),
    "mina_2_erros": (20, 35),
    "acampamento_descanso": (10, 20),
    "acampamento_bom": (10, 20),
    "acampamento_ruim": (10, 20),
    # Custos de energia de cada escolha/movimento
    "entrar_caverna": (3, 8),
    "escolher_caminho": (2, 6),
    "voltar": (2, 6),
    "urso_contornar": (3, 8),
    "urso_passo": (2, 5),
}

ARQUIVO_RESULTADOS = "resultadosCaverna.json"
MAX_BARRAS = 10


def lerJson(nome_arquivo="perguntasCaverna.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: não achei o arquivo '{nome_arquivo}' na pasta do jogo.")
        raise SystemExit
    except json.JSONDecodeError as erro:
        print(f"Erro: o arquivo '{nome_arquivo}' tem um problema na linha {erro.lineno}.")
        raise SystemExit


def ler_opcao(mensagem, validas):
    while True:
        resposta = input(mensagem).strip()
        if resposta in validas:
            return resposta
        print(f"Opção inválida! Digite uma destas: {', '.join(validas)}")


def perder_energia(energia, faixa):
    perda = random.randint(*faixa)
    energia = max(0, energia - perda)
    print(f"Você perdeu {perda} de energia. Sua energia atual é de {energia}")
    return energia


def ganhar_energia(energia, faixa):
    ganho = random.randint(*faixa)
    energia = min(100, energia + ganho)
    print(f"Você ganhou {ganho} de energia. Sua energia atual é de {energia}")
    return energia


def carregar_resultados(nome_arquivo=ARQUIVO_RESULTADOS):
    """Lê as partidas salvas (de você ou de outras pessoas)."""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_resultados(resultados, nome_arquivo=ARQUIVO_RESULTADOS):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(resultados, arquivo, ensure_ascii=False, indent=2)


def mostrar_grafico(resultados):
    """Gráfico de barras simples com pontos e energia final das últimas partidas."""
    recentes = resultados[-MAX_BARRAS:]
    nomes = [r["jogador"] for r in recentes]
    pontos = [r["pontos"] for r in recentes]
    energias = [r["energia"] for r in recentes]
    posicoes = list(range(len(recentes)))
    largura = 0.4

    fig, eixo = plt.subplots()
    barras_pontos = eixo.bar([p - largura / 2 for p in posicoes], pontos, largura,
                             label="Pontos", color="tab:blue")
    barras_energia = eixo.bar([p + largura / 2 for p in posicoes], energias, largura,
                              label="Energia final", color="tab:orange")
    eixo.bar_label(barras_pontos, padding=2)
    eixo.bar_label(barras_energia, padding=2)
    eixo.set_title("Pontos e energia das partidas")
    eixo.set_xticks(posicoes)
    eixo.set_xticklabels(nomes)
    eixo.legend()
    fig.tight_layout()
    plt.show()


def perguntas(banco, quantidade, pontos, historico, dificuldade=None,
              parar_acertos=None, parar_erros=None):
    acertos = 0
    erros = 0
    for _ in range(quantidade):
        candidatas = [p for p in banco
                      if dificuldade is None or p["dificuldade"] == dificuldade]
        if not candidatas:
            print("\n(As perguntas acabaram!)")
            break
        item = random.choice(candidatas)
        banco.remove(item)
        ganho, perda = PONTOS[item["dificuldade"]]
        pergunta = item["pergunta"]
        certa = item["resposta"]
        opcoes = item["opcoes"][:]
        random.shuffle(opcoes)
        print(f"\n[{DIFICULDADES[item['dificuldade']]} | vale {ganho} pontos] {pergunta}")
        for i, texto in enumerate(opcoes, start=1):
            print(f"{i} - {texto}")
        escolha = int(ler_opcao("Resposta: ", [str(i) for i in range(1, len(opcoes) + 1)]))

        if opcoes[escolha - 1] == certa:
            acertos += 1
            pontos += ganho
            print(f"Correto! +{ganho} pontos (total: {pontos})")
        else:
            erros += 1
            pontos = max(0, pontos - perda)
            print(f"Errado! A resposta certa era: {certa}. -{perda} pontos (total: {pontos})")
        historico.append(pontos)

        if parar_acertos and acertos >= parar_acertos:
            break
        if parar_erros and erros >= parar_erros:
            break
    return acertos, erros, pontos


def main():
    banco_perguntas = lerJson()

    energia = 100
    pontos = PONTOS_INICIAIS
    historico_pontos = [pontos]
    inventario = []
    urso_passou = False
    direita_bloqueada = False
    acampamento_usado = False
    destino = None

    print("\nApós andar pela montanha/floresta, você encontra a entrada de uma caverna.")
    print("1 - Entrar (um abrigo, mas você não sabe o que pode ter lá dentro)")
    print("2 - Não entrar (continua ao ar livre, com terreno aberto caso precise de algo)")
    escolha = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])
    if escolha == "2":
        print("\nVocê decide continuar ao ar livre. O terreno é aberto e você enxerga tudo ao redor.")
        energia = perder_energia(energia, ENERGIA["ar_livre"])
        destino = "ar_livre"
    else:
        print("\nA caverna é espaçosa, mas o barulho de goteira não para.")
        energia = perder_energia(energia, ENERGIA["entrar_caverna"])
        while destino is None:
            if energia <= 0:
                print("\nSuas forças acabaram e você desmaia dentro da caverna...")
                destino = "desmaiou"
                continue

            print("\nAo continuar andando, você se depara com 3 caminhos.")
            print("1 - Esquerda")
            print("2 - Meio")
            print("3 - Direita")
            escolha = ler_opcao("Escolha (1, 2 ou 3): ", ["1", "2", "3"])
            energia = perder_energia(energia, ENERGIA["escolher_caminho"])

            if escolha in ("1", "2"):
                local = "fundo"
                if escolha == "1":
                    print("\nVocê segue pela esquerda. O caminho é largo e sem obstáculos.")
                    energia = perder_energia(energia, ENERGIA["esquerda"])
                else:
                    print("\nO caminho do meio é estreito, com morcegos e pontas afiadas nas paredes.")
                    print("1 - Passar rapidamente")
                    print("2 - Passar com calma")
                    passagem = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])

                    print("\nVocê é obrigado a passar pelas partes pontudas da caverna e se machuca...")
                    energia = perder_energia(energia, ENERGIA["meio_pontas"])

                    if passagem == "1":
                        print("Você passou rápido e os morcegos mal perceberam, mas correr cansa.")
                        energia = perder_energia(energia, ENERGIA["meio_rapido"])
                    else:
                        print("Você passa com calma, mas os morcegos podem se agitar!")
                        if random.randint(1, 100) <= 50:
                            print("Os morcegos atacaram você!")
                            energia = perder_energia(energia, ENERGIA["meio_morcegos"])
                        else:
                            print("Por sorte, eles não se agitaram.")

                    local = "segunda_intersecao"
                    while local == "segunda_intersecao":
                        print("\nNo meio do caminho há outra intersecção.")
                        print("Quase não dá para ver nada dentro de um dos lados.")
                        print("1 - Seguir para a parte funda da caverna")
                        print("2 - Entrar no caminho escuro")
                        lado = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])
                        energia = perder_energia(energia, ENERGIA["escolher_caminho"])

                        if lado == "1":
                            local = "fundo"
                        else:
                            print("\nNo caminho escuro, você encontra um acampamento abandonado.")
                            if acampamento_usado:
                                print("Você já aproveitou tudo o que havia por aqui.")
                            else:
                                acampamento_usado = True
                                print("Aqui você consegue descansar. Há um mapa, suprimentos,")
                                print("bandagens para se recuperar e uma lanterna.")
                                energia = ganhar_energia(energia, ENERGIA["acampamento_descanso"])
                                inventario.extend(["mapa", "lanterna"])

                                print("\nNo fundo do acampamento, a caverna vai cada vez mais fundo.")
                                print("Será que você sabe usar as bandagens e se os suprimentos")
                                print("(água e alimentos) estão em estado ideal para consumo?")
                                acertos, erros, pontos = perguntas(
                                    banco_perguntas, 5, pontos, historico_pontos,
                                    dificuldade="facil")

                                if acertos >= 3:
                                    print("\nVocê usa as bandagens direito e os suprimentos estão em ótimo estado!")
                                    inventario.append("bandagens")
                                    energia = ganhar_energia(energia, ENERGIA["acampamento_bom"])
                                else:
                                    print("\nA bandagem ficou ok, mas os alimentos estavam estragados")
                                    print("e, como você comeu, agora está passando mal...")
                                    energia = perder_energia(energia, ENERGIA["acampamento_ruim"])

                            print("\n1 - Voltar pelo caminho que veio")
                            print("2 - Seguir em frente")
                            rumo = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])
                            energia = perder_energia(energia, ENERGIA["escolher_caminho"])

                            if rumo == "2":
                                print("\nApós passar um bom tempo andando, você encontra uma saída da caverna")
                                print("que leva ao pé de uma montanha.")
                                destino = "montanha"
                                local = "saiu"
                            else:
                                print("\nVocê volta pelo caminho que veio.")
                                energia = perder_energia(energia, ENERGIA["voltar"])

                if local == "fundo":
                    print("\nVocê chega à parte mais funda da caverna: é espaçosa, mas completamente vazia.")
                    print("Não há nenhuma saída por aqui.")
                    print("1 - Se abrigar aqui (você descansa, mas fica parado sem buscar resgate)")
                    print("2 - Dar meia volta até a intersecção")
                    fundo = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])

                    if fundo == "1":
                        print("\nVocê se acomoda no fundo da caverna e descansa.")
                        energia = ganhar_energia(energia, ENERGIA["fundo_descanso"])
                        destino = "abrigo"
                    else:
                        print("\nVocê volta para a intersecção.")
                        energia = perder_energia(energia, ENERGIA["voltar"])

            else:
                vai_mina = False
                if direita_bloqueada:
                    print("\nO urso está acordado e rondando o corredor. Não dá para passar por aqui de novo!")
                    energia = perder_energia(energia, ENERGIA["voltar"])
                elif urso_passou:
                    print("\nVocê atravessa de novo o corredor do urso, bem devagar...")
                    vai_mina = True
                else:
                    print("\nVocê entra na toca de um urso adormecido, que pode acordar a qualquer momento.")
                    print("Atrás dele, ao fundo, você vê uma luz que parece de uma lâmpada bem antiga.")
                    print("1 - Contornar o urso para ver a luz suspeita")
                    print("2 - Dar meia volta e voltar à intersecção")
                    opcao_urso = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])

                    if opcao_urso == "2":
                        print("\nVocê volta em silêncio para a intersecção.")
                        energia = perder_energia(energia, ENERGIA["voltar"])
                    else:
                        print("\nA cada passo, você precisa responder uma pergunta sem fazer barulho!")
                        print("(3 acertos = passa pelo urso | 3 erros = o urso acorda)")
                        print("Andar na ponta dos pés ao redor do urso cansa!")
                        energia = perder_energia(energia, ENERGIA["urso_contornar"])
                        acertos = 0
                        erros = 0
                        for _ in range(5):
                            a, e, pontos = perguntas(banco_perguntas, 1, pontos, historico_pontos,
                                                     dificuldade="media")
                            acertos += a
                            erros += e
                            if a + e == 0:
                                break
                            energia = perder_energia(energia, ENERGIA["urso_passo"])
                            if acertos >= 3 or erros >= 3 or energia <= 0:
                                break
                        if acertos >= 3:
                            print("\nVocê passou ao redor do urso sem acordá-lo!")
                            urso_passou = True
                            vai_mina = True
                        else:
                            print("\nO URSO ACORDOU! Você corre desesperado e se machuca no caminho,")
                            print("mas ele não te pega. Você volta correndo para a intersecção.")
                            energia = perder_energia(energia, ENERGIA["urso_fuga"])
                            direita_bloqueada = True
                if vai_mina:
                    print("\nVocê chega perto da luz: é uma mina abandonada, aparentemente caindo aos pedaços.")
                    print("1 - Entrar na mina")
                    print("2 - Não entrar e voltar à intersecção")
                    opcao_mina = ler_opcao("Escolha (1 ou 2): ", ["1", "2"])
                    if opcao_mina == "2":
                        print("\nVocê decide não arriscar e volta para a intersecção.")
                        energia = perder_energia(energia, ENERGIA["voltar"])
                    else:
                        print("\nAo entrar, você observa uma mesinha com alguns itens.")
                        print("Você só tem tempo de pegar um:")
                        print("1 - Rádio")
                        print("2 - Alimentos podres")
                        print("3 - Garrafa de água")
                        print("4 - Caderno")
                        item = ler_opcao("Escolha (1 a 4): ", ["1", "2", "3", "4"])
                        if item == "1":
                            print("\nVocê pegou o rádio. Está sem pilhas, mas talvez sirva depois.")
                            inventario.append("rádio")
                        elif item == "2":
                            print("\nVocê comeu os alimentos e passou mal...")
                            energia = perder_energia(energia, ENERGIA["item_comida"])
                        elif item == "3":
                            print("\nA água estava limpa! Você bebeu e guardou a garrafa.")
                            inventario.append("garrafa de água")
                            energia = ganhar_energia(energia, ENERGIA["item_agua"])
                        else:
                            print("\nO caderno tem anotações e um mapa da região. Isso vai ajudar!")
                            inventario.append("caderno")
                        print("\nPelas frestas você consegue ver o lado de fora, mas com seus movimentos")
                        print("a mina COMEÇA A DESMORONAR! Responda 3 perguntas para escapar!")
                        acertos, erros, pontos = perguntas(
                            banco_perguntas, 3, pontos, historico_pontos,
                            dificuldade="dificil")
                        if erros == 0:
                            print("\nVocê escapou da mina sem nenhum arranhão!")
                        elif erros == 1:
                            print("\nVocê escapou, mas distendeu o músculo da perna ao correr.")
                            print("Você não consegue mais correr até ser tratado ou se recuperar.")
                            energia = perder_energia(energia, ENERGIA["mina_1_erro"])
                        else:
                            print("\nUm pedaço de madeira que sustentava a mina caiu sobre o seu braço!")
                            print("Ele parece quebrado e você não consegue mexê-lo por enquanto.")
                            print("Sua perna também foi atingida e você não consegue mais correr.")
                            energia = perder_energia(energia, ENERGIA["mina_2_erros"])
                        print("\nVocê sai da caverna e volta ao ar livre, perto da floresta e de um riacho.")
                        destino = "riacho"

    print(f"\n[Caverna encerrada: {destino} | Energia: {energia} | Pontos: {pontos}]")

    nome = input("\nDigite seu nome para salvar o resultado: ").strip() or "Jogador"
    resultados = carregar_resultados()
    resultados.append({
        "jogador": nome,
        "pontos": pontos,
        "energia": energia,
        "destino": destino,
    })
    salvar_resultados(resultados)
    mostrar_grafico(resultados)


main()