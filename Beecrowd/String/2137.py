while True:
  try:
    entradas = []
    for _ in range(int(input())):
      entradas.append(int(input()))

    entradas.sort()

    for i in entradas:
      saida = str(i)
      print(saida.zfill(4))


  except EOFError:
    break