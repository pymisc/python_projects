""" the is to test factorial """

def factorial(n):
    """ this is the main function to find factorial """
    var_x= 1
    var_y= 1
    while var_x <= n:
        var_y = (var_x*var_y)
        var_x += 1    
    return var_y

# testing the function
NUMBER = 4
RESULT = factorial(NUMBER)
print(f"The factorial of {NUMBER} is : {RESULT}")
