import string

alfabeto = list(string.ascii_uppercase)

for _ in range(int(input())):
    total = 0
    for y in range(int(input())):
        linhas = list(input())
        count = 0
        for x in linhas: 
            total += alfabeto.index(x) + y + count
            count += 1
    print(total)