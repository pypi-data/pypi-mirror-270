from pybigdata import linear_algebra as LA

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A = LA.Matrix(data)

L, U = A.lu_decomposition()

print("..:: Lower triangular matrix ::..\n", L)
print("\n..:: Upper triangular matrix ::..\n", U)
