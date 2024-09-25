n = int(input())
l = list(map(int, input().split()))

total2, total3, total4, total5 = 0, 0, 0, 0

for i in range(n):
    if l[i] % 2 == 0:
        total2 += 1
    if l[i] % 3 == 0: 
        total3 += 1
    if l[i] % 4 == 0:
        total4 += 1
    if l[i] % 5 == 0:
        total5 += 1

print(f"{total2} Multiplo(s) de 2")
print(f"{total3} Multiplo(s) de 3")
print(f"{total4} Multiplo(s) de 4")
print(f"{total5} Multiplo(s) de 5")