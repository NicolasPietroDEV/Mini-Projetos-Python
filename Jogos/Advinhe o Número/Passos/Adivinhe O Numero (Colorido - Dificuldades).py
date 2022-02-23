import random
import os
import colorama
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
	print("Escolha a dificuldade")
	print("\033[32m(1)Fácil\033[33m (2)Médio\033[31m (3)Difícil\033[m")
	dificuldade = int(input(""))
	if dificuldade == 1:
		tentativas = 15
		numero = random.randint(1, 40)
		def modoinf():
			facil()
	if dificuldade == 2:
		tentativas = 10
		numero = random.randint(1, 80)
		def modoinf():
			medio()
	if dificuldade == 3:
		tentativas = 5
		numero = random.randint(1, 100)
		def modoinf():
			dificil()
	os.system('cls')
	numerodito = 0

	while tentativas != 0:
		modoinf()
		print("")
		numerodito = int(input("Chute o número: "))
		print("")
		tentativas -= 1
		if numerodito > numero:
			print("Escolha um número \033[31mmenor\033[m")
		elif numerodito < numero:
			print("Escolha um número \033[32mmaior\033[m")
		if numero == numerodito:
			break
		print("")
		input("Pressione Enter para tentar novamente: ")
		os.system('cls')
	os.system('cls')
	if numerodito == numero:
		print(f"\033[32mVocê acertou!\033[m O número é \033[32m{numero}\033[m ")
	elif numerodito != numero:
		print(f"\033[31mVocê perdeu!\033[m O número era \033[31m{numero}\033[m")
	print("----------------------------------------------------------")
	print("Você quer jogar denovo? (\033[32ms\033[m/\033[31mn\033[m)")
	denovo = input("")
	if denovo == "n":
		break
	os.system('cls')