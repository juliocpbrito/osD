def define_posicoes(linha,coluna,sentido,tamanho):
    posicoes = [] 
    for i in range(tamanho):
        if sentido == "vertical":
            posicoes.append([linha + i,coluna])
        else:
            posicoes.append([linha,coluna+i])
    return posicoes 

def preenche_frota(frota, nome_navio, linha, coluna, sentido, tamanho):
    posicoes = define_posicoes(linha, coluna, sentido, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro

