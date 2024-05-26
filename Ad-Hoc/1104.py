def trocas_alice(X, Y):
    unicosY = set(Y)
    X = [i for i in X if i not in unicosY]
    return len(set(X))

def trocas_beatriz(X, Y):
    unicosX = set(X)
    Y = [i for i in Y if i not in unicosX]
    return len(set(Y))

A, B = map(int, input().split())

while A != 0 and B != 0:
    X = input().split()
    Y = input().split()

    copiaX = X[:]
    copiaY = Y[:]

    print(min(trocas_alice(X, Y), trocas_beatriz(copiaX, copiaY)))

    A, B = map(int, input().split())
