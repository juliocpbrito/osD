def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for navios in frota.values():
        for navio in navios:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1
    return tabuleiro


def afundados(frota, tabuleiro):
    total = 0
    for navios in frota.values():
        for navio in navios:
            if all(tabuleiro[l][c] == 'X' for l, c in navio):
                total += 1
    return total


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
