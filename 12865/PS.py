N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    w, v = A[i]
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[K])
