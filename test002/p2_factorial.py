""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    X = 1
    Y = 1
    while X <= n:
        Y = (X*Y)
        X += 1    
    return Y

# testing the function
NUMBER = 4
result = factorial(NUMBER)
print(f"The factorial of {NUMBER} is : {result}")
