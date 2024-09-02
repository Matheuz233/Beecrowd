while True:
    try:
        entrada = input()
        partes = entrada.split('=')
        parte_esquerda = partes[0].split('+')
        R = parte_esquerda[0].strip()
        L = parte_esquerda[1].strip()
        J = partes[1].strip()

        if R.isdigit() and L.isdigit():
            print(int(R) + int(L))
        elif R.isdigit() and J.isdigit():
            print(int(J) - int(R))
        elif L.isdigit() and J.isdigit():
            print(int(J) - int(L))

    except EOFError:
        break