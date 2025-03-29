N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
dp = [[False] * N for _ in range(N)]
i = 1
ans = 100000000


def dfs(s, e, w):
    global N, i, ans
    if i == (1 << N) - 1:
        dp[e][s] = True
        if not Board[e][s]:
            return
        ans = min(ans, w + Board[e][s])
        return
    for j in range(N):
        if dp[e][j]:
            continue
        if i & (1 << j):
            continue
        if not Board[e][j]:
            continue
        i |= 1 << j
        dfs(s, j, w + Board[e][j])
        i &= (((1 << N) - 1) - (1 << j))
    return


for j in range(1, N):
    i |= 1 << j
    dfs(0, j, Board[0][j])
    i &= (((1 << N) - 1) - (1 << j))
print(ans)
