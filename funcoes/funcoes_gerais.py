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

def armazenar(informacao, arquivo):
    conteudo = ler_registro(arquivo)
    
    conteudo.append("%s\n"%informacao)

    registrar(arquivo, ''.join(conteudo))