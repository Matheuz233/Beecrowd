for _ in range(int(input())):
  luzes, alt = map(str, input().split())

  luzes = list(luzes)
  alt = int(alt)

  for i in range(len(luzes)):
    if alt == 0:
      break
    if alt % 2 != 0:
      if luzes[i] == 'X':
        luzes[i] = 'O'
      else:
        if luzes[i] == 'O':
            alt += 1
        luzes[i] = 'X'
    alt = alt // 2

  print(''.join(luzes))