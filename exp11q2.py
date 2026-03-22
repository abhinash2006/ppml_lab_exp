# wap for data type and structeres in numpy
import numpy as np
arr = np.array([1,2,3],dtype='int32')
print("data type:",arr.dtype)
arr=arr.astype('float64')
print("updateed type:",arr.dtype)