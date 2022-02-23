import random
numero = random.randint(1, 100)
numerodito = 0
tentativas = 0

while numerodito != numero:
	numerodito = int(input("Chute o número: "))
	tentativas += 1
	if numerodito > numero:
		print("Escolha um número menor")
	elif numerodito < numero:
		print("Escolha um número maior")
	
if numerodito == numero:
	print(f"Você acertou! O número é {numero} ")
elif numerodito != numero:
	print(f"Você perdeu! O número era {numero}")