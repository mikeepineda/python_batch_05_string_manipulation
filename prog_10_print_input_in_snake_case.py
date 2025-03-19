# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# ask for user's input
fullname = input("Enter your fullname in incorrect casing: ")

# convert all input into lowercase and change space to underscore
snake_case = fullname.lower().replace(" ", "_")

# print 
print(snake_case)