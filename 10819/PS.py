N = int(input())
A = list(map(int, input().split()))
visited = [False] * N
ans = 0
idx = []


def check():
    s = 0
    for i in range(N - 1):
        s += abs(A[idx[i]] - A[idx[i + 1]])
    return s


def f(k):
    global ans
    if k == N:
        ans = max(ans, check())
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        idx.append(i)
        f(k + 1)
        idx.pop()
        visited[i] = False
    return


f(0)
print(ans)
