import os
jojo: int = 0
while jojo<5:
    print("Qual você quer Calcular?")
    print("(1)P/L (2)VPA (3)P/VP (4)DIV/A")
    escolha = int(input(""))
    os.system('cls')
    if escolha == 1:
        print("Você possui o LPA? ")
        print("(1) Sim (2) Não")
        lpahave = int(input(""))
        os.system('cls')
        if lpahave == 1:
            lpa = float(input("Qual o LPA? "))
            os.system('cls')
        if lpahave == 2:
            ll = float(input("Qual o Lucro líquido? "))
            os.system('cls')
        cs = float(input("Qual o Capital Social? "))
        os.system('cls')
        pda = float(input("Qual o preço da ação? "))
        os.system('cls')
        if lpahave == 2:
            lpa = ll / cs
        pl = pda/lpa
        tdr = 1 / (pl) * 100
        print("")
        print(f"O P/L é {pl}")
        print(f"A Taxa de Retorno é de {tdr}% ao ano")
        print("______________")

    elif escolha == 2:
        cs = float(input("Qual é o Capital Social? "))
        os.system('cls')
        patliq = float(input("Qual é o Patrimônio Líquido? "))
        os.system('cls')
        vpa = patliq/cs
        print("")
        print(f"O VPA é {vpa}")
        print("______________")

    elif escolha == 3:
        print("Você tem o VPA?")
        print("(1)Sim (2)Não")
        vpahave = int(input(""))
        os.system('cls')
        if vpahave == 1:
            vpa = float(input("Qual o VPA? "))
            os.system('cls')
        if vpahave == 2:
            cs = float(input("Qual é o Capital Social? "))
            os.system('cls')
            patliq = float(input("Qual é o Patrimônio Líquido? "))
            os.system('cls')
            vpa = patliq / cs
        pda = float(input("Qual o preço da ação? "))
        os.system('cls')
        pvp = pda / vpa
        print("")
        print(f"O PV/P é {pvp}")
        print("______________")

    elif escolha == 4:
        ll = float(input("Qual o Lucro Líquido? "))
        os.system('cls')
        cs = float(input("Qual o Capital Social? "))
        os.system('cls')
        lucropercent = float(input("Qual o percentual do lucro distribuido? "))
        os.system('cls')
        diva = (ll / cs) * (lucropercent / 100)
        print("")
        print(f"O DIV/A é {diva}")
        print("______________")
    print("Você quer calcular novamente? (s/n)")
    denovo = input("")
    if denovo == "n":
        break
    os.system('cls')

#feito por Marcus Katsurayama e Nicolas Pietro
