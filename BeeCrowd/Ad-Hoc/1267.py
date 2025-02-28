while True:
    n, d = map(int, input().split())

    if n == 0 and d == 0:
        break

    alunos = []
    resultado = False

    for _ in range(d):
        aluno = list(map(int, input().split()))
        
        alunos.append(aluno)

    for i in range(n):
        alunoAtual = []
        for j in range(d):
            alunoAtual.append(alunos[j][i])

        if alunoAtual.count(1) == d:
            resultado = True

    print("yes" if resultado else "no")
