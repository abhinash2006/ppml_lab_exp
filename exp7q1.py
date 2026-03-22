m=int(input("enter m:"))
n=int(input("enter n:"))
lst=[i for i in range (m,n+1)] 
print("list:",lst)
print("sum:", sum(lst))
print("average:", sum(lst)/len(lst))            
print("largest:", max(lst))  
print("smallest:",min(lst))   
print("not divisible by 3:",[i for i  in lst if i%3 !=0])       

              
                        
            
