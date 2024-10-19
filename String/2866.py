for _ in range(int(input())):
    c = input()

    resultado = []

    for i in c:
        if i.islower():
            resultado.insert(0, i)

    print("".join(resultado))
