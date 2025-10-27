# A program to Count Special Characters in the Given Sentence
Sentence = input("Enter a sentence: ")
# Initialize a counter for special characters
count = 0
# Iterate through each character in the sentence
for char in Sentence:
    # Check if the character is a special character
    if not char.isalnum() and not char.isspace():
        count += 1
# Print the number of special characters
print("Number of special characters:", count)