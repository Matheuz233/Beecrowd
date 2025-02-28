a, b, c = map(int, input().split())

if a > b and b <= c:
    print(":)")
elif a < b and b >= c:
    print(":(")
elif a < b and b < c:
    if (c - b) < (b - a):
        print(":(")
    else:
        print(":)")
elif a > b and b > c:
    if (b - c) < (a - b):
        print(":)")
    else:
        print(":(")
elif a == b:
    if c > b:
        print(":)")
    else:
        print(":(")
