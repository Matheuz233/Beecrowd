from math import ceil

renas = ["Dasher", "Dancer", "Prancer", "Vixen",
         "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

entrada = list(map(int, input().split()))

total = sum(entrada)

bolasPassadas = (ceil(total/9) - 1) * 9

faltando = total - bolasPassadas

print(renas[faltando - 1])
