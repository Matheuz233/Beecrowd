b = int(input())
g = int(input())

if g % 2 != 0:
    g = g - 1

g = g/2

if g <= b:
    print("Amelia tem todas bolinhas!")
else:
    print(f'Faltam {int(g-b)} bolinha(s)')