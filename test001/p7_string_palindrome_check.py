""" this is a new re-write of palindrome """

def palindrome_check(x):
    """ function to check palindrome """
    return x == x[::-1]

X = "tatata"
print(f"{palindrome_check(X)}")
