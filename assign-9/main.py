import numpy as np
list = [1, 2, 3, 4, 5]

arr = np.array(list, dtype=np.int32)
print(arr)
print(arr.dtype)

listm = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
arrm = np.array(listm)
print(arrm)
print(arrm.ndim)
print(arrm.shape)
print(arrm.size)


arr2 = np.zeros((3,4), dtype=np.int32)
print(arr2)


arr3 = np.arange(10, 20, 2)
print(arr3)