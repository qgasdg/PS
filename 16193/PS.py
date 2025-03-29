import sys


def max_difference_sum(n, arr):
    arr.sort()
    result = []

    # 양쪽에서 하나씩 꺼내는 방식
    left, right = 0, n - 1
    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1

    # 최댓값 계산
    max_sum = sum(abs(result[i] - result[i + 1]) for i in range(n - 1))
    return max_sum


# 입력 처리
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# 결과 출력
print(max_difference_sum(n, arr))
