exer = input('Escolha um exercício de 1 a 4: ')

if exer == 1:
    listaNumero = [3, 5, 19, 7, 2, 11, 8, 10]
    soma = 0
    contador = 0
    while True:
        if listaNumero[contador] % 2 != 0:
            soma += listaNumero[contador]
        else:
            break
        contador += 1
    print(f'A soma é {soma}')
#################################################
if exer == 2:
    lista_numero = [1, 6, 3, 5, 3, 4]
    numero = int(input('Escreva um número: '))
    if numero in lista_numero:
        print("O número está na lista")
    else:
        print("O número não está na lista")
####################################################
if exer == 3:
    dicionario1 = {'Dez': 10, 'Vinte': 20, 'Trinta': 30}
    dicionario2 = {'Trinta': 30, 'Quarenta': 40, 'Cinquenta': 50}
    dicionario1.update(dicionario2)
    print(dicionario1)
#################################################
if exer == 4:
    lista = []
    for x in range(1, 11):
        elemento = float(input('Digite um número: '))
        lista.append(elemento)
    lista.sort()
    print(f'O maior valor é {lista[9]} e o segundo maior é {lista[8]}')
#################################################
if exer == 5:
    lista = [11, -21, 0, 45, 66, -93]
    for x in lista:
        if x > 0:
            print(x)


