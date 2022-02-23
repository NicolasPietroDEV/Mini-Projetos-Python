import random
import os
erros = 0
letrasErradas = []
palavras = ["E S P A D A", "M A C H A D O", "F A M A",
            "O U R O", "R I Q U E Z A", "P O D E R", "P I R O C A", "P A U", "R O L A", "P I N T O", "S A P A T E N I S", "C A D E I R A", "P U T A"]
palavra = random.choice(palavras)
palavraLista = palavra.split()
tamanho = len(palavraLista)
under = tamanho * "_ "
underlineLista = under.split()
print("------Jogo da Velha-----")
print(f"Erros: {erros}, Letras erradas: {letrasErradas}")
print(underlineLista)
while erros < 6:
    escolha = input("Escreva uma letra: ").upper()
    if escolha in palavraLista:
        while escolha in palavraLista:
            local = palavraLista.index(escolha)
            underlineLista[local] = escolha
            palavraLista[local] = "_"
        if len(set(palavraLista)) == 1:
            break
        os.system('cls')
        print("------Jogo da Velha-----")
        print(f"Erros: {erros}, Letras erradas: {letrasErradas}")
        print(underlineLista)
    else:
        letrasErradas.append(escolha)
        erros += 1
        os.system('cls')
        print("------Jogo da Velha-----")
        print(f"Erros: {erros}, Letras erradas: {letrasErradas}")
        print(underlineLista)
os.system('cls')
if erros < 6:
    print("Você acertou!")
    print(f"Palavra: {underlineLista}")
    print(f"Erros: {erros}, Letras erradas: {letrasErradas}")
else:
    print("Você perdeu!")
input("Pressione Enter para terminar")
