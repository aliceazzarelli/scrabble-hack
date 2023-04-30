# Assign values to letters
import json
with open('scrabble_values.json') as json_file:
    scrabble_data = json.load(json_file)
# Function that takes in words and calculates value
test_word = "butter"

def get_word_value(word):
    score = 0
    for letter in word :
        assert letter in scrabble_data.keys()
        value = scrabble_data[letter]
        score += value
    return score

test_score = get_word_value(test_word)
print(test_score)