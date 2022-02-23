import os
import random
import colorama
colorama.init()
os.system('cls')
blank = " "
p1 = "\033[34mX\033[m"
p2 = "\033[31mO\033[m"
def logo():
    print("\033[1;35m        _                                 _            __     __         _   _             ")
    print("       | |   ___     __ _    ___       __| |   __ _    \ \   / /   ___  | | | |__     __ _ ")
    print("    _  | |  / _ \   / _` |  / _ \     / _` |  / _` |    \ \ / /   / _ \ | | | '_ \   / _` |")
    print("   | |_| | | (_) | | (_| | | (_) |   | (_| | | (_| |     \ V /   |  __/ | | | | | | | (_| |")
    print("    \___/   \___/   \__, |  \___/     \__,_|  \__,_|      \_/     \___| |_| |_| |_|  \__,_|")
    print("                    |___/                                                           \033[m ")
def quadro():
    print("                                 \033[1;36m         1   2   3\033[m")
    print(f"{' ' * 39}\033[1;36ma\033[m  {c1} | {c2} | {c3}")
    print(f"{' ' * 41}{'-' * 11}")
    print(f"{' ' * 39}\033[1;36mb\033[m  {c4} | {c5} | {c6}")
    print(f"{' ' * 41}{'-' * 11}")
    print(f"{' ' * 39}\033[1;36mc\033[m  {c7} | {c8} | {c9}")
