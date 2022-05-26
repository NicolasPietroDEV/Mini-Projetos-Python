lista = []
for x in range(0, 4):
    lista.append(int(input()))
lista.sort()
print(abs((lista[0]+lista[3])-(lista[1]+lista[2])))