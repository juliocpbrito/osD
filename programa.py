from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

embarcacoes = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1],
}

for nome, (quantidade, tamanho) in embarcacoes.items():
    for _ in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "horizontal"
            else:
                opcao = int(input("Orientação: [1] Vertical [2] Horizontal "))
                if opcao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break

            print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = 0
for navios in frota_oponente.values():
    total_navios += len(navios)

ataques = []
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        while True:
            linha = int(input("Jogador, qual linha deseja atacar? "))
            if 0 <= linha <= 9:
                break
            print("Linha inválida!")

        while True:
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
            if 0 <= coluna <= 9:
                break
            print("Coluna inválida!")

        if [linha, coluna] in ataques:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            ataques.append([linha, coluna])
            break

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
