# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# ask for user's input
number = int(input("Enter a number from 0-1000: "))

# formats the number as a 6-digit string
formatted_number = f"{number:06d}"

# print input
print(formatted_number)
