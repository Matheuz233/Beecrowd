hi, mi, hf, mf = map(int, input().split(" "))

inicio = (hi * 60) + mi
final = (hf * 60) + mf

total_min = final - inicio

if total_min <= 0:
    total_min += 24*60

contador = 0
while total_min >= 60:
    total_min -= 60
    contador += 1

print(f"O JOGO DUROU {contador} HORA(S) E {total_min} MINUTO(S)")