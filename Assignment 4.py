# Matrix addition using lists

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

C = [[A[i][j] + B[i][j] 
      
for i in range(2)]
for j in range(3)] 

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition of matrices:")
print(C)

# Matrix addition using numpy
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

C = A + B

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition of matrices:")
print(C)
