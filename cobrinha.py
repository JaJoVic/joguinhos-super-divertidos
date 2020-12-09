import random
from os import system, name


def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()

    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols = int(input('Número de colunas do tabuleiro: '))
    x0 = int(input('Posição x inicial da cobrinha : '))
    y0 = int(input('Posição y inicial da cobrinha : '))
    t = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cameçar
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")

    else:

        ''' Inicia a variavel d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas a  esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1:
            d = d * 10 + 2
            i = i + 1

        # Laço que controla a interação com o jogador
        direcao = 1
        maca = [0, 0]
        posicao_maca(nlinhas, ncols, maca)
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d, maca)

            # lê o número do proximo movimento que sera executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu proximo movimento: "))

            if direcao != 5:
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao, maca)

    print()
    print("Tchau!")

# ======================================================================


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# ======================================================================


def num_digitos(n):
    """ (int) -> int

    Devolve o numero de di­gitos de um numero.

    ENTRADA
    - n: numero a ser verificado

    """

    c = 1
    n //= 10
    while n > 0:
        c += 1
        n //= 10

    return c

# ======================================================================


def posicao_maca(nlinhas, ncols, maca):
    maca[0] = random.randrange(0, nlinhas)
    maca[1] = random.randrange(0, ncols)

# ======================================================================


def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    """(int, int, int, int, int, int, int) -> bool

    Devolve True se alguma parte da cobra ocupa a posição (x,y) e
    False no caso contrario.

    ENTRADAS
    - nlinhas, ncols: numero de linhas e colunas do tabuleiro
    - x, y: posição a ser testada
    - x0, y0: posição da cabeça da cobra
    - d: sequencia de deslocamentos que levam a posição da cauda da cobra
         ate a cabeça; o di­gito menos significativo Ã© a direção na cabeça

    """

    if x == x0 and y == y0:
        return True         # Posição esta na cabeça da cobra

    while d != 0:
        direcao = d % 10
        if direcao == 1:    # esquerda
            x0 += 1
        elif direcao == 2:  # direita
            x0 -= 1
        elif direcao == 3:  # cima
            y0 += 1
        elif direcao == 4:  # baixo
            y0 -= 1

        if x == x0 and y == y0:
            return True     # PosiÃ§Ã£o estÃ¡ corpo da cobra

        d //= 10

    return False

# ======================================================================


def imprime_tabuleiro(nlinhas, ncols, x0, y0, d, maca):
    """(int, int, int, int, int, int)

    Imprime o tabuleiro com a cobra.

    ENTRADAS
    - nlinhas, ncols: numero de linhas e colunas do tabuleiro
    - x0, y0: posição da cabeça da cobra
    - d: sequencia de deslocamentos que levam a posição da cauda da cobra
         ate a cabeça; o di­gito menos significativo Ã© a direção na cabeça

    """
    clear()
    print()

    for x in range(0, ncols + 2):
        print('#', end='')

    print()

    for y in range(0, nlinhas):
        print('#', end='')

        for x in range(0, ncols):
            if (x == maca[0]) and (y == maca[1]):
                if (maca[0] != x0) or (maca[1] != y0):
                    print('M', end='')
            elif x == x0 and y == y0:
                print('C', end='')
            elif pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
                print('*', end='')
            else:
                print('.', end='')

        print('#')

    for x in range(0, ncols + 2):
        print('#', end='')

    print()
    print()

# ======================================================================


def move(nlinhas, ncols, x0, y0, d, direcao, maca):
    """(int, int, int, int, int, int) -> int, int, int

    Move a cobra na direÃ§Ã£o dada.    
    A funÃ§Ã£o devolve os novos valores de x0, y0 e d (nessa ordem).
    Se o movimento Ã© impossÃ­vel (pois a cobra vai colidir consigo mesma ou
    com a parede), entÃ£o a funÃ§Ã£o devolve os antigos valores e imprime a
    mensagem apropriada: "COLISÃƒO COM SI MESMA" ou "COLISÃƒO COM A PAREDE"

    ENTRADAS
    - nlinhas, ncols: numero de linhas e colunas do tabuleiro
    - x0, y0: posiÃ§Ã£o da cabeÃ§a da cobra
    - d: sequÃªncia de deslocamentos que levam a posiÃ§Ã£o da cauda da cobra
         atÃ© a cabeÃ§a; o dÃ­gito menos significativo Ã© a direÃ§Ã£o na cabeÃ§a
    - direcao: direÃ§Ã£o na qual a cabeÃ§a deve ser movida

    """

    ndig = num_digitos(d)
    novo_d = (d % 10 ** (ndig - 1)) * 10 + direcao

    x0_ant = x0
    y0_ant = y0

    if direcao == 1:    # esquerda
        x0 -= 1
    elif direcao == 2:  # direita
        x0 += 1
    elif direcao == 3:  # cima
        y0 -= 1
    elif direcao == 4:  # baixo
        y0 += 1
    else:
        raise ValueError

    if x0 == maca[0] and y0 == maca[1]:
        novo_d = novo_d * 10 + 2
        posicao_maca(nlinhas, ncols, maca)

    if pos_ocupada(nlinhas, ncols, x0, y0, x0_ant, y0_ant, d):
        print("COLISÃO COM SI MESMA")
        return x0_ant, y0_ant, d

    if x0 < 0 or y0 < 0 or x0 >= nlinhas or y0 >= ncols:
        print("COLISÃƒO COM A PAREDE")
        return x0_ant, y0_ant, d

    return x0, y0, novo_d


# ======================================================================
main()
