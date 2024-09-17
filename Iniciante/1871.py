m, n = map(int, input().split())

while m != 0 and n != 0:
    
    resultado = list(str(m+n))

    while '0' in resultado:
      resultado.remove('0')
    
    print(''.join(resultado))

    m, n = map(int, input().split())