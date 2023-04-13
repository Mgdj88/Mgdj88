import random

# Define a list of tarot cards
tarot_cards = [
    "The Fool: Represents spontaneity, new beginnings, and taking risks.",
    "The Magician: Symbolizes creativity, power, and manifestation.",
    "The High Priestess: Represents intuition, mystery, and the subconscious mind.",
    "The Empress: Symbolizes fertility, nurturing, and abundance.",
    "The Emperor: Represents authority, stability, and leadership.",
    "The Hierophant: Symbolizes tradition, spirituality, and guidance from higher powers.",
    "The Lovers: Represents romantic relationships, partnerships, and deep connections.",
    "The Chariot: Symbolizes determination, drive, and overcoming obstacles.",
    "Strength: Represents inner strength, courage, and perseverance.",
    "The Hermit: Symbolizes introspection, solitude, and inner guidance.",
    "Wheel of Fortune: Represents cycles, luck, and destiny.",
    "Justice: Symbolizes fairness, balance, and moral integrity.",
    "The Hanged Man: Represents surrender, letting go, and seeing things from a different perspective.",
    "Death: Symbolizes transformation, change, and new beginnings.",
    "Temperance: Represents balance, harmony, and moderation.",
    "The Devil: Symbolizes temptation, materialism, and bondage.",
    "The Tower: Represents sudden upheaval, change, and chaos.",
    "The Star: Symbolizes hope, inspiration, and spirituality.",
    "The Moon: Represents intuition, emotions, and the subconscious mind.",
    "The Sun: Symbolizes vitality, joy, and success.",
    "Judgment: Represents rebirth, renewal, and taking responsibility for one's actions.",
    "The World: Symbolizes completion, wholeness, and fulfillment."
]

# Define a function to pick a random tarot card
def pick_card():
    return random.choice(tarot_cards)

# Main program
print("Welcome to the Pick a Tarot Card app!")
while True:
    input("Press enter to pick a card...")
    card = pick_card()
    print(f"You have picked the '{card}' card.")
    repeat = input("Do you want to pick another card? (y/n) ")
    if repeat.lower() != "y":
        break
