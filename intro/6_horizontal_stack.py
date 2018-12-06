# imports
from numpy import array
from numpy import hstack

# create arrays
arr1 = array([1, 2, 3])
arr2 = array([9, 8, 5])
arr3 = array([4, 7, 6])

# horizontally stacking arrays
hstacked_arr = hstack([arr1, arr2, arr3])
print("arr1: {0} arr2: {1} and arr3: {2} horizontally stacked: \n{3}". format(arr1, arr2, arr3, hstacked_arr))
