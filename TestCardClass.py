# -*- coding: utf-8 -*-

import unittest

from Card import *


class TestCardClass(unittest.TestCase):

    def test__init__(self):
        card = Card('spade', '10')
        self.assertEqual([card.suit, card.rank], ['spade', '10'])
        with self.assertRaises(ValueError):
            card = Card('invalid_suit', '4')
        with self.assertRaises(ValueError):
            card = Card('club', '1')

    def test__str__(self):
        self.assertEqual(Card('club', 'K').__str__(), '♣K')
 
class TestHandClass(unittest.TestCase):

    def testConstruction(self):
        with self.assertRaises(ValueError): Hand('club A, heart A, spade A, diamond A')
        with self.assertRaises(ValueError): Hand([Card('club', 'A')])
        with self.assertRaises(ValueError): Hand([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError): Hand(1)
        Hand([Card('club', 'K'), Card('heart', 'J'), Card('spade', '10'), Card('spade', '3'), Card('club', '5')])
        Hand('club K, heart J, spade 10, spade 3, club 5')

    def test__getitem__(self):
        hand = Hand('club K, heart J, spade 10, spade 3, club 5')
        self.assertEquals(hand[0], Card('club', 'K'))
        self.assertEquals(hand[1], Card('heart', 'J'))
        self.assertEquals(hand[2], Card('spade', '10'))
        self.assertEquals(hand[3], Card('spade', '3'))
        self.assertEquals(hand[4], Card('club', '5'))

    def test__eq__(self):
        hand = Hand('club K, heart J, spade 10, spade 3, club 5')
        self.assertEquals(hand, hand)

    def testDividedBy(self):
        hand = Hand('club K, heart J, spade J, spade 5, club 5')
        self.assertEquals(hand.dividedBySuit(), {'spade': 2, 'heart': 1, 'club': 2})
        self.assertEquals(hand.dividedByRank(), {'5': 2, 'J': 2, 'K': 1})
        

if __name__ == '__main__':
    unittest.main()
