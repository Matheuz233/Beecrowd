l=int(input())
t=(input())

soma, media, total = 0, 0, 0

for i in range(12):
    for j in range(12):
        n=float(input())
        if i==l:
            total += 1
            soma+=n
            media=soma/total

if t.upper() == "S":
    print(soma)
else:
    print(media)