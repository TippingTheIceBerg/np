import numpy as np


a1 = np.array([[11,12,13,14,15],[16,17,18,19,20]])

a2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# concat at row of existing dimensions
a= np.concatenate((a1,a2),axis=0)

# add with new dimensions

b =np.stack((a1,a2))
# axis 0 like concat
b =np.vstack((a1,a2))
# axis 1
b =np.hstack((a1,a2))

c = np.array([[11,12,13,14,15],[16,17,18,19,20],[1,2,3,4,5],[6,7,8,9,10]])

# pass in the array we want to split, and how many arr we want, on what axis
print(np.split(c,4,axis=0))


print(a)
print(b)