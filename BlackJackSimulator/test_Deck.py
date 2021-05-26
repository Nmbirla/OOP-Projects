from unittest import TestCase
from Deck import Card


class TestCard(TestCase):
    def test_show(self):
        # case 1
        # arrange
        expected_card = print('┌─────┐ \n' + f'|{10}   |\n' + f'|  ♥  |\n' + f'|   {10}|\n' + '└─────┘')
        # act
        card1 = Card(10, 0)
        card_look = card1.show()
        # assert
        self.assertEqual(expected_card, card_look)

        # # case 2
        # # arrange
        # expected_card = print('┌─────┐ \n' + f'|{K}   |\n' + f'|  ♥  |\n' + f'|   {K}|\n' + '└─────┘')
        # # act
        # card1 = Card(14, 0)
        # card_look = card1.show()
        # # assert
        # self.assertEqual(expected_card, card_look)

    def test_card_points(self):
        # General Cards
        # arrange
        expected_card1_value = 10
        # act
        card2 = Card(10, 1)
        actual_card1_value = card2.Card_points()
        # assert
        self.assertEqual(expected_card1_value, actual_card1_value)

        # Tested Ace card
        # arrange
        expected_card2_value = 11

        # act
        card2 = Card(1, 3)
        actual_card2_value = card2.Card_points()

        # assert
        self.assertEqual(expected_card2_value, actual_card2_value)


class TestDeck(TestCase):
    def test_generate(self):
        # arrange
        deck_count = 4
        while deck_count != 0:
            expected_deck = []
            for i in range(4):
                for j in range(14):
                    expected_deck.append(Card(j, i))
            deck_count -= 1
        return expected_deck

        # act

        actual_deck = Deck(4)
        actual_deck.generate()

        # assert
        self.assertEqual(expected_deck, actual_deck)

    def test_draw(self):
        self.fail()
