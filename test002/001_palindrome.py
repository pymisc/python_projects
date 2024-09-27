""" checking if the given word is a palindrome """

def is_palindrome(string):
  reversed_string = string[::-1]
  print("REVERSED STRING IS: ", reversed_string)
  return string == reversed_string

# Testing above function now
word = "mdam"
if is_palindrome(word):
  print(f"{word} is a palindrome")
else:
  print(f"{word} is NOT a palindrome")
