arr = [[0] * 4 for _ in range(3)]
wrongarr = [[0] * 4] * 3
print(arr, wrongarr)
arr[0][0] += 1
wrongarr[0][0] += 1
print(arr, wrongarr)
