import random
numerodito = 0
tentativas = 0

final = int(input("Qual vai ser o limite do número? (de 1 até quanto?) "))

numero = random.randint(1, final)

tentativasquant = int(input("Quantas tentativas você quer ter? "))
while tentativas != tentativasquant:
	numerodito = int(input("Chute o número: "))
	tentativas += 1
	if numerodito > numero:
		print("Escolha um número menor")
	elif numerodito < numero:
		print("Escolha um número maior")
	if numero == numerodito:
		break
if numerodito == numero:
	print(f"Você acertou! O número é {numero} ")
elif numerodito != numero:
	print(f"Você perdeu! O número era {numero}")