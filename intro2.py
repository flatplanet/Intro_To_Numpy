import numpy as np

# Create a numpy array
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)


# Arange
np2 = np.arange(10)
print(np2)

# step
np3 = np.arange(0,10, 2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

# Convert a python list to a np
my_list3 = [0,1,2,3,4,5,6,7,8,9]
print(my_list3)
np8 = np.array(my_list3)
print(np8)
print(np8[0])