
'''Write a program to generate the Fibonacci sequence up to 100.'''


#Initialize the first two numbers in the sequence
a, b = 0, 1

#Print the first two numbers in the sequence
print(a)
print(b)

#Generate the rest of the sequence*
while a + b <= 100:
#Calculate the next number in the sequence
    c = a + b
#Print the next number in the sequence
    print(c)
#Update a and b for the next iteration
    a, b = b, c