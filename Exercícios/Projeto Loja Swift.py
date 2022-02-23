import os
"""
Projeto: Loja Swift
Turma: 9°C
Nome dos integrantes:
Mariana Martins Silva - N°20
Matheus Gomes De Souza - N°21
Nicolas Pietro Leal de Souza - N°22
"""
while True:
    print("Bem vindo ao sistema swift!")
    print("Digite o produto da sua escolha a partir do codigo e a quantidade em quilos")
    print("")
    print("+----------------------------------------+")
    print("|               Loja Swift               |")
    print("+----------------------------------------+")
    print("|            Tabela de Preço             |")
    print("+--------+----------------+--------------+")
    print("| Código |Descrição       | Preço por kg |")
    print("+--------+----------------+--------------+")
    print("|   1    |Picanha         |   R$ 45.00   |")
    print("+--------+----------------+--------------+")
    print("|   2    |Salmão Selvagem |   R$ 70.00   |")
    print("+--------+----------------+--------------+")
    print("|   3    |Alcatra         |   R$ 35.00   |")
    print("+--------+----------------+--------------+")
    print("|   4    |Maminha         |   R$ 40.00   |")
    print("+--------+----------------+--------------+")
    picanha = 45
    salmao = 70
    alcatra = 35
    maminha = 40
    quantidade = 0
    somaanterior = 0
    acabou = False
    listapossibilidades = ["1", "2", "3", "4", "0"]
    print("+-------------------------------------------------------------------")
    print("|                          Nota de compra                           |")
    print("+-------------------------------------------------------------------+")
    print("| Código | Produto                      |Preço (R$)| Total (R$)     |")
    print("+-------------------------------------------------------------------+")
    while True:
        codigo = input("Informe o código do produto: ")
        if codigo not in listapossibilidades:
            print("Digite um código válido! (Pressione enter para tentar novamente)")
            input("")
            continue
        kgstr = input("Informe a quantidade em kg: ").upper()
        if not kgstr.isdigit():
            print("Digite numero válido de quilos! (Pressione enter para tentar novamente)")
            input("")
            continue
        kg = float(kgstr)
        if codigo == "0" and kg == 0:
            acabou = True
        elif codigo == "1":
            codproduto1 = 1
            produto1 = "Picanha"
            preco1 = kg * picanha
            somaanterior += preco1
        elif codigo == "2":
            codproduto1 = 2
            produto1 = "Salmão"
            preco1 = kg * salmao
            somaanterior += preco1
        elif codigo == "3":
            codproduto1 = 3
            produto1 = "Alcatra"
            preco1 = kg * alcatra
            somaanterior += preco1
        elif codigo == "4":
            codproduto1 = 4
            produto1 = "Maminha"
            preco1 = kg * maminha
            somaanterior += preco1
        if acabou == True:
            break
        print("+-------------------------------------------------------------------+")
        print(f"|   {codproduto1}    | {produto1}                      |   R$ {preco1}|    R$ {somaanterior}     |")
        print("+-------------------------------------------------------------------+")
    print("+-------------------------------------------------------------------+")
    print(f"O total da compra foi: R$ {somaanterior}")
    print("")
    while True:
        print("Você quer começar novamente? (S/N)")
        jogardenovo = input("").upper()
        if jogardenovo == "N":
            break
        if jogardenovo == "S":
            os.system('cls')
            break
        else:
            print("Escreva S (sim) ou N (não)!")
            input("Dê enter para tentar novamente")
