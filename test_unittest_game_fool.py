import unittest
from game_fool import Deck

class TestDeck_unittest(unittest.TestCase):

    def setup(self):
        self.deck = Deck()
        print('Start test')

    def tearDown(self):
        print('Test completed')
        del self.deck

    def test_init(self):
        self.assertEqual(len(self.deck._suits), 4)
        self.assertEqual(len(self.deck._cards), 9)
        self.assertFalse(len(self.deck._suits) < 4)

    def test_mix_deck(self):
        self.assertEqual(len(self.deck._mixed_deck), 36)

    def test_hand_cards(self):
        self.deck.hand_cards()
        self.deck._comp_hand()
        self.assertEqual(len(self.deck.player_hand), 6)
        self.assertTrue((len(self.deck.player_hand) == 6) and (len(self.deck._comp_hand) == 6))


