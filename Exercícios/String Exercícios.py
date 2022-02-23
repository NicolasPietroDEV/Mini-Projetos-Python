
print("Exercícios de String")
exe = int(input("Selecione o exercício (1 a 14): "))

if exe == 1:
    string1 = input("Escreva uma String: ")
    string2 = input("Escreva outra String: ")
    string1len = len(string1)
    string2len = len(string2)
    print(f"String 1: {string1}")
    print(f"String 2: {string2}")
    print(f"Tamanho de {string1}: {string1len}")
    print(f"Tamanho de {string2}: {string2len}")
    if string1len == string2len:
        print("As strings são do mesmo tamanho")
    else:
        print("As strings tem tamanhos diferentes")
    if string1 == string2:
        print("As strings são iguais")
    else:
        print("As strings são diferentes")

if exe == 2:
    nome = input("Escreva seu nome: ").upper()
    print(nome[::-1])

if exe == 3:
    nomelinhas = input("Escreva seu nome: ")
    nomelinhasn = len(nomelinhas)
    contadorlinhas = 0
    while contadorlinhas < nomelinhasn:
        print(nomelinhas[contadorlinhas])
        contadorlinhas += 1

if exe == 4:
    nomeescada = input("Escreva seu nome: ")
    nomeescadan = len(nomeescada)
    contadorescada = 0
    while contadorescada < nomeescadan:
        contadorescada += 1
        print(nomeescada[:contadorescada])
    
if exe == 5:
    nomeescada = input("Escreva seu nome: ")
    nomeescadan = len(nomeescada)
    while nomeescadan > 0:
        print(nomeescada[:nomeescadan])    
        nomeescadan -= 1
    
if exe == 6:
    datadeniver = input("Escreva sua data de nascimento em dd/mm/aaaa: ")
    dianiver = int(datadeniver[0:2])
    mesniver = int(datadeniver[3:5])
    anoniver = int(datadeniver[6:])
    if mesniver == 1:
        print(f"Você nasceu em {dianiver} de Janeiro de {anoniver}")
    if mesniver == 2:
        print(f"Você nasceu em {dianiver} de Fevereiro de {anoniver}")
    if mesniver == 3:
        print(f"Você nasceu em {dianiver} de Março de {anoniver}")
    if mesniver == 4:
        print(f"Você nasceu em {dianiver} de Abril de {anoniver}")
    if mesniver == 5:
        print(f"Você nasceu em {dianiver} de Maio de {anoniver}")
    if mesniver == 6:
        print(f"Você nasceu em {dianiver} de Junho de {anoniver}")
    if mesniver == 7:
        print(f"Você nasceu em {dianiver} de Julho de {anoniver}")
    if mesniver == 8:
        print(f"Você nasceu em {dianiver} de Agosto de {anoniver}")
    if mesniver == 9:
        print(f"Você nasceu em {dianiver} de Setembro de {anoniver}")
    if mesniver == 10:
        print(f"Você nasceu em {dianiver} de Outubro de {anoniver}")
    if mesniver == 11:
        print(f"Você nasceu em {dianiver} de Novembro de {anoniver}")
    if mesniver == 12:
        print(f"Você nasceu em {dianiver} de Dezembro de {anoniver}")
    
if exe == 7:
    frase = input("Escreva uma frase: ").lower()
    fraseespaço = frase.count(" ")
    frasevogal = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
    print(f"Vogais: {frasevogal}")
    print(f"Espaços: {fraseespaço}")

if exe == 8:
    palindromo = input("Escreva uma palavra: ").upper()
    palindromoinv = palindromo[::-1]
    if palindromo == palindromoinv:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

if exe == 9:
    cpf = input("Digite seu CPF (xxx.xxx.xxx-xx): ")
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        print("CPF válido")
    else:
        print("CPF inválido")

