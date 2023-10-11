"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

string = input("String: ")
words = string.split(" ")
words.sort()
word_to_count = {word: (words.count(word)) for word in words}
print(word_to_count)
