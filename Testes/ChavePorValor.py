dicionario = {"Lilian": 826, "Lais": 830, "Marcus": 750,
              "Joao Pedro": 2740, "Guilherme": 1500, "Sophia": 800}
valorinformado = int(input())


def chavedovalor(valorinformado):
    for key in dicionario:
        if dicionario[key] == valorinformado:
            print(key)
            break


chavedovalor(valorinformado)
print(lusca)
