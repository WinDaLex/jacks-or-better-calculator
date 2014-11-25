import unittest

from Card import *

class TestCardClass(unittest.TestCase):

    def testConstruction(self):
        card = Card('spade', '4')
        self.assertEqual([card.suit, card.rank], ['spade', '4'])


if __name__ == '__main__':
    unittest.main()
