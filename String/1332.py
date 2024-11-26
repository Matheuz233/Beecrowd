for _ in range(int(input())):
    palavra = list(input())

    one = ["o", "n", "e"]
    two = ["t", "w", "o"]

    one_total = 0
    tow_total = 0

    if len(palavra) == 5:
        print(3)
    else:
        for i in range(3):
            if palavra[i] == one[i]:
                one_total += 1
            if palavra[i] == two[i]:
                tow_total += 1
        if one_total > tow_total:
            print(1)
        else:
            print(2)