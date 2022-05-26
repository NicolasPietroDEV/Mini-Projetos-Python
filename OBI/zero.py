quant = int(input())
lista = []
for x in range(0, quant):
    numero = int(input())
    if numero == 0:
        lista.pop()
    else:
        lista.append(numero)

print(sum(lista))
