def manipulaListas(lista, comando, localização, valor):
    if comando == 'remover' and localização == 'fim':
        elementoremov = lista.pop(len(lista) - 1)
        return elementoremov

    if comando == 'remover' and localização == 'inicio':
        elementoremov = lista.pop(0)
        return elementoremov

    if comando == 'adicionar' and localização == 'inicio':
        lista.insert(0, valor)
        return(lista)

    if comando == 'adicionar' and localização == 'fim':
        lista.insert(len(lista), valor)
        return(lista)


lista = ['1', '2', '3', '4', '5']
comando = input('remover ou adicionar?: ')
localização = input('inicio ou fim?: ')
if comando == 'adicionar':
    valor = input('digite o valor: ')
else:
    valor = None
print(manipulaListas(lista, comando, localização, valor))
