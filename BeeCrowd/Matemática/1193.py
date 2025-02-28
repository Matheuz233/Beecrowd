n = int(input())

for i in range(1, n + 1):
    x, y = input().split()

    if y == 'dec':
        decimal = int(x)
        hexadecimal = hex(decimal)[2:]
        binario = bin(decimal)[2:]

        print(f"Case {i}:")
        print(f"{hexadecimal} hex")
        print(f"{binario} bin")

    elif y == 'hex':
        decimal = int(x, 16)
        hexadecimal = x.lower()
        binario = bin(decimal)[2:]

        print(f"Case {i}:")
        print(f"{decimal} dec")
        print(f"{binario} bin")

    elif y == 'bin':
        decimal = int(x, 2)
        hexadecimal = hex(decimal)[2:]

        print(f"Case {i}:")
        print(f"{decimal} dec")
        print(f"{hexadecimal} hex")

    print()
