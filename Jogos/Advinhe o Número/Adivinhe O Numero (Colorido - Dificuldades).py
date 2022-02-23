import random
import os
import colorama
escolhido = 0
colorama.init()
def facil():
	print("\033[32mModo fácil\033[m")
	print("------------------------------")
	print("Número de \033[31m1\033[m à \033[31m40\033[m")
	print(f"\033[32m{tentativas}\033[m tentativas restantes")
	print("------------------------------")
def medio():
	print("\033[33mModo médio\033[m")
	print("------------------------------")
	print("Número de \033[31m1\033[m à \033[31m80\033[m")
	print(f"\033[32m{tentativas}\033[m tentativas restantes")
	print("------------------------------")
def dificil():
	print("\033[31mModo difícil\033[m")
	print("------------------------------")
	print("Número de \033[31m1\033[m à \033[31m100\033[m")
	print(f"\033[32m{tentativas}\033[m tentativas restantes")
	print("------------------------------")
while True:
	os.system('cls')
	while True:
		print("Escolha a dificuldade")
		print("\033[32m(1)Fácil\033[33m (2)Médio\033[31m (3)Difícil\033[m")
		dificuldade = input("")
		if dificuldade == "1":
			tentativas = 15
			espaço = range(1, 40)
			numero = random.randint(1, 40)
			def modoinf():
				facil()
			escolhido == 1
			break
		if dificuldade == "2":
			tentativas = 10
			espaço = range(1, 80)
			numero = random.randint(1, 80)
			def modoinf():
				medio()
			escolhido == 1
			break
		if dificuldade == "3":
			tentativas = 5
			espaço = range(1, 100)
			numero = random.randint(1, 100)
			def modoinf():
				dificil()
			escolhido == 1
			break
		else:
			print("Escolha uma das dificuldades!!")
			input("")
		os.system('cls')

		numerodito = 0
	os.system('cls')
	while tentativas != 0:
		os.system('cls')
		modoinf()
		print("")
		numerodito = input("Chute o número: ")
		print("")
		if not numerodito.isdigit():
			print("Insira um número!! (Pressione Enter para tentar novamente)")
			input("")
			continue

		numeronum = int(numerodito)

		if numeronum not in espaço:
			print("O número não está no espaço definido")

		elif numeronum > numero:
			print("Escolha um número \033[31mmenor\033[m")
			tentativas -= 1
		elif numeronum < numero:
			print("Escolha um número \033[32mmaior\033[m")
			tentativas -= 1
		if numero == numeronum:
			break
		print("")
		input("Pressione Enter para tentar novamente: ")
		os.system('cls')
	os.system('cls')
	if numeronum == numero:
		print(f"\033[32mVocê acertou!\033[m O número é \033[32m{numero}\033[m ")
	elif numeronum != numero:
		print(f"\033[31mVocê perdeu!\033[m O número era \033[31m{numero}\033[m")
	print("----------------------------------------------------------")
	while True:
		print("Você quer jogar novamente? (\033[32ms\033[m/\033[31mn\033[m)")
		jogardenovo = input("").upper()
		if jogardenovo == "N":
			break
		if jogardenovo == "S":
			break
		else:
			print("Escreva S (sim) ou N (não)!")
			input("Dê enter para tentar novamente")
			os.system("cls")
	if jogardenovo == "N":
		break