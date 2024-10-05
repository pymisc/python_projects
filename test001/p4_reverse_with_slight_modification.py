""" this script is a slight modification of previous one """

def function_to_rev(x):
    """ this function will do actual reverse, when passed a parameter """
    LEN = len(x)
    print(f"String length is: {LEN}")
    for n in range(1, LEN+1, 1):
        print(x[-n], end="")

STR1="test 123"
function_to_rev(STR1)

print("")
