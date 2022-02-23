
'''
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
contador = 0
potencia = 1
while contador != expoente:
    contador += 1
    potencia *= base
print(f"{base} elevado à {expoente} é igual à {potencia}")

n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))
n3 = int(input("Insira um número: "))
n4 = int(input("Insira um número: "))
n5 = int(input("Insira um número: "))
n6 = int(input("Insira um número: "))
n7 = int(input("Insira um número: "))                                          
n8 = int(input("Insira um número: "))
n9 = int(input("Insira um número: "))
n10 = int(input("Insira um número: "))
'''

ano = 2007
salario = 1000
percentual = 0.015
while ano <= 2021:
    print(f"Em {ano}: R$ {salario:.2f}")
    salario += salario * percentual
    ano += 1
    percentual *= 2
