import sys

t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())
    src = list(map(int, sys.stdin.readline().rstrip()))
    while True:
        if len(src) == 0:
            print(0)
            break
        if src[0] == 1 and src[-1] == 0:
            src.pop(-1)
            src.pop(0)
        elif src[0] == 0 and src[-1] == 1:
            src.pop(-1)
            src.pop(0)
        else:
            print(len(src))
            break
