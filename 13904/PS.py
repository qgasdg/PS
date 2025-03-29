import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))

A.sort(key=lambda x: -x[1])
room = [0] * 1001
for d, w in A:
    for i in range(d, 0, -1):
        if room[i] == 0:
            room[i] = w
            break

print(sum(room))