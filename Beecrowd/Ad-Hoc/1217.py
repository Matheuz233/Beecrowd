kgs = []
frutas = []

for _ in range(int(input())):
    kgs.append(float(input()))
    frutas.append(list(input().split(" ")))

totalFrutas = 0
for i in range(len(frutas)):
    print(f"day {i+1}: {len(frutas[i])} kg")
    totalFrutas += len(frutas[i])

print(f"{totalFrutas/len(frutas):.2f} kg by day")

print(f"R$ {sum(kgs)/len(kgs):.2f} by day")
