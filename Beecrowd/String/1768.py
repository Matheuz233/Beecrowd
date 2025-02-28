while True:
    try:
        n = int(input())
        
        for i in range(1, n + 1, 2):
            espacos = (n - i) // 2
            print(" " * espacos + "*" * i)

        print(" " * ((n - 1) // 2) + "*")
        print(" " * ((n - 3) // 2) + "***")
        print()

    except EOFError:
        break