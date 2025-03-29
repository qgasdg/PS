import sys
from sortedcontainers import SortedDict

input = sys.stdin.readline

N, M = map(int, input().split())
ab, cd = [], []
for _ in range(N):
    ab.append(tuple(map(int, input().split()))[::-1])
for _ in range(M):
    cd.append(tuple(map(int, input().split()))[::-1])
ab.sort()
cd.sort()

ans = 0
idx = 0
bus = SortedDict(int)
for i in range(N):
    while idx < M and cd[idx][0] <= ab[i][0]:
        if not cd[idx][1] in bus:
            bus[cd[idx][1]] = 0
        bus[cd[idx][1]] += 1
        idx += 1
    kidx = bus.bisect_left(ab[i][1])
    if len(bus) == kidx:
        continue
    key = bus.keys()[kidx]
    ans += 1
    bus[key] -= 1
    if bus[key] == 0:
        del bus[key]

print(ans)