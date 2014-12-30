# -*- coding: utf-8 -*-

import unittest

from Card import *


class TestCardClass(unittest.TestCase):

    def test__init__(self):
        card = Card('S', 'T')
        self.assertEqual([card.suit, card.rank], ['S', 'T'])
        with self.assertRaises(ValueError):
            card = Card('invalid_suit', '4')
        with self.assertRaises(ValueError):
            card = Card('C', '1')

    def test__str__(self):
        self.assertEqual(Card('C', 'K').__str__(), '♣K')
 
class TestHandClass(unittest.TestCase):

    def testConstruction(self):
        with self.assertRaises(ValueError): Hand('AC, AH, AS, AD')
        with self.assertRaises(ValueError): Hand([Card('C', 'A')])
        with self.assertRaises(ValueError): Hand([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError): Hand(1)
        Hand([Card('C', 'K'), Card('H', 'J'), Card('S', 'T'), Card('S', '3'), Card('C', '5')])
        Hand('KC, JH, TS, 3S, 5C')

    def test__getitem__(self):
        hand = Hand('KC, JH, TS, 3S, 5C')
        self.assertEquals(hand[0], Card('C', 'K'))
        self.assertEquals(hand[1], Card('H', 'J'))
        self.assertEquals(hand[2], Card('S', 'T'))
        self.assertEquals(hand[3], Card('S', '3'))
        self.assertEquals(hand[4], Card('C', '5'))

    def test__eq__(self):
        hand = Hand('KC, JH, TS, 3S, 5C')
        self.assertEquals(hand, hand)

    def testDividedBy(self):
        hand = Hand('KC, JH, JS, 5S, 5C')
        self.assertEquals(hand.dividedBySuit(), {'S': 2, 'H': 1, 'C': 2})
        self.assertEquals(hand.dividedByRank(), {'5': 2, 'J': 2, 'K': 1})
        

if __name__ == '__main__':
    unittest.main()
