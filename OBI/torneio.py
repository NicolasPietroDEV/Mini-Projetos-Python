lista = []
venceu = 0
for x in range(0, 6):
    jogo = input()
    lista.append(jogo)

for x in lista:
    if x == "V":
        venceu += 1

if venceu == 0:
    print(-1)
elif venceu == 1 or venceu == 2:
    print(3)
elif venceu == 3 or venceu == 4:
    print(2)
elif venceu == 5 or venceu == 6:
    print(1)

