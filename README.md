import random

# Define a dictionary of tarot cards with their meanings
tarot_cards = {
    "The Fool": "Represents spontaneity, new beginnings, and taking risks.",
    "The Magician": "Symbolizes creativity, power, and manifestation.",
    "The High Priestess": "Represents intuition, mystery, and the subconscious mind.",
    "The Empress": "Symbolizes fertility, nurturing, and abundance.",
    "The Emperor": "Represents authority, stability, and leadership.",
    "The Hierophant": "Symbolizes tradition, spirituality, and guidance from higher powers.",
    "The Lovers": "Represents romantic relationships, partnerships, and deep connections.",
    "The Chariot": "Symbolizes determination, drive, and overcoming obstacles.",
    "Strength": "Represents inner strength, courage, and perseverance.",
    "The Hermit": "Symbolizes introspection, solitude, and inner guidance.",
    "Wheel of Fortune": "Represents cycles, luck, and destiny.",
    "Justice": "Symbolizes fairness, balance, and moral integrity.",
    "The Hanged Man": "Represents surrender, letting go, and seeing things from a different perspective.",
    "Death": "Symbolizes transformation, change, and new beginnings.",
    "Temperance": "Represents balance, harmony, and moderation.",
    "The Devil": "Symbolizes temptation, materialism, and bondage.",
    "The Tower": "Represents sudden upheaval, change, and chaos.",
    "The Star": "Symbolizes hope, inspiration, and spirituality.",
    "The Moon": "Represents intuition, emotions, and the subconscious mind.",
    "The Sun": "Symbolizes vitality, joy, and success.",
    "Judgment": "Represents rebirth, renewal, and taking responsibility for one's actions.",
    "The World": "Symbolizes completion, wholeness, and fulfillment."
}

# Function to pick a random tarot card
def pick_card():
    card = random.choice(list(tarot_cards.keys()))
    meaning = tarot_cards[card]
    return card, meaning

# Game loop
while True:
    print("Welcome to the Tarot Card Picking Game!")
    print("Press 'p' to pick a card or 'q' to quit.")
    choice = input("Enter your choice: ")
    if choice == 'p':
        card, meaning = pick_card()
        print("You picked the card:", card)
        print("Meaning:", meaning)
    elif choice == 'q':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
