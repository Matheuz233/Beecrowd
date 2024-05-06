def elevado_digito(numero):
    return  10 ** numero
def elevado_consoante(numero):
    return 26 ** numero

for _ in range(int(input())):
    c, d = map(int, input().split(" "))
    if c == 0 and d == 0:
        print(0)
    else:
        print(elevado_consoante(c) * elevado_digito(d))