# A program to Count Number of Vowels in the Given Sentence
Sentence = input("Enter a sentence: ")
# Initialize a counter for vowels
count = 0
# Iterate through each character in the sentence
for char in Sentence:
    # Check if the character is a vowel
    if char.lower() in 'aeiouAEIOU':
        count += 1
# Print the number of vowels
print("Number of vowels:", count)
