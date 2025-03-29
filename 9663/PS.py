N = int(input())

row = [-1] * N
ans = 0


def possible(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if x - i == abs(row[x] - row[i]):
            return False
    return True


def possibility(n):
    global ans
    if n == N:
        ans += 1
        return
    for i in range(N):
        row[n] = i
        if possible(n):
            possibility(n + 1)


possibility(0)
print(ans)