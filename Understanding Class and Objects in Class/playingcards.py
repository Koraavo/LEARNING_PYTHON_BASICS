import random


class Card():
    def __init__(self, name, value, suit):
        self.name = name
        self.suit = suit
        self.value = value
        self.showing = False

    def __repr__(self):
        if self.showing:
            return str(self.name) + " of " + str(self.suit)
        else:
            return "Card"


class StandardDeck(list):

    def __init__(self):
        super().__init__()
        self.cards = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = {"Ace": 1,
                  "Two": 2,
                  "Three": 3,
                  "Four": 4,
                  "Five": 5,
                  "Six": 6,
                  "Seven": 7,
                  "Eight": 8,
                  "Nine": 9,
                  "Ten": 10,
                  "Jack": 11,
                  "Queen": 12,
                  "King": 13}

        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    def __repr__(self):
        return f"Standard Deck of {len(self.cards)} cards"

    def shuffle(self):
        random.shuffle(self.cards)
        print("Cards shuffled")

    def deal(self):
        return self.cards.pop(0)



deck = StandardDeck()
deck.shuffle()
print(deck.cards)
print(deck)
