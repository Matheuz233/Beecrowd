def somasSucessivas(num):
    num = str(num)
    
    while len(num) > 1:
        total = sum(int(d) for d in num)
        num = str(total)
    
    return int(num)


while True:
    n, m = map(int, list(input().split()))

    if n == 0 and m == 0:
        break

    if len(str(n)) > 1:
        n = somasSucessivas(n)
    if len(str(m)) > 1:
        m = somasSucessivas(m)

    if n == m:
        print(0)
    elif n > m:
        print(1)
    elif n < m:
        print(2)
