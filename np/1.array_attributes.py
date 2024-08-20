import numpy as np
# np not so different from normal python array
# written in c
# np arrays are separated by spaces instead of commas

a = np.array([1,2,3,4])

# works the same as python
# print(a[:2])
# a[2] = 10

# create multi-dimensional arrays
a_mul = np.array([[1,2,3],[4,5,6]])

print(a_mul[0])
# second element of the first list
print(a_mul[0,1])

# 2 arrays with each having 3 elements, (2,3)
print(a_mul.shape)

# 2 since it only goes 2 deep
print(a_mul.ndim)

# all elements in the data, 6 here
print(a_mul.size)

# data types
print(a_mul.dtype)