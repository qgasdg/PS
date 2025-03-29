import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
PS = [0] * N
Mod = [0] * M
PS[0] = A[0] % M
Mod[PS[0]] += 1

for i in range(1, N):
    PS[i] = (PS[i - 1] + A[i]) % M
    Mod[PS[i]] += 1

cnt = Mod[0]
for i in range(M):
    cnt += Mod[i] * (Mod[i] - 1) / 2

print(int(cnt))