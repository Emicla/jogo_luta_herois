import pygame, random
pygame.init()

from funcoes.funcoes_eventos import recolheInformacoes, desenhaPersonagem, verificaColisao, animacaoOponente, desenhaCenario, desenhaPoder
from funcoes.variaveis_jogador import variaveisJogador, variaveisOponente

largura_tela = 950
altura_tela = 550
tamanho_tela = (largura_tela, altura_tela)
pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

def luta(personagemPlayer, personagemComputador, indicePlayer, indiceMaquina):
    dadosPersonagens = recolheInformacoes(indicePlayer, indiceMaquina)
    dadosPlayer = dadosPersonagens[0]
    dadosOponente = dadosPersonagens[1]

    larguraPersonagens = 105
    alturaPersonagens = 119

    jogador = desenhaPersonagem(personagemPlayer, 1, "parado", variaveisJogador["Virou"])
    
    oponente = desenhaPersonagem(personagemComputador, 1, "parado", variaveisJogador["Virou"])
    oponente = pygame.transform.flip(oponente, True, False)

    poderOponente = pygame.image.load("Imagens Personagens/{0}/{0} poder.png".format(personagemComputador))
    poderOpodnenteposX = 0
    poderOpodnenteposY = 0

    poderJogador = pygame.image.load("Imagens Personagens/{0}/{0} poder.png".format(personagemPlayer))
    poderJodgadorposX = 0
    poderJodgadorposY = 0

    larguraPoder = 51
    alturaPoder = 50
    velocidePoder = 20
    velocidePoderPlayer = 20

    numeroAleatorio = random.randrange(1, 5)

    imagemFundo = pygame.image.load("Imagens/fundo luta.png")

    while True:
        pixelsXJogador = list(range(variaveisJogador["PosX"], variaveisJogador["PosX"] + larguraPersonagens + 1))
        pixelsXOponente = list(range(variaveisOponente["oponentePosX"], variaveisOponente["oponentePosX"] + larguraPersonagens + 1))

        pixelsXPoderOponente = list(range(poderOpodnenteposX, poderOpodnenteposX + larguraPoder + 1))
        pixelsXPoderJogador = list(range(poderJodgadorposX, poderJodgadorposX + larguraPoder + 1))

        pixelsYPoderOponente = list(range(poderOpodnenteposY, poderOpodnenteposY + alturaPoder + 1))
        pixelsYPoderJogador = list(range(poderJodgadorposY, poderJodgadorposY + alturaPoder + 1))

        pixelsYJogador = list(range(variaveisJogador["PosY"], variaveisJogador["PosY"] + alturaPersonagens + 1))
        pixelsYOponente = list(range(variaveisOponente["oponentePosY"], variaveisOponente["oponentePosY"] + alturaPersonagens + 1))


        for event in pygame.event.get():
            pygame.time.set_timer(pygame.USEREVENT + 1, 50)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if variaveisJogador["podeJogar"] == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        variaveisJogador["MovimentoX"] = -int(dadosPlayer["Velocidade"])
                        variaveisJogador["Andando"] = True

                        if variaveisJogador["Virou"] == False:
                            variaveisJogador["Virou"] = True
                            jogador = pygame.transform.flip(jogador, True, False)

                    elif event.key == pygame.K_RIGHT:
                        variaveisJogador["MovimentoX"] = +int(dadosPlayer["Velocidade"])
                        variaveisJogador["Andando"] = True

                        if variaveisJogador["Virou"] == True:
                            variaveisJogador["Virou"] = False
                            jogador = pygame.transform.flip(jogador, True, False)

                    elif event.key == pygame.K_UP and variaveisJogador["Pulou"] == False:
                        variaveisJogador["Pulou"] = True
                        variaveisJogador["MovimentoY"] = -int(dadosPlayer["Velocidade"])
                    
                    elif event.key == pygame.K_a and variaveisJogador["Andando"] == False and variaveisJogador["Atacou"] == False:
                        variaveisJogador["Atacou"] = True
                        variaveisJogador["podeJogar"] = False
                        variaveisJogador["Frames"] = 1
                        if len(list(set(pixelsXJogador) & set(pixelsXOponente))) > 10:
                            variaveisOponente["Vida"] -= 2
                    
                    elif event.key == pygame.K_s and variaveisJogador["Andando"] == False and variaveisJogador["Disparou"] == False:
                        variaveisJogador["Especial"] = True
                        variaveisJogador["podeJogar"] = False
                        variaveisJogador["Frames"] = 1
                        poderJodgadorposX = variaveisJogador["PosX"]
                        poderJodgadorposY = variaveisJogador["PosY"]
                    
                    elif event.key == pygame.K_d and variaveisJogador["Andando"] == False:
                        variaveisJogador["Frames"] = 1.5
                        jogador = desenhaPersonagem(personagemPlayer, int(variaveisJogador["Frames"]), "carregando", variaveisJogador["Virou"])
                        if variaveisJogador["Energia"] < 400:
                            variaveisJogador["Energia"] += 10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        variaveisJogador["MovimentoX"] = 0
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", variaveisJogador["Virou"])
                        variaveisJogador["Andando"] = False
            else:
                variaveisJogador["MovimentoX"] = 0
                variaveisJogador["MovimentoY"] = 0

            if event.type == pygame.USEREVENT + 1:
                if variaveisJogador["Andando"] == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(variaveisJogador["Frames"]), "andando", variaveisJogador["Virou"])

                    if variaveisJogador["Frames"] >= int(dadosPlayer["Andando"]):
                        variaveisJogador["Frames"] = 1
                    else:
                        variaveisJogador["Frames"] += 1

                if variaveisOponente["socoOponente"] == True:
                    if verificaColisao(pixelsXJogador, pixelsYJogador, pixelsXOponente, pixelsYOponente) == True:
                        variaveisJogador["Vida"] -= (int(dadosOponente["Forca"]) - 5)
                    
                    infOponente = animacaoOponente(variaveisOponente["oponenteFrame"], int(dadosOponente["Luta"]), 1, 0.6, personagemComputador, variaveisJogador["Virou"], variaveisOponente["Enegia"], numeroAleatorio, "soco")
                    variaveisOponente["oponenteFrame"] = infOponente[0]
                    variaveisOponente["habilitaOponente"] = infOponente[1]
                    numeroAleatorio = infOponente[2]
                    oponente = infOponente[3]
                    variaveisOponente["Enegia"] = infOponente[4]

                    if infOponente[5] == True:
                        variaveisOponente["socoOponente"] = False
                
                if variaveisOponente["oponenteEspecial"] == True:
                    infOponente = animacaoOponente(variaveisOponente["oponenteFrame"], int(dadosOponente["Poder"]), 0, 0.4, personagemComputador, variaveisJogador["Virou"], variaveisOponente["Enegia"], numeroAleatorio, "especial")
                    variaveisOponente["oponenteFrame"] = infOponente[0]
                    variaveisOponente["habilitaOponente"] = infOponente[1]
                    numeroAleatorio = infOponente[2]
                    oponente = infOponente[3]
                    variaveisOponente["Enegia"] = infOponente[4]

                    if infOponente[5] == True:
                        variaveisOponente["oponenteEspecial"] = False
                        variaveisOponente["oponentePoder"] = True
                        poderOpodnenteposX = variaveisOponente["oponentePosX"]
                        poderOpodnenteposY = variaveisOponente["oponentePosY"]
                    
                if variaveisJogador["Atacou"] == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(variaveisJogador["Frames"]), "soco", variaveisJogador["Virou"])

                    if variaveisJogador["Frames"] >= int(dadosPlayer["Luta"]):
                        variaveisJogador["Frames"] = 1
                        variaveisJogador["Atacou"] = False
                        variaveisJogador["podeJogar"] = True
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", variaveisJogador["Virou"])

                    else:
                        variaveisJogador["Frames"] += 1
                
                if variaveisJogador["Especial"] == True:
                    jogador = desenhaPersonagem(personagemPlayer, int(variaveisJogador["Frames"]), "especial", variaveisJogador["Virou"])
                    if variaveisJogador["Frames"] >= int(dadosPlayer["Poder"]) + 0.5:
                        variaveisJogador["Frames"] = 1
                        variaveisJogador["Especial"] = False
                        variaveisJogador["podeJogar"] = True
                        jogador = desenhaPersonagem(personagemPlayer, 1, "parado", variaveisJogador["Virou"])
                        variaveisJogador["Energia"] -= 10
                        variaveisJogador["jogadorPoder"] = True
                        velocidePoderPlayer = 20
                    else:
                        variaveisJogador["Frames"] += 0.5

        if variaveisOponente["habilitaOponente"] == True:
            if numeroAleatorio == 1:
                if 0 < variaveisOponente["oponentePosX"] - variaveisJogador["PosX"] < 300:
                    variaveisOponente["oponenteMovimentoX"] = int(dadosOponente["Velocidade"])

                elif 0 > variaveisOponente["oponentePosX"] - variaveisJogador["PosX"] > -300:
                    variaveisOponente["oponenteMovimentoX"] = -int(dadosOponente["Velocidade"])
                else:
                    numeroAleatorio = random.randrange(1, 5)
                
                print(variaveisOponente["oponentePosX"] - variaveisJogador["PosX"])

            elif numeroAleatorio == 2:
                if variaveisOponente["Enegia"] < 400:
                    oponente = pygame.image.load("Imagens Personagens/{0}/{0} carregando 1.png".format(personagemComputador))
                    variaveisOponente["Enegia"] += 1
                    variaveisOponente["oponenteMovimentoX"] = 0
                else:
                    oponente = desenhaPersonagem(personagemComputador, 1, "parado", variaveisJogador["Virou"])
                    variaveisOponente["oponenteMovimentoX"] = 0
                    numeroAleatorio = random.randrange(1, 5)

            elif numeroAleatorio == 3:
                if variaveisJogador["PosX"] + larguraPersonagens - 10 < variaveisOponente["oponentePosX"] and variaveisOponente["socoOponente"] == False:
                    variaveisOponente["oponenteMovimentoX"] = -int(dadosOponente["Velocidade"])

                elif variaveisJogador["PosX"] > variaveisOponente["oponentePosX"] and variaveisOponente["socoOponente"] == False:
                    variaveisOponente["oponenteMovimentoX"] = int(dadosOponente["Velocidade"])

                else:
                    variaveisOponente["socoOponente"] = True
                    variaveisOponente["habilitaOponente"] = False
                    variaveisOponente["oponenteMovimentoX"] = 0
            
            elif numeroAleatorio == 4:
                if variaveisOponente["oponentePoder"] == False:
                    variaveisOponente["oponenteEspecial"] = True
                    variaveisOponente["habilitaOponente"] = False
                    variaveisOponente["oponenteMovimentoX"] = 0
                    velocidePoder = 20
                    variaveisOponente["oponenteDisparou"] = False
                else:
                    numeroAleatorio = random.randrange(1, 5)

        desenhaCenario(oponente, jogador, variaveisJogador["Vida"], variaveisJogador["Energia"], variaveisOponente["Vida"], variaveisOponente["oponentePosX"], variaveisJogador["PosX"], variaveisJogador["PosY"] , variaveisOponente["Enegia"], imagemFundo)

        if variaveisOponente["oponentePoder"] == True:
            colisaoX = len(list(set(pixelsXJogador) & set(pixelsXPoderOponente)))
            colisaoY = len(list(set(pixelsYJogador) & set(pixelsYPoderOponente)))
            colidiuPoderOponente = desenhaPoder(poderOponente, poderOpodnenteposX, poderOpodnenteposY, colisaoX, colisaoY, variaveisOponente["oponenteDisparou"])

            if colidiuPoderOponente == True:
                variaveisJogador["Vida"] -= int(dadosOponente["Energia"])
                variaveisOponente["oponentePoder"] = False

            elif poderOpodnenteposX > variaveisJogador["PosX"] and variaveisOponente["oponenteDisparou"] == False:
                velocidePoder = -20

            elif poderOpodnenteposX <= 20 or poderOpodnenteposX >= largura_tela:
                variaveisOponente["oponentePoder"] = False

            poderOpodnenteposX = poderOpodnenteposX + velocidePoder
            variaveisOponente["oponenteDisparou"] = True

        if variaveisJogador["jogadorPoder"] == True:
            colisaoXJogador = len(list(set(pixelsXOponente) & set(pixelsXPoderJogador)))
            colisaoYJogador = len(list(set(pixelsYOponente) & set(pixelsYPoderJogador)))
            colidiuPoderJogador = desenhaPoder(poderJogador, poderJodgadorposX, poderJodgadorposY, colisaoXJogador, colisaoYJogador, variaveisJogador["Disparou"])

            if colidiuPoderJogador == True:
                variaveisOponente["Vida"] -= int(dadosPlayer["Energia"])
                variaveisJogador["jogadorPoder"] = False
                variaveisJogador["Disparou"] = False
            
            elif poderJodgadorposX <= 20 or poderJodgadorposX >= largura_tela:
                variaveisJogador["jogadorPoder"] = False

            elif poderJodgadorposX > variaveisOponente["oponentePosX"] and variaveisJogador["Disparou"] == False:
                velocidePoderPlayer = -20

            else:
                variaveisJogador["Disparou"] = True

            poderJodgadorposX = poderJodgadorposX + velocidePoderPlayer
        
        if variaveisJogador["PosY"] < 20:
            variaveisJogador["MovimentoY"] = -variaveisJogador["MovimentoY"]
        
        elif variaveisJogador["PosY"] > 190:
            variaveisJogador["MovimentoY"] = 0
            variaveisJogador["PosY"] = 190
            variaveisJogador["Pulou"] = False

        variaveisJogador["PosX"] += variaveisJogador["MovimentoX"]
        variaveisJogador["PosY"] += variaveisJogador["MovimentoY"]

        if variaveisOponente["oponentePosX"] + larguraPersonagens > largura_tela:
            print("Maior que a tela")
            variaveisOponente["oponentePosX"] = variaveisOponente["oponentePosX"] - larguraPersonagens - 5
            variaveisOponente["oponenteMovimentoX"] = 0
            numeroAleatorio = random.randrange(1, 5)
            print(variaveisOponente["oponentePosX"])

        elif variaveisOponente["oponentePosX"] < 0:
            print("Menor que a tela")
            variaveisOponente["oponentePosX"] = 5
            variaveisOponente["oponenteMovimentoX"] = 0
            numeroAleatorio = random.randrange(1, 5)

        variaveisOponente["oponentePosX"] += variaveisOponente["oponenteMovimentoX"]

        if variaveisJogador["Vida"] <= 0:
            return ["Resultado", "PERDEU"]

        elif variaveisOponente["Vida"] <= 0:
            return ["Resultado", "GANHOU"]

        pygame_display.update()
        clock.tick(60)