# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask for user's input

fullname = input("Enter your full name: ").lstrip() # remove leading spaces from the input

# print input

print(fullname)