# class Card:
#     suits = ("hearts", "diamonds", "clubs", "spades")
#     values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

#     def __init__(self, value, suit):
#         if not value in Card.values:
#             raise ValueError(f"{value} is not a value option")
#         if not suit.lower() in Card.suits:
#             raise ValueError(f"{suit} is not a suit option")
#         self.suit = suit.capitalize()
#         self.value = value

#     def __repr__(self):
#         return f"{self.value} of {self.suit}"


# class Deck:

#     def __init__(self):
#         suits = ["hearts", "diamonds", "clubs", "spades"]
#         values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#         self.cards = [Card(value, suit) for suit in suits for value in values]

#     def __repr__(self):
#         return f"Deck of {self.count()} cards"

#     def count(self):
#         return len(self.cards)

#     def shuffle(self):
#         from random import shuffle

#         if len(self.cards) < 52:
#             raise ValueError("Only full decks can be shuffled")
#         shuffle(self.cards)
#         return self.cards

#     def _deal(self, num):
#         if len(self.cards) == 0:
#             raise ValueError("All cards have been dealt")
#         elif len(self.cards) <= abs(num):
#             self.cards = []

#         else:
#             delt_cards = self.cards[-num:]
#             self.cards = self.cards[0:-num]
#             return delt_cards

#     def deal_card(self):
#         single_card = self._deal(-1)
#         return single_card[0]

#     def deal_hand(self, num):
#         delt_hand = self._deal(num)
#         return delt_hand


# # deck_1 = Deck()
# # print(deck_1.shuffle())
# # num = -1
# print(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][0:5])


class Card:
    suits = ("hearts", "diamonds", "clubs", "spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, value, suit):
        if not value in Card.values:
            raise ValueError(f"{value} is not a value option")
        if not suit.lower() in Card.suits:
            raise ValueError(f"{suit} is not a suit option")
        self.suit = suit.capitalize()
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit.capitalize()}"


class Deck:

    def __init__(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def shuffle(self):
        from random import shuffle

        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        single_card = self._deal(1)
        return single_card[0]

    def deal_hand(self, num):
        delt_hand = self._deal(num)
        return delt_hand
