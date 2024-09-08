entrada = list(map(int, input().split(" ")))

a = entrada[0]

index = 1

while entrada[index] <= 0:
    index += 1

n = entrada[index]

total = [a]

for i in range(1, n):
    total.append(a + i)

print(sum(total))
