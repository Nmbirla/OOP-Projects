from Deck import Deck
from Deck import Card
from Player import Player
from ReadStrategy import *

class BlackjackS2:
    def __init__(self, num_of_decks):
        self.deck = Deck(num_of_decks)
        self.deck.generate(num_of_decks)
        self.dealer = Player(True, self.deck)
        self.player = Player(False, self.deck)
        self.hard_total_status = []
        self.soft_total_status = []


    def BlackJack_GameS2(self):
        player_cards = []
        for i in range(2):
            player_initialsum = self.player.deal()
            player_cards.append(self.player.deal())
            dealer_initialsum = self.dealer.deal()
            if i == 0:
                dfaceupcardval = dealer_initialsum

        soft_strategy = False
        if (player_cards[0] == 11 and player_cards[1] != 11) or (player_cards[0] != 11 and player_cards[1] == 11):
            soft_strategy = True
        else:
            return

        # self.player.show()
        # self.dealer.show()

        if player_initialsum == 21:
            if dealer_initialsum == 21:
                print("Dealer Won")
                if player_initialsum == 21:
                    print("Tie")
                return 1
        if soft_strategy == 'True':
            BlackjackS2.HardTotal(player_initialsum, dfaceupcardval)
            BlackjackS2.SoftTotal(player_initialsum, dfaceupcardval)
        return self.hard_total_status, self.soft_total_status

    # Game 1: Hard Total
    player_input = ""

    def HardTotal(self, player_initialsum, dfaceupcardval):
        while player_input != "stand":
            result = 0
            # print(player_initialsum, dfaceupcardval)
            player_input = ReadStrategy.getStrategy(player_initialsum, dfaceupcardval)
            if player_input == 'hit':
                result = self.player.hit()
                # self.player.show()
            if result == 1:
                # print("player busted")
                return self.hard_total_status.append("Dealer Won")

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                # self.dealer.show()
                print("Dealer busted")
            return self.hard_total_status.append("Player Won")
            # self.dealer.show()
        # self.player.show()
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

    # Game 2: Soft Total
    def SoftTotal(self, player_initialsum, dfaceupcardval):
        while player_input != "stand":
            result = 0
            # print(player_initialsum, dfaceupcardval)
            player_input = ReadStrategy.getSoftStrategy(player_initialsum, dfaceupcardval)
            if player_input == 'hit':
                result = self.player.hit()
                # self.player.show()
            if result == 1:
                # print("player busted")
                return self.soft_total_status.append("Dealer Won")

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                # self.dealer.show()
                print("Dealer busted")
            return self.soft_total_status.append("Player Won")
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