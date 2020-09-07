"""
https://numpy.org/doc/stable/user/quickstart.html
https://numpy.org/devdocs/reference/routinesd
"""
import numpy as np
from numpy import pi

# Array creation
list1 = [1,2,3,4,5]
np_array = np.array(list1)

# Array manipulation routines
# numpy.copyto(dst, src, casting='same_kind', where=True)
"""https://numpy.org/devdocs/reference/generated/numpy.copyto.html#numpy.copyto"""

# # Both arrays should be the same size
# np_array2 = np.array([7,9,10,78,98])
# np.copyto(np_array2, np_array)
# print(np_array2)
# print(np_array)

# var = np.array([[1], [2], [3], [4], [5]])
# for elements in var.flat:
#     print(elements)



# kanto = [73, 67, 43]
# johto = [91, 88, 64]
# hoenn = [87, 134, 58]
# sinnoh = [102, 43, 37]
# unova = [69, 96, 70]
# w1, w2, w3 = 0.3, 0.2, 0.5
# weights = [w1, w2, w3]
#
# # def crop_yield(region, weights):
# #     result = 0
# #     for x, w in zip(region, weights):
# #         result += x * w
# #     return result
# #
# # print(crop_yield(kanto, weights))
#
# # making the region data into np arrays
# kanto1 = np.array([73, 67, 43])
# weights1 = np.array([w1, w2, w3])
#
# # dot_multiplication (matrix_multiplication)
# # 1 x 3 to 3 x 1
# print(np.dot(kanto1, weights1))
#
# climate_data = np.array([[73, 67, 43],
#                          [91, 88, 64],
#                          [87, 134, 58],
#                          [102, 43, 37],
#                          [69, 96, 70]])
#
# # matrix_multiplication
# output = np.matmul(climate_data, weights)
# print(output)
# second_way = climate_data @ weights
# print(second_way)
#
# # Types of arrays
# # 1d array
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1.shape)  # (5,)
# arr2 = np.array([[1], [2], [3], [4], [5]])
# print(arr2.shape)  # (5, 1)
#
# # 2D array
# arr3 = np.array([[1, 2, 3, 4],
#                  [5, 6, 7, 8],
#                  [9, 1, 2, 3]])
# print(arr3.shape)  # (3, 4)
# print(arr3.size)  # number of elements in the array
#
# # 3D array
# arr4 = np.array([
#     [
#         [11, 12, 13],
#         [13, 14, 15]
#     ],
#
#     [
#         [15, 16, 17],
#         [17, 18, 19.5]
#     ]
# ])
# print(arr4.shape)  # (2, 2, 3)
# print(arr4.dtype)
#
#
# zero_array = np.zeros((3, 4))
# print(zero_array)
#
# ones_array = np.ones((2, 3, 4), dtype=np.int16)
# print(ones_array)
#
# # create an array range
# print(np.arange( 10, 30, 5 ))
#
#
# print(np.linspace(0, 2, 9))  # 9 numbers from 0 to 2
#
# b = np.arange(12).reshape(3, 4)
# print(b)
# print(b.sum(axis=0))  # sum of each column
# print(b.min(axis=1))  # min of each row
# print(b.cumsum(axis=1))  # cumulative sum along each row
#
# a = np.arange(8).reshape((2,2,2))
# print(a)
# print(np.trace(a))


# x = np.array([[3., 7., 3., 4.],
#               [1., 4., 2., 2.],
#               [7., 2., 4., 9.]])
# print(x.shape)
# print(x.ravel()) # returns the array, flattened
# print(x.reshape(6,2))  # returns the array with a modified shape
# print(x.T)
# print(x.T.shape)
# print(x.shape)
# # The reshape function returns its argument with a modified shape,
# # whereas the ndarray.resize method modifies the array itself:
# # like sort and sorted
# print(x.resize((2,6)))

# # stacking
# # Horizontal stacking or hstack and vertical stacking or vstack
# a = np.array([[9., 7.],
#        [5., 2.]])
# b = np.array([[1., 9.],
#        [5., 1.]])
# # vertical stack
# print(np.vstack((a,b)))
#
# # horizontal stack
# print(np.hstack((a,b)))


a = np.arange(25).reshape(5,5)
print(a)
# in rows starting from row2 take every other row
# [[11, 12, 13, 14, 15]
#  [21, 22, 23, 24, 25]]
# columns take evey alternate column from these rows
# [[11, 13, 15],
#  [21, 23, 25]]

# print(a[2::2,::2])
print(a[1:4:2,:3:2])
print(a[:,1::2])
print(a[4:,:])
print(a[4])

print(a[a%3==0])


