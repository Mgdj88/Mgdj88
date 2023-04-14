import tkinter as tk
import random

# Define an array of tarot cards
tarotCards = [
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

# Function to pick a random tarot card
def pick_card():
    card_display.config(text=random.choice(tarotCards))

# Create the main window
root = tk.Tk()
root.title("Pick a Tarot Card App")

# Create a label for card display
card_display = tk.Label(root, text="", wraplength=300, font=("Arial", 16), justify="center")
card_display.pack(pady=20)

# Create a "Pick a Card" button
pick_button = tk.Button(root, text="Press to Pick a Card", command=pick_card)
pick_button.pack()

# Create a "Pick Another Card" button
repeat_button = tk.Button(root, text="Pick Another Card", command=pick_card)
repeat_button.pack(pady=10)

root.mainloop()
