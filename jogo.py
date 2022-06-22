import pygame, os
from funcoes.funcoes_gerais import armazenar, ler_registro

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

conteudoArmazenado = ler_registro("Registro de acessos.txt")

achou = False
for posicao, palavra in enumerate(conteudoArmazenado):
    if palavra.strip("\n") == email:
        registroPartidas = ler_registro("Registro de partidas.txt")
        nivel = registroPartidas[posicao-2]
        achou = True
        break

if achou == False:
    armazenar("1", "Registro de partidas.txt")

armazenar(nomeJogador, "Registro de acessos.txt")
armazenar(email, "Registro de acessos.txt")

from funcoes.funcoes_telas import telaMenu, telaModos, telaContinuar, telaBatalha, telaTorneio, telaResulta
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

def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame_display.update()
        clock.tick(60)

while True:
    if telaAtual == "Menu":
        arrayCena = telaMenu()
        telaAtual = arrayCena[0]
        saves = arrayCena[1]
    
    elif telaAtual == "Continuar":
        savesNomes = []

        if len(saves) == 0:
            savesNomes.append("Nenhum Save encontrado")

        else:
            for posicao, save in enumerate(saves):
                save = list(save)
                save[-2] = ""
                save = ''.join(save)
                savesNomes.append(save)

        arrayCena = telaContinuar(saves, savesNomes)
        telaAtual = arrayCena[0]
        nivel = int(arrayCena[1])

    elif telaAtual == "Modos":
        telaAtual = telaModos(nivel)
    
    elif telaAtual == "Torneio":
        arrayCena = telaTorneio(nivel, nomesPersonagens)
        telaAtual = arrayCena[0]
        resutado = arrayCena[1]
        nivel += arrayCena[2]

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