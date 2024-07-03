while True:
    try:
        N = list(input())
        total = 0
        for i in N:
            if i == "(":
                total += 1
            if i == ")":
                total -= 1
                if total == -1:
                    break
        if total == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break