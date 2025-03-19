# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# ask for user's input
fullname = input("Enter your full name: ")

# reverse the uppercase to lowercase and vice versa and print
print(fullname.swapcase())