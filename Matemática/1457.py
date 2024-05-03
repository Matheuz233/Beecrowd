def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def oraculo(N, K):
    if K == 1:
        print(calcular_fatorial(N))
    if K == 2:
        print(N * (N-K))
    if K>=3:
        total = N * (N-K)
        count = 1
        while count < K:
            total = total * (N - K*(count+1))
            count += 1
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
