for i in range(int(input())): 
    X = int(input())

    total=0

    for j in range(1, X+1):

        if(X % j ==0):
            total += 1
            if total > 2:
                break


    if (total>2):
        print(f"{X} nao eh primo")
    else:
        print(f"{X} eh primo")