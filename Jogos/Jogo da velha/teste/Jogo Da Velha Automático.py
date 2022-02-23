import colorama
import os
import random
colorama.init()
blank = " "
p1 = "\033[34mX\033[m"
p2 = "\033[31mO\033[m"
winx = 0
wino = 0
listaNome = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


def logo():
    print("\033[1;35m        _                                 _            __     __         _   _             ")
    print("       | |   ___     __ _    ___       __| |   __ _    \ \   / /   ___  | | | |__     __ _ ")
    print("    _  | |  / _ \   / _` |  / _ \     / _` |  / _` |    \ \ / /   / _ \ | | | '_ \   / _` |")
    print("   | |_| | | (_) | | (_| | | (_) |   | (_| | | (_| |     \ V /   |  __/ | | | | | | | (_| |")
    print("    \___/   \___/   \__, |  \___/     \__,_|  \__,_|      \_/     \___| |_| |_| |_|  \__,_|")
    print(
        "                    |___/                                                           \033[m ")


def quadro():
    print(
        "                                 \033[1;36m         1   2   3\033[m")
    print(
        f"{' ' * 39}\033[1;36ma\033[m  {listaVar[0]} | {listaVar[1]} | {listaVar[2]}")
    print(f"{' ' * 41}{'-' * 11}")
    print(
        f"{' ' * 39}\033[1;36mb\033[m  {listaVar[3]} | {listaVar[4]} | {listaVar[5]}")
    print(f"{' ' * 41}{'-' * 11}")
    print(
        f"{' ' * 39}\033[1;36mc\033[m  {listaVar[6]} | {listaVar[7]} | {listaVar[8]}")


