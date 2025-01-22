while True:
    try:
        entrada = input().strip()
        
        b1 = 0
        for i in range(9):
            b1 += int(entrada[i]) * (i + 1)
        b1 %= 11
        if b1 == 10:
            b1 = 0
        
        b2 = 0
        for i in range(9):
            b2 += int(entrada[i]) * (9 - i)
        b2 %= 11
        if b2 == 10:
            b2 = 0
        
        
        print(f"{entrada[:3]}.{entrada[3:6]}.{entrada[6:9]}-{b1}{b2}")
    
    except EOFError:
        break
