for _ in range(int(input())):
  entrada = list(input())

  total, numero = 0, 0
  numerosSequencia = False

  for i in entrada:
    if i.isdigit():
      if numerosSequencia == False:
        numero = int(i)
        numerosSequencia = True
      else:
        numero = int(str(numero) + i)
    else:
      numerosSequencia = False
      total += numero
      numero = 0

  total += numero

  print(total)