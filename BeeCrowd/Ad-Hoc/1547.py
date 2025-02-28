for _ in range(int(input())):
  qt, s = map(int, input().split())
  valores = list(map(int, input().split()))

  if valores.count(s) > 0:
    print(valores.index(s) + 1)
  else:
    proximo = 1
    menor = abs(s - valores[0])

    for numero in valores:
      if numero - s < menor:
        menor_atual = abs(s - numero)
        if menor_atual < menor:
          menor = abs(s - numero)
          proximo = valores.index(numero) + 1
    
    print(proximo)