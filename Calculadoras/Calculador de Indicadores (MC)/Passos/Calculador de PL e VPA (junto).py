while True:
        print("Você possui o LPA? ")
        print("(1) Sim (2) Não")
        lpahave = int(input(""))
        print("")
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
        patliq = float(input("Qual é o Patrimônio Líquido? "))
        vpa = patliq / cs
        plredondo = round(pl)
        print("")
        print(f"O P/L é de aproximadamente {plredondo} anos")
        print(f"O VPA é {vpa}")
        preçobarato = pda < vpa
        if preçobarato is True:
            print("O preço da ação está barato")
        else:
            print("O preço da ação está caro")
        print("")
        print("______________")
        print("")
#feito por Marcus Katsurayama e Nicolas Pietro
