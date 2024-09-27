""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    VAR_X= 1
    VAR_Y= 1
    while VAR_X <= n:
        VAR_Y = (VAR_X*VAR_Y)
        VAR_X += 1    
    return VAR_Y

# testing the function
NUMBER = 4
RESULT = factorial(NUMBER)
print(f"The factorial of {NUMBER} is : {RESULT}")
