def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


text = "Hello World"
reversed_text = reverse_string(text)
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

                 