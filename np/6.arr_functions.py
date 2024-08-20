import numpy as np

# how do we append, insert, delete from an arr

a =  np.array([[1,2,3],[4,5,6]])

# add onto an array
# np and panda does not save a change in arr unless reassigned
c = np.append(a,[4,5,6])
# takes arr and where to inser into the arr

b = np.insert(a,3,[4,5,6])
# delete from an array
# takes the arr, index, and axis, without the axis, just deltes on num at the index

print(np.delete(a,1))
print(np.delete(a,2))
# dep on number, either delete the row or col
# delete the first row, or the second if 1
# second parameter is the axis, 0 = row, 1= col
print(np.delete(a,0,0))
# print(np.delete(a,1,0))

print(np.delete(a,0,1))
