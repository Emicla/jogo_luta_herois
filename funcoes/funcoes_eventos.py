import pygame, random
pygame.init()
largura_tela = 950
altura_tela = 550

tamanho_tela = (largura_tela, altura_tela)

pygame_display = pygame.display
gameDisplay = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

from funcoes.funcoes_gerais import ler_registro

def desenhaRetangulo(cor, x, y, largura, comprimento):
    pygame.draw.rect(gameDisplay, cor, pygame.Rect(x, y, largura, comprimento))

def linhaRetangulo(cor, x, y, largura, comprimento):
    pygame.draw.rect(gameDisplay, cor, pygame.Rect(x, y, largura, comprimento), 2)

def escreveTela(texto, cor, tamanho):
    fonte = pygame.font.Font("freesansbold.ttf", tamanho)
    frase = fonte.render(texto, True, cor)
    return frase

def recolheInformacoes(indicePlayer, indiceMaquina):
    dados = ler_registro("Arquivos/Dados personagens.txt")
    numeroHabilidade = ""
    contaHabilidade = 0
    dadosPersonagens = []
    indice = indicePlayer
    nomeDado = ""
    nomesHabilidades = []

    for posicao, letraDado in enumerate(dados[2]):
        if letraDado != " " and letraDado != "\n":
            nomeDado += letraDado

        elif letraDado == " " and len(nomeDado) > 0:
            nomesHabilidades.append(nomeDado)
            nomeDado = ""

    for vez in range(1, 3):
        dadosPersonagem = []

        for posicao, numero in enumerate(dados[4 + indice]):
            if numero == " " and len(numeroHabilidade) > 0 and numero != "\n":
                dado = (nomesHabilidades[contaHabilidade], numeroHabilidade)
                dadosPersonagem.append((dado))
                contaHabilidade += 1
                numeroHabilidade = ""

            elif numero != " " and numero != "\n":
                numeroHabilidade = numeroHabilidade + numero

            # if numero != " ":
            #     numeroHabilidade = numeroHabilidade + numero
            # else:
            #     dado = (dados[contaHabilidade].strip("\n"), numeroHabilidade)
            #     dadosPersonagem.append((dado))
            #     contaHabilidade += 1
            #     numeroHabilidade = ""
                
        dadosPersonagem = dict(dadosPersonagem)
        dadosPersonagens.append(dadosPersonagem)
        indice = indiceMaquina
        contaHabilidade = 0
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

def desenhaPoder(imagemPoder, poderPosX, poderPosY, colisaoX, colisaoY, verificacao):
    gameDisplay.blit(imagemPoder, (poderPosX, poderPosY))

    if colisaoX > 5 and verificacao == True and colisaoY > 5:
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

def desenhaCenario(oponente, jogador, jogadorVida, jogadorEnergia, oponenteVida, oponentePosX, jogadorPosX, jogadorPosY , oponenteEnegia,imagemFundo):
    # gameDisplay.fill((65, 81, 106))
    gameDisplay.blit(imagemFundo, (0, 0))
    
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
    
    pygame_display.update()
    clock.tick(60)