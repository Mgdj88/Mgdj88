
import random

# List of Tarot card names
tarot_cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgment",
    "The World"
]

# Function to get a random tarot card
def get_random_tarot_card():
    return random.choice(tarot_cards)

# Main function to run the Daily Tarot Card app
def daily_tarot_card():
    print("Welcome to the Daily Tarot Card app!")
    print("Today's Tarot Card is: {}".format(get_random_tarot_card()))

# Run the app
if __name__ == "__main__":
    daily_tarot_card()
