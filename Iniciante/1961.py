p, n = map(int, input().split())
canos = list(map(int, input().split()))

resultado = True

for i in range(n - 1):
    if abs(canos[i] - canos[i + 1]) > p:
        resultado = False
        break

print("YOU WIN" if resultado else "GAME OVER")
