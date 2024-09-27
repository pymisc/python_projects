""" this program will help to find if a number is a prime number or not """

def prime_finder(number):
    """ the function where it checks and return if prime or not """
    counter = 2 
    for counter in range(2,number,1):
        print(f" counter value is: {counter}")
        REMAINDER = number % counter
        if REMAINDER == 0:
            return False
    return True
          

# main function calling 
NUMBER = 67
#prime_finder(NUMBER)
if prime_finder(NUMBER):
    print(f"YES, the {NUMBER} is a prime number")
else:
    print(f"No, the {NUMBER} is NOT a prime number")
