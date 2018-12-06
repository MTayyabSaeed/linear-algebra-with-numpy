# import empty
from numpy import empty

"""
    creating an empty array of a specific shape
    the values will be random and assigned before use
"""
# arg = list
arr_l = empty([3,3])
print(arr_l)
# arg = tuple
arr_t = empty((3,2))
print(arr_t)
print(arr_l[0][0])

