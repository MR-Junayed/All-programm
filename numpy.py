import numpy as np

li={1,2,3,4,5}
list1=np.array(li)
arr=np.array([5,6,7,8])
print(arr)
print(list1)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a)
mul=np.dot(a,b)
print(mul)

transpose_matrix = np.transpose(mul)
print(transpose_matrix)
determinant = np.linalg.det(mul)
print(determinantp