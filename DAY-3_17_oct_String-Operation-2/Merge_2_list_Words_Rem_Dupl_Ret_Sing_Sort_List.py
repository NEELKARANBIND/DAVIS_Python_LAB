 A program to merge two lists of words, remove duplicates, and return a  single sorted list
list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "date", "fig", "apple"]
# Merge the two lists
merged_list = list1 + list2
# Remove duplicates while keeping order
unique_words = []
for w in merged_list:
    if w not in unique_words:
        unique_words.append(w)
# Sort the final list
unique_words.sort()
# Print the result
print("Merged and sorted list of unique words:", unique_words)
