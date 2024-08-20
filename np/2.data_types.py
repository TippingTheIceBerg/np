import numpy as np
# string with less than 11 characters, data type is now a string
a = np.array([[1,2,3],[4,"hello",6],[7,8,9]])

b = np.array([[1,2,3],[4,"5",6],[7,8,9]], dtype=np.int32)

# all integers in the array are now strings becaus of that one hellow
print(a.dtype)

print(b.dtype)
