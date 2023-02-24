import sys
import time
import copy
from collections import deque

start_time = time.time()

n, m = map(int, input().split())
board = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False] * m for _ in range(n)]
ans = 0


def bfs(x, y, case):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        v = q.popleft()
        for i in range(4):
            if v[0] + dx[i] < 0 or v[0] + dx[i] > n - 1:
                continue
            if v[1] + dy[i] < 0 or v[1] + dy[i] > m - 1:
                continue
            if case[v[0] + dx[i]][v[1] + dy[i]] == 0:
                q.append((v[0] + dx[i], v[1] + dy[i]))
                case[v[0] + dx[i]][v[1] + dy[i]] = 2


for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

print(board)
