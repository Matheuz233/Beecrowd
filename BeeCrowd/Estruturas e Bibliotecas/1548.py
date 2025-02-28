for _ in range(int(input())):
  n = int(input())
  m = list(map(int, input().split()))

  copyM = m.copy()

  m.sort(reverse=True)

  total = 0

  for i in range(n):
    if copyM[i] == m[i]:
      total += 1
    
  print(total)