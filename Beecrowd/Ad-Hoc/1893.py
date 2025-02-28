n1, n2 = map(int, input().split(" "))

if n2 <= 2:
    print("nova")
elif 3 <= n2 <= 96:
    if n2 > n1:
        print("crescente")
    else:
        print("minguante")
elif 97 <= n2 <= 100:
    print("cheia")