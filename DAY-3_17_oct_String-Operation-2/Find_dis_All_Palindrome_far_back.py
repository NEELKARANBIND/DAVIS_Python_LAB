# A program to Find or display all Palindromes in a given sentence same farward or backward
sentence = input("Enter a sentence: ")
word = ""
words = []
palindromes = []
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
# Find palindromes
for w in words:
    if w == w[::-1]:  # Check if the word is the same forwards and backwards
        palindromes.append(w)
# Manually join the palindrome words (without using join)
for i in range(len(palindromes)):
    result += palindromes[i]
    if i != len(palindromes) - 1:
        result += " "
# Print the result
print("Palindromes in the sentence are:", result)
