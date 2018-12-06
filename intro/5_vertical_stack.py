# imports
from numpy import array
from numpy import vstack

# create arrays
arr1 = array([1, 2, 3])
arr2 = array([7, 5, 4])

print("array 1: {0},   array 2: {1}". format(arr1, arr2))
arr3 = vstack([arr1, arr2])
print("vertically stacked array and array2:\n{}". format(arr3))
