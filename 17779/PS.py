N = int(input())
A = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
ans = float('inf')


def solve(d1, d2, x, y):
    global N
    if not (1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N):
        return 10000000
    s = [0, 0, 0, 0, 0]
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    for i in range(d2 + 1):  # 3번 경계선
        s[4] += A[x + d1 + i][y - d1 + i]
        visited[x + d1 + i][y - d1 + i] = True
    for i in range(d1 + 1):  # 4번 경계선
        s[4] += A[x + d2 + i][y + d2 - i]
        visited[x + d2 + i][y + d2 - i] = True

    for i in range(d1):
        s[4] += A[x + i][y - i]
        visited[x + i][y - i] = True
        k = 1
        while not visited[x + i + k][y - i]:
            s[4] += A[x + i + k][y - i]
            visited[x + i + k][y - i] = True
            k += 1
    for i in range(1, d2):
        s[4] += A[x + i][y + i]
        visited[x + i][y + i] = True
        k = 1
        while not visited[x + i + k][y + i]:
            s[4] += A[x + i + k][y + i]
            visited[x + i + k][y + i] = True
            k += 1

    s[4] -= A[x + d1 + d2][y - d1 + d2]

    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if visited[r][c]:
                break
            s[0] += A[r][c]
    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if visited[r][c]:
                break
            s[1] += A[r][c]
    for r in range(N, x + d1 - 1, -1):
        for c in range(1, y - d1 + d2):
            if visited[r][c]:
                break
            s[2] += A[r][c]
    for r in range(N, x + d2, -1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if visited[r][c]:
                break
            s[3] += A[r][c]

    return max(s) - min(s)


for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(1, N):
            for y in range(1, N):
                ans = min(ans, solve(d1, d2, x, y))

print(ans)
