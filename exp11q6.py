#wap to create and work with a pandas series.
import pandas as pd
data = [10,20,30]
labels = ['a','b','c']
Series = pd.Series(data,index = labels)
print("pandas series:")
print(Series)
print("values at label 'b':",Series['b'])