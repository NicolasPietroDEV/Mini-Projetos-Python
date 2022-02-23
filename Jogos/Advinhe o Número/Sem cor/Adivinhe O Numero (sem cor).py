import random
import os
def facil():
	print("------------------------------")
	print("Número de 1 à 40")
	print(f"{tentativas} tentativas restantes")
	print("------------------------------")
def medio():
	print("------------------------------")
	print("Número de 1 à 80")
	print(f"{tentativas} tentativas restantes")
	print("------------------------------")
def dificil():
	print("------------------------------")
	print("Número de 1 à 100")
	print(f"{tentativas} tentativas restantes")
	print("------------------------------")
while True:
	print("Escolha a dificuldade")
	print("(1)Fácil (2)Médio (3)Difícil")
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
			print("Escolha um número menor")
		elif numerodito < numero:
			print("Escolha um número maior")
		if numero == numerodito:
			break
		print("")
		input("Pressione Enter para tentar novamente: ")
		os.system('cls')
	os.system('cls')
	if numerodito == numero:
		print(f"Você acertou! O número é {numero} ")
	elif numerodito != numero:
		print(f"Você perdeu! O número era {numero}")
	print("----------------------------------------------------------")
	print("Você quer jogar denovo? (s/n)")
	denovo = input("")
	if denovo == "n":
		break
	os.system('cls')