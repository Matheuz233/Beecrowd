n = int(input())

figurinhas = []

for _ in range(int(input())):
    figura = int(input())

    if figurinhas.count(figura) == 0:
        figurinhas.append(figura)

print(n - len(figurinhas))