import numpy as np

a = np.array([[11,12,13,14,15],[16,17,18,19,20],[1,2,3,4,5],[6,7,8,9,10]])

print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(a.sum())
print(np.median(a))

# random number with up  to 
# can even create dimensions
numbers1 = np.random.randint(100,size=(2,3,4))
print(numbers1)
# size, propability, size with binomial distribution
numbers2 = np.random.binomial(10, p=0.5, size= (5,10))
print(numbers2)
# choose one of thse numbers
numbers3 = np.random.choice([10,20,30,40,50], size=(1,2))
print(numbers3)
