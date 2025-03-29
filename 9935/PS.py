import sys
input = sys.stdin.readline

S = input().rstrip()
C = input().rstrip()
v = [False] * len(S)
idx = 0
c = 0
save = 0

while idx < len(S):
    if v[idx]:
        idx += 1
        continue
    if S[idx] == C[c]:
        if c == 0:
            save = idx
        if c == len(C) - 1:
            for i in range(save, idx + 1):
                v[i] = True
            c = 0
            idx = 0
        else:
            c += 1
            idx += 1
    else:
        c = 0
        if S[idx] == C[c]:
            save = idx
            c += 1
            if c == len(C):
                for i in range(idx, idx - len(C), -1):
                    v[i] = True
                c = 0
                idx = 0
        idx += 1

f = True
for i in range(len(S)):
    if not v[i]:
        f = False
        print(S[i], end='')

if f:
    print("FRULA")
