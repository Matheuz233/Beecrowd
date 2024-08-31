def knapsack(W, weights, values, N):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[N][W]

    w = W
    num_included_items = 0
    total_weight_used = 0
    for i in range(N, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            num_included_items += 1
            total_weight_used += weights[i - 1]
            w -= weights[i - 1]

    return max_value, num_included_items, total_weight_used


for _ in range(int(input())):
    pac = int(input())
    weight = []
    value = []
    for _ in range(pac):
        n, w = map(int, input().split())
        weight.append(w)
        value.append(n)

    total_brinquedos, total_usados, total_peso = knapsack(
        50, weight, value, pac)
    print(f"{total_brinquedos} brinquedos")
    print(f"Peso: {total_peso} kg")
    print(f"sobra(m) {pac - total_usados} pacote(s)")
    print("")
