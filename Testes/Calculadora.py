while True:
    print("Escolha a operação:")
    print("(1)Soma          (2)Subtração")
    print("(3)Multiplicação (4)Divisão")
    escolha = int(input(""))
    if escolha == 1:
        numerosescritos = 0
        inserido = 0
        numerosqtd = int(input("Quantos números você quer somar? "))
        print("Escreva o(s) número(s)")
        while numerosescritos < numerosqtd:
            numerosescritos += 1
            inserido = inserido + float(input(""))
        print(f"O resultado é {inserido}")
        print("______________________")
    if escolha == 2:
            numerosescritos = 0
            inicialnumero = float(input("Qual é o número inicial? "))
            numerosqtd = int(input("Quantos números você quer subtrair dele? "))
            menossoma = 0
            print("Escreva o(s) número(s)")
            while numerosescritos < numerosqtd:
                numerosescritos += 1
                menossoma += float(input(""))
                subt = inicialnumero - menossoma
            print(f"O resultado é {subt}")
            print("______________________")
    if escolha == 3:
            numerosescritos = 0
            inicialnumero = float(input("Escreva o número inicial: "))
            numerosqtd = int(input("Por quantos números você quer multiplicar ele? "))
            print("Escreva o(s) número(s)")
            while numerosescritos < numerosqtd:
                numerosescritos += 1
                inicialnumero *= float(input(""))
            print(f"O resultado é {inicialnumero}")
            print("______________________")
    if escolha == 4:
            numerosescritos = 0
            inicialnumero = float(input("Escreva o número inicial: "))
            numerosqtd = int(input("Por quantos números você quer dividir ele? "))
            print("Escreva o(s) número(s)")
            while numerosescritos < numerosqtd:
                numerosescritos += 1
                inicialnumero /= float(input(""))
            print(f"O resultado é {inicialnumero}")
            print("______________________")