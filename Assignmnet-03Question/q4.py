#4>WAP TO CHECK WETHER THE STRING IS SYMMETERICAL OR PALINDROME .
x=int(input("enter a  string "))
z=(str(str(x)[::-1]))
if x==z:
    print("it is a plaindrome ")
else:
    print("it is not a  palindrome")