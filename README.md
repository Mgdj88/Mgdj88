import random

# Constants
RANKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
SUITS = ['C', 'D', 'H', 'S']
TRUMP_SUITS = ['M', 'O']
PLAYERS = ['Player 1', 'Player 2', 'Player 3', 'Player 4']

# Deck of cards
DECK = [rank + suit for suit in SUITS for rank in RANKS] + [rank + trump for trump in TRUMP_SUITS for rank in RANKS]

# Game state
player_hands = {player: [] for player in PLAYERS}
trick = []
trump_suit = None

def deal_cards():
    """Deal cards to players."""
    random.shuffle(DECK)
    for i in range(len(DECK)):
        player_hands[PLAYERS[i % len(PLAYERS)]].append(DECK[i])

def play_trick(leading_player):
    """Play a trick."""
    trick.clear()
    for i in range(len(PLAYERS)):
        player = PLAYERS[(PLAYERS.index(leading_player) + i) % len(PLAYERS)]
        card = get_played_card(player)
        trick.append(card)

def get_played_card(player):
    """Get the card played by a player."""
    valid_cards = get_valid_cards(player)
    print(f"{player}, it's your turn to play. Valid cards: {valid_cards}")
    while True:
        card = input("Enter card (e.g. '2C' for 2 of Clubs): ").upper()
        if card in valid_cards:
            player_hands[player].remove(card)
            return card
        else:
            print("Invalid card. Please choose a valid card.")

def get_valid_cards(player):
    """Get the valid cards that a player can play."""
    valid_cards = []
    if not trick:
        valid_cards = player_hands[player]
    else:
        leading_suit = trick[0][1]
        has_suit = any(card[1] == leading_suit for card in player_hands[player])
        if has_suit:
            valid_cards = [card for card in player_hands[player] if card[1] == leading_suit]
        else:
            valid_cards = player_hands[player]
    return valid_cards

def determine_trick_winner():
    """Determine the winner of a trick."""
    leading_suit = trick[0][1]
    highest_card = None
    winning_player = None
    for card in trick:
        if card[1] == leading_suit and (highest_card is None or card > highest_card):
            highest_card = card
            winning_player = PLAYERS[trick.index(card)]
    return winning_player

def play_game():
    """Play a game of Spades with tarot cards."""
    print("Welcome to Spades with Tarot cards!")
    deal_cards()
    print("Cards have been dealt.")
    print("Trump suit is determined by the highest ranking Major Arcana card in your hand.")
    trump_suit = determine_trump_suit()
    print(f"Trump suit is: {trump_suit}")

    leading_player = PLAYERS[0]
    while len(player_hands[leading_player]) > 0:
        play_trick(leading_player)
        trick_winner = determine_trick_winner()
        print(f"{trick_winner}
