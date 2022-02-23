import time
import os
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
lista = ["1", "2", "3", "4"]
porcentagem = 0
def loading():
    print(f"[{a}{b}{c}{d}{e}{f}{g}{h}{i}]{porcentagem}%")

while True:
        print("Bem vindo ao RAM Dowloader!")
        print("Qual tipo de RAM você quer instalar?")
        print("(1)4 GB (2)8 GB (3)16 GB (4)32 GB")
        ram = input("")
        os.system('cls')
        if ram not in lista:
            print("Escolha umas das RAM disponíveis (Pressione Enter)")
            input("")
            os.system('cls')
            continue
        print("Você tem certeza? (S/N)")
        certeza = input("").upper()
        os.system('cls')
        if certeza == "S":
            print("Iniciando...")
            loading()
            time.sleep(5)
            os.system('cls')
            a = "█"
            porcentagem = 10
            print("Acessando servidor...")
            loading()
            time.sleep(5)
            os.system('cls')
            b = "█"
            porcentagem = 20
            print("Procurando dados...")
            loading()
            time.sleep(5)
            os.system('cls')
            c = "█"
            porcentagem = 30
            print("Organizando dados...")
            loading()
            time.sleep(5)
            os.system('cls')
            d = "█"
            porcentagem = 40
            print("Organizando dados...")
            loading()
            time.sleep(5)
            os.system('cls')
            e = "█"
            porcentagem = 50
            print("Iniciando Dowload...")
            loading()
            time.sleep(5)
            os.system('cls')
            f = "█"
            porcentagem = 60
            print("Baixando...")
            loading()
            time.sleep(5)
            os.system('cls')
            g = "█"
            porcentagem = 70
            print("Baixando...")
            loading()
            time.sleep(5)
            os.system('cls')
            h = "█"
            porcentagem = 80
            print("Instalando RAM...")
            loading()
            time.sleep(5)
            os.system('cls')
            i = "█"
            porcentagem = 99
            print("Finalizando instalação...")
            loading()
            time.sleep(5)
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




