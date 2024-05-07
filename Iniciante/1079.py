for _ in range(int(input())):
    n1, n2, n3 = map(float, input().split(" "))
    total = (n1*2 + n2*3 + n3*5) / 10
    print(f"{total:.1f}")