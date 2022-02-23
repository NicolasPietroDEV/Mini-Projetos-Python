def retangulo(linha, coluna):
    if linha in range(1, 21) and coluna in range(1, 21):
        print('+', '-'*(coluna-2), '+')
        for x in range(1, linha+1):
            print('|', ' '*(coluna-2), '|')
        print('+', '-'*(coluna-2), '+')
    else:
        print('Os valores que você digitou não estão entre 1 e 20')


retangulo((int(input('Escreva o número de linhas: '))),
          (int(input('Escreva o número de colunas: '))))
