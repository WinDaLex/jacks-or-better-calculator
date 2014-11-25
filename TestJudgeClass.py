import unittest

from Card import *
from Judge import *

class TestJudgeClass(unittest.TestCase):

    def testRoyalFlush(self):
        for suit in Card.suits:
            judge = Judge([Card(suit, 'A'), Card(suit, '10'), \
                    Card(suit, 'J'), Card(suit, 'K'), Card(suit, 'Q')])
            self.assertEqual([judge.result, judge.payoff], ['Royal Flush', 5000])

    def testStraightFlush(self):
        judge = Judge([Card('club', '5'), Card('heart', '3'), \
                Card('diamand', '6'), Card('diamand', '4'), Card('heart', '7')])
        self.assertEqual([judge.result, judge.payoff], ['Straight Flush', 1500])

    def testFourOfAKind(self):
        judge = Judge([Card('spade', '9'), Card('heart', '9'), \
                Card('diamand', '9'), Card('heart', '10'), Card('club', '9')])
        self.assertEqual([judge.result, judge.payoff], ['Four of a Kind', 600])

    def testFullHouse(self):
        pass

    def testFlush(self):
        pass

    def testStraight(self):
        pass

    def testThreeOfAKind(self):
        pass

    def testTwoPair(self):
        pass

    def testJacksOrBetter(self):
        pass

    def testNothing(self):
        pass


if __name__ == '__main__':
    unittest.main()
