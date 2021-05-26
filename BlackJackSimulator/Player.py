from Deck import *


class Player:
    def __init__(self, is_Dealer, deck):
        self.cards = []
        self.is_Dealer = is_Dealer
        self.deck = deck
        self.score = 0

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        return self.score

    def check_score(self):
        count = 0
        self.score = 0
        for card in self.cards:
            if card.Card_points() == 11:
                count += 1
            self.score += card.Card_points()
        while count !=0 and self.score > 21:
            count -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.is_Dealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")
        for i in self.cards:
            i.show()
        print("Score:" + str(self.score))
