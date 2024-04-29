while True:
    try:
        a, b, c = map(int, input().split())
        
        if (a == 0 and b == 0 and c == 1) or (a == 1 and b == 1 and c == 0):
            print("C")
        if (a == 0 and b == 1 and c == 0) or (a == 1 and b == 0 and c == 1):
            print("B")
        if (a == 1 and b == 0 and c == 0) or (a == 0 and b == 1 and c == 1):
            print("A")
        if (a == 0 and b == 0 and c == 0) or (a == 1 and b == 1 and c == 1):
            print("*")
    except EOFError:
        break