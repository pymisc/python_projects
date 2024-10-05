""" this program can be used to find higestest and second highest number in a list """

def smallest_number_finder(x):
    """ this is to find smallest number in the list """
    LEN1=len(x)
    print(LEN1)
    # below is starting assumption
    SMALLEST=x[0]
    for i in range(0, LEN1, 1):
        if x[i] < SMALLEST:
            SMALLEST = x[i]
    return SMALLEST

def biggest_number_finder(x):
    """ this is to find biggest number in the list """
    LEN1=len(x)
    print(LEN1)
    # below is starting assumption
    BIGGEST=x[0]
    for i in range(0, LEN1, 1):
        if x[i] > BIGGEST:
            BIGGEST = x[i]
    return BIGGEST




LIST1=[50, 10, 20, 9, 12, 99, 19, 21, 29, 4]
print(f"INPUT LIST IS: {LIST1}")
RESULT1=smallest_number_finder(LIST1)
RESULT2=biggest_number_finder(LIST1)

print(f"Smallest number is: {RESULT1}")
print(f"Largest number is: {RESULT2}")
 
