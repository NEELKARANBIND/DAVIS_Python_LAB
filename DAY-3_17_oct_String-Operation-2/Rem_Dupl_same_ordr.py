# A program to Remove Duplicates words while Maintaining same  Order from a given sentence
'''
Sentence = input("Enter a sentence: ")
# Split the sentence into words
words = Sentence.split()
# Create a list to store unique words
unique_words = []
# Iterate through each word in the original order
for word in words:
    # If the word is not already in the unique_words list, add it
    if word not in unique_words:
        unique_words.append(word)
# Join the unique words back into a sentence
result = ' '.join(unique_words)
# Print the result
print("Sentence after removing duplicates:", result)

'''
sentence = input("Enter a sentence: ")

word = ""
words = []
unique_words = []
result = ""

# Manually split the sentence into words (without using split)
for ch in sentence:
    if ch == " ":
        if word != "":
            words.append(word)
            word = ""
    else:
        word += ch

# Add the last word if it exists
if word != "":
    words.append(word)

# Remove duplicates while keeping order
for w in words:
    if w not in unique_words:
        unique_words.append(w)

# Manually join the words (without using join)
for i in range(len(unique_words)):
    result += unique_words[i]
    if i != len(unique_words) - 1:
        result += " "
# Print the result
print("Sentence after removing duplicates:", result)
