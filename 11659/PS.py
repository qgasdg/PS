import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
PS = [0] * N
PS[0] = A[0]

for i in range(1, N):
    PS[i] = PS[i - 1] + A[i]

for _ in range(M):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    if i == 0:
        print(PS[j])
    else:
        print(PS[j] - PS[i - 1])
