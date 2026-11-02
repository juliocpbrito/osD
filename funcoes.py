def define_posicoes(linha,coluna,sentido,tamanho):
    posicoes = [] 
    for i in range(tamanho):
        if sentido == "vertical":
            posicoes.append([linha + i,coluna])
        else:
            posicoes.append([linha,coluna+i])
    return posicoes 

