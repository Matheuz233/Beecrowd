n = int(input())
resultados = []

for _ in range(n):
    t = int(input())

    if t < 2015:
        ano = 2015 - t
        resultados.append(f"{ano} D.C.")
    else:
        ano = t - 2014
        resultados.append(f"{ano} A.C.")

print("\n".join(resultados))
