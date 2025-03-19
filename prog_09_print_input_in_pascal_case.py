# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# ask for user's input 
fullname = input("Enter your name in incorrect casing: ")

# capitalize first letter of every word and remove spacing 
pascal_case = fullname.title().replace(" ", "")

# print
print(pascal_case)

