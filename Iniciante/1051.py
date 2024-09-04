s = float(input())

if (s >= 0 and s <= 2000.00):
    print("Isento")

if (s > 2000.01 and s <= 3000.00):
    s = s - 2000.00
    s = s * 8/100
    print("R$ %.2f" % s)

if (s > 3000.01 and s <= 4500.00):
    s = (s-2000)
    s1 = s-1000
    taxa1 = (1000*8)/100
    taxa2 = (s1*18)/100
    print("R$ %.2f" % (taxa1+taxa2))

if (s > 4500.01):
    s = s-2000
    s1 = s-1000
    taxa1 = 1000*8/100
    s2 = s1-1500
    taxa2 = (1500*18)/100
    taxa3 = (s2*28)/100
    print("R$ %.2f" % (taxa3+taxa1+taxa2))