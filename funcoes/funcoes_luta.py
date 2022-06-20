import pygame
pygame.init()

largura_tela = 950
altura_tela = 550

tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

def luta(personagemPlayer, personagemMaquina):
    personagemJogador = pygame.image.load("Imagens Personagens/{0}/{0} parado.png".format(personagemPlayer))
    personagemComputador = pygame.image.load("Imagens Personagens/{0}/{0} parado.png".format(personagemMaquina))
    personagemComputador = pygame.transform.flip(personagemComputador, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill((65, 81, 106))

        gameDisplay.blit(personagemJogador, (216, 190))
        gameDisplay.blit(personagemComputador, (440, 190))

        pygame_display.update()
        clock.tick(60)