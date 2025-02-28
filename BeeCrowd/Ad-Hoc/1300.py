while True:
    try:
        entrada = int(input())
        if entrada % 6 == 0:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
