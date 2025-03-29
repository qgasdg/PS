import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
PS = [0] * N
PS[0] = A[0]

for i in range(1, N):
    PS[i] = PS[i - 1] + A[i]

cnt = 0
for i in range(1, N):
    if PS[i - 1] == M:
        cnt += 1
    for j in range(i, N):
        if PS[j] - PS[j - i] == M:
            cnt += 1

if PS[N - 1] == M:
    cnt += 1

print(cnt)