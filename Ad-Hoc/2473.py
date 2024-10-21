apostas = list(map(int, input().split()))
sorteados = list(map(int, input().split()))

total = 0

for i in apostas:
	if sorteados.count(i) > 0:
		total += 1

if total < 3:
	print("azar")
elif total == 3:
	print("terno")
elif total == 4:
	print("quadra")
elif total == 5:
	print("quina")
else:
	print("sena")
