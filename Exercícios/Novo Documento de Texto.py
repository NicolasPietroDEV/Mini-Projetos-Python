'''
contador1 = 0
lista1 = []
while contador1 < 5:
    lista1.append(int(input("Escreva um número: ")))
    contador1 += 1
for x in lista1:
    print(x)
'''''''''''''''''''''''''''''''''''''
contador2 = 0
lista2 = []
while contador2 < 10:
    lista2.append(int(float("Escreva um número: ")))
    contador2 += 1
print(lista2[::-1])
''''''''''''''''''''''''''''''''''''''
contador3 = 0
lista3 = []
while contador3 < 4:
    lista3.append(float(input("Escreva um número: ")))
    contador3 += 1
print(f'A média é {sum(lista3)/4}')
''''''''''''''''''''''''''''''''''''''''''
contador4 = 0
lista4 = []
listacons = []
while contador4 < 10:
    lista4.append(input("Escreva um caractere: ").upper())
    contador4 += 1
for x in lista4:
    if x not in "AEIOU":
        listacons.append(x)
print(listacons)
''''''''''''''''''''''''''''''''''''''''''
contador10 = 0
lista101 = []
lista102 = []
lista103 = []

while contador10 < 10:
    lista101.append(input("1 - Escreva um número: "))
    contador10 += 1
contador10 = 0
print(lista101)

while contador10 < 10:
    lista102.append(input("2 - Escreva um número: "))
    contador10 += 1
contador10 = 0
print(lista102)

while contador10 < 10:
    lista103.append(lista101[contador10])
    lista103.append(lista102[contador10])
    contador10 += 1
print(f'A lista intercalada é: {lista103}')
'''''''''''''''''''''''''''''''''''''''''''''

