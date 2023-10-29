from spellchecker import SpellChecker

# Example text with spaces in words
text = "tur ning and twist ing are fun acti vities."

# Initialize the spellchecker
spell = SpellChecker()

# Split the text into words
words = text.split()

# Correct any misspelled words
for i in range(len(words)):
    if spell.unknown([words[i]]):
        corrected_word = spell.correction(words[i])
        words[i] = corrected_word

# Join the words to form a sentence
normalized_text = ' '.join(words)

# Print the modified text
print(normalized_text)
