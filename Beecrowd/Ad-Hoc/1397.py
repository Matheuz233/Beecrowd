n = int(input())

while n != 0:
  j1, j2 = 0, 0
  
  for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
      j1 += 1 
    elif b > a:
      j2 += 1

  print(j1, j2)
  n = int(input())
