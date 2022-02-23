jojo = 0
while jojo<5:
 print("Você possui o LPA?")
 print("(1) Sim (2) Não")
 lpahave = int(input(""))
 if lpahave == 1:
  print("Qual o LPA?")
  lpa = float(input(""))
  print("Qual o preço da ação?")
  pda1 = float(input(""))
  pl1 = pda1/lpa
  print(f"O P/L é {pl1}")
  print("______________")
 if lpahave == 2:
  print("Qual o Lucro líquido?")
  ll = float(input(""))
  print("Qual o Capital Social?")
  cs = float(input(""))
  print("Qual o preço da ação?")
  pda2 = float(input(""))
  pl2 = ll/cs
  print(f"O P/L é {pl2}")
  print("______________")
 else:
  print("Escreva 1 ou 2")
