# A Program to Count Number of Uppercase Characters in the Given Sentence
Sentence = input("Enter a sentence: ")
# Initialize a counter for uppercase characters
count = 0
# Iterate through each character in the sentence
for char in Sentence:
    # Check if the character is uppercase
    if char.isupper():
        count += 1
        #Print the number of uppercase characters
print("Number of uppercase characters:", count)
