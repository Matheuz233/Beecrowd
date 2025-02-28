a, b = map(int, input().split())

q = a // b
r = a % b
    
if r < 0:
    r += abs(b)
    q += 1
    

print(f"{q} {r}")
