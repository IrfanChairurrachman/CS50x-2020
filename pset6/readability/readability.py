# I can do it more efficient
# I just want to implement my pset2 C code to python

from cs50 import get_string

# function for count letter
def count_letters(s):
    letter = 0
    for i in s:
        if i >= 'A' and i <= 'z':
            letter += 1
    return letter

# for count word
def count_words(s):
    word = 1
    for i in s:
        if i == ' ':
            word += 1
    return word

# for count sentences
def count_sentences(s):
    sentence = 0
    for i in s:
        if i == '!' or i == '.' or i == '?':
            sentence += 1
    return sentence

# Get input
text = get_string("Text: ")
# Get counting from each funtion
letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

L = (float(letters) / float(words)) * 100
S = (float(sentences) / float(words)) * 100

# calculate grade
grade = 0.0588 * L - 0.296 * S - 15.8;

# print grade
if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade", round(grade))