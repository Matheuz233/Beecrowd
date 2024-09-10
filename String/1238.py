for _ in range(int(input())):
    s1, s2 = map(str, input().split())

    resultado = []

    total = 0

    for i in range(min(len(s1), len(s2))):
        resultado.append(s1[i])
        resultado.append(s2[i])
        total += 1

    if len(s1) > len(s2):
        resultado.append(s1[total:])

    else:
        resultado.append(s2[total:])

    print(''.join(resultado))
