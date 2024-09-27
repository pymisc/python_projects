""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# testing the function
number = 5

result = factorial(number)
print(f"The factorial of {number} is : {result}")
