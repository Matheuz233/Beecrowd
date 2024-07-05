N = int(input())

while N != 0:
    total_raposo = N

    if N == 1:
        total_raposo = 0
    
    for i in range(1, N):
        if total_raposo - i >= 0:
            total_raposo -= i
        else:
            break
    
    total_pica_pau = N - total_raposo 
    
    print(f"{total_pica_pau} {total_raposo}")

    N = int(input())
