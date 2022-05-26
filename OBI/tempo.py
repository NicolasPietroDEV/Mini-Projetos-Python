totalregs = int(input())
amigosespera = {}
amigosfinal = {}
anterior = 0

for i in range(0, totalregs):
    registro = input()
    registroSplit = registro.split()
    if registroSplit[0] ==  "R":
        if anterior == False:
            for x in amigosespera:
                amigosespera[x] += 1
        amigosespera[registroSplit[1]] = 0
        anterior = False
    elif registroSplit[0] ==  "T":
        for x in amigosespera:
            amigosespera[x] += int(registroSplit[1])
        anterior = "T"
    elif registroSplit[0] == "E":
        if anterior != "T":
            for x in amigosespera:
                amigosespera[x] += 1
        retiradaValue = amigosespera[registroSplit[1]]
        amigosespera.pop(registroSplit[1])
        if registroSplit[1] in amigosfinal.keys():
            amigosfinal[registroSplit[1]] += retiradaValue
        else:
            amigosfinal[registroSplit[1]] = retiradaValue
        anterior = False

for x in amigosespera:
    amigosfinal[x] = -1

for x in sorted(amigosfinal):
    print(x, amigosfinal[x])

