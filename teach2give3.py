'''Write a program that takes an integer as input and returns true if the input is a power of two.'''


def isPowerOfTwo(n):
    return n != 0 and (n & (n - 1)) == 0

#Prompt the user to enter an integer
user_input = int(input("Enter an integer: "))

#Check if the input is a power of 2 and display the result
print(isPowerOfTwo(user_input))