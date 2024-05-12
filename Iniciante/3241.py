for _ in range(int(input())):
    linha = input()
    if linha == "P=NP":
        print("skipped")
    else:
        a, b = map(int, linha.split("+"))
        print(a+b)