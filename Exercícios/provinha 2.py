def contaMultiplasLetras(palavra):
    listaUsados = []
    dicFinal = {}
    for x in palavra:
        listaUsados.append(x)
        dicFinal[x] = palavra.count(x)
    return dicFinal


print(contaMultiplasLetras(input('Digite uma palavra: ')))
