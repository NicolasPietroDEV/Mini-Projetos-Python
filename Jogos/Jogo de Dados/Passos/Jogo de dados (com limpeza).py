import random
import os
blank = " "
enter = "\n"
rodadas = 0
def quadro():
    print(f"| {c1} | {c2} | {c3} | {c4} | {c5} |")
    print("---------------------")
    print(f"| {c6} | {c7} | {c8} | {c9} | {c10} |")
def logo():
    print("     _                                 _            ____                _               ")
    print("    | |   ___     __ _    ___       __| |   ___    |  _ \    __ _    __| |   ___    ___ ")
    print(" _  | |  / _ \   / _` |  / _ \     / _` |  / _ \   | | | |  / _` |  / _` |  / _ \  / __|")
    print("| |_| | | (_) | | (_| | | (_) |   | (_| | |  __/   | |_| | | (_| | | (_| | | (_) | \__ \ ")
    print(" \___/   \___/   \__, |  \___/     \__,_|  \___|   |____/   \__,_|  \__,_|  \___/  |___/")
    print("                 |___/                                                                  ")
    print("")
while True:
    os.system("cls")
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c10 = 0
    while True:
        logo()
        quadro()
        print("")
        print(f"Rodadas: {rodadas}")
        quadrofinal = [c1 == blank, c2 == blank, c3 == blank, c4 == blank, c5 == blank, c6 == blank, c7 == blank,
                       c8 == blank, c9 == blank, c10 == blank]
        final = all(quadrofinal)
        if final:
            break
        input("Dê enter para rolar: ")
        print("")
        if c1 != blank:
            c1 = random.randint(0,6)
        if c2 != blank:
            c2 = random.randint(0,6)
        if c3 != blank:
            c3 = random.randint(0,6)
        if c4 != blank:
            c4 = random.randint(0,6)
        if c5 != blank:
            c5 = random.randint(0,6)
        if c6 != blank:
            c6 = random.randint(0,6)
        if c7 != blank:
            c7 = random.randint(0,6)
        if c8 != blank:
            c8 = random.randint(0,6)
        if c9 != blank:
            c9 = random.randint(0,6)
        if c10 != blank:
            c10 = random.randint(0,6)

        if c1 == 6:
            c1 = blank
        if c2 == 6:
            c2 = blank
        if c3 == 6:
            c3 = blank
        if c4 == 6:
            c4 = blank
        if c5 == 6:
            c5 = blank
        if c6 == 6:
            c6 = blank
        if c7 == 6:
            c7 = blank
        if c8 == 6:
            c8 = blank
        if c9 == 6:
            c9 = blank
        if c10 == 6:
            c10 = blank

        rodadas += 1

        os.system("cls")
    print("")
    print("---------------------------------------------------")
    print(f"Final: {rodadas} rodadas")
    print("---------------------------------------------------")
    print("Você quer recomeçar? (s/n)")
    jogardenovo = input("")
    if jogardenovo == "n":
        break
    rodadas = 0
    print("")
