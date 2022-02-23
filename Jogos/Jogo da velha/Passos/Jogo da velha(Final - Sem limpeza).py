blank = " "
p1 = "X"
p2 = "O"
winx = 0
wino = 0
c1 = blank
c2 = blank
c3 = blank
c4 = blank
c5 = blank
c6 = blank
c7 = blank
c8 = blank
c9 = blank
RED = "\033[1;31m"
WHITE = "\033[0;0m"
while True:
    print("      _                                 _            __     __         _   _             ")
    print("     | |   ___     __ _    ___       __| |   __ _    \ \   / /   ___  | | | |__     __ _ ")
    print("  _  | |  / _ \   / _` |  / _ \     / _` |  / _` |    \ \ / /   / _ \ | | | '_ \   / _` |")
    print(" | |_| | | (_) | | (_| | | (_) |   | (_| | | (_| |     \ V /   |  __/ | | | | | | | (_| |")
    print("  \___/   \___/   \__, |  \___/     \__,_|  \__,_|      \_/     \___| |_| |_| |_|  \__,_|")
    print("                  |___/                                                                  ")
    print("")
    print(f" {c1} | {c2} | {c3}")
    print(f"-----------")
    print(f" {c4} | {c5} | {c6}")
    print(f"-----------")
    print(f" {c7} | {c8} | {c9}")
    print("")
    while True:
        escolhido = 0
        while escolhido != 1:
            escolhax = int(input("Player 1: "))
            if escolhax == 1:
                if c1 != blank:
                    print("Esta casa já foi escolhida")
                if c1 == blank:
                    c1 = p1
                    escolhido += 1
            if escolhax == 2:
                if c2 != blank:
                    print("Esta casa já foi escolhida")
                if c2 == blank:
                    c2 = p1
                    escolhido += 1
            if escolhax == 3:
                if c3 != blank:
                    print("Esta casa já foi escolhida")
                if c3 == blank:
                    c3 = p1
                    escolhido += 1
            if escolhax == 4:
                if c4 != blank:
                    print("Esta casa já foi escolhida")
                if c4 == blank:
                    c4 = p1
                    escolhido += 1
            if escolhax == 5:
                if c5 != blank:
                    print("Esta casa já foi escolhida")
                if c5 == blank:
                    c5 = p1
                    escolhido += 1
            if escolhax == 6:
                if c6 != blank:
                    print("Esta casa já foi escolhida")
                if c6 == blank:
                    c6 = p1
                    escolhido += 1
            if escolhax == 7:
                if c7 != blank:
                    print("Esta casa já foi escolhida")
                if c7 == blank:
                    c7 = p1
                    escolhido += 1
            if escolhax == 8:
                if c8 != blank:
                    print("Esta casa já foi escolhida")
                if c8 == blank:
                    c8 = p1
                    escolhido += 1
            if escolhax == 9:
                if c9 != blank:
                    print("Esta casa já foi escolhida")
                if c9 == blank:
                    c9 = p1
                    escolhido += 1

        escolhido = 0

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

        print("")
        print(f" {c1} | {c2} | {c3}")
        print(f"-----------")
        print(f" {c4} | {c5} | {c6}")
        print(f"-----------")
        print(f" {c7} | {c8} | {c9}")
        print("")

        if winx > 0:
            break
        if empate is True:
            break

        while escolhido != 1:
            escolhao = int(input("Player 2: "))
            if escolhao == 1:
                if c1 != blank:
                    print("Esta casa já foi escolhida")
                if c1 == blank:
                    c1 = p2
                    escolhido += 1
            if escolhao == 2:
                if c2 != blank:
                    print("Esta casa já foi escolhida")
                if c2 == blank:
                    c2 = p2
                    escolhido += 1
            if escolhao == 3:
                if c3 != blank:
                    print("Esta casa já foi escolhida")
                if c3 == blank:
                    c3 = p2
                    escolhido += 1
            if escolhao == 4:
                if c4 != blank:
                    print("Esta casa já foi escolhida")
                if c4 == blank:
                    c4 = p2
                    escolhido += 1
            if escolhao == 5:
                if c5 != blank:
                    print("Esta casa já foi escolhida")
                if c5 == blank:
                    c5 = p2
                    escolhido += 1
            if escolhao == 6:
                if c6 != blank:
                    print("Esta casa já foi escolhida")
                if c6 == blank:
                    c6 = p2
                    escolhido += 1
            if escolhao == 7:
                if c7 != blank:
                    print("Esta casa já foi escolhida")
                if c7 == blank:
                    c7 = p2
                    escolhido += 1
            if escolhao == 8:
                if c8 != blank:
                    print("Esta casa já foi escolhida")
                if c8 == blank:
                    c8 = p2
                    escolhido += 1
            if escolhao == 9:
                if c9 != blank:
                    print("Esta casa já foi escolhida")
                if c9 == blank:
                    c9 = p2
                    escolhido += 1

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

        print("")
        print(f" {c1} | {c2} | {c3}")
        print(f"-----------")
        print(f" {c4} | {c5} | {c6}")
        print(f"-----------")
        print(f" {c7} | {c8} | {c9}")
        print("")

        if wino > 0:
            break

        elif empate is True:
            break

    if winx > 0:
        print("")
        print("Player 1 ganhou a partida")
    elif wino > 0:
        print("")
        print("Player 2 ganhou a partida")
    elif empate is True:
        print("")
        print("Empate/Velha")
    print("")
    print("__________________________________")
    print("")