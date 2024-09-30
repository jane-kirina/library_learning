import numpy as np

'''Index:
    Basic
    Creating Arrays
    Random
    Reshape
    Slicing
    Linear algebra
    Broadcasting
    Seed
    Viewing, manipulating, comparing arrays
    Standard Deviation and Variance
    Dot product
    Sorting
    Images and NumPy
'''

separator_header = '-------------------------'

'''Basic'''
print(separator_header + 'Basic')

A = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print(A.shape)

B = np.arange(20, 100, 3)  # for i in range(20, 100, 3)

print(np.random.permutation(np.arange(10)))  # random order of np.arange(10)

'''Creating Arrays'''
a1 = np.array([3, 8, 2, 6])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)  # uniformly random between 0 and 1
a5 = np.random.randn(10)  # normal distribution
a6 = np.linspace(0, 10, 100)  # 100 - number of elements in array
a7 = np.arange(0, 10, 0.02)  # 100 - spacing

'''Random'''
print(separator_header + 'Random')

A = np.random.randint(1, 5)
print(A)
print("type of c: " + str(type(A)))

B = np.random.randint(1, 5, 2)
print(B)
print("type of c: " + str(type(B)))

'''Reshape'''
print(separator_header + 'Reshape')

A = np.random.rand(2, 3, 4, 2)
print(A)
print("------------------------")

B = np.arange(100).reshape(4, 25)
print(B)
print("------------------------")

C = np.arange(100).reshape(4, 5, 5)
print(C)
print("------------------------")

'''Slicing'''
print(separator_header + 'Slicing')

# A[start:end:step] - > [start, end)

A = np.arange(100)

B = A[3:10]  # B is not a copy of A

print(B)
print("------------------------")
B[0] = 1010
print(B)
print("------------------------")
print(A)

print("------------------------")
B = A[10:20].copy()
print(B)

print("------------------------")
print(np.argwhere(A == 1010))  # find index of element, return array of indexes

print("------------------------")
print("------------------------")

aaa = np.round(10 * np.random.rand(5, 4))

print(aaa)

print(aaa[1, 2])  # specific element
print("------------------------")

print(aaa[1, :])  # specific row
print("------------------------")

print(aaa[:, 1])  # specific column
print("------------------------")

print(aaa[1:3, 2:4])  # specific column

'''Linear algebra'''
print(separator_header + 'Linear algebra')

import numpy.linalg as la

print(la.inv(np.random.rand(3, 3)))

print("------------------------")

A = np.round(10 * np.random.rand(4, 5))
print(A)
print("------------------------")
A.sort(axis=0)  # sort column
print(A)
print("------------------------")
A.sort(axis=1)  # sort row
print(A)

'''Broadcasting'''
print(separator_header + 'Broadcasting')

A = np.round(10 * np.random.rand(2, 3))
print(A)
print("------------------------")
print(A + 3)
print("------------------------")
B = np.arange(2).reshape(2, 1)
print(B)
print(A + B)

print("------------------------")
print("------------------------")
B = np.round(10 * np.random.rand(2, 2))
print(A)
print("------------------------")
print(B)
print("------------------------")
C = np.hstack((A, B))
print(C)

print("------------------------")
print("------------------------")

A = np.random.permutation(np.arange(10))
A.sort()
print(A)
A = A[::-1]
print(A)

'''Seed'''
print(separator_header + 'Seed')
# Pseudo-random number
np.random.seed(1)
a = np.random.randint(10, size=(5, 3))
print(a)

'''Viewing, manipulating, comparing arrays'''
print(separator_header + 'Viewing, manipulating, comparing arrays')
b = np.unique(a)
print(b)

a4 = np.random.randint(10, size=(2, 3, 4, 5))
print(a4.shape)

print(a4[:, :, :1, :2])

print("------------------------")

a1 = np.array([1, 2, 3])
print(a1)
print(a1 + np.ones(3))
print(a1 * np.ones(3))
print(a1 / np.array([2, 2, 2]))

print("------------------------")

a2 = np.random.randint(10, size=(2, 3))
a3 = np.arange(1, 19).reshape(2, 3, 3)
print(a2)
print(a3)

'''Standard Deviation and Variance'''
print(separator_header + 'Standard Deviation and Variance')
high_arr = np.array([1, 100, 200, 300, 4000, 5000])
low_arr = np.array([2, 4, 6, 8, 10])

print('Variance')
print(np.var(high_arr))
print(np.var(low_arr))

print('Standard Deviation')
print(np.std(high_arr))
print(np.std(low_arr))

'''Dot product'''
print(separator_header + 'Dot product')
np.random.seed(0)

mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))

print('mat1: ' + str(mat2.shape))
print(mat1)

print('mat2: ' + str(mat2.shape))
print(mat2)
# Element—wise multiplication (Hadamard product)
mat3 = mat1 * mat2

# np.dot(mat1, mat2) # error
# Transpose mat1
mat2 = mat2.T.shape

print("Dot product")
print(np.dot(mat1.shape, mat2))

'''Sorting'''
print(separator_header + 'Sorting')

arr = np.random.randint(10, size=(3, 5))
print(arr)

print('Sort:')
print(np.sort(arr))

print('Return the indices that would sort an array:')
print(np.argsort(arr))

print('Min and Max:')
print(str(np.argmin(arr)) + ' -- ' + str(np.argmax(arr)))

print('Array:')
print(arr)

print('Min, axis=0:')
print(np.argmin(arr, axis=0))

print('Max, axis=1:')
print(np.argmin(arr, axis=1))

'''Images and NumPy'''
print(separator_header + 'Images and NumPy')
from matplotlib.image import imread

img1 = imread('01.png')
print(type(img1))
print(img1)
print('Size of image array: ' + str(img1.size))
print('Shape of image array: ' + str(img1.shape))
print('Number of image array dimensions: ' + str(img1.ndim))
