import sys
input = sys.stdin.readline

N, T = map(int, input().split())
wp = []
for _ in range(N):
    wp.append(tuple(map(int, input().split())))

wp.sort(key=lambda x: x[1])

ans = 0
for i in range(T - N + 1, T + 1):
    ans += wp[i - (T - N + 1)][1] * (i - 1) + wp[i - (T - N + 1)][0]

print(ans)