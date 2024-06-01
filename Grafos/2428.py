A = list(map(int, input().split()))

A.sort()

area1 = A[0] * A[3]
area2 = A[1] * A[2]

if area1 == area2:
    print("S")
else:
    print("N")