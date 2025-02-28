nomes = []

while True:
  try:
    nome = input()
    nome.lower()

    nomes.append(nome)

  except EOFError:
    break

print()