print("\033[1;35mJogo da Velha\033[m")
print("Escreva a posição que você quer utilizando a tabela (Exemplo: a1, b2)")
print("Para terminar o jogo no meio dele, escreva 'reset' ao invés de uma posição")
print("\033[1;31mBom jogo!\033[m")
input("Dê enter para começar o jogo")
os.system('cls')
while True:
    listaVar = [blank, blank, blank, blank, blank, blank, blank, blank, blank]
    wino = 0
    winx = 0
    while True:
        logo()
        quadro()
        while True:
            casaEscolhida = input(f"\n{' '*37}\033[34mVez do Player 1:\033[m ")
            if casaEscolhida == "reset":
                break
            if casaEscolhida not in listaNome:
                input("Esta casa não existe (Enter para tentar novamente)")
                os.system('cls')
                continue
            lugar = listaNome.index(casaEscolhida)
            if listaVar[lugar] != blank:
                input("Esta casa já foi preenchida (Enter para tentar novamente)")
                os.system('cls')
                continue
            listaVar[lugar] = p1

            vitxria1x = all([listaVar[0] == p1, listaVar[4]
                            == p1, listaVar[8] == p1])
            vitxria2x = all([listaVar[0] == p1, listaVar[1]
                            == p1, listaVar[2] == p1])
            vitxria3x = all([listaVar[3] == p1, listaVar[4]
                            == p1, listaVar[5] == p1])
            vitxria4x = all([listaVar[6] == p1, listaVar[7]
                            == p1, listaVar[8] == p1])
            vitxria5x = all([listaVar[0] == p1, listaVar[3]
                            == p1, listaVar[6] == p1])
            vitxria6x = all([listaVar[1] == p1, listaVar[4]
                            == p1, listaVar[7] == p1])
            vitxria7x = all([listaVar[2] == p1, listaVar[5]
                            == p1, listaVar[8] == p1])
            vitxria8x = all([listaVar[2] == p1, listaVar[4]
                            == p1, listaVar[6] == p1])

            if vitxria1x is True:
                winx += 1
            if vitxria2x is True:
                winx += 1
            if vitxria3x is True:
                winx += 1
            if vitxria4x is True:
                winx += 1
            if vitxria5x is True:
                winx += 1
            if vitxria6x is True:
                winx += 1
            if vitxria7x is True:
                winx += 1
            if vitxria8x is True:
                winx += 1
            break
        os.system('cls')
        logo()
        quadro()

        if winx == 1:
            print("--------------------------")
            print("\033[34mPlayer 1 \033[32mganhou a partida\033[m")
            print("--------------------------")
            break
        if wino == 1:
            print("--------------------------")
            print("\033[34mPlayer 2 \033[32mganhou a partida\033[m")
            print("--------------------------")
            break
        listaEmpate = [listaVar[0] != blank, listaVar[1] != blank, listaVar[2] != blank, listaVar[3] != blank,
                       listaVar[4] != blank, listaVar[5] != blank, listaVar[6] != blank, listaVar[7] != blank, listaVar[8] != blank]
        if all(listaEmpate):
            print("--------------------------")
            print("\033[33mEmpate/Velha\033[m")
            print("--------------------------")
            break
        os.system('cls')

        if casaEscolhida == "reset":
            break

        while True:
            logo()
            quadro()
            casaEscolhida = random.choice(listaNome)
            lugar = listaNome.index(casaEscolhida)
            if listaVar[lugar] != blank:
                os.system('cls')
                continue
            listaVar[lugar] = p2

            vitoria1o = all([listaVar[0] == p2, listaVar[4]
                            == p2, listaVar[8] == p2])
            vitoria2o = all([listaVar[0] == p2, listaVar[1]
                            == p2, listaVar[2] == p2])
            vitoria3o = all([listaVar[3] == p2, listaVar[4]
                            == p2, listaVar[5] == p2])
            vitoria4o = all([listaVar[6] == p2, listaVar[7]
                            == p2, listaVar[8] == p2])
            vitoria5o = all([listaVar[0] == p2, listaVar[3]
                            == p2, listaVar[6] == p2])
            vitoria6o = all([listaVar[1] == p2, listaVar[4]
                            == p2, listaVar[7] == p2])
            vitoria7o = all([listaVar[2] == p2, listaVar[5]
                            == p2, listaVar[8] == p2])
            vitoria8o = all([listaVar[2] == p2, listaVar[4]
                            == p2, listaVar[6] == p2])

            if vitoria1o is True:
                wino += 1
            if vitoria2o is True:
                wino += 1
            if vitoria3o is True:
                wino += 1
            if vitoria4o is True:
                wino += 1
            if vitoria5o is True:
                wino += 1
            if vitoria6o is True:
                wino += 1
            if vitoria7o is True:
                wino += 1
            if vitoria8o is True:
                wino += 1
            break
        os.system('cls')
        if winx == 1:
            print("--------------------------")
            print("\033[34mPlayer 1 \033[32mganhou a partida\033[m")
            print("--------------------------")
            break
        if wino == 1:
            print("--------------------------")
            print("\033[34mPlayer 2 \033[32mganhou a partida\033[m")
            print("--------------------------")
            break
        listaEmpate = [listaVar[0] != blank, listaVar[1] != blank, listaVar[2] != blank, listaVar[3] != blank,
                       listaVar[4] != blank, listaVar[5] != blank, listaVar[6] != blank, listaVar[7] != blank, listaVar[8] != blank]
        if all(listaEmpate):
            print("--------------------------")
            print("\033[33mEmpate/Velha\033[m")
            print("--------------------------")
            break
        os.system('cls')

        if casaEscolhida == "reset":
            break

    while True:
        print("Você quer jogar novamente? (\033[32ms\033[m/\033[31mn\033[m)")
        jogardenovo = input("").upper()
        if jogardenovo == "N":
            break
        if jogardenovo == "S":
            os.system('cls')
            break
        else:
            print("Escreva S (sim) ou N (não)!")
            input("Dê enter para tentar novamente")
            os.system("cls")
    if jogardenovo == "N":
        break
