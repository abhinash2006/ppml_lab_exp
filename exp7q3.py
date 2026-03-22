s=input("enter paragraph:")
words=s.split()
print("word count:",len(words))
print("palindrome count:")
sum(1 for w in words if w==w[::-1])
print("reverse words:")
for w in words:
    print(w [::-1],end=" ")