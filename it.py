import numpy as np

# 1-d
#np1 = np.array([1,2,3,4,5])
#for x in np1:
#	print(x)

# 2-d

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
'''
for x in np2:
	#print(x)
	for y in x:
		print(y)
'''

# 3-d
np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
'''
for x in np3:
	#print(x)
	for y in x:
		#print(y)
		for z in y:
			print(z)
'''

# np.nditer()
for x in np.nditer(np2):
	print(x)
