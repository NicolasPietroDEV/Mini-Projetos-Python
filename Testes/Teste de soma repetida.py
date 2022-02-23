inserido = 0
print("Escreva um número para começar a soma")
while True:
    inserido = inserido + int(input(""))
    print("Quer escrever mais um número?")
    print("(1)Sim (2)Não")
    denovo = int(input(""))
    if denovo == 1:
        print("Escreva mais um número")
    if denovo == 2:
        print(inserido)
