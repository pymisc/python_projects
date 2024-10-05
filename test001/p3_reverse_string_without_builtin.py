""" this is a program to reverse string without using a builtin function """

def myfunction(x):
    """ this is the function to actually reverse string """
    len_string = len(x)
    for i in range(1, len_string+1, 1):
        # print(i)
        print(x[-i], end="")


STR1 = "this is to reverse"
print(f"String passed: {STR1}")
myfunction(STR1)

print("")
