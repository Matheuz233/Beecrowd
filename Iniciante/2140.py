notas = [100, 50, 20, 10, 5, 2]

n, m = map(int, input().split())

while n != 0 and m != 0:
    
    total = m - n
    
    index = 0
    
    for i in notas:
        if total - i >= 0:
            total -= i
            index += 1
    
    if index == 2:
        print("possible")
    else:
        print("impossible")
        
    n, m = map(int, input().split())