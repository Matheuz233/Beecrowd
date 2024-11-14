for _ in range(int(input())):
    entrada = input().split()
    substring = "oulupukk"

    resultado = []

    for i in entrada:
        if substring.lower() in i.lower():
            if i[-1] == ".":
                resultado.append("Joulupukki.")
            else:
                resultado.append("Joulupukki")
        else:
            resultado.append(i)

    print(" ".join(resultado))
