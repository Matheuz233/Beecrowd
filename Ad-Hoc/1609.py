for _ in range(int(input())):
    n = int(input())
    carneiros = list(map(int, input().split()))

    print(len(set(carneiros)))
