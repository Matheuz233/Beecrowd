F1,F2=map(float,input().split())
F1 = 100.00 + F1
F2 = F2/100.00+1
resultado = F1 * F2 - 100.00
print(f'{resultado:.6f}')