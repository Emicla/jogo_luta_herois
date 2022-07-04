import pygame, os
from funcoes.funcoes_gerais import armazenar, ler_registro, registrar

os.system("cls")

def verificaInf(frase):
    while True:
        resposta = input(frase)
        os.system("cls")
        try:
            resposta = int(resposta)
            print("Não pode ser só números")

        except:
            if len(resposta) < 2:
                print("Deve conter mais de 2 letras")
            elif resposta[0] == " ":
                print("Por favor, sem espaços em branco no ínicio")
            else:
                return resposta

nomeJogador = verificaInf("Informe seu nome:")

while True:
    email = verificaInf("Informe seu email: ")
    if "@" not in email or ".com" not in email:
        print("Escreva corretamente seu email")

    elif email.index(".com") !=len(email)-4 or email.index("@") == 1:
        print("Email inválido")

    else:
        break

nivel = 1

conteudoArmazenado = ler_registro("Arquivos/Registro de acessos.txt")
registroPartidas = ler_registro("Arquivos/Registro de partidas.txt")
posicaoSave = 0
achou = False

for posicao, palavra in enumerate(registroPartidas):
    palavra = palavra.strip("\n")
    palavra = list(palavra)
    numero = palavra.pop()
    palavra = ''.join(palavra)
    if palavra == email:
        nivel = int(numero)
        posicaoSave = posicao
        achou = True
        break

if achou == False:
    armazenar("%s1"%email, "Arquivos/Registro de partidas.txt")

armazenar(nomeJogador, "Arquivos/Registro de acessos.txt")
armazenar(email, "Arquivos/Registro de acessos.txt")

from funcoes.funcoes_telas import telaMenu, telaBatalha, telaTorneio, telaResulta
from funcoes.funcoes_luta import luta
pygame.init()

largura_tela = 950
altura_tela = 550
tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
pygame_display.set_caption("Luta dos Campeões")
gameDisplay = pygame.display.set_mode(tamanho_tela)

clock = pygame.time.Clock()

telaAtual = "Menu"
saves = []

nomesPersonagens = ["Hyoga", "Goku"]
player = ""
oponente = ""

resutado = "Indefinido"
clicou = False

while True:
    if telaAtual == "Menu" or telaAtual == "Jogo":
        telaAtual = telaMenu(telaAtual, nivel)
    
    elif telaAtual == "Torneio":
        arrayCena = telaTorneio(nivel, nomesPersonagens)
        telaAtual = arrayCena[0]
        resutado = arrayCena[1]
        if resutado == "GANHOU":
            nivel += 1
            registroPartidas = ler_registro("Arquivos/Registro de partidas.txt")
            registroPartidas[posicaoSave] = "%s%d"%(email, nivel)
            registroPartidas = ''.join(registroPartidas)
            registrar("Arquivos/Registro de partidas.txt", registroPartidas)

    elif telaAtual == "Batalha":
        arrayCena = telaBatalha()
        telaAtual = arrayCena[0]
        player = nomesPersonagens[arrayCena[1]]
        oponente = nomesPersonagens[arrayCena[2]]

    elif telaAtual == "Luta":
        arrayCena = luta(player, oponente, nomesPersonagens.index(player), nomesPersonagens.index(oponente))
        telaAtual = arrayCena[0]
        resutado = arrayCena[1]

    elif telaAtual == "Resultado":
        telaAtual = telaResulta(resutado)