blank = " "
p1 = "x"
p2 = "o"
c1 = blank
c2 = blank
c3 = blank
c4 = blank
c5 = blank
c6 = blank
c7 = blank
c8 = blank
c9 = blank
winx = 0
wino = 0
while winx == 0 and wino == 0:
    c1 = input("Escreva um número: ")
    c2 = input("Escreva um número: ")
    c3 = input("Escreva um número: ")
    c4 = input("Escreva um número: ")
    c5 = input("Escreva um número: ")
    c6 = input("Escreva um número: ")
    c7 = input("Escreva um número: ")
    c8 = input("Escreva um número: ")
    c9 = input("Escreva um número: ")
    print(f" {c1} | {c2} | {c3}")
    print(f"-----------")
    print(f" {c4} | {c5} | {c6}")
    print(f"-----------")
    print(f" {c7} | {c8} | {c9}")

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

    if vitxria1xv == True:
        winx += 1
    if vitxria2xv == True:
        winx += 1
    if vitxria3xv == True:
        winx += 1
    if vitxria4xv == True:
        winx += 1
    if vitxria5xv == True:
        winx += 1
    if vitxria6xv == True:
        winx += 1
    if vitxria7xv == True:
        winx += 1
    if vitxria8xv == True:
        winx += 1



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

    if vitoria1ov == True:
        wino += 1
    if vitoria2ov == True:
        wino += 1
    if vitoria3ov == True:
        wino += 1
    if vitoria4ov == True:
        wino += 1
    if vitoria5ov == True:
        wino += 1
    if vitoria6ov == True:
        wino += 1
    if vitoria7ov == True:
        wino += 1
    if vitoria8ov == True:
        wino += 1

    empate = [winx < 1, wino < 1]
    empatev = all(empate)

if winx > 0:
    print("Player 1 ganhou a partida")
if wino > 0:
    print("Player 2 ganhou a partida")
if empatev is True:
    print("Empate")
