#1>wap to  print the second largest and  second  smallest element in alist of  10 integer without using sort function .
arr=[]
x=int(input("enter the no f elements :"))
for i in range(x):
    m=int(input("enter the element :"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted  array is :")    
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("seconf larges  element is :",second_largest)
print("second_largest elment is  :",second_smallest 
      )