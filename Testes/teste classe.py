class bunda:
    def __init__(self, limpeza, tamanho, cor):
        self.limpeza = limpeza
        self.tamanho = tamanho
        self.cor = cor


bunda_do_nicolas = bunda('sujo', 'grande', 'preto')
bunda_do_erick = bunda('sujo', 'pequeno', 'preto')
bunda_do_gustavo = bunda('sujo', 'pequeno', 'branco')

print(bunda_do_gustavo.limpeza)
