for _ in range(int(input())):
  c = list(map(int, input().split()))

  mediaTurma = sum(c[1:])/c[0]

  alunosAcima = 0

  for i in c[1:]:
    if i > mediaTurma:
      alunosAcima += 1

  print(f"{alunosAcima/c[0]*100:.3f}%")