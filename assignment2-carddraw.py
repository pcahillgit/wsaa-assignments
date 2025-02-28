# This is a Python program that interacts with the Deck of Cards API to shuffle a deck, draw 5 cards and print their values and suits.
# It then check for pairs, triples, straights or all of the same suit and indicates if any of these conditions have been met.
# Author: Paul Cahill

import requests
from collections import Counter

# Shuffling the deck from the deck of cards API
deck_id = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()["deck_id"]

# Drawing 5 cards
cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5").json()["cards"]

# Dictionary for face card values
card_values = {"ACE": 1, "JACK": 11, "QUEEN": 12, "KING": 13}

# Extracting the values and suits from the drawn cards and printing
values = [card_values.get(card["value"], int(card["value"])) for card in cards]  
suits = [card["suit"] for card in cards]

for card in cards:
    print(f"{card['value']} of {card['suit']}")

# Counting occurrences
value_counts = Counter(values)
suit_counts = Counter(suits)

if 4 in value_counts.values():
    print("... Wow, four of a kind!")
elif 3 in value_counts.values():
    print("... Nice, a triple!")
elif 2 in value_counts.values():
    print("... You got a pair!")

# Straight
sorted_values = sorted(values)
if sorted_values == list(range(sorted_values[0], sorted_values[0] + 5)):
    print("... That's a straight!")

# Flush
if max(suit_counts.values()) == 5:
    print("... Wow, you got a flush!")

# References:
# Deck of Cards API: https://deckofcardsapi.com/
# W3 Schools guide to the requests module: https://www.w3schools.com/python/module_requests.asp
# W3 Schools guide to if elif statements: https://www.w3schools.com/python/gloss_python_elif.asp#:~:text=The%20elif%20keyword%20is%20pythons,%2C%20then%20try%20this%20condition%22.
# Stack Overflow thread on giving values to face cards: https://stackoverflow.com/questions/70676067/making-card-game-how-do-i-give-the-face-cards-value
# Stack Overflow thread on identifying poker hands in Python: https://stackoverflow.com/questions/56874468/identifying-straight-flush-and-other-categories-from-poker-using-python