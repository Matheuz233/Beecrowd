for _ in range(int(input())):
    ataque = list(map(str, input().split("me")))

    parte1 = ataque[0].split("h")[1]
    parte2 = ataque[1].split("k")[1]

    total = len(parte1) * len(parte2)

    print(f"k{'a'*total}")
