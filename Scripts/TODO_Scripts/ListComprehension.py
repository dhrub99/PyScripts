#This function is an implementation of how list comprehension works

# TODO: Build a program on your own which works like this without using list comprehension.

n = int(input("Enter a number as a range: "))
print("A list of numbers of squares up to the given number is:")
print([x**2 for x in range(n)]) 
print("Converting the list of numbers till the given number to string data type:")
print([str(x) for x in range(n)])
