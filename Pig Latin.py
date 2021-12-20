word = input("Input a sentence")
word_capital = word.upper()
word1 = word_capital.split()
new_word = ' '
for letters in word1:
    if len(letters) < 1:
        letters2 = letters + 'AY'
        new_word += letters2
    else:
        letters1 = letters[1:] + letters[0]
        pig_latin = letters1 + 'AY'
        new_word += pig_latin + ' '
print(new_word)