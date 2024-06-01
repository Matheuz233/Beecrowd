from math import ceil


while True:
    try:
        testes = list(input())
        P = int(input())
        count = 0
        total = 0
        for x in testes:
            if x == "R":
                count += 1
            elif x == "W":
                if count > 0:
                    total += 2
                    count = 0
                else:
                    total += 1
                    count = 0
            
            if count == P:
                total += 1
                count = 0

        if count > 0:
            print(total+1)
        else:
            print(total)

    except EOFError:
        break
