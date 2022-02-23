from tkinter import *

# Janela
janela = Tk()

# configurações da janela:
# Nome da Janela
janela.title("Tela de Login")
# Tamanho da Janela
janela.geometry("340x160")
# Cor do fundo
janela.configure(background="#4842f5")

# Textos na tela e seus respectivos lugares
txt1 = Label(janela, text="Nome do usuário")
txt1.place(x=10, y=10, width=150, height=30)
txt2 = Label(janela, text="Senha")
txt2.place(x=10, y=50, width=150, height=30)

# Caixas de texto e suas respectivas posições
nomecaixa = Entry(janela)
nomecaixa.place(x=170, y=10, width=150, height=30)
senhacaixa = Entry(janela)
senhacaixa.place(x=170, y=50, width=150, height=30)

# função que mostra os dados inseridos


# Botão e seu lugar
enviardados = Button(janela, text="Enviar dados", command=print("Daora fera"))
enviardados.place(x=100, y=90, width=120, height=20)

janela.mainloop()
