

def checkWords(words,letter):
    new_words = []
    for word in words:
        if word.lower()[0:1] == letter:
            new_words.append(word)

    return new_words

def getLetter():
    letter = input("Enter a letter:")

    if len(letter) > 1:
        letter = letter[0:1]
    
    return letter

def seperateSentence(string):
    word = ''
    words = []
    for character in string:
        if character != " " and character.isalpha():
            word += character
        else:
            words.append(word)
            word = ''

    return words

string = input("Enter a sentence (or even an essay):\n")
words_in_sen = seperateSentence(string)
print()
letter = getLetter()

words_of_letter = checkWords(words_in_sen,letter)

print(f"Here are the words in your sentence that start with {letter}:\n{words_of_letter}")
            
# list = seperateSentence("Wow this is a great function")

# print(list)

# let = getLetter()

# print(let)

# letter_of_words = checkWords(["This","That","maybe","thor"],"t")
# print(letter_of_words)

# word = "Among Us"
# print(word[0:2])