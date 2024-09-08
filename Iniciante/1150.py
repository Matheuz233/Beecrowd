x = int(input())
total, y = 0, 0

while x >= y:
    y = int(input())

xArray = [x]

while sum(xArray) <= y:
    x += 1
    xArray.append(x)

print(len(xArray))
