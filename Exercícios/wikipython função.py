ex = int(input("Exercício: "))
###########################################################
if ex == 1:
    def escadinha(valor):
        for x in range(1, (valor+1)):
            escada = ''
            for y in range(1, (x+1)):
                escada += str(y)
                escada += ' '
            print(escada)

    escadinha(20)
###########################################################
if ex == 3:
    def soma(a, b, c):
        return a + b + c

    a = float(input("Primeiro Valor: "))
    b = float(input("Segundo Valor: "))
    c = float(input("Terceiro Valor: "))
    print(soma(a, b, c))
###########################################################
if ex == 4:
    def posorneg(valor):
        if valor > 0:
            return "P"
        else:
            return "N"
    print(posorneg(0))
###########################################################
if ex == 5:
    def somaImposto(taxaImposto, custo):
        return custo + ((taxaImposto / 100) * custo)

    print(somaImposto(10, 100))
###########################################################
