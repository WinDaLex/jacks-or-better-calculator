import time

from Card import *
from Judge import *
from Game import *

class Solver():

    def __init__(self):
        self.desk = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.desk.append(Card(suit, rank))
        self.choice = []
        self.cur_sum = 0
        self.cur_num = 0

    def solve(self, hand):
        before_all_starts = time.time()

        print 'Hand: |',
        for card in hand:
            print card, '|',
            self.desk.remove(card)
        print

        hands = self.hold(hand)

        # TO-DO: to output all cards set which have the maximum expectation

        max_e = 0
        max_cards = None
        no = 0
        for cards in hands:
            self.cur_sum = 0
            self.cur_num = 0
            start = time.time()
            e, s, n = self.expectation(cards)
            end = time.time()
            no += 1
            print '[No.%2d] E = %7d/%6d = %5.2f, spent: %6.3fs, held: |' % (no, s, n, e, end - start),
            for card in cards:
                print card, '|',
            print

            if e > max_e:
                max_e, max_cards = e, cards

        print 'Recommendation: E = %.2f, Hold |' % max_e,
        for card in max_cards:
            print card, '|',
        print

        after_all_ends = time.time()
        print 'Total time spent: %.3fs' % (after_all_ends - before_all_starts)

    def hold(self, hand):
        res = []
        # not include the situation that nothing is held, coz it spends too much time.
        for i in range(1, 2**5):
            cur = []
            for j in range(5):
                if 2**j & i != 0:
                    cur.append(hand[j])
            res.append(cur)
        return res

    def expectation(self, cards):
        self.choose(cards, 0)
        return float(self.cur_sum) / self.cur_num, self.cur_sum, self.cur_num
        
    def choose(self, cards, index):
        if len(cards) == 5:
            self.cur_sum += Judge(Hand(cards)).payoff
            self.cur_num += 1
            return

        for i in range(index, len(self.desk)):
            cards.append(self.desk[i])
            self.choose(cards, i + 1)
            cards.remove(self.desk[i])
