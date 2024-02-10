'''Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
'''

def capitalize_first_letter(input_string):
    return input_string.title()


user_input = input("Enter a string: ")

#Capitalize and display results
result = capitalize_first_letter(user_input)
print(result)