abc = list(map(float, input().split()))
x = sorted(abc)
A = x[2]
B = x[1]
C = x[0]
if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")

if A == B and B == C and A == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")