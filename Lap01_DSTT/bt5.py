import numpy as np

M1 = np.array([[9, 12], [23, 30]])
u = np.array([2, 1])
print(M1.dot(u))
print(u.dot(M1))

print(np.dot(M1, u))
print(np.dot(u, M1))

mat1 = np.zeros([5, 5])
print(mat1)

mat2 = np.ones([5, 5])
mat3 = mat1 + 2 * mat2
mat4 = mat3
mat3[3][2] = 10

mat5 = np.copy(mat3)
mat3[3][2] = 5

mat6 = np.empty([4, 5])

mat7 = np.identity(4)

mat8 = np.random.random([4, 5])