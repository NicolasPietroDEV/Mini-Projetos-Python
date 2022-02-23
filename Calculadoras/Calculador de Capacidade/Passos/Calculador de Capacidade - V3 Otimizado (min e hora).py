plch = 0
while plch < 5:
    print("A produção está em horas ou minutos?")
    print("(1)Horas (2)Minutos")
    horasoumin = int(input(""))
    if horasoumin == 1:
        print("Escolha uma capacidade")
        print("(1)Capacidade Instalada (2)Capacidade Disponível")
        print("(3)Capacidade Efetiva   (4)Capacidade Real")
        escolha = int(input(""))
        if escolha == 1:
            quant = int(input("Escreva a quantidade p/ hora: "))
            print("")
            tempo = 24
            cd = quant * tempo
            print(f"A Capacidade Instalada é de {cd}")
            print("_______________________")
        elif escolha == 2:
            quant = int(input("Escreva a quantidade p/ hora: "))
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            ci = quant * minhora
            print(f"A Capacidade Disponível é de {ci}")
            print("_______________________")
        elif escolha == 3:
            quant = int(input("Escreva a quantidade p/ hora: "))
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos paradas programadas você tem? "))
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as horas da parada: "))
                paradasmin = paradasmin + int(input("Escreva os minutos da parada: "))
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                ce = quant * (minhora - paradasminhora)
            print(f"A capacidade efetiva é {ce}")
            print("")
        elif escolha == 4:
            quant = int(input("Escreva a quantidade p/ hora: "))
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos paradas você tem? "))
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as horas da parada: "))
                paradasmin = paradasmin + int(input("Escreva os minutos da parada: "))
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                cr = quant * (minhora - paradasminhora)
            print(f"A capacidade real é {cr}")
            print("")
        else:
            print("Escreva um dos números citados")
            print("")

    if horasoumin == 2:
        print("Escolha uma capacidade")
        print("(1)Capacidade Instalada (2)Capacidade Disponível")
        print("(3)Capacidade Efetiva   (4)Capacidade Real")
        escolha = int(input(""))
        if escolha == 1:
            quant = int(input("Escreva a quantidade p/ minuto: ")) * 60
            print("")
            tempo = 24
            cd = quant * tempo
            print(f"A Capacidade Instalada é de {cd}")
            print("_______________________")
        elif escolha == 2:
            quant = int(input("Escreva a quantidade p/ minuto: ")) * 60
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            ci = quant * minhora
            print(f"A Capacidade Disponível é de {ci}")
            print("_______________________")
        elif escolha == 3:
            quant = int(input("Escreva a quantidade p/ minuto: ")) * 60
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos paradas programadas você tem? "))
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as horas da parada: "))
                paradasmin = paradasmin + int(input("Escreva os minutos da parada: "))
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                ce = quant * (minhora - paradasminhora)
            print(f"A capacidade efetiva é {ce}")
            print("")
        elif escolha == 4:
            quant = int(input("Escreva a quantidade p/ minuto: ")) * 60
            print("")
            hora = int(input("Escreva as Horas: "))
            mins = int(input("Escreva os Minutos: "))
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos paradas você tem? "))
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as horas da parada: "))
                paradasmin = paradasmin + int(input("Escreva os minutos da parada: "))
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                cr = quant * (minhora - paradasminhora)
            print(f"A capacidade real é {cr}")
            print("")
        else:
            print("Escreva um dos números citados")
            print("")
