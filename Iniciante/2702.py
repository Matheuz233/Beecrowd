ca, ba, pa = map(int, input().split())
cr, br, br = map(int, input().split())

frango = max(0, cr - ca)
bife = max(0, br - ba)
massa = max(0, br - pa)

print(frango + bife + massa)