if exe == 10:
    numero = input("Escreva um número: ")
    numeronumero = int(numero)
    if len(numero) == 1:
        if numero[0] == "0":
            numeroext = "Zero"
        if numero[0] == "1":
            numeroext = "Um"
        if numero[0] == "2":
            numeroext = "Dois"
        if numero[0] == "3":
            numeroext = "Três"
        if numero[0] == "4":
            numeroext = "Quatro"
        if numero[0] == "5":
            numeroext = "Cinco"
        if numero[0] == "6":
            numeroext = "Seis"
        if numero[0] == "7":
            numeroext = "Sete"
        if numero[0] == "8":
            numeroext = "Oito"
        if numero[0] == "9":
            numeroext = "Nove"

        print(numeroext)

    elif len(numero) == 2:
        if numero == "10":
            numeroext = "Dez"
        elif numero == "11":
            numeroext = "Onze"
        elif numero == "12":
            numeroext = "Doze"
        elif numero == "13":
            numeroext = "Treze"
        elif numero == "14":
            numeroext = "Catorze"
        elif numero == "15":
            numeroext = "Quinze"
        elif numero == "16":
            numeroext = "Desesseis"
        elif numero == "17":
            numeroext = "Desessete"
        elif numero == "18":
            numeroext = "Dezoito"
        elif numero == "19":
            numeroext = "Dezenove"

        if numero[0] == "2":
            numero1 = "Vinte"
        elif numero[0] == "3":
            numero1 = "Trinta"
        elif numero[0] == "4":
            numero1 = "Quarenta"
        elif numero[0] == "5":
            numero1 = "Cinquenta"
        elif numero[0] == "6":
            numero1 = "Sessenta"
        elif numero[0] == "7":
            numero1 = "Setenta"
        elif numero[0] == "8":
            numero1 = "Oitenta"
        elif numero[0] == "9":
            numero1 = "Noventa"

        if numero[1] == "0":
            numero2 = ""
        if numero[1] == "1":
            numero2 = "Um"
        if numero[1] == "2":
            numero2 = "Dois"
        if numero[1] == "3":
            numero2 = "Três"
        if numero[1] == "4":
            numero2 = "Quatro"
        if numero[1] == "5":
            numero2 = "Cinco"
        if numero[1] == "6":
            numero2 = "Seis"
        if numero[1] == "7":
            numero2 = "Sete"
        if numero[1] == "8":
            numero2 = "Oito"
        if numero[1] == "9":
            numero2 = "Nove"

        if numeronumero in range(10, 20):
            print(numeroext)
        elif numero[0] != "0" and numero[1] != "0":
            print(f"{numero1} e {numero2}")
        elif numero[1] == "0":
            print(numero1)
        elif numero[0] == "0":
            print(numero2)

if exe == 11:
    import random
    import os
    erros = 0
    letrasErradas = []
    palavras = ["E S P A D A", "M A C H A D O", "F A M A", "O U R O", "R I Q U E Z A", "P O D E R"]
    palavra = random.choice(palavras)
    palavraLista = palavra.split()
    palavraPalavra = ""
    print(palavraPalavra)
    tamanho = len(palavraLista)
    under = tamanho * "_ "
    underlineLista = under.split()
    print("------Jogo da Velha-----")
    for i in underlineLista:
        palavraPalavra += i
        palavraPalavra += " "
    print(f"A palavra é: {palavraPalavra}")
    palavraPalavra = ""
    while erros < 6:
        print("")
        escolha = input("Digite uma letra: ").upper()
        if escolha in palavraLista:
            while escolha in palavraLista:
                local = palavraLista.index(escolha)
                underlineLista[local] = escolha
                palavraLista[local] = "_"
            if len(set(palavraLista)) == 1:
                break
            for i in underlineLista:
                palavraPalavra += i
                palavraPalavra += " "
            print(f"A palavra é: {palavraPalavra}")
            palavraPalavra = ""
        else:
            letrasErradas.append(escolha)
            erros += 1
            print(f"-> Você errou pela {erros}° vez. Tente de novo!")
    if erros < 6:
        print("")
        print("Você acertou!")
        print(f"Palavra: {palavra}")
    else:
        print("")
        print("Você perdeu!")
    input("Pressione Enter para terminar")
                
        
        

