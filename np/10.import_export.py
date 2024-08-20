import numpy as np

# import with csv filies or np format


a= np.array([[1,2,3,4],[5,6,7,8]])
# # creates a path
# np.save("path.npy",a)


# as a csv
np.savetxt("second_path.csv",a, delimiter=",")

# we have the array back into the script with load
# b = np.load("path.npy")
# print(b)

#loads as floating point values
c = np.loadtxt("second_path.csv",delimiter=",")
print(c)