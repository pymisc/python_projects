""" this is a program to reverse string without using a builtin function """

def myfunction(x):
    """ this is the function to actually reverse string """
    LEN = len(x)
    for i in range(1, LEN+1, 1):
        # print(i)
        print(x[-i], end="")


str1 = "this is to reverse"
print(f"String passed: {str1}")
myfunction(str1)

print("")
