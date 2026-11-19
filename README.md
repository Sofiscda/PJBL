PJBL - Jogo de Aventura


Sobre o projeto
Este projeto foi desenvolvido como atividade de PjBL da disciplina de Raciocínio Algorítmico. O objetivo é desenvolver um jogo de aventura em Python, no qual o jogador pode escolher diferentes fases, enfrentar desafios e tomar decisões que influenciam sua energia e pontuação ao longo da partida.

O jogo possui uma interface gráfica que permite navegar entre as fases e acompanhar o desempenho do jogador.

Funcionalidades
- Menu principal para escolher entre as fases disponíveis.
- Três fases: Montanha, Floresta e Caverna.
- Sistema de energia, que diminui conforme os desafios enfrentados.
- Sistema de pontuação, de acordo com as escolhas e resultados do jogador.
- Eventos e obstáculos aleatórios durante as partidas.
- Possibilidade de jogar novamente ou escolher outra fase ao finalizar.
- Ranking geral com os resultados dos jogadores.
- Armazenamento dos dados do ranking em arquivo JSON.
- Gráficos para visualizar a energia e a pontuação.
- Interface gráfica desenvolvida com Tkinter.
Tecnologias e bibliotecas utilizadas
O projeto foi desenvolvido utilizando Python e as seguintes bibliotecas:
Biblioteca	Utilização
tkinter	Criação da interface gráfica
random	Geração de eventos aleatórios
json	Armazenamento e leitura do ranking
matplotlib	Criação de gráficos
os	Manipulação de caminhos e arquivos, caso utilizada no código

A única biblioteca externa necessária é o Matplotlib. As demais fazem parte da biblioteca padrão do Python, com exceção do Tkinter, que precisa estar disponível na instalação.
Requisitos
Para executar o projeto, é necessário:
- Python 3.11 ou superior.
- Tkinter instalado e disponível.
- Matplotlib instalado.
- Sistema operacional com suporte à interface gráfica.
Instalação
1. Instalar o Python

Baixe e instale o Python pelo site oficial:

https://www.python.org/downloads/

Durante a instalação no Windows, marque a opção Add Python to PATH.

2. Baixar o projeto

Clone o repositório utilizando o Git:
git clone https://github.com/Sofiscda/PJBL.git

3. Acessar a pasta do projeto
cd PJBL


4. Instalar as dependências
python -m pip install -r requirements.txt


Caso não exista o arquivo requirements.txt, instale o Matplotlib diretamente:
python -m pip install matplotlib


Execução
Após instalar as dependências, execute o arquivo principal do projeto:
python main.py


A interface gráfica será aberta e o jogador poderá selecionar a fase desejada para iniciar a aventura.
Arquivos do projeto
- main.py: arquivo principal responsável pelo menu e pela integração das fases.
- montanha.py: contém a lógica e os desafios da fase Montanha.
- floresta.py: contém a lógica e os desafios da fase Floresta.
- caverna.py: contém a lógica e os desafios da fase Caverna.
- ranking.json: armazena os resultados dos jogadores.
- requirements.txt: lista as bibliotecas externas necessárias para executar o projeto.
Considerações finais
O projeto busca aplicar conceitos de lógica de programação, estruturas condicionais, estruturas de repetição, funções, manipulação de arquivos e bibliotecas Python em uma aplicação interativa.

Além disso, o desenvolvimento em equipe permitiu trabalhar com integração de códigos, organização de arquivos e utilização do Git e GitHub para controle de versões.