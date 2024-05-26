N = int(input())
S = list(input())

sequencia, total = 0, 0

for i in range(N):
    if S[i] == "a":
        sequencia += 1
    else:
        if sequencia > 1:
            total += sequencia
        sequencia = 0 
    
if sequencia > 1:
    total += sequencia
    
print(total)