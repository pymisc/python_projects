""" checking if the given word is a palindrome """

def is_palindrome(string):
    reversed_string = string[::-1]
    print("REVERSED STRING IS: ", reversed_string)
    return string == reversed_string

# Testing above function now
WORD = "mdam"
if is_palindrome(WORD):
    print(f"{WORD} is a palindrome")
else:
    print(f"{WORD} is NOT a palindrome")
