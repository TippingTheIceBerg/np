import numpy as np


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

# repeates the list 5 times if python arr
print(l1*5)

# if np array, mults the values of the arr
print(a1*5)
 
#  np also allows with this lists of different dimensions
b1 = np.array([1,2,3])
# this won't work
# b2 = np.array[[1,2],[2,1]]
b2 = np.array([[2],[3]])

# results in a 2 by 3 matrix, works as 
# 1 plus 2, 1 plus 3
# 2 plus 2, 2 plus 3...etc

print(b1+b2)


c1 = np.array([[1,2,3],[4,5,6]])
print("___________________________")
print(np.sqrt(c1))
print(np.sin(c1))