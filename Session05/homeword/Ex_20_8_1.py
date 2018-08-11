strings = input(" Enter a string ")
letter_counts = {}

for letter in strings:
    # print(letter)
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
    # print(letter_counts)
print(letter_counts)
