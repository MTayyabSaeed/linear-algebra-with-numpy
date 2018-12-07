# import array
from numpy import array
# one-dimentional list
X = [1, 10, 100, 1000, 10000, 100000]
print(X)
# converting list to 1D array, or a vector
X = array(X)
print(X)

# two - dimensinal list
Y = [[1, 10],
     [100, 1000],
     [10000, 1000000]]
print(Y)
# conveting two dimensional array to 2D array
Y = array(Y)
print(Y)

# three-dimensional list
Z = [[[1, 2, 3, 4],
      [4, 5, 6, 7]],
     [[7, 8, 9, 10],
      [10, 11, 12, 13]]]
print(Z)
# converting a 3D list to a 3D array
Z = array(Z)
print(Z)
