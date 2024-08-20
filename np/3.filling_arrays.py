import numpy as np

# sometimes we want an array filled with a value
# takes the shape and val you want filled in it
# creates two 2 lists, with 4 digits in each list, of num 9
a = np.full((2,4),6)
print(a)

# range of values
# start at 0, up to but not include 1000, use steps of 5
x_values = np.arange(0,1000,5)

lin_space = np.linspace(0,1000,2)
print(x_values)
print(lin_space)