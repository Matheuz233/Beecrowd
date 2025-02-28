from math import ceil

while True:
    try:
        jogadores = int(input())

        votos = list(map(int, input().split()))

        if votos.count(1) >= ceil((jogadores*2)/3):
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break
