#wap for statistical operation and broadcasting on arrays
import numpy as np
arr = np.array([1,2,3,4])
print("Max:",arr.max())
print("Min:",arr.min())
print("sum:",arr.sum())
print("product:",arr.prod())
print("Broadcasted result:",arr+5)