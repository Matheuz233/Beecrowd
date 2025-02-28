pares, impares = [], []
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        if len(pares) == 5:
            for i in range(5):
                print(f"par[{i}] = {pares[i]}")
            pares = []
        pares.append(num)
    else:
        if len(impares) == 5:
            for i in range(5):
                print(f"impar[{i}] = {impares[i]}")
            impares = []
        impares.append(num)
if len(impares):
    for i in range(len(impares)):
        print(f"impar[{i}] = {impares[i]}")

if len(pares):
    for i in range(len(pares)):
        print(f"par[{i}] = {pares[i]}")
