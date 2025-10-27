# A program to reverse the words in a sentence while keeping the original order
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
# Reverse the words
reversed_words = []
for w in words:
    reversed_words.insert(0, w)
# Manually join the reversed words (without using join)
result = ""
for i in range(len(reversed_words)):
    result += reversed_words[i]
    if i != len(reversed_words) - 1:
        result += " "
# Print the result
print("Sentence after reversing words:", result)
