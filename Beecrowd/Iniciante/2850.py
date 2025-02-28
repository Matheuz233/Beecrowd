while True:
    try:
        situacao = input()

        if situacao == "esquerda":
            print("ingles")
        elif situacao == "direita":
            print("frances")
        elif situacao == "nenhuma":
            print("portugues")
        else:
            print("caiu")
    
    except EOFError:
        break