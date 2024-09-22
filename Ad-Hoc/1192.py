for _ in range(int(input())):
  entrada = input()
  a = int(entrada[0])
  b = int(entrada[2])
  operacao = entrada[1]
  
  if a == b:
    print(a*b)
  elif operacao.islower():
    print(a+b)
  else:
    print(b-a)