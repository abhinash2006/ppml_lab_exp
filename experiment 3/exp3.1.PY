def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1] 
inputstring = "121"
if is_palindrome(inputstring):
    print(f'"{inputstring}" is a palindrome!')
else:
    print(f'"{inputstring}" is not a palindrome.')
