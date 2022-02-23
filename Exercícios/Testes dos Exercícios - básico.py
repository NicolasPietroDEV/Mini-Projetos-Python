print("Bem vindo ao exercício 1! Conceitos básicos")
print("")
print("Escolha um exercício")
print("(1)Dizer uma frase legal  (2)Dizer um número")
print("(3)Somar 2 números        (4)Média de Notas")
print("(5)Converter metros em centímetros")
escolha = int(input(""))

if escolha == 1:
 print("Alô Mundo")

if escolha == 2:
 numero = int(input("Escreva um número: "))
 print(f"O número informado foi {numero}")

if escolha == 3:
 n1 = int(input("Escreva um número pra somar: "))
 n2 = int(input("Escreva outro número para somar: "))
 soma = n1 + n2
 print(f"A soma desses números é {soma}")

if escolha == 4:
 nota1 = float(input("Escreva a primeira nota: "))
 nota2 = float(input("Escreva a segunda nota: "))
 nota3 = float(input("Escreva a terceira nota: "))
 nota4 = float(input("Escreva a quarta nota: "))
 media = (nota1 + nota2 + nota3 + nota4) / 4
 print(f"A sua média é {media}")

if escolha == 5:
 metro = float(input("Escreva uma quantidade de metros: "))
 cent = metro * 100
 print(f"A conversão resulta em {cent} centímetros: ")
