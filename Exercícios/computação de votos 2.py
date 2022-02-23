jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maior = 0
while True:
    voto = int(input('Número do jogador (0=fim): '))
    if voto == 0:
        break
    if voto not in range(1, 24):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        continue
    voto -= 1
    jogadores[voto] += 1

total = sum(jogadores)

print('Resultado da votação:')
print(f'Foram computados {total} votos')

maiora = max(jogadores)
indicea = (jogadores.index(maiora))
porcentagema = (maiora/total)*100

print('Jogador | Votos | %')
while True:
    maior = max(jogadores)
    if maior == 0:
        break
    indice = (jogadores.index(maior))
    porcentagem = (maior/total)*100
    print(f'{indice + 1}        {maior}        {porcentagem:.2f}')
    jogadores[indice] = 0

print(f'O melhor jogador foi o número {indicea+1}, com {maiora} votos, correspondendo a {porcentagema:.2f}% do total de votos')