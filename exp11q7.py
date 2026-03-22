#wap to create and manipulate a data frame.
import pandas as pd
data = {
    'Name':['Alice','Bob','charcie'],'Age':[25,30,35],'city':['New york','sanfrancisco','Los Angles']
}
df = pd.DataFrame(data)
print("DtatFrame:")
print(df)
print("\nAge column:")
print(df['Age'])
print("\nRow at index1:")
print(df.iloc[1])

