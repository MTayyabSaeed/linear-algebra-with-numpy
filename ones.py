# import ones
from numpy import ones
# create a ones array
ones_arr = ones([2])
print(ones_arr)
ones_arr2 = ones([2,3])
print(ones_arr2)
ones_arr3 = ones((2, 3, 4))
print(ones_arr3)


# checking the shapes of each vector or matrix
print("ones_arr shape: {}". format(ones_arr.shape))
print("ones_arr2 shape: {}". format(ones_arr2.shape))
print("ones_arr3 shape: {}". format(ones_arr3.shape))

# checking if all have the same data type
print("ones_arr dtype: {}". format(ones_arr))
if ones_arr.dtype == ones_arr2.dtype == ones_arr3.dtype:
    print("All arrays have the same dtype")
else:
    print("Something is wrong the condition statement")
