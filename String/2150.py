while True:
  try:
    vogais = list(input())
    frase = list(input())

    resultado = 0

    for vogal in vogais:
      resultado += frase.count(vogal)

    print(resultado)

  except EOFError:
    break
