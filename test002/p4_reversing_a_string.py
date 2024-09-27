""" this program will reverse a string """

def reverse_a_string(input_string):
    """ this function takes input_string as argument and return its reversed """
    return input_string[::-1]

INPUT="Hello, World!"
REVERSE=reverse_a_string(INPUT)
print(f"{INPUT} string will be written as reversed as follows: {REVERSE}")
