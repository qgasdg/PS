import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

PSA = [0] * n
PSA[0] = A[0]
for i in range(1, n):
    PSA[i] = PSA[i - 1] + A[i]

PSB = [0] * m
PSB[0] = B[0]
for i in range(1, m):
    PSB[i] = PSB[i - 1] + B[i]

c = Counter()
for i in range(m):
    c[PSB[i]] += 1
    for j in range(i + 1, m):
        c[PSB[j] - PSB[i]] += 1

ans = 0
for i in range(n):
    ans += c[T - PSA[i]]
    for j in range(i + 1, n):
        ans += c[T - (PSA[j] - PSA[i])]

print(ans)