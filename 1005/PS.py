from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    dp = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        dp[i] = D[i]
        if indegree[i] == 0:
            q.append(i)
    while q:
        tmp = q.popleft()
        for adj in graph[tmp]:
            adj: int
            dp[adj] = max(dp[adj], dp[tmp] + D[adj])
            indegree[adj] -= 1
            if indegree[adj] == 0:
                q.append(adj)
    W = int(input())
    print(dp[W])