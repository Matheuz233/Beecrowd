base32 = "0123456789ABCDEFGHIJKLMNOPQRSTUV"

while True:
    n = int(input())
    if n == 0:
        print(0)
        break
    else:
        resultado = []
        while n > 0:
            resultado.append(base32[n % 32])
            n //= 32
        print(''.join(reversed(resultado)))
