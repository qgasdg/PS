import sys

Board = []
zero = []

c1 = [[False] * 10 for _ in range(9)]
c2 = [[False] * 10 for _ in range(9)]
c3 = [[False] * 10 for _ in range(9)]

for i in range(9):
    INP = list(map(int, sys.stdin.readline().rstrip()))
    Board.append(INP)
    for j in range(9):
        if INP[j] == 0:
            zero.append((i, j))
        c1[i // 3 * 3 + j // 3][INP[j]] = True
        c2[i][INP[j]] = True
        c3[j][INP[j]] = True


def check(x, y, k):
    if c1[x // 3 * 3 + y // 3][k]:
        return False
    if c2[x][k]:
        return False
    if c3[y][k]:
        return False
    return True


def fill(n):
    if n == len(zero):
        for row in Board:
            print(*row, sep='')
        exit()

    x, y = zero[n]

    for i in range(1, 10):
        if not check(x, y, i):
            continue
        Board[x][y] = i
        c1[x // 3 * 3 + y // 3][i] = True
        c2[x][i] = True
        c3[y][i] = True
        fill(n + 1)
        Board[x][y] = 0
        c1[x // 3 * 3 + y // 3][i] = False
        c2[x][i] = False
        c3[y][i] = False


fill(0)
