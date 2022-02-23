import statistics
import os
while True:
    escritas = 0
    lista = []
    quantidade = int(input("Quantos números tem na sua lista? "))
    os.system('cls')
    while escritas < quantidade:
      numero = float(input("Escreva um número e pressione enter: "))
      os.system('cls')
      lista.append(numero)
      escritas += 1
    media = statistics.mean(lista)
    moda = statistics.multimode(lista)
    tamanhomoda = len(moda)
    tamanholista = len(lista)
    mediana = statistics.median(lista)
    print(f"A média é {media}")
    if tamanhomoda == 1:
        print(f"A moda é {moda}")
    elif tamanhomoda == tamanholista:
        print("O conjunto é amodal")
    else:
        print(f"As modas são: {moda}")
    print(f"A mediana é {mediana}")
    print("-------------------------------")
    denovo = input("Quer calcular outra vez? (s/n)")
    os.system('cls')
    if denovo == "n":
      break





