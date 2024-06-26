N = int(input())
X = []
for i in range(N):
    X.append(int(input()))

X.sort()

while len(X) > 0:
    num = X[0]
    print(f"{num} aparece {X.count(num)} vez(es)")
    while X.count(num) > 0:
        X.remove(num)