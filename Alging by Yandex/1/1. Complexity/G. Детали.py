def solve(N, K, M):
    ans = 0
    number_M = K // M
    if number_M == 0:
        return ans

    while N >= K:
        number_K = N // K
        ans += number_M * number_K
        N = (K - number_M * M) * number_K + N - (K * number_K)

    return ans


N, K, M = map(int, input().split())

print(solve(N, K, M))
