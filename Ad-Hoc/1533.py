n = int(input())

while n != 0:
    v = list(map(int, input().split()))
    vCopy = v.copy()

    v.remove(max(v))

    print(vCopy.index(max(v)) + 1)

    n = int(input())
