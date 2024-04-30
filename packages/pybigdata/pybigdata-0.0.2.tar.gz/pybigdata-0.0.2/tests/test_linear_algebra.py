from pybigdata import linear_algebra as LA

data = [[1, 2, 5, 3], [2, 5, 9, 8], [3, 6, 1, 1], [2, 0, 1, 0]]

A = LA.Matrix(data)

print(f"Number of rows: {A.get_num_rows()}")
print(f"Number of columns: {A.get_num_cols()}")
print(f"Second row: {A.get_row(1)}")
print(f"Third col: {A.get_column(2)}")
print(f"Determinant: {A.det()}")
print(f"Trace: {A.trace()}")
print(f"Is singular? {A.is_singular()}")
print(f"Is squared? {A.is_squared()}")
print(f"Is sparse? {A.is_sparse()}")
print(f"Is symmetric? {A.is_symmetric()}")
print(f"Is orthogonal? {A.is_orthogonal()}")
print(f"Is orthonormal? {A.is_orthonormal()}")
print(f"Is triangular? {A.is_triangular()}")
print(f"Is diagonal? {A.is_diagonal()}")
print(f"\nTransposed:\n{A.T()}")
print(f"\nInversed:\n{A.inverse()}")
L, U = A.lu_decomposition()
print(f"\nLU Decomposition:\n{L}\n\n{U}")
Q, R = A.qr_decomposition()
print(f"\nQR Decomposition:\n{Q}\n\n{R}")
