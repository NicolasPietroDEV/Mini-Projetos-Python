listadeclientes = []
class cliente:
        def __init__(self, nome, rg, cpf):
            self.nome = nome
            self.rg = rg
            self.cpf = cpf
while True:
    escolha = input("O que deseja? \n (1)Adicionar Cleinte (2)Consultar cliente")

    if escolha == "1":
        print("Insira os  dados abaixo")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        atualcliente = cliente(nome, rg, cpf)
        listadeclientes.append(atualcliente)
        print(listadeclientes)


