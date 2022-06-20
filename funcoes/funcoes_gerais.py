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
    try:
        arquivo = open(arquivo, "r")
        conteudo = arquivo.readlines()
        arquivo.close()
        return conteudo
        
    except:
        return []

def armazenar(arquivo):
    conteudo = ler_registro(arquivo)
    
    conteudo.append("Historico %s 1\n"%str(len(conteudo)+1))

    registrar(arquivo, ''.join(conteudo))