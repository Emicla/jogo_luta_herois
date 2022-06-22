import pygame
pygame.init()

from funcoes.funcoes_gerais import armazenar, ler_registro, escreveTela

largura_tela = 950
altura_tela = 550

tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

def telaMenu():
    imagemMenu = pygame.image.load("Imagens/Imagem menu.jpg")
    selecionado = 190
    corOp1 = (0, 228, 251)
    corOp2 = (255, 255, 255)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selecionado == 190:
                        selecionado += 130
                    else:
                        selecionado -= 130

                elif event.key == pygame.K_DOWN:
                    if selecionado == 320:
                        selecionado -= 130
                    else:
                        selecionado += 130

                elif event.key == pygame.K_RETURN:
                    if selecionado == 190:
                        armazenar("Registro de partidas.txt")
                        return ["Modos", ""]

                    elif selecionado == 320:
                        conteudo = ler_registro("Registro de partidas.txt")
                        return ["Continuar", conteudo]

        if selecionado == 190:
            corOp1 = (0, 228, 251)
            corOp2 = (255, 255, 255)

        elif selecionado == 320:
            corOp2 = (0, 228, 251)
            corOp1 = (255, 255, 255)

        # gameDisplay.fill((40, 80, 100))
        gameDisplay.blit(imagemMenu, (0, 0))

        pygame.draw.rect(gameDisplay, (45, 52, 51), pygame.Rect(216, 190, 500, 90))
        pygame.draw.rect(gameDisplay, (45, 52, 51), pygame.Rect(216, 320, 500, 90))

        pygame.draw.rect(gameDisplay, (0, 228, 251), pygame.Rect(216, selecionado, 500, 90), 2)
        
        gameDisplay.blit(escreveTela("Novo Jogo", corOp1, 50), (328, 215))
        gameDisplay.blit(escreveTela("Continuar", corOp2, 50), (328, 343))

        pygame_display.update()
        clock.tick(60)

def telaModos(nivel):
    selecionado = 190
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selecionado == 190:
                        selecionado += 130
                    else:
                        selecionado -= 130

                elif event.key == pygame.K_DOWN:
                    if selecionado == 320:
                        selecionado -= 130
                    else:
                        selecionado += 130

                elif event.key == pygame.K_RETURN:
                    if selecionado == 190:
                        return "Torneio"

                    elif selecionado == 320:
                        return "Batalha"

                elif event.key == pygame.K_x:
                    return "Menu"
                    
        gameDisplay.fill((65, 81, 106))

        gameDisplay.blit(escreveTela("Nível: %s"%str(nivel), (255, 255, 255), 25), (100, 100))

        pygame.draw.rect(gameDisplay, (76, 154, 173), pygame.Rect(216, 190, 500, 90))
        pygame.draw.rect(gameDisplay, (76, 154, 173), pygame.Rect(216, 320, 500, 90))
        pygame.draw.rect(gameDisplay, (255, 255, 255), pygame.Rect(216, selecionado, 500, 90), 2)

        gameDisplay.blit(escreveTela("Torneio", (255, 255, 255), 50), (375, 215))
        gameDisplay.blit(escreveTela("Batalha", (255, 255, 255), 50), (375, 343))

        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))

        pygame_display.update()
        clock.tick(60)

def telaContinuar(saves, saveNomes):
    numeroSave = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if numeroSave >= len(saveNomes):
                        numeroSave = 1
                    else:
                        numeroSave += 1
                elif event.key == pygame.K_DOWN:

                    if numeroSave <= 1:
                        numeroSave = len(saveNomes)
                    else:
                        numeroSave -= 1
                elif event.key == pygame.K_RETURN and len(saves) > 0:
                    return ["Modos", saves[numeroSave - 1][-2]]

                elif event.key == pygame.K_x:
                    return ["Menu", 1]

        gameDisplay.fill((65, 81, 106))
        gameDisplay.blit(escreveTela("Saves", (255, 255, 255), 70), (380, 10))
        gameDisplay.blit(escreveTela("Número de saves: %d"%len(saveNomes), (255, 255, 255), 25), (30, 100))
        gameDisplay.blit(escreveTela(''.join(saveNomes), (255, 255, 255), 25), (30, 135))
        gameDisplay.blit(escreveTela("Use as setas para acessar o número do save: %s"%str(numeroSave), (255, 255, 255), 25), (30, 200))
        
        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))
        
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
                    return "Modos"

        gameDisplay.fill((65, 81, 106))

        gameDisplay.blit(escreveTela("Personagens", (255, 255, 255), 40), (280, 90))

        gameDisplay.blit(hyoga, (216, 190))
        gameDisplay.blit(goku, (340, 190))
        pygame.draw.rect(gameDisplay, corSelecionando, pygame.Rect(selecionado, 190, 100, 100), 2)

        gameDisplay.blit(escreveTela("Clique [X] para voltar", (255, 255, 255), 20), (20, 500))

        pygame_display.update()
        clock.tick(60)