import sys
sys.setrecursionlimit(10000000)

V, E = map(int, input().split())
parents = [x for x in range(V + 1)]
edges = []
for _ in range(E):
    edges.append(list(map(int, sys.stdin.readline().split())))
edges.sort(key=lambda x: x[2])


def get_parent(x):
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)
    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def same_parent(a, b):
    if get_parent(a) == get_parent(b):
        return True
    else:
        return False


answer = 0
for edge in edges:
    if same_parent(edge[0], edge[1]):
        continue
    union_parent(edge[0], edge[1])
    answer += edge[2]
print(answer)

