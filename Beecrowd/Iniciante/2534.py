while True:
    try:
      n, q = map(int, input().split())

      notas = []

      for _ in range(n):
          notas.append(int(input()))

      notas.sort(reverse=True)

      for _ in range(q):
          print(notas[int(input()) - 1])
          
    except EOFError:
        break