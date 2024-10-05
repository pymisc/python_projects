""" this program can be used to find higestest and second highest number in a list """

def smallest_number_finder(x):
    """ this is to find smallest number in the list """
    len1=len(x)
    print(len1)
    # below is starting assumption
    smallest_number=x[0]
    for i in range(0, len1, 1):
        if x[i] < smallest_number:
            smallest_number = x[i]
    return smallest_number

def biggest_number_finder(x):
    """ this is to find biggest number in the list """
    len1=len(x)
    print(len1)
    # below is starting assumption
    biggest_number=x[0]
    for i in range(0, len1, 1):
        if x[i] > biggest_number:
            biggest_number = x[i]
    return biggest_number




LIST1=[50, 10, 20, 9, 12, 99, 19, 21, 29, 4]
print(f"INPUT LIST IS: {LIST1}")
RESULT1=smallest_number_finder(LIST1)
RESULT2=biggest_number_finder(LIST1)

print(f"Smallest number is: {RESULT1}")
print(f"Largest number is: {RESULT2}")
