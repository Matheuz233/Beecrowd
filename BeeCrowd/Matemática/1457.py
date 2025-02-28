def oraculo(N, K):
    total = N
    I = 1
    while (N-I*K) > 1:
        total *= (N - I*K)
        I += 1
    print(total)

for _ in range(int(input())):
    entrada = list(input())
    qtdExclamacoes = 0
    numeros = []
    for x in entrada:
        if x == '!':
            qtdExclamacoes += 1
        else:
            numeros.append(x)
    inteiros = int("".join(numeros))
    oraculo(inteiros, qtdExclamacoes)
