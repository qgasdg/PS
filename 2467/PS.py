import sys

N = int(input())
Arr = list(map(int, sys.stdin.readline().split()))
S = []

for a in Arr:
    if a < 0:
        S.append((-1, -a))
    else:
        S.append((1, a))

S.sort(key=lambda x: x[1])

ans = 0
M = 100000000

for i in range(N - 1):
    tmp = S[i][0] * S[i][1] + S[i + 1][0] * S[i + 1][1]
    if abs(tmp) < M:
        M = abs(tmp)
        ans = i

Ans = [S[ans][0] * S[ans][1], S[ans + 1][0] * S[ans + 1][1]]
Ans.sort()
print(*Ans)