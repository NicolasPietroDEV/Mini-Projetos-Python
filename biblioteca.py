def valuekey(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            correct_key = key
            break
    return correct_key


def listmean(list):
    return sum(list) / len(list)


def loading(tamanho, aumento_por_passo, duracao_do_passo):
    import time
    import os
    lista = []
    while len(lista) < tamanho:
        lista += ' '
    listasum = ''
    pct = 0
    for x in lista:
        lista[lista.index(x)] = '█'
        listasum = ''
        for x in lista:
            listasum += x
        pct += aumento_por_passo
        print(f"\n[{listasum}]{pct}%")
        time.sleep(duracao_do_passo)
        os.system('cls')


def autoloading(tamanho, duracao_do_passo):
    import time
    import os
    lista = []
    while len(lista) < tamanho:
        lista += ' '
    listasum = ''
    pct = 0
    for x in lista:
        lista[lista.index(x)] = '█'
        listasum = ''
        for x in lista:
            listasum += x
        pct += 100/tamanho
        print(f"\n[{listasum}]{round(pct)}%")
        time.sleep(duracao_do_passo)
        os.system('cls')


def bask(a, b, c):
    Δ = b**2-(4*a*c)
    if Δ >= 0:
        raizpos = (-b + Δ**0.5)/(2*a)
        raizneg = (-b - Δ**0.5)/(2*a)
        return (raizpos, raizneg)
    else:
        return None


def scramble(texto, caixaaleatoria):
    import random
    palavraEmb = ''
    textolista = []
    for x in texto:
        textolista.append(x)
    for x in texto:
        letra = random.choice(textolista)
        textolista.remove(letra)
        if caixaaleatoria == True:
            caixa = random.choice(['alta', 'baixa'])
            if caixa == 'alta':
                letra = letra.upper()
            else:
                letra = letra.lower()
        palavraEmb += letra
    return palavraEmb


def scramblelist(palavra, caixaaleatoria, imprimir_ou_escrever):
    #############################
    lista = []
    if caixaaleatoria == True:
        fatorial = 2
        tamanho = len(palavra) * 2
        cont = tamanho - 2
    elif caixaaleatoria == False:
        fatorial = 1
        tamanho = len(palavra)
        cont = tamanho - 1
    if len(palavra) != 1:
        for x in range(1, len(palavra)+1):
            tamanho *= cont
            cont -= fatorial
            if cont <= 1:
                break
    #############################
    palavrac = palavra
    for x in palavrac:
        letra = x
        quant = palavrac.count(x)
        if palavrac.count(x) > 1:
            cont = quant
            for x in range(1, quant+1):
                cont -= 1
                if cont == 0:
                    break
                quant *= cont
            tamanho /= quant
            palavrac = palavrac.replace(letra, "")
    #############################
    while len(lista) < tamanho:
        rodada = scramble(palavra, caixaaleatoria)
        if rodada not in lista:
            lista.append(rodada)
            print(len(lista), "/", tamanho)
        else:
            continue
    if imprimir_ou_escrever == 'w':
        with open('Word List.txt', 'w') as arquivo:
            for comb in lista:
                arquivo.write(comb + '\n')
    elif imprimir_ou_escrever == 'p':
        print(lista)


def weekday(dia, mes, ano):
    if mes == 1:
        mes = 13
        ano -= 1
    elif mes == 2:
        mes = 14
        ano -= 1
    k = dia + 2*mes + (3*(mes+1))/5 + ano + ano/4 - ano/100 + ano/400 + 2
    diadasemana = k % 7
    dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça',
            4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
    return dias[int(diadasemana)]
