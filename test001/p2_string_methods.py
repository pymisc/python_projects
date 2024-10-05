""" this is to test string operations """

def print_func1():
    """ to print some same headers """
    print("***" * 15)

def print_reverse(x):
    """ function to print reverse to whatever string is passed """
    return x[::-1]

# print_func1()
# print("Hello " * 5)
# print_func1()

s1 = "this is a test string"

# STRING METHODS:
print(f"Capitalize: {s1.capitalize()}") # To capitalize first letter of string
print(f"Upper case: {s1.upper()}")      # To UPPERCASE entire string
print(f"Lower case: {s1.lower()}")      # To lowercase entire string
print(f"Casefold: {s1.casefold()}")     # Casefold is same as lower but also deals with unicode
print(f"Centralized: {s1.center(40)}")  # Centralize the text with a total of n number of spaces
print(f"Count text: {s1.count(' ')}")   # Count the occurance of specific word etc


# REVERSING STRINGS
STR1 = "This is how we reverse a string using a function"
STR2 = print_reverse(STR1)
STR3 = print_reverse(STR2)

print(f"{STR2} :: {STR3}")