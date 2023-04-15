<!DOCTYPE html>
<html>
<head>
    <title>Pick a Tarot Card App</title>
    <style>
        /* CSS for tarot card app */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            text-align: center;
        }

        h1 {
            color: #333;
            margin-top: 40px;
        }

        button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            margin-top: 20px;
            transition: background-color 0.3s ease-in-out;
        }

        button:hover {
            background-color: #0056b3;
        }

        #cardDisplay {
            margin-top: 40px;
            font-size: 24px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .cardImage {
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Pick a Tarot Card app!</h1>
    <button onclick="pickCard()">Press to Pick a Card</button>
    <button onclick="pickCard()">Pick Another Card</button>
    <div id="cardDisplay">
        <img src="" alt="Tarot Card Image" class="cardImage" id="cardImage">
        <p id="cardDescription"></p>
    </div>

    <script>
        // Define an array of tarot cards with images
        const tarotCards = [
            {
                name: "The Fool",
                description: "Represents spontaneity, new beginnings, and taking risks.",
                image: "https://example.com/images/fool.jpg"
            },
            {
                name: "The Magician",
                description: "Symbolizes creativity, power, and manifestation.",
                image: "https://example.com/images/magician.jpg"
            },
            // Add more tarot cards with their descriptions and image URLs
        ];

        // Function to pick a random tarot card
        function pickCard() {
            const cardDisplay = document.getElementById("cardDisplay");
            const cardImage = document.getElementById("cardImage");
            const cardDescription = document.getElementById("cardDescription");
            const randomIndex = Math.floor(Math.random() * tarotCards.length);
            const card = tarotCards[randomIndex];
            cardImage.src = card.image;
            cardImage.alt = card.name;
            cardDescription.textContent = card.description;
        }
    </script>
</body>
</html>
