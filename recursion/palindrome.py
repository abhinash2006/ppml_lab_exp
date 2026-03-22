def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(f"madam: {is_palindrome('madam')}")
print(f"hello: {is_palindrome('hello')}")
print(f"racecar: {is_palindrome('racecar')}")
print(f"level: {is_palindrome('level')}")
print(f"world: {is_palindrome('world')}")

