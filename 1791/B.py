import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ans = False
    pos = [0, 0]
    tt = int(sys.stdin.readline())
    src = sys.stdin.readline().rstrip()
    for i in range(tt):
        if src[i] == 'U':
            pos[0] += 1
        elif src[i] == 'D':
            pos[0] -= 1
        elif src[i] == 'R':
            pos[1] += 1
        else:
            pos[1] -= 1
        if pos == [1, 1]:
            ans = True
    if ans:
        print("YES")
    else:
        print("NO")
