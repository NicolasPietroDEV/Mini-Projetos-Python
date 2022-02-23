import os
import colorama
colorama.init("")
#\033[m
plch = 0
while plch < 5:
    print("A produção está em \033[31mhoras\033[m ou \033[34mminutos\033[m?")
    print("\033[31m(1)Horas\033[m \033[34m(2)Minutos\033[m")
    horasoumin = int(input(""))
    os.system('cls')
    if horasoumin == 1:
        print("Escolha uma \033[1;32mcapacidade\033[m")
        print("\033[32m(1)Capacidade Instalada (2)Capacidade Disponível")
        print("(3)Capacidade Efetiva   (4)Capacidade Real\033[m")
        escolha = int(input(""))
        os.system('cls')
        if escolha == 1:
            quant = int(input("Escreva a \033[4mquantidade p/ hora\033[m: "))
            print("")
            os.system('cls')
            tempo = 24
            cd = quant * tempo
            print("--------------------------------")
            print(f"A Capacidade Instalada é de \033[4;33m{cd}\033[m")
            print("--------------------------------")
        elif escolha == 2:
            quant = int(input("Escreva a \033[4mquantidade p/ hora\033[m: "))
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            print("")
            minhora = (mins / 60) + hora
            ci = quant * minhora
            print("--------------------------------")
            print(f"A Capacidade Disponível é de \033[4;33m{ci}\033[m")
            print("--------------------------------")
        elif escolha == 3:
            quant = int(input("Escreva a \033[4mquantidade p/ hora\033[m: "))
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            os.system('cls')
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos \033[4mparadas programadas\033[m você tem? "))
            os.system('cls')
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as \033[4mhoras\033[m da parada: "))
                paradasmin = paradasmin + int(input("Escreva os \033[4mminutos\033[m da parada: "))
                os.system('cls')
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                ce = quant * (minhora - paradasminhora)
            print("--------------------------------")
            print(f"A capacidade efetiva é \033[4;33m{ce}\033[m")
            print("--------------------------------")
        elif escolha == 4:
            quant = int(input("Escreva a \033[4mquantidade p/ hora\033[m: "))
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            os.system('cls')
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos \033[4mparadas\033[m você tem? "))
            os.system('cls')
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as \033[4mhoras\033[m da parada: "))
                paradasmin = paradasmin + int(input("Escreva os \033[4mminutos\033[m da parada: "))
                os.system('cls')
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                cr = quant * (minhora - paradasminhora)
            print("--------------------------------")
            print(f"A capacidade real é \033[4;33m{cr}\033[m")
            print("--------------------------------")
        else:
            print("\033[4;31mEscreva um dos números citados!!\033[m")
            print("")

    if horasoumin == 2:
        print("Escolha uma \033[1;32mcapacidade\033[m")
        print("\033[32m(1)Capacidade Instalada (2)Capacidade Disponível")
        print("(3)Capacidade Efetiva   (4)Capacidade Real\033[m")
        escolha = int(input(""))
        os.system('cls')
        if escolha == 1:
            quant = int(input("Escreva a quantidade p/ minuto: ")) * 60
            os.system('cls')
            print("")
            tempo = 24
            cd = quant * tempo
            print("--------------------------------")
            print(f"A Capacidade Instalada é de \033[4;33m{cd}\033[m")
            print("--------------------------------")
        elif escolha == 2:
            quant = int(input("Escreva a \033[4mquantidade p/ minuto\033[m: ")) * 60
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            os.system('cls')
            print("")
            minhora = (mins / 60) + hora
            ci = quant * minhora
            print("--------------------------------")
            print(f"A Capacidade Disponível é de \033[4;33m{ci}\033[m")
            print("--------------------------------")
        elif escolha == 3:
            quant = int(input("Escreva a \033[4mquantidade p/ minuto\033[m: ")) * 60
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            os.system('cls')
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos \033[4mparadas programadas\033[m você tem? "))
            os.system('cls')
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as \033[4mhoras\033[m da parada: "))
                paradasmin = paradasmin + int(input("Escreva os \033[4mminutos\033[m da parada: "))
                os.system('cls')
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                ce = quant * (minhora - paradasminhora)
            print("--------------------------------")
            print(f"A capacidade efetiva é \033[4;33m{ce}\033[m")
            print("--------------------------------")
        elif escolha == 4:
            quant = int(input("Escreva a \033[4mquantidade p/ minuto\033[m: ")) * 60
            os.system('cls')
            print("")
            hora = int(input("Escreva as \033[4mHoras\033[m: "))
            mins = int(input("Escreva os \033[4mMinutos\033[m: "))
            os.system('cls')
            print("")
            minhora = (mins / 60) + hora
            paradas = 0
            paradashora = 0
            paradasmin = 0
            paradasqtd = int(input("Quantos \033[4mparadas\033[m você tem? "))
            os.system('cls')
            print("")
            while paradas < paradasqtd:
                paradas += 1
                paradashora = paradashora + int(input("Escreva as \033[4mhoras\033[m da parada: "))
                paradasmin = paradasmin + int(input("Escreva os \033[4mminutos\033[m da parada: "))
                os.system('cls')
                print("")
                paradasminhora = (paradasmin / 60) + paradashora
                cr = quant * (minhora - paradasminhora)
            print("--------------------------------")
            print(f"A capacidade real é \033[4;33m{cr}\033[m")
            print("--------------------------------")
        else:
            print("\033[4;31mEscreva um dos números citados!!\033[m")
            print("")

    print("Você quer calcular novamente? (\033[4;31ms\033[m/\033[4;32mn\033[m)")
    denovo = input("")
    if denovo == "n":
        break
    os.system('cls')