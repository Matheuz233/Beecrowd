precos = {
    '1001': 1.50,
    '1002': 2.50,
    '1003': 3.50,
    '1004': 4.50,
    '1005': 5.50
}

total = 0

for _ in range(int(input())):
    p, q = map(int, input().split())

    total += precos[str(p)] * q

print(f"{total:.2f}")

