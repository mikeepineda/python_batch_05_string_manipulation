# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

# ask for user's input
statement = input("Enter a statement: ")

# splits the statement into words and  counts the number of words in the list
word_count = len(statement.split())

# print
print (word_count)