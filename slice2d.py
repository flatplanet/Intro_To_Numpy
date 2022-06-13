import numpy as np

# Slicing 2-d Numpy Arrays
np1 = np.array([
	[1,2,3,4,5],
	[6,7,8,9,10]
	])

# Return 8 
print(np1[1,2])

# Return slice 2,3
print(np1[0:1, 1:3])

# Return from both dimensions 2,3 and 7,8
print(np1[0:2, 1:3])