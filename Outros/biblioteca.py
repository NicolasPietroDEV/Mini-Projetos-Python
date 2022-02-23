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
