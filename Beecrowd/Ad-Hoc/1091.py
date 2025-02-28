while True:
  consultas = int(input())

  if consultas == 0:
    break

  xd, yd = map(int, input().split())

  for _ in range(consultas):
    resultado = ""
    xa, ya = map(int, input().split())

    if xd == xa or yd == ya:
      resultado = 'divisa'
    
    else:
      if yd - ya < 0:
        resultado += 'N'

      if yd - ya > 0:
        resultado += 'S'

      if xd - xa < 0:
        resultado += 'E'

      if xd - xa > 0:
        resultado += 'O'

    print(resultado)