print("\033[1;35mJogo da Velha\033[m")
print("Escreva a posição que você quer utilizando a tabela (Exemplo: a1, b2)")
print("Para terminar o jogo no meio dele, escreva 'reset' ao invés de uma posição")
print("\033[1;31mBom jogo!\033[m")
input("Dê enter para começar o jogo")
os.system('cls')
while True:
    winx = 0
    wino = 0
    empate = 0
    c1 = blank
    c2 = blank
    c3 = blank
    c4 = blank
    c5 = blank
    c6 = blank
    c7 = blank
    c8 = blank
    c9 = blank
    lista = ['a1', 'a2', 'a3', 'b2', 'b1', 'b3', 'c1', 'c2', 'c3']
    while True:
        os.system("cls")
        escolhido = 0
        while escolhido != 1:
            os.system("cls")
            logo()
            print("")
            quadro()
            print("")
            escolhax = input(f"{' '*37}\033[34mVez do Player 1:\033[m ")
            if escolhax == "reset":
                break
            if escolhax == "a1":
                if c1 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c1 == blank:
                    c1 = p1
                    escolhido += 1
            elif escolhax == "a2":
                if c2 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c2 == blank:
                    c2 = p1
                    escolhido += 1
            elif escolhax == "a3":
                if c3 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c3 == blank:
                    c3 = p1
                    escolhido += 1
            elif escolhax == "b1":
                if c4 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c4 == blank:
                    c4 = p1
                    escolhido += 1
            elif escolhax == "b2":
                if c5 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c5 == blank:
                    c5 = p1
                    escolhido += 1
            elif escolhax == "b3":
                if c6 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c6 == blank:
                    c6 = p1
                    escolhido += 1
            elif escolhax == "c1":
                if c7 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c7 == blank:
                    c7 = p1
                    escolhido += 1
            elif escolhax == "c2":
                if c8 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c8 == blank:
                    c8 = p1
                    escolhido += 1
            elif escolhax == "c3":
                if c9 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c9 == blank:
                    c9 = p1
                    escolhido += 1
            else:
                input("\033[31mInsira uma das casas! (Pressione Enter)\033[m")
                os.system("cls")
        if escolhax == "reset":
            break
        escolhido = 0

        os.system("cls")

        vitxria1x = [c1 == p1, c5 == p1, c9 == p1]
        vitxria1xv = all(vitxria1x)
        vitxria2x = [c1 == p1, c2 == p1, c3 == p1]
        vitxria2xv = all(vitxria2x)
        vitxria3x = [c4 == p1, c5 == p1, c6 == p1]
        vitxria3xv = all(vitxria3x)
        vitxria4x = [c7 == p1, c8 == p1, c9 == p1]
        vitxria4xv = all(vitxria4x)
        vitxria5x = [c1 == p1, c4 == p1, c7 == p1]
        vitxria5xv = all(vitxria5x)
        vitxria6x = [c2 == p1, c5 == p1, c8 == p1]
        vitxria6xv = all(vitxria6x)
        vitxria7x = [c3 == p1, c6 == p1, c9 == p1]
        vitxria7xv = all(vitxria7x)
        vitxria8x = [c3 == p1, c5 == p1, c7 == p1]
        vitxria8xv = all(vitxria8x)

        if vitxria1xv is True:
            winx += 1
        if vitxria2xv is True:
            winx += 1
        if vitxria3xv is True:
            winx += 1
        if vitxria4xv is True:
            winx += 1
        if vitxria5xv is True:
            winx += 1
        if vitxria6xv is True:
            winx += 1
        if vitxria7xv is True:
            winx += 1
        if vitxria8xv is True:
            winx += 1

        empatelista = [c1 != blank, c2 != blank, c3 != blank, c4 != blank, c5 != blank, c6 != blank, c7 != blank,
                       c8 != blank, c9 != blank]
        empate = all(empatelista)

        if winx > 0:
            break
        if empate is True:
            break

        while escolhido != 1:
            os.system("cls")
            logo()
            print("")
            quadro()
            print("")
            escolhao = input(f"{' '*37}\033[31mVez do Player 2:\033[m ")
            if escolhao == "reset":
                break
            if escolhao == "a1":
                if c1 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c1 == blank:
                    c1 = p2
                    escolhido += 1
            elif escolhao == "a2":
                if c2 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c2 == blank:
                    c2 = p2
                    escolhido += 1
            elif escolhao == "a3":
                if c3 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c3 == blank:
                    c3 = p2
                    escolhido += 1
            elif escolhao == "b1":
                if c4 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c4 == blank:
                    c4 = p2
                    escolhido += 1
            elif escolhao == "b2":
                if c5 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c5 == blank:
                    c5 = p2
                    escolhido += 1
            elif escolhao == "b3":
                if c6 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c6 == blank:
                    c6 = p2
                    escolhido += 1
            elif escolhao == "c1":
                if c7 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c7 == blank:
                    c7 = p2
                    escolhido += 1
            elif escolhao == "c2":
                if c8 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c8 == blank:
                    c8 = p2
                    escolhido += 1
            elif escolhao == "c3":
                if c9 != blank:
                    print("Esta casa já foi escolhida (Pressione Enter)")
                    input("")
                if c9 == blank:
                    c9 = p2
                    escolhido += 1
            else:
                input("\033[31mInsira uma das casas! (Pressione Enter)\033[m")
                input("")
                os.system("cls")
        if escolhao == "reset":
            break
        vitoria1o = [c1 == p2, c5 == p2, c9 == p2]
        vitoria1ov = all(vitoria1o)
        vitoria2o = [c1 == p2, c2 == p2, c3 == p2]
        vitoria2ov = all(vitoria2o)
        vitoria3o = [c4 == p2, c5 == p2, c6 == p2]
        vitoria3ov = all(vitoria3o)
        vitoria4o = [c7 == p2, c8 == p2, c9 == p2]
        vitoria4ov = all(vitoria4o)
        vitoria5o = [c1 == p2, c4 == p2, c7 == p2]
        vitoria5ov = all(vitoria5o)
        vitoria6o = [c2 == p2, c5 == p2, c8 == p2]
        vitoria6ov = all(vitoria6o)
        vitoria7o = [c3 == p2, c6 == p2, c9 == p2]
        vitoria7ov = all(vitoria7o)
        vitoria8o = [c3 == p2, c5 == p2, c7 == p2]
        vitoria8ov = all(vitoria8o)

        if vitoria1ov is True:
            wino += 1
        if vitoria2ov is True:
            wino += 1
        if vitoria3ov is True:
            wino += 1
        if vitoria4ov is True:
            wino += 1
        if vitoria5ov is True:
            wino += 1
        if vitoria6ov is True:
            wino += 1
        if vitoria7ov is True:
            wino += 1
        if vitoria8ov is True:
            wino += 1

        empatelista = [c1 != blank, c2 != blank, c3 != blank, c4 != blank, c5 != blank, c6 != blank, c7 != blank,
                       c8 != blank, c9 != blank]
        empate = all(empatelista)

        os.system("cls")

        if wino > 0:
            break

        elif empate is True:
            break

    os.system("cls")
    logo()
    print("")
    quadro()
    print("")
    if winx > 0:
        print("--------------------------")
        print("\033[34mPlayer 1 \033[32mganhou a partida\033[m")
        print("--------------------------")
    elif wino > 0:
        print("--------------------------")
        print("\033[31mPlayer 2 \033[32mganhou a partida\033[m")
        print("--------------------------")
    elif empate is True:
        print("--------------------------")
        print("\033[33mEmpate/Velha\033[m")
        print("--------------------------")
    input("Dê enter para finalizar")
    jogardenovo = 0
    os.system('cls')

    while True:
        print("Você quer jogar novamente? (\033[32ms\033[m/\033[31mn\033[m)")
        jogardenovo = input("").upper()
        if jogardenovo == "N":
            break
        if jogardenovo == "S":
            break
        else:
            print("Escreva S (sim) ou N (não)!")
            input("Dê enter para tentar novamente")
            os.system("cls")
    if jogardenovo == "N":
        break

