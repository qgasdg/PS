import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
info = []

for _ in range(M):
    info.append(tuple(map(int, input().split())))

info.sort(key=lambda x: (x[1], -x[0]))

truck = [0] * N
ans = 0
for i in range(M):
    frm = info[i][0]
    to = info[i][1]
    cnt = info[i][2]
    m = cnt
    for j in range(frm, to):
        m = min(m, C - truck[j])
    for j in range(frm, to):
        truck[j] += m
    ans += m

print(ans)
