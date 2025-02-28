x = list(map(int, input().split()))
y = list(map(int, input().split()))

compativel = True

for i in range(5):
    if x[i] == 0 and y[i] == 1:
        pass
    elif x[i] == 1 and y[i] == 0:
        pass
    else:
        compativel = False
        break

if compativel:
    print("Y")
else:
    print("N")