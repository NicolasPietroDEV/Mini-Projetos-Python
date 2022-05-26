s = int(input())
a = int(input())
b = int(input())
total = 0

for x in range(a, b+1):
    soma = 0
    for i in str(x):
        soma += int(i)
    if soma == s:
        total += 1

print(total)