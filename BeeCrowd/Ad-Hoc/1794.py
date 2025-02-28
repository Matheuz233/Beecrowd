n = int(input().strip())
la, lb = [int(x) for x in input().strip().split(' ')]
sa, sb = [int(x) for x in input().strip().split(' ')]

if(la <= n <= lb and sa <= n <= sb):
    print("possivel")
else:
    print("impossivel")