##  decks for the game to shuffle though

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11  # blackjack starts by treating Ace as 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"



class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A"]

    def __init__(self, num_decks=1):
        self.cards = []

        for _ in range(num_decks):
            for suit in self.SUITS:
                for rank in self.RANKS:
                    self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
shoe = Deck(num_decks=4)  # 4 decks shuffled together
print(len(shoe.cards))    # 208 cards
