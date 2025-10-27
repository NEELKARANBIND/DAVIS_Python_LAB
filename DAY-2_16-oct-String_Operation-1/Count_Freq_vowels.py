# A program to Count Frequency of Vowels in the Given Sentence
Sentence = input("Enter a sentence: ")
# Initialize a dictionary to store frequency of each vowel
vowel_freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A':0, 'E':0,'I':0,'O':0,'U':0}
# Iterate through each character in the sentence
for char in Sentence:
    # Check if the character is a vowel
    if char in vowel_freq:
        vowel_freq[char] += 1
# Print the frequency of each vowel
print("Frequency of vowels:")
for vowel, freq in vowel_freq.items():
    print(f"{vowel}: {freq}")
