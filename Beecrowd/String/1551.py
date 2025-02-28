for _ in range(int(input())):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    frase = input()

    for i in frase:
        if alfabeto.count(i):
            alfabeto.remove(i)

    if len(alfabeto) == 0:
        print("frase completa")
    elif len(alfabeto) <= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
