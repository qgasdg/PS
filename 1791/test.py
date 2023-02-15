import sys

a = list(sys.stdin.readline().rstrip())
a.pop(-1)
print(a)