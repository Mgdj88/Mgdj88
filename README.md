# Spades Royale Game Logic

import random

# Constants
SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
COIN_REWARD_WIN = 0.1
COIN_REWARD_LOSE = 0.01

# Initialize game state
players = 4
deck = [(rank, suit) for rank in RANKS for suit in SUITS]
random.shuffle(deck)
player_scores = [0] * players

# Game Loop
while True:
    # Deal cards to players
    player_hands = [[] for _ in range(players)]
    for i in range(len(deck)):
        player_hands[i % players].append(deck.pop())

    # Bidding phase
    bids = [0] * players
    for i in range(players):
        print("Player", i+1, "hand:", player_hands[i])
        bids[i] = int(input("Player " + str(i+1) + ", enter your bid (0-13): "))

    # Trick-taking phase
    tricks_won = [0] * players
    for _ in range(13):
        trick = []
        for i in range(players):
            card = input("Player " + str(i+1) + ", play a card from your hand: ")
            trick.append(card)
            player_hands[i].remove(card)

        # Determine trick winner
        winning_card = max(trick, key=lambda x: (RANKS.index(x[0]), SUITS.index(x[1])))
        winning_player = trick.index(winning_card)
        tricks_won[winning_player] += 1
        print("Trick won by Player", winning_player+1)

    # Update player scores and virtual currency rewards
    for i in range(players):
        if tricks_won[i] >= bids[i]:
            player_scores[i] += bids[i] + COIN_REWARD_WIN
        else:
            player_scores[i] += tricks_won[i] + COIN_REWARD_LOSE

    # End of round
    print("Round scores: ", player_scores)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Game over!")
