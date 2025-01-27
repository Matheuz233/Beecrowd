for _ in range(int(input())):
  frase = input().split(' ')
  resultado = ""

  for palavra in frase:
    if palavra != '':
      resultado += palavra[0]
    
  print(resultado)