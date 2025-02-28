n = int(input())

for _ in range(n):
    x, y = map(int, input().split('x'))

    for i in range(5, 11):
        if x == y:
            print(f"{x} x {i} = {x * i}")
        else:
            print(f"{x} x {i} = {x * i} && {y} x {i} = {y * i}")
