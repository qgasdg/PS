import sys
from collections import deque

V = int(input())
tree = [[] for _ in range(V)]

for _ in range(V):
    line = list(map(int, sys.stdin.readline().split()))
    idx = 1
    while line[idx] != -1:
        adj_node, adj_dist = line[idx], line[idx + 1]
        tree[line[0] - 1].append((adj_node - 1, adj_dist))
        idx += 2


def bfs(x):
    visited = [False] * V
    visited[x] = True
    ret = [0, 0]
    dist = 0
    q = deque()
    q.append((x, 0))
    while q:
        tmp_node, tmp_dist = q.popleft()
        if ret[1] < tmp_dist:
            ret[0] = tmp_node
            ret[1] = tmp_dist
        nxt = tree[tmp_node]
        for nxt_node, nxt_dist in nxt:
            if visited[nxt_node]:
                continue
            visited[nxt_node] = True
            q.append((nxt_node, tmp_dist + nxt_dist))
    return ret


print(bfs(bfs(0)[0])[1])