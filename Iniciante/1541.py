import math

while True:
    entrada = input()
    
    if entrada == "0":
        break

    entrada = entrada.split(" ")
    
    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    
    area_casa = a * b
    
    area_terreno = (area_casa * 100) / c
    
    lado_terreno = int(math.sqrt(area_terreno))
    
    print(lado_terreno)
