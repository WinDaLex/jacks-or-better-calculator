import unittest

from Card import *
import Judge

class TestJudgeClass(unittest.TestCase):

    def testRoyalFlush(self):
        for suit in Card.suits:
            result, payoff, time = Judge.judge(Hand([Card(suit, 'A'), Card(suit, 'T'), \
                    Card(suit, 'J'), Card(suit, 'K'), Card(suit, 'Q')]))
            self.assertEqual([result, payoff], ['Royal Flush', 5000])

    def testStraightFlush(self):
        result, payoff, time = Judge.judge(Hand('5C, 3C, 6C, 4C, 7C'))
        self.assertEqual([result, payoff], ['Straight Flush', 1500])

    def testFourOfAKind(self):
        result, payoff, time = Judge.judge(Hand('9S, 9H, 9D, TH, 9C'))
        self.assertEqual([result, payoff], ['Four of a Kind', 600])

    def testFullHouse(self):
        result, payoff, time = Judge.judge(Hand('AS, AH, AD, 2C, 2S'))
        self.assertEqual([result, payoff], ['Full House', 300])

    def testFlush(self):
        result, payoff, time = Judge.judge(Hand('AS, KS, 5S, 4S, JS'))
        self.assertEqual([result, payoff], ['Flush', 200])

    def testStraight(self):
        result, payoff, time = Judge.judge(Hand('AS, 2H, 3D, 4H, 5S'))
        self.assertEqual([result, payoff], ['Straight', 125])
        result, payoff, time = Judge.judge(Hand('TS, JH, QD, KH, AS'))
        self.assertEqual([result, payoff], ['Straight', 125])

    def testThreeOfAKind(self):
        result, payoff, time = Judge.judge(Hand('AS, AH, AD, 4H, 5S'))
        self.assertEqual([result, payoff], ['Three of a Kind', 75])

    def testTwoPair(self):
        result, payoff, time = Judge.judge(Hand('AS, AH, 4D, 4H, 5S'))
        self.assertEqual([result, payoff], ['Two Pair', 40])

    def testJacksOrBetter(self):
        result, payoff, time = Judge.judge(Hand('JS, JH, 4D, 9H, 5S'))
        self.assertEqual([result, payoff], ['Jacks or Better', 10])

    def testNothing(self):
        result, payoff, time = Judge.judge(Hand('AC, 3C, 6H, 4C, 7C'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('AS, KC, 5S, 4S, JS'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('6S, AH, 4D, 4H, 5S'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('2S, 4H, 5D, 6H, 7S'))
        self.assertEqual([result, payoff], ['Nothing', 0])


if __name__ == '__main__':
    unittest.main()
