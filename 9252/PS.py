from collections import deque

A = [0] + list(input())
B = [0] + list(input())

LCS = [[0] * (len(B)) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1], LCS[i - 1][j - 1] + 1)
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])
ans = deque()
x, y = len(A) - 1, len(B) - 1

while x != 0 and y != 0:
    if LCS[x][y] == LCS[x][y - 1]:
        y -= 1
    elif LCS[x][y] == LCS[x - 1][y]:
        x -= 1
    else:
        ans.append(A[x])
        x -= 1
        y -= 1

while ans:
    print(ans.pop(), end='')