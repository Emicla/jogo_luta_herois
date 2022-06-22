import pygame, random
pygame.init()
from funcoes.funcoes_gerais import ler_registro

largura_tela = 950
altura_tela = 550
tamanho_tela = (largura_tela, altura_tela)
pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

def desenhaRetangulo(cor, x, y, largura, comprimento):
    pygame.draw.rect(gameDisplay, cor, pygame.Rect(x, y, largura, comprimento))

def linhaRetangulo(cor, x, y, largura, comprimento):
    pygame.draw.rect(gameDisplay, cor, pygame.Rect(x, y, largura, comprimento), 2)

def recolheInformacoes(indicePlayer, indiceMaquina):
    dados = ler_registro("Dados personagens.txt")
    numeroHabilidade = ""
    contaHabilidade = 2
    dadosPersonagens = []
    indice = indicePlayer

    for vez in range(1, 3):
        dadosPersonagem = []

        for posicao, numero in enumerate(dados[10 + indice]):
            if numero != " ":
                numeroHabilidade = numeroHabilidade + numero
            else:
                dado = (dados[contaHabilidade].strip("\n"), numeroHabilidade)
                dadosPersonagem.append((dado))
                contaHabilidade += 1
                numeroHabilidade = ""
                
        dadosPersonagem = dict(dadosPersonagem)
        dadosPersonagens.append(dadosPersonagem)
        indice = indiceMaquina
        contaHabilidade = 2
    return dadosPersonagens

def desenhaPersonagem(nomePersonagem, frame, evento, jogadorVirou):
    imagemJogador = pygame.image.load("Imagens Personagens/{0}/{0} {1} {2}.png".format(nomePersonagem, evento, frame))
    if jogadorVirou == True:
        imagemJogador = pygame.transform.flip(imagemJogador, True, False)
    return imagemJogador

def verificaColisao(xJogador, yJogador, xOponente, yOponente):
    if len(list(set(xJogador) & set(xOponente))) > 5 and len(list(set(yJogador) & set(yOponente))) > 5:
        return True
    else:
        return False

def animacaoOponente(oponenteFrame, dadosOponente, incrementoVeri, incrementoFrame, personagemComputador, jogadorVirou, oponenteEnegia, numeroAleatorio, evento):
    habilitaOponente = False
    habilita = False
    if oponenteFrame >= dadosOponente + incrementoVeri:
        oponenteFrame = 1
        habilitaOponente = True
        numeroAleatorio = random.randrange(1, 5)
        oponente = desenhaPersonagem(personagemComputador, 1, "parado", jogadorVirou)
        oponenteEnegia -= 100
        habilita = True
    else:
        oponente = desenhaPersonagem(personagemComputador, int(oponenteFrame), evento, jogadorVirou)
        oponenteFrame += incrementoFrame

    return [oponenteFrame, habilitaOponente, numeroAleatorio, oponente, oponenteEnegia, habilita]

