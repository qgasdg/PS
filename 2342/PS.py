import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

A = list(map(int, input().split()))
A.pop()
b = [
    [1, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]
dp = {}


def dfs(n, pointer):
    if n == len(A) - 1:
        return 0
    if (n, pointer) in dp:
        return dp[(n, pointer)]
    cost = min(dfs(n + 1, pointer % 10 + A[n + 1] * 10) + b[pointer // 10][A[n + 1]],
               dfs(n + 1, (pointer // 10) * 10 + A[n + 1]) + b[pointer % 10][A[n + 1]])
    dp[(n, pointer)] = cost
    return cost


print(dfs(-1, 0))
