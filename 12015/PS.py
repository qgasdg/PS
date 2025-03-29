N = int(input())
A = list(map(int, input().split()))
# N = 1000000
# A = [i for i in range(1000000, 0, -1)]
# dp = [-1] * N
# dp[N - 1] = 1
# for i in range(N - 2, -1, -1):
#     for j in range(i + 1, N):
#         if A[j] > A[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# 1 2 9 2 3 5 7 1
# 9
# 7 8 9 10 1 2 3 4 5
# 14
# 1 2 3 4 5 7 8 9 10 1 2 3 4 5
# 10
# 1 7 8 9 10 1 2 3 4 5
# 5
# 2 3 4 5 1
# ==
# 7
# 2 3 4 5 1 2 3
# 6
# 3 2 3 4 5 1


def binary_search(start, end, arr, key):
    s = start
    e = end
    while s < e:
        mid = (s + e) // 2
        if arr[mid] < key:
            s = mid + 1
        else:
            e = mid
    return e


arr = [A[0]]
cnt = 1
for i in range(1, N):
    if arr[-1] > A[i]:
        arr[binary_search(0, cnt, arr, A[i])] = A[i]
    elif arr[-1] < A[i]:
        arr.append(A[i])
        cnt += 1
print(cnt)