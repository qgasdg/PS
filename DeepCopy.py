# Shallow Copy
a = [1, 2, 3]
b = a
b[0] = 7
print(a, b)

# Deep Copy
import copy

c = [4, 5, 6]
d = copy.deepcopy(c)
d[0] = 9
print(c, d)
