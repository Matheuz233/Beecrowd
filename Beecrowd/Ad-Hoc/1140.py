entrada = list(map(str, input().split()))

while entrada[0] != "*":
  iniciais = []

  for i in entrada:
    iniciais.append(i[0].lower())

  if iniciais.count(iniciais[0]) == len(entrada):
    print("Y")
  else:
    print("N")
  
  entrada = list(map(str, input().split()))