a, b, c, d = map(int, input().split())

if (a + b > c and a + c > b and b + c > a) or \
   (a + b > d and a + d > b and b + d > a) or \
   (a + c > d and a + d > c and c + d > a) or \
   (b + c > d and b + d > c and c + d > b):
    print('S')
else:
    print('N')
