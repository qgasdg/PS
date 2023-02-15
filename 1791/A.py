import sys

t = int(sys.stdin.readline())
str = "codeforces"
for _ in range(t):
    tmp = sys.stdin.readline().rstrip()
    if tmp in str:
        print("yes")
    else:
        print("no")