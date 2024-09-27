""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    XX = 1
    YY = 1
    while XX <= n:
        YY = (XX*YY)
        XX += 1    
    return YY

# testing the function
NUMBER = 4
RESULT = factorial(NUMBER)
print(f"The factorial of {NUMBER} is : {RESULT}")
