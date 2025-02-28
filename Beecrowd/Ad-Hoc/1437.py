direcoes = ["N", "O", "S", "L"]

while True:
    n = int(input())

    if n == 0:
        break

    comandos = list(input())

    index = 0

    for i in comandos:
        if i == "E":
            index += 1
        if i == "D":
            index -= 1

        if index >= 4 or index <= -4:
            index = 0
    
    print(direcoes[index])
