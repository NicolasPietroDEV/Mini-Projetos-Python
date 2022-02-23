dicionario = {"Lilian": 826, "Lais": 830, "Marcus": 750,
              "Joao Pedro": 2740, "Guilherme": 1500, "Sophia": 800}
def chaveporvalor(value):
    for key in dicionario:
        if dicionario[key] == value:
            nome = key
            break
    return key
###################Media####################
print(f"Média:{sum(dicionario.values())/len(dicionario)}")
###################Melhor vendedor####################
mais = max(dicionario.values())
nome = chaveporvalor(mais)
print(f"Melhor vendedor: {nome}, Quantidade Vendida: {mais}")
###################Pior Vendedor####################
menos = min(dicionario.values())
nome = chaveporvalor(menos)
print(f"Pior vendedor: {nome}, Quantidade Vendida: {menos}")
###################Tirando o Pior Vendedor####################
dicionariotemp = dicionario.copy()
del dicionario[nome]
print(f"\nExceto o menor: {sum(dicionario.values())/len(dicionario)}")
##################Adicionando a Odete#####################
dicionario = dicionariotemp.copy()
dicionario["Odete"] = 1300
print(f"\nCom a Odete: {sum(dicionario.values())/len(dicionario)}")
