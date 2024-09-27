""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# testing the function
NUMBER = 5

result = factorial(NUMBER)
print(f"The factorial of {NUMBER} is : {result}")
