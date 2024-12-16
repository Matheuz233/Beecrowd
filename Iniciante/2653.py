joias = []

while True:
    try:
        joia = input()
        if joias.count(joia) == 0:
            joias.append(joia)
        
    except EOFError:
        break

print(len(joias))   