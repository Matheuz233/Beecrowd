d, n = map(str, input().split())

while d != "0" and n != "0":

    n = n.replace(d, '')

    if not n or len(n) == n.count("0"):
        print(0)
    else:
        n = n.lstrip("0")
        print(n)

    d, n = map(str, input().split())