def luta(personagemPlayer, personagemComputador, indicePlayer, indiceMaquina):

    dadosPersonagens = recolheInformacoes(indicePlayer, indiceMaquina)
    dadosPlayer = dadosPersonagens[0]
    dadosOponente = dadosPersonagens[1]

    jogadorVirou = False
    jogadorAndando = False
    jogadorPulou = False
    habilitaOponente = True
    oponenteEspecial = False
    socoOponente = False
    oponenteDisparou = False
    podeJogar = True
    jogadorAtacou = False
    jogadorEspecial = False
    jogadorPoder = False
    jogadorDisparou = False

    jogador = desenhaPersonagem(personagemPlayer, 1, "parado", jogadorVirou)
    jogadorPosX = 216
    jogadorPosY = 190
    jogadorMovimentoX = 0
    jogadorMovimentoY = 0
    jogadorFrame = 1
    jogadorVida = 400
    jogadorEnergia = 400
    oponente = desenhaPersonagem(personagemComputador, 1, "parado", jogadorVirou)
    oponente = pygame.transform.flip(oponente, True, False)
    oponentePosX = 440
    oponentePosY = 190
    oponenteMovimentoX = 0
    oponenteFrame = 1
    oponenteEnegia = 400
    oponenteVida = 400
    oponentePoder = False

    larguraPersonagens = 105
    alturaPersonagens = 119
    poderOponente = pygame.image.load("Imagens Personagens/{0}/{0} poder.png".format(personagemComputador))
    poderOponenteposX = 0
    poderOponenteposY = 0

    poderJogador = pygame.image.load("Imagens Personagens/{0}/{0} poder.png".format(personagemPlayer))
    poderJogadorposX = 0
    poderJogadorposY = 0

    larguraPoder = 51
    alturaPoder = 50
    velocidePoder = 10
    velocidePoderPlayer = 10

    numeroAleatorio = random.randrange(1, 5)

    while True:
        pixelsXJogador = list(range(jogadorPosX, jogadorPosX + larguraPersonagens + 1))
        pixelsXOponente = list(range(oponentePosX, oponentePosX + larguraPersonagens + 1))

        pixelsXPoderOponente = list(range(poderOponenteposX, poderOponenteposX + larguraPoder + 1))
        pixelsXPoderJogador = list(range(poderJogadorposX, poderJogadorposX + larguraPoder + 1))

        pixelsYPoderOponente = list(range(poderOponenteposY, poderOponenteposY + alturaPoder + 1))
        pixelsYPoderJogador = list(range(poderJogadorposY, poderJogadorposY + alturaPoder + 1))

        pixelsYJogador = list(range(jogadorPosY, jogadorPosY + alturaPersonagens + 1))
        pixelsYOponente = list(range(oponentePosY, oponentePosY + alturaPersonagens + 1))


        for event in pygame.event.get():
            pygame.time.set_timer(pygame.USEREVENT + 1, 50)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if podeJogar == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jogadorMovimentoX = -int(dadosPlayer["Velocidade"])
                        jogadorAndando = True

                        if jogadorVirou == False:
                            jogadorVirou = True
                            jogador = pygame.transform.flip(jogador, True, False)

                    elif event.key == pygame.K_RIGHT:
                        jogadorAndando = True
                        jogadorMovimentoX = +int(dadosPlayer["Velocidade"])
                        if jogadorVirou == True:
                            jogadorVirou = False
                            jogador = pygame.transform.flip(jogador, True, False)

                    elif event.key == pygame.K_UP:
                        jogadorPulou = True
                    
                    elif event.key == pygame.K_a and jogadorAndando == False:
                        jogadorAtacou = True
                        podeJogar = False
                        jogadorFrame = 1
                    
                    elif event.key == pygame.K_s and jogadorAndando == False and jogadorDisparou == False:
                        jogadorEspecial = True
                        podeJogar = False
                        jogadorFrame = 1
                        poderJogadorposX = jogadorPosX
                        poderJogadorposY = jogadorPosY
                    
                    elif event.key == pygame.K_d and jogadorAndando == False:
                        jogador = desenhaPersonagem(personagemPlayer, int(jogadorFrame), "carregando", jogadorVirou)
                        if jogadorEnergia < 400:
                            jogadorEnergia += 10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        jogadorMovimentoX = 0
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", jogadorVirou)
                        jogadorAndando = False
            else:
                jogadorMovimentoX = 0
                jogadorMovimentoY = 0

            if event.type == pygame.USEREVENT + 1:
                if jogadorAndando == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(jogadorFrame), "andando", jogadorVirou)

                    if jogadorFrame >= int(dadosPlayer["Frames Andando"]):
                        jogadorFrame = 1
                    else:
                        jogadorFrame += 1

                if socoOponente == True:
                    if verificaColisao(pixelsXJogador, pixelsYJogador, pixelsXOponente, pixelsYOponente) == True:
                        jogadorVida -= (int(dadosOponente["Forca"]) - 5)
                    
                    infOponente = animacaoOponente(oponenteFrame, int(dadosOponente["Frames Luta"]), 1, 0.6, personagemComputador, jogadorVirou, oponenteEnegia, numeroAleatorio, "soco")
                    oponenteFrame = infOponente[0]
                    habilitaOponente = infOponente[1]
                    numeroAleatorio = infOponente[2]
                    oponente = infOponente[3]
                    oponenteEnegia = infOponente[4]

                    if infOponente[5] == True:
                        socoOponente = False
                
                if oponenteEspecial == True:
                    infOponente = animacaoOponente(oponenteFrame, int(dadosOponente["Frames Poder"]), 0, 0.4, personagemComputador, jogadorVirou, oponenteEnegia, numeroAleatorio, "especial")
                    oponenteFrame = infOponente[0]
                    habilitaOponente = infOponente[1]
                    numeroAleatorio = infOponente[2]
                    oponente = infOponente[3]
                    oponenteEnegia = infOponente[4]

                    if infOponente[5] == True:
                        oponenteEspecial = False
                        oponentePoder = True
                        poderOponenteposX = oponentePosX
                        poderOponenteposY = oponentePosY
                    
                if jogadorAtacou == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(jogadorFrame), "soco", jogadorVirou)
                    if len(list(set(pixelsXJogador) & set(pixelsXOponente))) > 10:
                        oponenteVida -= 2

                    if jogadorFrame >= int(dadosPlayer["Frames Luta"]):
                        jogadorFrame = 1
                        jogadorAtacou = False
                        podeJogar = True
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", jogadorVirou)
                    else:
                        jogadorFrame += 1
                
                if jogadorEspecial == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(jogadorFrame), "especial", jogadorVirou)
                    if jogadorFrame >= int(dadosPlayer["Frames Poder"]) + 0.5:
                        jogadorFrame = 1
                        jogadorEspecial = False
                        podeJogar = True
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", jogadorVirou)
                        jogadorEnergia -= 10
                        jogadorPoder = True
                    else:
                        jogadorFrame += 0.5

        if habilitaOponente == True:
            print(numeroAleatorio)
            if numeroAleatorio == 1:
                if oponentePosX + larguraPersonagens > largura_tela or oponentePosX < 0:
                    oponenteMovimentoX = 0
                    numeroAleatorio = random.randrange(1, 5)

                elif 0 < oponentePosX - jogadorPosX < 200:
                    oponenteMovimentoX = int(dadosOponente["Velocidade"])

                elif 0 > oponentePosX - jogadorPosX > -200:
                    oponenteMovimentoX = -int(dadosOponente["Velocidade"])
                else:
                    oponenteMovimentoX = 0
                    numeroAleatorio = random.randrange(1, 5)

            elif numeroAleatorio == 2:
                if oponenteEnegia < 400:
                    oponente = pygame.image.load("Imagens Personagens/{0}/{0} carregando 1.png".format(personagemComputador))
                    oponenteEnegia += 1
                else:
                    oponente = desenhaPersonagem(personagemComputador, 1, "parado", jogadorVirou)
                    numeroAleatorio = random.randrange(1, 5)

            elif numeroAleatorio == 3:
                if jogadorPosX + larguraPersonagens - 10 < oponentePosX and socoOponente == False:
                    oponenteMovimentoX = -int(dadosOponente["Velocidade"])

                elif jogadorPosX > oponentePosX and socoOponente == False:
                    oponenteMovimentoX = int(dadosOponente["Velocidade"])

                else:
                    socoOponente = True
                    habilitaOponente = False
                    oponenteMovimentoX = 0
            
            elif numeroAleatorio == 4:
                if oponentePoder == False:
                    oponenteEspecial = True
                    habilitaOponente = False
                    oponenteMovimentoX = 0
                else:
                    numeroAleatorio = random.randrange(1, 5)
        
        gameDisplay.fill((65, 81, 106))

        if oponentePoder == True:
            gameDisplay.blit(poderOponente, (poderOponenteposX, poderOponenteposY))
            if len(list(set(pixelsXJogador) & set(pixelsXPoderOponente))) > 5 and oponenteDisparou == True and len(list(set(pixelsYJogador) & set(pixelsYPoderOponente))) > 5:
                jogadorVida -= int(dadosOponente["Dano Energia"])
                oponentePoder = False
                oponenteDisparou = False
                velocidePoder = 10

            else:
                if poderOponenteposX > jogadorPosX and oponenteDisparou == False:
                    velocidePoder = -10

                poderOponenteposX = poderOponenteposX + velocidePoder
                oponenteDisparou = True

                if poderOponenteposX <= 20 or poderOponenteposX >= largura_tela:
                    velocidePoder = 10
                    oponentePoder = False
                    oponenteDisparou = False

        if jogadorPoder == True:
            gameDisplay.blit(poderJogador, (poderJogadorposX, poderJogadorposY))
            if len(list(set(pixelsXOponente) & set(pixelsXPoderJogador))) > 5 and jogadorDisparou == True and len(list(set(pixelsYOponente) & set(pixelsYPoderJogador))) > 5:
                oponenteVida -= int(dadosPlayer["Dano Energia"])
                jogadorPoder = False
                jogadorDisparou = False
                velocidePoderPlayer = 10

            else:
                if poderJogadorposX > oponentePosX and jogadorDisparou == False:
                    velocidePoderPlayer = -10

                poderJogadorposX = poderJogadorposX + velocidePoderPlayer
                jogadorDisparou = True

                if poderJogadorposX <= 20 or poderJogadorposX >= largura_tela:
                    velocidePoderPlayer = 10
                    jogadorPoder = False
                    jogadorDisparou = False

        if jogadorPulou == True and jogadorPosY > 20:
            jogadorPosY -= int(dadosPlayer["Velocidade"])

        elif jogadorPosY < 200:
            jogadorPulou = False
            jogadorPosY += int(dadosPlayer["Velocidade"])
        
        jogadorPosX += jogadorMovimentoX
        jogadorPosY += jogadorMovimentoY

        oponentePosX += oponenteMovimentoX

        desenhaRetangulo((255, 0, 0), 30, 30, jogadorVida, 40)
        desenhaRetangulo((255, 255, 0), 30, 80, jogadorEnergia, 20)
        linhaRetangulo((0, 0, 0), 30, 30, 400, 40)
        linhaRetangulo((0, 0, 0), 30, 80, 400, 20)

        desenhaRetangulo((255, 0, 0), 500, 30, oponenteVida, 40)
        desenhaRetangulo((255, 255, 0), 500, 80, oponenteEnegia, 20)
        linhaRetangulo((0, 0, 0), 500, 30, 400, 40)
        linhaRetangulo((0, 0, 0), 500, 80, 400, 20)

        gameDisplay.blit(oponente, (oponentePosX, 190))
        gameDisplay.blit(jogador, (jogadorPosX, jogadorPosY))

        if jogadorVida <= 0:
            return ["Resultado", "PERDEU", 0]

        elif oponenteVida <= 0:
            return ["Resultado", "GANHOU", 1]

        pygame_display.update()
        clock.tick(60)