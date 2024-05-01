import math
X, Y = map(int, input().split(" "))
voltas = math.ceil(X / (Y - X)) + 1
print(voltas)