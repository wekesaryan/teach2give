''' a program that counts the number of vowels in a sentence.
'''

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

#Prompt the user to enter a sentence*
user_input = input("Enter a sentence: ")

#Count the number of vowels in the input sentence and display the result*
result = count_vowels(user_input)
print("Number of vowels:", result)