for i in range(int(input())):
    entrada = list(input())
    total = 0
    for num in entrada:
        num = int(num)
        if num == 1:
            total += 2
        if num == 2 or num == 3 or num == 5:
            total += 5
        if num == 4:
            total += 4
        if num == 6 or num == 9 or num == 0:
            total += 6
        if num == 7:
            total += 3
        if num == 8:
            total += 7
    print(f"{total} leds")