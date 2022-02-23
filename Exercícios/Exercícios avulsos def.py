'''
def retquad(largura, comprimento):
    if largura == comprimento:
        print('As dimensões inseridas indicam que a figura é um quadrado')
    else: 
        print('As dimensões inseridas indicam que a figura é um retângulo')
    print(f'A área é {largura * comprimento} cm²')

largura = float(input('Digite a largura (em cm): '))
comprimento = float(input('Digite o comprimento (em cm): '))

print()
retquad(largura, comprimento)
'''
tupla = (8, 2, 3, -1, 7)


def mult(tupla):
    produto = 1
    for x in tupla:
        produto *= x
    return produto


print(f'A multiplicação dos itens é {mult(tupla)}')
