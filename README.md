<!DOCTYPE html>
<html>
<head>
    <title>Pick a Tarot Card App</title>
    <style>
        /* Add any custom CSS styling here */
    </style>
</head>
<body>
    <h1>Welcome to the Pick a Tarot Card app!</h1>
    <button onclick="pickCard()">Press to Pick a Card</button>
    <p id="cardDisplay"></p>
    <button onclick="repeat()">Pick Another Card</button>

    <script>
        // Define an array of tarot cards
        const tarotCards = [
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
        ];

        // Function to pick a random tarot card
        function pickCard() {
            const cardDisplay = document.getElementById("cardDisplay");
            const randomIndex = Math.floor(Math.random() * tarotCards.length);
            const card = tarotCards[randomIndex];
            cardDisplay.textContent = `You have picked the '${card}' card.`;
        }

        // Function to pick another card
        function repeat() {
            pickCard();
        }
    </script>
</body>
</html>
