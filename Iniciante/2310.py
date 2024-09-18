total1, total2, total3 = 0, 0, 0
totalS1, totalB1, totalA1 = 0, 0, 0

for _ in range(int(input())):
  nome = input()
  s, b, a = map(int, input().split())
  s1, b1, a1 = map(int, input().split())

  total1 += s
  total2 += b
  total3 += a

  totalS1 += s1
  totalB1 += b1
  totalA1 += a1

print(f"Pontos de Saque: {totalS1*100/total1:.2f} %.")
print(f"Pontos de Bloqueio: {totalB1*100/total2:.2f} %.")
print(f"Pontos de Ataque: {totalA1*100/total3:.2f} %.")
