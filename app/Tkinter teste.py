from tkinter import *

# cria a janela
janela = Tk()
# define o nome da janela
janela.title("Tela de Login")
# define o tamanho da janela, XxY e a posição da tela onde irá aparecer x+y
janela.geometry("500x250+400+200")
# define se poderá redimensionar a altura e a largura
janela.resizable(True, True)
# define o mínimo para redimensionar (x e y)
janela.minsize(500, 250)
# define o máximo para redimensionar (x e y)
janela.maxsize(700, 500)
# define o icone
janela.iconbitmap(r"app/icon.ico")
# define a cor da janela
janela['bg'] = 'lightgray'

# cria um botão, defina primeiro a quem ele pertence e depois o texto
# além disso, colocar em command a função a ser executada


def dadosenviados():
    print("Dados enviados!")
    # fecha a janela
    janela.destroy()


botao_enviar = Button(janela, text="Enviar Dados", command=dadosenviados)

# cria um texto/label, mesmos parametros que o button
email = Label(janela, text="Email")
senha = Label(janela, text="Senha")

# pack, inserir o que eu fiz no programa
email.pack()
senha.pack()
botao_enviar.pack()

# cria o looping da aplicação, colocado entre o código e a janela
janela.mainloop()
