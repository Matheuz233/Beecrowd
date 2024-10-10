n = input()

while n != "-1":
    if n[:2] == "0x":
        print(int(n, 16))
    else:
        n = hex(int(n))
        n = n[:2] + n[2:].upper()
        print(n)

    n = input()
