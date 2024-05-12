total = 0
coelhos = 0
ratos = 0
sapos  = 0
for _ in range(int(input())):
    a, b = map(str, input().split(" "))
    a = int(a)
    total += a
    if b == "C":
        coelhos += a
    if b == "R":
        ratos += a
    if b == "S":
        sapos += a

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos*100/total:.2f} %")
print(f"Percentual de ratos: {ratos*100/total:.2f} %")
print(f"Percentual de sapos: {sapos*100/total:.2f} %")