while True:
    try:
        s = input()
        min = any(c.islower() for c in s)
        mai = any(c.isupper() for c in s)
        num = any(c.isdigit() for c in s)
        especiais = s.isalnum()
        tamanho = 6 <= len(s) <= 32

        if min and mai and num and especiais and tamanho:
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break
