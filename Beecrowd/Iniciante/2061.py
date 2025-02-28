n, m = map(int, input().split())

for _ in range(m):
    acao = input()
    if acao == "fechou":
        n += 1
    elif acao == "clicou":
        n -= 1

print(n)