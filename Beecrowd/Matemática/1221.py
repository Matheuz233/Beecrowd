for _ in range(int(input())):
    n = int(input())

    primo = True

    if n < 2:
        primo = False
        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
    
    if primo:
        print("Prime")
    else:
        print("Not Prime")