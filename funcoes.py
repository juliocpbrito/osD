def afundados(frota, tabuleiro):
    total = 0

    for navios in frota.values():
        for navio in navios:
            afundou = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                    break
            if afundou:
                total += 1

    return total