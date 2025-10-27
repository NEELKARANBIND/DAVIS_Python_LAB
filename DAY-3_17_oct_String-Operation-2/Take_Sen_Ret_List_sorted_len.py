# A program to take a sentence and return a list of all words sorted by their length
sentence = input("Enter a sentence: ")
word = ""
words = []
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
# Sort words by length
words.sort(key=len)
# Print the result
print("Words sorted by length:", words)
