from tkinter import *

player = 'X'


def preencher(casa):
    global tabela
    tabela = ([a1['text'], a2['text'], a3['text']],
              [b1['text'], b2['text'], b3['text']],
              [c1['text'], c2['text'], c3['text']])
    global player
    global label_atual
    if player == 'X':
        player = 'O'
        label_atual = 'Vez do Player 2 (X)'
    elif player == 'O':
        player = 'X'
        label_atual = 'Vez do Player 1 (O)'
    casa['text'] = player
    vez['text'] = label_atual
    casa['state'] = 'disabled'
    tabela = ([a1['text'], a2['text'], a3['text']],
              [b1['text'], b2['text'], b3['text']],
              [c1['text'], c2['text'], c3['text']])
    ganhador()


def ganhador():
    for x in range(3):
        soma = tabela[x][0] + tabela[x][1] + tabela[x][2]
        if soma == 'XXX':
            vez['text'] = '(X) Player 2 ganhou!!'
            vez['fg'] = 'blue'
            disableall()
        elif soma == 'OOO':
            vez['text'] = '(O) Player 1 ganhou!!'
            vez['fg'] = 'red'
            disableall()
    for x in range(3):
        soma = tabela[0][x] + tabela[1][x] + tabela[2][x]
        if soma == 'XXX':
            vez['text'] = '(X) Player 2 ganhou!!'
            vez['fg'] = 'blue'
            disableall()
        elif soma == 'OOO':
            vez['text'] = '(O) Player 1 ganhou!!'
            vez['fg'] = 'red'
            disableall()
    diagonal1 = tabela[0][0]+tabela[1][1]+tabela[2][2]
    diagonal2 = tabela[0][2]+tabela[1][1]+tabela[2][0]
    if diagonal1 == 'XXX' or diagonal2 == 'XXX':
        vez['text'] = '(X) Player 2 ganhou!!'
        vez['fg'] = 'blue'
        disableall()
    if diagonal1 == 'OOO' or diagonal2 == 'OOO':
        vez['text'] = '(O) Player 2 ganhou!!'
        vez['fg'] = 'red'
        disableall()


janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('340x155')

a1 = Button(janela, text='', command=lambda: preencher(a1))
a1.place(x=20, y=3, width=40, height=40)
a2 = Button(janela, text='', command=lambda: preencher(a2))
a2.place(x=77, y=3, width=40, height=40)
a3 = Button(janela, text='', command=lambda: preencher(a3))
a3.place(x=135, y=3, width=40, height=40)

b1 = Button(janela, text='', command=lambda: preencher(b1))
b1.place(x=20, y=53, width=40, height=40)
b2 = Button(janela, text='', command=lambda: preencher(b2))
b2.place(x=77, y=53, width=40, height=40)
b3 = Button(janela, text='', command=lambda: preencher(b3))
b3.place(x=135, y=53, width=40, height=40)

c1 = Button(janela, text='', command=lambda: preencher(c1))
c1.place(x=20, y=103, width=40, height=40)
c2 = Button(janela, text='', command=lambda: preencher(c2))
c2.place(x=77, y=103, width=40, height=40)
c3 = Button(janela, text='', command=lambda: preencher(c3))
c3.place(x=135, y=103, width=40, height=40)


def disableall():
    lista = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    for x in lista:
        x['state'] = 'disabled'


vez = Label(janela, text='Início. Vez do Player 1 (O)')
vez.place(x=195, y=53)

janela.mainloop()
