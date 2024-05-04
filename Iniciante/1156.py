count = 0
S = 1
A = 1
B = 1
while count != 39:
    A += 2
    B *= 2
    S = S + A/B
    count += 1
print(f"%.2f" % S)