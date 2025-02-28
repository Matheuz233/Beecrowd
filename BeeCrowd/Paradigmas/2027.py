def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


resultados = []

while True:
    try:
        a, b = map(int, input().split())
        resultado_mdc = mdc(a, b)
        resultados.insert(0, resultado_mdc)
        if resultado_mdc > 5:
            print("Noel")
        else:
            print("Gnomos")
    except EOFError:
        break

print(" ".join(map(str, resultados)) + " ")
