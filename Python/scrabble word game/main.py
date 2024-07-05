scores = {}
dictionary = []
tiles = []
import random

with open("scores.txt", "r") as f:
    for line in f:
        line = line.strip()
        key, val = line.split(None, 1)
        scores[key] = val.split()
        #scores.append(line)
print("SCORES:" , scores)

with open("tiles.txt", "r") as f:
    for line in f:
        line = line.strip()
        tiles.append(line)
        random.shuffle(tiles)
    left_tiles = tiles[:7]
print("TILES: ", left_tiles)

with open("dictionary.txt", "r") as f:
    for line in f:
        line = line.strip()
        dictionary.append(line)
print("DIC:", dictionary)

def getLetterScore(letter):
    # Check if the input is a string with a single character
    if not isinstance(letter, str) or len(letter) != 1:
        # Return 0 if the input is invalid
        return 0
    letter == letter.upper()

    if letter in scores:
        print("letter score is ", scores[letter])
    else:
        return 0

def getWordScore(word):
    total = 0
    for letter in word:
        try:
            total += getLetterScore(letter)
        except KeyError:
            return 0
    return total

def canBeMade(word, tiles):
    left_tiles = tiles[:7]
    left_tiles_copy = left_tiles.copy()
    for letter in word:
        if letter in left_tiles:
            left_tiles_copy.remove(letter)
        else:
            return False

    return True

def onlyEnglishLetters(word):
    if not isinstance(word, str) or word != word.upper():
        return False
    for letter in word:
        if not letter.isalpha():
            return False
    return True

def is_valid(word, tiles, dictionary):
    if not type(dictionary) == list :
        return False

    # rule number 1
    if not word in dictionary:
        print("Not in the dictionary")
        return False

    # rule number 2
    if not onlyEnglishLetters(word):
        print("Only English")
        return False

    # rule number 3
    if not canBeMade(word,tiles):
        print("Cant be made")
        return False

    # valid
    return True

while True:
    word = input("please input a word or &&& to quit")
    if word == "&&&":
        print("game terminated")
        break
    elif getWordScore(word):
        break
    else:
        print("please input a word using the tiles")
