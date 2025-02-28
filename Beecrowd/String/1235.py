for _ in range(int(input())):
  n = input()

  metade = len(n)//2

  p1 = n[:metade]
  p2 = n[metade:]

  print(p1[::-1] + p2[::-1])
