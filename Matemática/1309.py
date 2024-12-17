def formatar(valor, decimal):
    int_part, dec_part = format(valor, ',.2f').split('.')
    dec_part = str(decimal)
    return f"${int_part}.{dec_part}"


while True:
    try:
        dolares = int(input())
        centavos = input().zfill(2)

        print(formatar(dolares, centavos))
    except EOFError:
        break
