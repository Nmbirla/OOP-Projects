from Deck import Deck
from Deck import Card
from Player import Player
from ReadStrategy import *

class Blackjack:
    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
        self.deck.generate(num_of_decks)
        self.dealer = Player(True, self.deck)
        self.player = Player(False, self.deck)

    # def play(self):
    #     player_status = self.player.deal()
    #     dealer_status = self.dealer.deal()
    #
    #     self.player.show()
    #
    #     if player_status == 1:

    def BlackJack_Game(self):
        for i in range(2):
            player_initialsum = self.player.deal()
            dealer_initialsum = self.dealer.deal()
            if i == 0:
                dfaceupcardval = dealer_initialsum

        # self.player.show()
        # self.dealer.show()

        if player_initialsum == 21:
             if dealer_initialsum == 21:
                print("Dealer Won")
                if player_initialsum == 21:
                    print("Tie")
                return 1
        player_input = ""

        while player_input != "stand":
            result = 0
            # print(player_initialsum, dfaceupcardval)
            player_input = ReadStrategy.getStrategy(player_initialsum, dfaceupcardval)
            if player_input == 'hit':
                result = self.player.hit()
                # self.player.show()
            if result == 1:
                # print("player busted")
                return "Dealer Won"

        # self.player.show()
        
        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                # self.dealer.show()
                print("Dealer busted")
            return "Player Won"
            # self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            final_result = "Tie"
            print("Tie")
        elif self.dealer.check_score() < self.player.check_score():
            final_result = "Player Won"
            print("Player Won")
        else:
            final_result = "Dealer Won"
            print("Dealer Won")
        return final_result