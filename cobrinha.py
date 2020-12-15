import random
from os import system, name


def main():
    NumeroLinhas = int(input('Número de linhas do tabuleiro : '))
    NumeroColunas = int(input('Número de colunas do tabuleiro: '))
    x0 = int(input('Posição x inicial da cobrinha : '))
    y0 = int(input('Posição y inicial da cobrinha : '))
    t = int(input('Tamanho da cobrinha            : '))

    if x0 - (t - 1) < 0:
        print()
        print("A não pode iniciar na posição informada")
    else:
        CorpoCobrinha = 0
        i = 1
        while i <= t-1:
            CorpoCobrinha = CorpoCobrinha * 10 + 2
            i = i + 1

        Direcao = 1
        Maca = [0, 0]
        Posicao_Maca(NumeroLinhas, NumeroColunas, Maca)
        while Direcao != 5:
            Imprime_Tabuleiro(NumeroLinhas, NumeroColunas,
                              x0, y0, CorpoCobrinha, Maca)
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            Direcao = int(
                input("Digite o número correspondente ao seu proximo movimento: "))

            if Direcao != 5:
                x0, y0, CorpoCobrinha = Move(NumeroLinhas, NumeroColunas,
                                             x0, y0, CorpoCobrinha, Direcao, Maca)

    print()
    print("Obrigada por Jogar!")


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def Num_Digitos(n):
    c = 1
    n //= 10
    while n > 0:
        c += 1
        n //= 10

    return c


def Posicao_Maca(NumeroLinhas, NumeroColunas, Maca):
    Maca[0] = random.randrange(0, NumeroLinhas)
    Maca[1] = random.randrange(0, NumeroColunas)


def Pos_Ocupada(NumeroLinhas, NumeroColunas, x, y, x0, y0, CorpoCobrinha):
    if x == x0 and y == y0:
        return True

    while CorpoCobrinha != 0:
        Direcao = CorpoCobrinha % 10
        if Direcao == 1:
            x0 += 1
        elif Direcao == 2:
            x0 -= 1
        elif Direcao == 3:
            y0 += 1
        elif Direcao == 4:
            y0 -= 1

        if x == x0 and y == y0:
            return True

        CorpoCobrinha //= 10

    return False


def Imprime_Tabuleiro(NumeroLinhas, NumeroColunas, x0, y0, CorpoCobrinha, Maca):
    clear()
    print()

    for x in range(0, NumeroColunas + 2):
        print('▅', end='')

    print()

    for y in range(0, NumeroLinhas):
        print('█', end='')

        for x in range(0, NumeroColunas):
            if (x == Maca[0]) and (y == Maca[1]):
                if (Maca[0] != x0) or (Maca[1] != y0):
                    print('❣', end='')
            elif x == x0 and y == y0:
                print('▣', end='')
            elif Pos_Ocupada(NumeroLinhas, NumeroColunas, x, y, x0, y0, CorpoCobrinha):
                print('∎', end='')
            else:
                print('∙', end='')

        print('█')

    for x in range(0, NumeroColunas + 2):
        print('▅', end='')

    print()
    print()


def Move(NumeroLinhas, NumeroColunas, x0, y0, CorpoCobrinha, Direcao, Maca):
    ndig = Num_Digitos(CorpoCobrinha)
    Novo_CorpoCobrinha = (CorpoCobrinha % 10 ** (ndig - 1)) * 10 + Direcao

    x0_ant = x0
    y0_ant = y0

    if Direcao == 1:
        x0 -= 1
    elif Direcao == 2:
        x0 += 1
    elif Direcao == 3:
        y0 -= 1
    elif Direcao == 4:
        y0 += 1
    else:
        raise ValueError

    if x0 == Maca[0] and y0 == Maca[1]:
        Novo_CorpoCobrinha = Novo_CorpoCobrinha * 10 + 2
        Posicao_Maca(NumeroLinhas, NumeroColunas, Maca)

    if Pos_Ocupada(NumeroLinhas, NumeroColunas, x0, y0, x0_ant, y0_ant, CorpoCobrinha):
        print("Colisão consigo mesma")
        return x0_ant, y0_ant, CorpoCobrinha

    if x0 < 0 or y0 < 0 or x0 >= NumeroLinhas or y0 >= NumeroColunas:
        print("Colisão com a parede")
        return x0_ant, y0_ant, CorpoCobrinha

    return x0, y0, Novo_CorpoCobrinha


main()
