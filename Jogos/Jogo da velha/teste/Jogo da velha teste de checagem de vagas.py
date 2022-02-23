blank = " "
c9 = blank
escolhido = 0
while escolhido != 1:
    escolha = int(input("pla1: "))
    if escolha == 1:
        if c9 != blank:
          print("Esta casa já foi escolhida")
        if c9 == blank:
          c9 = "x"
          escolhido += 1
        print(c9)
escolhido = 0
while escolhido != 1:
    escolha2 = int(input("play2: "))
    if escolha2 == 1:
        if c9 != blank:
            print("Esta casa já foi escolhida")
        if c9 == blank:
            c9 = "o"
            escolhido += 1
        print(c9)
