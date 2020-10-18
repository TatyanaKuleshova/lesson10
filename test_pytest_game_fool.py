import pytest
from game_fool import Deck

class TestDeck_pytest:

    def setup(self):
        self.deck = Deck()
        print('Start test')

    def tearDown(self):
        print('Test completed')

    def test_init(self):
        assert len(self.deck._suits) == 4
        assert len(self.deck._cards) == 9

    def test_mix_deck(self):
        assert len(self.deck._mixed_deck) == 36

    def test_hand_cards(self):
        self.deck.hand_cards()
        self.deck._comp_hand()
        assert len(self.deck.player_hand) == 6
        assert len(self.deck.player_hand) == len(self.deck._comp_hand)




