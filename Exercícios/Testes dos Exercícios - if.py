import os
print("Bem vindo ao exercício 2! Condições no Python")
while True:
    print("Escolha um exercício")
    print("(1) Maior e Menor  (2) Gênero")
    print("(3) Alfabeto       (4) Média escolar")
    escolha = int(input(""))
    os.system('cls')

    if escolha == 1:

        n1 = float(input("Escreva o primeiro número: "))
        n2 = float(input("Escreva o segundo número: "))
        n3 = float(input("Escreva o terceiro número: "))
        if n1 > n2 and n1 > n3:
            maior = n1
        elif n2 > n1 and n2 > n3:
            maior = n2
        elif n3 > n1 and n3 > n2:
            maior = n3

        if n1 < n2 and n1 < n3:
            menor = n1
        elif n2 < n1 and n2 < n3:
            menor = n2
        elif n3 < n1 and n3 < n2:
            menor = n3

        print(f"O maior número entre eles é {maior}")
        print(f"O menor número entre eles é {menor}")


    if escolha == 2:

        feminino = "F"
        masculino = "M"
        gender = input("Escreva seu gênero (F/M): ").upper()
        if gender == feminino:
            print("Feminino")
        elif gender == masculino:
            print("Masculino")
        else:
            print("Sexo Inválido")

    if escolha == 3:

        letra = input("Escreva uma letra: ").upper()
        if letra in "AEIOU":
            print("Sua letra é vogal")
        elif letra in "BCDFGJKLMNPQRSTVWXZ":
            print("Sua letra é consoante")
        else:
            print("Caractere inválido (não está no alfabeto)")

    if escolha == 4:

        nota1 = float(input("Escreva a primeira nota: "))
        nota2 = float(input("Escreva a segunda nota: "))
        media = (nota1 + nota2) / 2
        if media == 10:
            print("Aprovado com Distinção")
        elif media > 10:
            print("Sua média está acima dos limites da escola, verifique os valores inseridos")
        elif media >= 7:
            print("Aprovado")
        elif media < 7:
            print("Reprovado")

    print("--------------------------------------")
    denovo = input("Você quer ver outro exercício? (s/n)")
    os.system('cls')
    if denovo == "n":
        break
