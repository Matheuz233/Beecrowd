n = int(input())

casas = n**2

if n % 2 == 0:
	print(f"{casas//2} casas brancas e {casas//2} casas pretas")
else:
	print(f"{casas//2 + 1} casas brancas e {casas//2} casas pretas")
