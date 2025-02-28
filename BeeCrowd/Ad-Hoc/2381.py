criancas = []
comportaram, naoComportaram = 0, 0

for _ in range(int(input())):
    comportamento, nome = map(str, input().split())

    if comportamento == "+":
        comportaram += 1
    else:
        naoComportaram += 1

    criancas.append(nome)

criancas.sort()

for i in criancas:
    print(i)

print(f"Se comportaram: {comportaram} | Nao se comportaram: {naoComportaram}")