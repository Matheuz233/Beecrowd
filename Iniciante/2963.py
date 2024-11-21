votos = []

for i in range(int(input())):
    votos.append(int(input()))

carlos = votos.pop(0)

if max(votos) < carlos:
    print("S")
elif max(votos) == carlos:
    print("S")
else:
    print("N")