jojo = 0
while jojo < 5:
    print("Escolha uma capacidade")
    print("(1)Capacidade Instalada (2)Capacidade Disponível (3)Capacidade Efetiva (4)Capacidade Real")
    escolha = int(input(""))
    if escolha == 1:
        quant = int(input("Escreva a quantidade p/ hora: "))
        tempo = 24
        cd = quant * tempo
        print(f"A Capacidade Instalada é de {cd}")
        print("_______________________")
    if escolha == 2:
        quant = int(input("Escreva a quantidade p/ hora: "))
        hora = int(input("Escreva as Horas: "))
        mins = int(input("Escreva os Minutos: "))
        minhora = (mins / 60) + hora
        ci = quant * minhora
        print(f"A Capacidade Disponível é de {ci}")
        print("_______________________")
    if escolha == 3:
        quant = int(input("Escreva a quantidade p/ hora: "))
        hora = int(input("Escreva as horas: "))
        mins = int(input("Escreva os minutos: "))

        #daqui
        print("Some todas as paradas programadas")
        falproghora = int(input("Escreva as horas do resultado: "))
        falprogmin = int(input("Escreva os minutos do resultado: "))
        #até aqui

        falprogtot = (falprogmin/60)+falproghora
        minhora = (mins / 60) + hora
        ce = quant * (minhora-falprogtot)
        print(f"A capacidade efetiva é {ce}")
        print("_______________________")
    if escolha == 4:
        quant = int(input("Escreva a quantidade p/ hora: "))
        hora = int(input("Escreva as horas: "))
        mins = int(input("Escreva os minutos: "))

        #daqui
        print("Some todas as paradas (programadas ou não)")
        falproghora = int(input("Escreva as horas do resultado: "))
        falprogmin = int(input("Escreva os minutos do resultado: "))
        #até aqui

        falprogtot = (falprogmin / 60) + falproghora
        minhora = (mins / 60) + hora
        ce = quant * (minhora - falprogtot)
        print(f"A capacidade efetiva é {ce}")
        print("_______________________")
    else:
        print("Escreva um dos números citados")
