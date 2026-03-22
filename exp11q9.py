#wap to calculate the correlation between columns in a data frame 
import pandas as pd
data = {
    'Math':[90,85,80,95],'science':[88,82,85,90],'English':[78,75,80,85]
}
df=pd.DataFrame(data)
print("DataFrame")
print(df)
correlation=df.corr()
print("\n correlation Matrix:")
print(correlation)