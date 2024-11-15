while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    volumeParalelepipedo = a * b * c

    arestasCubo = int(volumeParalelepipedo ** (1/3))

    print(arestasCubo)