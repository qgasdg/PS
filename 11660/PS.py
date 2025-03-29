import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
b = [[0] * N for _ in range(N)]
for i in range(N):
    s = 0
    for j in range(N):
        s += Board[i][j]
        b[i][j] = s
        if i > 0:
            b[i][j] += b[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        print(b[x2][y2])
    elif x1 == 0:
        print(b[x2][y2] - b[x2][y1 - 1])
    elif y1 == 0:
        print(b[x2][y2] - b[x1 - 1][y2])
    else:
        print(b[x2][y2] - b[x2][y1 - 1] - b[x1 - 1][y2] + b[x1 - 1][y1 - 1])

