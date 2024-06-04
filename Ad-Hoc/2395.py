A, B, C = map(int, input().split(" "))
X, Y, Z = map(int, input().split(" "))

largura = int(X/A)
comprimento = int(Y/B)
altura = int(Z/C)
print(f"{largura * comprimento * altura:.0f}")
