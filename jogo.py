import pygame
pygame.init()

from funcoes.funcoes_gerais import armazenar

largura_tela = 950
altura_tela = 550

tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
pygame_display.set_caption("Luta dos Campeões")
gameDisplay = pygame.display.set_mode(tamanho_tela)

clock = pygame.time.Clock()

telas = [0]

telaAtual = 0

def escreveTela(texto, cor, tamanho):
    fonte = pygame.font.Font("freesansbold.ttf", tamanho)
    frase = fonte.render(texto, True, cor)
    return frase

def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame_display.update()
        clock.tick(60)

def telaMenu():
    imagemMenu = pygame.image.load("Imagens/Imagem menu.jpg")
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
                        armazenar("Registro de partidas.txt")
                        return "Modos"

        # gameDisplay.fill((40, 80, 100))
        gameDisplay.blit(imagemMenu, (0, 0))

        pygame.draw.rect(gameDisplay, (40, 80, 100), pygame.Rect(216, 190, 500, 90))
        pygame.draw.rect(gameDisplay, (40, 80, 100), pygame.Rect(216, 320, 500, 90))
        pygame.draw.rect(gameDisplay, (255, 255, 255), pygame.Rect(216, selecionado, 500, 90), 2)

        gameDisplay.blit(escreveTela("Novo Jogo", (255, 255, 255), 50), (328, 215))
        gameDisplay.blit(escreveTela("Continuar", (255, 255, 255), 50), (328, 343))

        pygame_display.update()
        clock.tick(60)

def telaModos():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill((40, 80, 100))

        pygame_display.update()
        clock.tick(60)

while True:
    if telaAtual == telas[0]:
        telaAtual = telaMenu()
    elif telaAtual == "Modos":
        telaAtual = telaModos()