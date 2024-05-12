def mdc(m, n):
    if m % n == 0:
        return n
    else:
        return mdc(n, m % n)

for _ in range(int(input())):
    numeros = list(map(str, input().split()))
    operacao = numeros[3]
    N1 = int(numeros[0])
    N2 = int(numeros[4])
    D1 = int(numeros[2])
    D2 = int(numeros[6])
    if (operacao == '+'):
        t1 = (N1*D2 + N2*D1)
        t2 = (D1*D2)
    if (operacao == '-'):
        t1 = (N1*D2 - N2*D1)
        t2 = (D1*D2)
    if (operacao == '*'):
        t1 = (N1*N2)
        t2 = (D1*D2)
    if (operacao == '/'):
        t1 = (N1*D2)
        t2 = (N2*D1)

    decomp = mdc(t1,t2)

    if decomp != 1:
        print(f"{t1}/{t2} = {t1/decomp:.0f}/{t2/decomp:.0f}")
    else:
        print(f"{t1}/{t2} = {t1}/{t2}")
