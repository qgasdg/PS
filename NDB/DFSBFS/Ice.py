import sys
from collections import deque

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(4):
    board[i] = list(map(int, board[i]))

visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0


def bfs(x, y):
    global ans
    ans += 1
    q = deque([(x, y)])
    while q:
        v = q.popleft()
        visited[v[0]][v[1]] = True
        for j in range(4):
            if v[0] + dx[j] < 0 or v[0] + dx[j] > n - 1:
                continue
            if v[1] + dy[j] < 0 or v[1] + dy[j] > m - 1:
                continue
            if board[v[0] + dx[j]][v[1] + dy[j]] == 0:
                if not visited[v[0] + dx[j]][v[1] + dy[j]]:
                    q.append((v[0] + dx[j], v[1] + dy[j]))


for i in range(n * m):
    if board[i // m][i % m] == 0:
        if not visited[i // m][i % m]:
            bfs(i // m, i % m)

print(ans)
