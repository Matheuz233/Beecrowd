for _ in range(int(input())):
    entrada = input()

    if len(entrada) != 8 or entrada[3] != "-":
        print("FAILURE")
        continue

    parte1, parte2 = entrada.split("-")

    if len(parte1) != 3 or not parte1.isalpha() or not parte1.isupper():
        print("FAILURE")
        continue
      
    if len(parte2) != 4 or not parte2.isdigit():
        print("FAILURE")
        continue
      
    ultimoNum = int(parte2[-1])

    if ultimoNum in [1, 2]:
        print("MONDAY")
    elif ultimoNum in [3, 4]:
        print("TUESDAY")
    elif ultimoNum in [5, 6]:
        print("WEDNESDAY")
    elif ultimoNum in [7, 8]:
        print("THURSDAY")
    elif ultimoNum in [9, 0]:
        print("FRIDAY")
