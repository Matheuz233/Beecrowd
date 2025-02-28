n = int(input())

for _ in range(n):
    k = int(input())
    
    idiomas = set(input().strip() for _ in range(k))
    
    if len(idiomas) == 1:
        print(idiomas.pop())
    else:
        print("ingles")
