entrada = input().strip()
N, X = map(int, entrada.split())

quantidadePessoas = N + 2

dias = X / quantidadePessoas

print(f"{dias:.2f}")
