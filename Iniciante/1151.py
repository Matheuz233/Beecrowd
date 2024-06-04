def fibonacci(num):
    count = 0
    anterior = 1
    anterior1 = 1
    while count <= num-4:       
        resultado = anterior1 + anterior
        lista.append(resultado)
        anterior1 = anterior
        anterior = resultado
        count += 1

N = int(input())
lista = [0,1,1]
fibonacci(N)

lista_str = [str(x) for x in lista]
print(' '.join(lista_str))