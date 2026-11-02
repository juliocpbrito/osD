from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

# nome do navio: [quantidade, tamanho]
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
                opcao = int(input("[1] Vertical [2] Horizontal >"))
                if opcao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break

            print("Esta posição não está válida!")

print(frota)
