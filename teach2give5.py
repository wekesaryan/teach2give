'''Write a program that takes an integer as input and returns an integer with reversed digit 
ordering.'''


def reverse_digits(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
    return reversed_num

#Prompt the user to enter an integer
user_input = int(input("Enter an integer: "))

#Reverse the digits of the input and display the result
result = reverse_digits(user_input)
print("Reversed number:", result)
