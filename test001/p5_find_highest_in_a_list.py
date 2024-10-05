""" this program can be used to find higestest and second highest number in a list """

LIST1=[5, 10, 10, 20, 9, 12, 19, 29, 4]
LIST1.sort()
L2=len(LIST1)

print(LIST1)
print(L2)

print(f"Largest number of list: {LIST1[L2-1]}")
print(f"Second Largest number of list: {LIST1[L2-2]}")
#print(LIST1[L2-1])
