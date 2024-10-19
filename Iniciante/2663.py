equipes = int(input())
aprovados = int(input())
pontos = []

for _ in range(equipes):
    pontos.append(int(input()))

pontos.sort(reverse=True)

equipesSelecionadas = pontos[:aprovados]
equipesReprovadas = pontos[aprovados:]

for i in equipesReprovadas:
    if i == equipesSelecionadas[-1]:
        equipesSelecionadas.append(i)
    else:
        break

print(len(equipesSelecionadas))
