import pygame
pygame.init()

from funcoes.funcoes_luta import luta
from funcoes.funcoes_eventos import escreveTela

largura_tela = 950
altura_tela = 550

tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

def telaMenu(telaAtual, nivel):
    imagemMenu = pygame.image.load("Imagens/Imagem menu.jpg")
    corOp1 = (0, 228, 251)
    corOp2 = (255, 255, 255)
    corBorda = (0, 228, 251)
    selecionado = 190
    opcao1 = "Jogo"
    opcao2 = "Como jogar"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selecionado == 190:
                        selecionado += 130
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)
                    else:
                        selecionado -= 130
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)

                elif event.key == pygame.K_DOWN:
                    if selecionado == 320:
                        selecionado -= 130
                        corOp1 = (0, 228, 251)
                        corOp2 = (255, 255, 255)
                    else:
                        selecionado += 130
                        corOp1 = (255, 255, 255)
                        corOp2 = (0, 228, 251)

                elif event.key == pygame.K_RETURN:
                    if selecionado == 190:
                        return opcao1

                    elif selecionado == 320:
                        return opcao2

        if telaAtual == "Menu":
            gameDisplay.blit(imagemMenu, (0, 0))
            opcao1 = "Jogo"
            opcao2 = "Como jogar"

        elif telaAtual == "Jogo":
            opcao1 = "Torneio"
            opcao2 = "Batalha"
            gameDisplay.fill((65, 81, 106))
            gameDisplay.blit(escreveTela("Nível: %d"%int(nivel), (255, 255, 255), 25), (100, 100))
            corBorda = (255, 255, 255)

        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 190, 500, 90))
        pygame.draw.rect(gameDisplay, (0, 0, 0), pygame.Rect(216, 320, 500, 90))
        pygame.draw.rect(gameDisplay, corBorda, pygame.Rect(216, selecionado, 500, 90), 2)

        gameDisplay.blit(escreveTela(opcao1, corOp1, 50), (375, 215))
        gameDisplay.blit(escreveTela(opcao2, corOp2, 50), (375, 343))

        pygame_display.update()
        clock.tick(60)

def telaBatalha():
    hyoga = pygame.image.load("Imagens/Hyoga.jpg")
    goku = pygame.image.load("Imagens/Goku.jpg")
    personagemJogador = ""
    personagemMaquina = ""
    posicaoPersonagem = 0
    selecionado = 216
    corSelecionando = (76, 154, 173)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if selecionado == 216:
                        selecionado += 124
                        posicaoPersonagem += 1
                    else:
                        selecionado -= 124
                        posicaoPersonagem -= 1

                elif event.key == pygame.K_RIGHT:
                    if selecionado == 340:
                        selecionado -= 124
                        posicaoPersonagem -= 1
                    else:
                        selecionado += 124
                        posicaoPersonagem += 1

                elif event.key == pygame.K_RETURN:
                    if personagemJogador == "":
                        personagemJogador = posicaoPersonagem
                        corSelecionando = (255, 0, 0)
                    else:
                        personagemMaquina = posicaoPersonagem

                elif event.key == pygame.K_z:
                    return ["Luta", personagemJogador, personagemMaquina]

                elif event.key == pygame.K_x:
                    return ["Jogo", 0, 0]

        gameDisplay.fill((65, 81, 106))

        gameDisplay.blit(escreveTela("Personagens", (255, 255, 255), 40), (280, 90))

        gameDisplay.blit(hyoga, (216, 190))
        gameDisplay.blit(goku, (340, 190))
        pygame.draw.rect(gameDisplay, corSelecionando, pygame.Rect(selecionado, 190, 100, 100), 2)

        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))

        pygame_display.update()
        clock.tick(60)

def telaTorneio(nivel, nomesPersonagens):
    numeroOponente = 1

    if nivel > len(nomesPersonagens)-1:
        nivel = len(nomesPersonagens) - 1

    personagemOponente = pygame.image.load("Imagens/%s.jpg"%nomesPersonagens[nivel])
    personagemJogador = pygame.image.load("Imagens/%s.jpg"%nomesPersonagens[nivel-1])
    numeroOponente = nivel

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    resultado = luta(nomesPersonagens[nivel-1], nomesPersonagens[numeroOponente], nivel-1, numeroOponente)
                    return resultado

                elif event.key == pygame.K_x:
                    return ["Jogo", ""]
        
        gameDisplay.fill((65, 81, 106))

        gameDisplay.blit(escreveTela("Torneio", (255, 255, 255), 40), (280, 90))
        gameDisplay.blit(personagemJogador, (216, 190))
        gameDisplay.blit(personagemOponente, (416, 190))
        gameDisplay.blit(escreveTela("Clique [a] para começar", (255, 255, 255), 20), (20, 400))

        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))
        pygame_display.update()
        clock.tick(60)

def telaResulta(resultado):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return "Jogo"

        gameDisplay.fill((65, 81, 106))
        gameDisplay.blit(escreveTela("Resutado", (255, 255, 255), 40), (380, 90))
        gameDisplay.blit(escreveTela("Você %s"%resultado, (255, 0, 0), 40), (290, 200))

        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))
        pygame_display.update()
        clock.tick(60)