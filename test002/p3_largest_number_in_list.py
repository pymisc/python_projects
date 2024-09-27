""" this program is to find largest number in a list """

def find_largest_number(input_list):
    """ this function will help to find max number from given list """
    largest_number = input_list[0]
    for num in input_list:
        largest_number = max(largest_number, num)
    return largest_number

list_to_test = [ 2 , 5 , 10 , 20 , 100 , 1 ]
RESULT = find_largest_number(list_to_test)

print(f"Largest number in given list is: {RESULT}")
