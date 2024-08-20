import numpy as np
# methods to change shape and structure of the arr
# 4 lists with 5 elements each
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[10,11,12,13,14],[15,16,17,18,19]])

# not using np, use a.reshape
# 5 lists with 4 elements each
print(a.reshape((5,4)))
# one list with 20 elements
print(a.reshape((20,)))
# 20 lists with one element each
print(a.reshape((20,1)))
# 3 dimensional
# 5 collections, 2 lists each, with 5 elements each
print(a.reshape((5,2,2)))

# reshape we must assign back to a to take effect
# resize causes it to take effect immediately
a.resize((5,4))

print(a)
# flatten returns a copy, while ravel will change the orginal values

print(a.flatten())
print(a.ravel())

# var1 = a.flatten()
# ravel changes the orginal arr
var1 = a.ravel()
var1[2] = 100
print(var1)
print(a)

# transposing, making col into rows, and vice versa
print(a.T)
print(a.transpose())