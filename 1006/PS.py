import sys
input = sys.stdin.readline

T = int(input())

a = [0] * 10001
b = [0] * 10000
c = [0] * 10000

def solve(start):
    for i in range(start, N):
        a[i + 1] = min(b[i] + 1, c[i] + 1)
        if e[0][i] + e[1][i] <= W:
            a[i + 1] = min(a[i] + 1, a[i + 1])
        if i > 0 and e[0][i - 1] + e[0][i] <= W and e[1][i - 1] + e[1][i] <= W:
            a[i + 1] = min(a[i - 1] + 2, a[i + 1])
        if i < N - 1:
            b[i + 1] = a[i + 1] + 1
            if e[0][i] + e[0][i + 1] <= W:
                b[i + 1] = min(c[i] + 1, b[i + 1])
            c[i + 1] = a[i + 1] + 1
            if e[1][i] + e[1][i + 1] <= W:
                c[i + 1] = min(b[i] + 1, c[i + 1])

for _ in range(T):
    N, W = map(int, input().split())
    e = [list(map(int, input().split())) for _ in range(2)]

    b[0] = c[0] = 1

    solve(0)
    ans = min(30000, a[N])

    if N > 1 and e[0][N - 1] + e[0][0] <= W:
        a[1] = 1
        b[1] = 2
        c[1] = 1 if e[1][0] + e[1][1] <= W else 2
        solve(1)
        ans = min(ans, c[N - 1] + 1)
    if N > 1 and e[1][N - 1] + e[1][0] <= W:
        a[1] = 1
        b[1] = 1 if e[0][0] + e[0][1] <= W else 2
        c[1] = 2
        solve(1)
        ans = min(ans, b[N - 1] + 1)
    if N > 1 and e[0][N - 1] + e[0][0] <= W and e[1][N - 1] + e[1][0] <= W:
        a[1] = 0
        b[1] = c[1] = 1
        solve(1)
        ans = min(ans, a[N - 1] + 2)

    print(ans)

'''
1
1 9
3
5
=>
1

1
1 5
3
5
=>
2

1
2 100
30 50
40 60
=>
2
'''