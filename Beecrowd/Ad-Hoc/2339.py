c, p, f = map(int, input().split())

quantidade = p/f

if c <= quantidade:
  print('S')
else:
  print('N')