import unittest

from Card import *
import Judge

class TestJudgeClass(unittest.TestCase):

    def testRoyalFlush(self):
        for suit in Card.suits:
            result, payoff, time = Judge.judge(Hand([Card(suit, 'A'), Card(suit, '10'), \
                    Card(suit, 'J'), Card(suit, 'K'), Card(suit, 'Q')]))
            self.assertEqual([result, payoff], ['Royal Flush', 5000])

    def testStraightFlush(self):
        result, payoff, time = Judge.judge(Hand('club 5, club 3, club 6, club 4, club 7'))
        self.assertEqual([result, payoff], ['Straight Flush', 1500])

    def testFourOfAKind(self):
        result, payoff, time = Judge.judge(Hand('spade 9, heart 9, diamond 9, heart 10, club 9'))
        self.assertEqual([result, payoff], ['Four of a Kind', 600])

    def testFullHouse(self):
        result, payoff, time = Judge.judge(Hand('spade A, heart A, diamond A, club 2, spade 2'))
        self.assertEqual([result, payoff], ['Full House', 300])

    def testFlush(self):
        result, payoff, time = Judge.judge(Hand('spade A, spade K, spade 5, spade 4, spade J'))
        self.assertEqual([result, payoff], ['Flush', 200])

    def testStraight(self):
        result, payoff, time = Judge.judge(Hand('spade A, heart 2, diamond 3, heart 4, spade 5'))
        self.assertEqual([result, payoff], ['Straight', 125])
        result, payoff, time = Judge.judge(Hand('spade 10, heart J, diamond Q, heart K, spade A'))
        self.assertEqual([result, payoff], ['Straight', 125])

    def testThreeOfAKind(self):
        result, payoff, time = Judge.judge(Hand('spade A, heart A, diamond A, heart 4, spade 5'))
        self.assertEqual([result, payoff], ['Three of a Kind', 75])

    def testTwoPair(self):
        result, payoff, time = Judge.judge(Hand('spade A, heart A, diamond 4, heart 4, spade 5'))
        self.assertEqual([result, payoff], ['Two Pair', 40])

    def testJacksOrBetter(self):
        result, payoff, time = Judge.judge(Hand('spade J, heart J, diamond 4, heart 9, spade 5'))
        self.assertEqual([result, payoff], ['Jacks or Better', 10])

    def testNothing(self):
        result, payoff, time = Judge.judge(Hand('club A, club 3, heart 6, club 4, club 7'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('spade A, club K, spade 5, spade 4, spade J'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('spade 6, heart A, diamond 4, heart 4, spade 5'))
        self.assertEqual([result, payoff], ['Nothing', 0])
        result, payoff, time = Judge.judge(Hand('spade 2, heart 4, diamond 5, heart 6, spade 7'))
        self.assertEqual([result, payoff], ['Nothing', 0])


if __name__ == '__main__':
    unittest.main()
