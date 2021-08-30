#letter_game

# initialize letter and point lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# create dictionary from lists "letters" and "points"
letters_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}


# amend dictionary "letters_to_points" to add zero points if no letter is played
letters_to_points[" "] = 0


# word point counting function
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter, 0)
    return point_total


# created second dictionary "player_to_words"
player_to_words = {
    "player1": ["YELLOW", "HAT", "CORNCOB"],
    "wordNerd": ["WATER", "FELINE", "COBRA"],
    "Lexi Con": ["SPINSTER", "ZERO", "FINICKY"],
    "Prof Reader": ["STAIRWELL", "CAMPER", "WATERFALL"]
}

# create empty dictionary
player_to_points = {}


# create for-loop to tally points for each player based on words played in dict player_to_words
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points


print(player_to_points)








