memo = {
    1: 1,
    2: 1
}


def fibonacci(n):
    if n in memo:
        return memo.get(n)

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


resultado = []

n = int(input())

if n == 1:
    print(1)

else:

    fibonacci(n)

    for chave, valor in memo.items():
        resultado.append(valor)

    resultado.sort(reverse=True)

    print(" ".join(map(str, resultado)))
