for _ in range(int(input())):
    placar1 = list(map(str, input().split()))
    placar2 = list(map(str, input().split()))

    time1, time2 = 0, 0

    time1 += (int(placar1[0]) + int(placar2[2]))
    time2 += (int(placar1[2]) + int(placar2[0]))

    if time1 == time2:
        if int(placar1[2]) == int(placar2[2]):
            print("Penaltis")
        elif int(placar1[2]) > int(placar2[2]):
            print("Time 2")
        else:
            print("Time 1")
    elif time1 > time2:
        print("Time 1")
    elif time2 > time1:
        print("Time 2")
