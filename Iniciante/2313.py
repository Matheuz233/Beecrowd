a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
  if a == b == c:
    tipo = "Valido-Equilatero"
  elif a == b or b == c or a == c:
    tipo = "Valido-Isoceles"
  else:
    tipo = "Valido-Escaleno"
        
  if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    retangulo = "Retangulo: S"
  else:
    retangulo = "Retangulo: N"


  print(f"{tipo}")
  print(f"{retangulo}")
else:
  print("Invalido")