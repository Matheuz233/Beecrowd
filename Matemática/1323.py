while True:
    n = int(input())
    
    if n == 0:
        break
    
    total = 0

    for i in range(1, n+1):
        total += i**2
    
    print(total)
