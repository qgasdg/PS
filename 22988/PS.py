import sys
input = sys.stdin.readline

N, X = map(int, input().split())
C = sorted(list(map(int, input().split())))

s = 0
e = N - 1
ans = 0
rest = []
while C[e] == X:
    e -= 1
    ans += 1
    if e == -1:
        break

while s < e:
    if C[e] == X:
        ans += 1
        e -= 1
        continue
    if C[s] + C[e] + X / 2 >= X:
        ans += 1
        s += 1
        e -= 1
    else:
        rest.append(C[s])
        s += 1

if s == e:
    rest.append(C[s])

print(ans + len(rest) // 3)