for _ in range(int(input())):
    word = input()

    wordLen = len(word)

    if wordLen > 10:
        print(f"{word[0]}{wordLen - 2}{word[-1]}")
    else:
        print(word)
