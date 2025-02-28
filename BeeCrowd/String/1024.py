for _ in range(int(input())):
    entrada = input()
    resultado = ''
    for char in entrada:
        if char.isalpha():
            resultado += chr(ord(char) + 3)
        else:
            resultado += char

    resultado = resultado[::-1]

    resultado_final = ""

    for i, char in enumerate(resultado):
        if i >= len(resultado) // 2:
            resultado_final += chr(ord(char) - 1)
        else:
            resultado_final += char

    print(resultado_final)
