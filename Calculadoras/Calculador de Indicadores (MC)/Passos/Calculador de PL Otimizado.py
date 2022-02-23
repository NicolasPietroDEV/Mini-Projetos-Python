jojo: int = 0
while jojo<5:
        print("Você possui o LPA? ")
        print("(1) Sim (2) Não")
        lpahave = int(input(""))
        if lpahave == 1:
            lpa = float(input("Qual o LPA? "))
        if lpahave == 2:
            ll = float(input("Qual o Lucro líquido? "))
        print("")
        cs = float(input("Qual o Capital Social? "))
        lpa = ll/cs
        print("")
        pda = float(input("Qual o preço da ação? "))
        pl = pda/lpa
        print("")
        print(f"O P/L é {pl}")
        print("______________")

#feito por Marcus Katsurayama e Nicolas Pietro
