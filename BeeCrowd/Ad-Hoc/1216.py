m, p = 0, 0

while True:
    try:
        n = input()
        d = int(input())

        m += d
        p += 1
    except EOFError:
        break

print(f"{(m/p):.1f}")