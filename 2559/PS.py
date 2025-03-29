import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
PS = [0] * N
PS[0] = A[0]

for i in range(1, N):
    PS[i] = PS[i - 1] + A[i]

ans = PS[K - 1]
for i in range(K, N):
    ans = max(ans, PS[i] - PS[i - K]) # K ~ 0 까지 합 - 1 ~ 0 까지 합 = K ~ 2
print(ans)

