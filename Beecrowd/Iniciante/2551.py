while True:
    try:
        recorde = 0

        for i in range(1, int(input())+1):
            t, d = map(int, input().split())

            if (d/t) > recorde:
                recorde = d/t
                print(i)
                
    except EOFError:
        break
