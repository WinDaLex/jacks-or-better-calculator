import unittest

from Card import *
from Judge import *

class TestJudgeClass(unittest.TestCase):

    def testRoyalFlush(self):
        self.judge = Judge([Card('club', '10'), Card('club', 'J'), Card('club', 'Q'), Card('club', 'K'), Card('club', 'A')])
        self.assertEqual(self.judge.result, 'Royal Flush')
        self.assertEqual(self.judge.payoff, 5000)

if __name__ == '__main__':
    unittest.main()
