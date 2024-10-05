""" this script is a slight modification of previous one """

def function_to_rev(x):
    """ this function will do actual reverse, when passed a parameter """
    str_len = len(x)
    print(f"String length is: {str_len}")
    for n in range(1, str_len+1, 1):
        print(x[-n], end="")

STR1="test 123"
function_to_rev(STR1)

print("")
