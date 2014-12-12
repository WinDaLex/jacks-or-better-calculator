import unittest

from Card import *
from Judge import *

class TestJudgeClass(unittest.TestCase):

    def testRoyalFlush(self):
        for suit in Card.suits:
            judge = Judge(Hand([Card(suit, 'A'), Card(suit, '10'), \
                    Card(suit, 'J'), Card(suit, 'K'), Card(suit, 'Q')]))
            self.assertEqual([judge.result, judge.payoff], ['Royal Flush', 5000])

    def testStraightFlush(self):
        judge = Judge(Hand('club 5, club 3, club 6, club 4, club 7'))
        self.assertEqual([judge.result, judge.payoff], ['Straight Flush', 1500])

    def testFourOfAKind(self):
        judge = Judge(Hand('spade 9, heart 9, diamand 9, heart 10, club 9'))
        self.assertEqual([judge.result, judge.payoff], ['Four of a Kind', 600])

    def testFullHouse(self):
        judge = Judge(Hand('spade A, heart A, diamand A, club 2, spade 2'))
        self.assertEqual([judge.result, judge.payoff], ['Full House', 300])

    def testFlush(self):
        judge = Judge(Hand('spade A, spade K, spade 5, spade 4, spade J'))
        self.assertEqual([judge.result, judge.payoff], ['Flush', 200])

    def testStraight(self):
        judge = Judge(Hand('spade A, heart 2, diamand 3, heart 4, spade 5'))
        self.assertEqual([judge.result, judge.payoff], ['Straight', 125])
        judge = Judge(Hand('spade 10, heart J, diamand Q, heart K, spade A'))
        self.assertEqual([judge.result, judge.payoff], ['Straight', 125])

    def testThreeOfAKind(self):
        judge = Judge(Hand('spade A, heart A, diamand A, heart 4, spade 5'))
        self.assertEqual([judge.result, judge.payoff], ['Three of a Kind', 75])

    def testTwoPair(self):
        judge = Judge(Hand('spade A, heart A, diamand 4, heart 4, spade 5'))
        self.assertEqual([judge.result, judge.payoff], ['Two Pair', 40])

    def testJacksOrBetter(self):
        judge = Judge(Hand('spade J, heart J, diamand 4, heart 9, spade 5'))
        self.assertEqual([judge.result, judge.payoff], ['Jacks or Better', 10])

    def testNothing(self):
        judge = Judge(Hand('club A, club 3, heart 6, club 4, club 7'))
        self.assertEqual([judge.result, judge.payoff], ['Nothing', 0])
        judge = Judge(Hand('spade A, club K, spade 5, spade 4, spade J'))
        self.assertEqual([judge.result, judge.payoff], ['Nothing', 0])
        judge = Judge(Hand('spade 6, heart A, diamand 4, heart 4, spade 5'))
        self.assertEqual([judge.result, judge.payoff], ['Nothing', 0])
        judge = Judge(Hand('spade 2, heart 4, diamand 5, heart 6, spade 7'))
        self.assertEqual([judge.result, judge.payoff], ['Nothing', 0])


if __name__ == '__main__':
    unittest.main()
