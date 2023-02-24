import sys

n, m = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False] * m for _ in range(n)]

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y, step):
    if x < 0 or x > n - 1:
        return 1e9
    if y < 0 or y > m - 1:
        return 1e9
    if visited[x][y]:
        return 1e9
    if board[x][y] != 1:
        return 1e9
    if x == n - 1 and y == m - 1:
        return step
    k = 1e9
    visited[x][y] = True
    for i in range(4):
        k = min(k, dfs(x + dx[i], y + dy[i], step + 1))
    return k


print(dfs(0, 0, 0))
