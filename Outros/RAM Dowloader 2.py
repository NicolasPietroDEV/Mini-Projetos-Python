import time
import os
while True:
    print("Bem vindo ao RAM Dowloader!")
    print("Qual tipo de RAM você quer instalar?")
    print("(1)4 GB (2)8 GB (3)16 GB (4)32 GB")
    ram = int(input(""))
    os.system('cls')
    if ram not in range(1, 5):
        print("Escolha umas das RAM disponíveis (Pressione Enter)")
        input("")
        os.system('cls')
        continue
    print("Você tem certeza? (S/N)")
    certeza = input("").upper()
    os.system('cls')
    if certeza == "S":
        lista = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        frases = ["Acessando servidor...", "Procurando dados...", "Organizando dados...", "Organizando dados...",
                  "Iniciando Dowload...", "Baixando...", "Baixando...", "Instalando RAM...", "Finalizando instalação...", "Concluido!"]
        fraseatual = 0
        listasum = ''
        pct = 0
        for x in lista:
            lista[lista.index(x)] = '█'
            listasum = ''
            for x in lista:
                listasum += x
            pct += 10
            print(frases[fraseatual])
            print(f"\n[{listasum}]{pct}%")
            fraseatual += 1
            time.sleep(2)
            os.system('cls')
        os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        os.system('start https://www.youtube.com/watch?v=9t5vnSQ3NS4')
        os.system('start https://www.youtube.com/watch?v=YCrR6UqIn6Q')
        break
    if certeza == "N":
        continue
    else:
        print("Escolha uma das opções (Pressione Enter)")
        input("")
        os.system('cls')
