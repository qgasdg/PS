N = int(input())
A = list(map(int, input().split()))
dp = [1] * 1000
dp[0] = 1  # 1번이 가장 큰 증가부분수열
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

m = max(dp)
print(m)
ans = []
for i in range(N - 1, -1, -1):
    if m == dp[i]:
        ans.append(A[i])
        m -= 1
print(' '.join(map(str, ans[::-1])))

