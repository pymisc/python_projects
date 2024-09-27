""" this program is to find largest number in a list """

def find_largest_number(input_list):
    largest_number = input_list[0]
    for num in input_list:
        if num > largest_number:
            largest_number = num
    return largest_number

""" testing main function """
list_to_test = [ 2 , 5 , 10 , 20 , 100 , 1 ]
resultant_number = find_largest_number(list_to_test)

print(f"Largest number in given list is: {resultant_number}")
 
