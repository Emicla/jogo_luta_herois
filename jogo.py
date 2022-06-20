import pygame, os
pygame.init()
os.system("cls")

from funcoes.funcoes_telas import telaMenu, telaModos, telaContinuar, telaBatalha
from funcoes.funcoes_luta import luta

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
personagemPlayer = ""
personagemMaquina = ""

nivel = 1

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

        for posicao, save in enumerate(saves):
            print(save)
            save = list(save)
            save[-2] = ""
            save = ''.join(save)
            savesNomes.append(save)

        arrayCena = telaContinuar(saves, savesNomes)
        telaAtual = arrayCena[0]
        nivel = arrayCena[1]

    elif telaAtual == "Modos":
        telaAtual = telaModos(nivel)
    
    elif telaAtual == "Batalha":
        arrayCena = telaBatalha()
        telaAtual = arrayCena[0]
        personagemPlayer = nomesPersonagens[arrayCena[1]]
        personagemMaquina = nomesPersonagens[arrayCena[2]]

    elif telaAtual == "Luta":
        telaAtual = luta(personagemPlayer, personagemMaquina)