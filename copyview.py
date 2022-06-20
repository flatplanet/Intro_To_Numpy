import numpy as np

# Copy Vs. View
np1 = np.array([0,1,2,3,4,5])

'''
# Create a view
np2 = np1.view()

print(f'Original NP1: {np1}')
print(f'Original NP2: {np2}')

# change np1
np2[0] = 41

print(f'Changed NP1: {np1}')
print(f'Original NP2: {np2}')
'''

# Make a copy
np2 = np1.copy()
print(f'Original NP1: {np1}')
print(f'Original NP2: {np2}')

# change np1
np2[0] = 41

print(f'Changed NP1: {np1}')
print(f'Original NP2: {np2}')