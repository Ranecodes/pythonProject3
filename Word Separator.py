word = "ILoveYouRaneh"
new_word = ' '
for letters in word:
    if letters.isupper():
        new_word += ' '

    new_word += letters
new1_word = new_word.strip()
new1_word_capitalize = new1_word.capitalize()
print(new1_word_capitalize)