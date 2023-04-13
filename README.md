- 👋 Hi, I’m @Mgdj88
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Mgdj88/Mgdj88 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview linjk to take a look at your changes.
--->




import random

# Define a list of tarot cards
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
    "Judgement",
    "The World"
]

# Define a function to pick a random tarot card
def pick_card():
    return random.choice(tarot_cards)

# Main program
print("Welcome to the Pick a Tarot Card app!")
while True:
    input("Press enter to pick a card...")
    card = pick_card()
    print(f"You have picked the {card} card.")
    repeat = input("Do you want to pick another card? (y/n) ")
    if repeat.lower() != "y":
        break
```

