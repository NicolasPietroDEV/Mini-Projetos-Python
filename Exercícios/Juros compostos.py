def juros_comp(valor, taxa, tempo):
    taxa_perc = taxa / 100
    calculo = valor * (1 + taxa_perc)**tempo
    return calculo


valor = float(input("Digite o valor inicial: "))
taxa = float(input("Digite a taxa: "))
tempo = float(input("Digite o tempo: "))
divida = juros_comp(valor, taxa, tempo)
print(f"O juros composto é de {'{:.2f}'.format(divida)}")
