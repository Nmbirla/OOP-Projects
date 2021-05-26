import random

class Card:
    # Choose card_value from 1 for A to 13 for K
    # Choose suit: 0:♥,  1:♦, 2:♣, 3:♠
    def __init__(self, card_value, suit):
        self.points = card_value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][card_value -1]
        self.suit = '♥♦♣♠'[suit]

    # Display card same as physical card from a deck
    # This is just for better visualization
    def show(self):
        print('┌─────┐')
        print(f'|{self.value:<2}   |')
        print(f'|  {self.suit}  |')
        print(f'|   {self.value:>2}|')
        print('└─────┘')

    # Function return points associated with card as per the blackjack rules
    # A can have 1 or 11 points
    # Cards 2 to 10 has points
    # J, Q and K has 10 points

    def Card_points(self):
        if self.points >= 10:
            return 10
        elif self.points == 1:
            return 11
        return self.points
'''
card1 = Card(1, 1)
card2 = Card(4, 2)
card1.show()
print(card1.Card_points())
card2.show()
print(card2.Card_points())
'''

class Deck:
    # deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 6

    def __init__(self, num_of_decks = 1):
        self.cards = []
        self.num_of_decks = num_of_decks

    def generate(self,num_of_decks):
        while self.num_of_decks!= 0:
            for i in range(1, 14):
                for j in range(4):
                    self.cards.append(Card(i, j))
            self.num_of_decks -= 1
        return self.cards

    def draw(self, num_of_cards):
        card = []
        for i in range(num_of_cards):
            if len(self.cards) < 52:
                random.shuffle(self.cards)
            tcard = random.choice(self.cards)
            self.cards.remove(tcard)
            card.append(tcard)
        return card


