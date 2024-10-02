""" this is to test string operations """

def print_func1():
    """ to print some same headers """
    print("***" * 15)


print_func1()
#print("Hello " * 5)
#print_func1()

s1 = "this is a test string"

# STRING METHODS:
print(f"Capitalize: {s1.capitalize()}")
print(f"Upper case: {s1.upper()}")
print(f"Lower case: {s1.lower()}")
# Casefold is kinda same as lower but also deals with unicode
print(f"Casefold: {s1.casefold()}") # Casefold is same as lower BUT also deals with unicode



