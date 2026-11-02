def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for l, c in posicoes:
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False

    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                if posicao in posicoes:
                    return False

    return True