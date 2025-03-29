N, M = map(int, input().split())
vRoot = [i for i in range(N)]

def find(x):
    if x != vRoot[x]:
        vRoot[x] = find(vRoot[x])
    return vRoot[x]

ans = False
for i in range(M):
    A, B = map(find, map(int, input().split()))
    if ans:
        continue
    if A == B:
        ans = i + 1
    elif A > B:
        vRoot[A] = B
    else:
        vRoot[B] = A
print(ans if ans else 0)
