import sys

input = sys.stdin.readline

N = int(input())
X, Y = [], []
for _ in range(N):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

s = 0
for i in range(1, N):
    s += X[i - 1] * Y[i]
s += X[N - 1] * Y[0]
for i in range(1, N):
    s -= X[i] * Y[i - 1]
s -= X[0] * Y[N - 1]
s *= 1/2

print(abs(s))