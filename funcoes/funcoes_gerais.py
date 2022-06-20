import pygame
pygame.init()

def escreveTela(texto, cor, tamanho):
    fonte = pygame.font.Font("freesansbold.ttf", tamanho)
    frase = fonte.render(texto, True, cor)
    return frase

def registrar(arquivo, informacoes):
    arquivo = open(arquivo, "w")
    arquivo.write(informacoes)
    arquivo.close()

def ler_registro(arquivo):
    arquivo = open(arquivo, "r")
    conteudo = arquivo.readlines()
    arquivo.close()
    return conteudo

def armazenar(arquivo):
    try:
        conteudo = ler_registro(arquivo)
    except:
        conteudo = []
    
    conteudo.append("Historico %s 1\n"%str(len(conteudo)+1))

    registrar(arquivo, ''.join(conteudo))