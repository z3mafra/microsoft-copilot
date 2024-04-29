
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def exibe():
    for linha in board:
        for valor in linha:
            if valor == 0:
                print("__", end=" ")
            elif valor == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def exibe():
    for linha in board:
        for valor in linha:
            if valor == 0:
                print("__", end=" ")
            elif valor == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def ganhou():
    # Verifica linhas
    for linha in board:
        if all(valor == 1 for valor in linha):
            return 1  # Jogador 1 (X) venceu
        elif all(valor == -1 for valor in linha):
            return -1  # Jogador 2 (O) venceu

    # Verifica colunas
    for coluna in range(3):
        if all(board[linha][coluna] == 1 for linha in range(3)):
            return 1
        elif all(board[linha][coluna] == -1 for linha in range(3)):
            return -1

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return 0  # Nenhum vencedor ainda

# Exemplo de uso:
# Se a função retornar 1, o jogador 1 (X) venceu; se retornar -1, o jogador 2 (O) venceu; se retornar 0, não há vencedor.


def main():
    jogada = 0
    while True:
        exibe()
        jogador = (jogada % 2) + 1
        print(f"Jogador {jogador}, é sua vez:")
        linha = int(input("Digite a linha (1, 2 ou 3): ")) - 1
        coluna = int(input("Digite a coluna (1, 2 ou 3): ")) - 1

        if board[linha][coluna] == 0:
            board[linha][coluna] = 1 if jogador == 1 else -1
            jogada += 1
        else:
            print("Posição já ocupada. Tente novamente.")

        resultado = ganhou()
        if resultado != 0:
            exibe()
            if resultado == 1:
                print("Jogador 1 (X) venceu!")
            else:
                print("Jogador 2 (O) venceu!")
            break

    print("Fim do jogo!")

if __name__ == "__main__":
    main()

