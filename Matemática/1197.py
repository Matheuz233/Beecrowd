while True:
  try:
    v, t = map(int, input().split())
    deslocamento = v * 2 * t
    print(deslocamento)
  except EOFError:
    break