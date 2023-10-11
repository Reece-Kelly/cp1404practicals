"""
Word Occurrences
Estimate: 30 minutes
Actual: 32 minutes
"""

string = input("String: ")
words = string.split(" ")
words.sort()
word_to_count = {word: (words.count(word)) for word in words}
max_length = len(max(words))
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
