""" this program will check list and count frequency of each element """

def count_frequency(numbers):
    """ function to count frequency of given list """
    frequency = {}
    for num in numbers:
        print(num) 
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        print(type(frequency))
        print(f"{num} is appearing {frequency} times")
    return frequency

# Testing the function
nums = [ 1, 2, 3, 1, 2, 5, 1, 3, 5]
RESULT = count_frequency(nums)
print(RESULT)
