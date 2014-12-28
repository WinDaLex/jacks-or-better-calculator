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

        for card in hand:
            print card
            self.desk.remove(card)

        hands = self.hold(hand)

        # TO-DO: to output all cards set which have the maximum expectation

        max_e = 0
        max_cards = None
        for cards in hands:
            self.cur_sum = 0
            self.cur_num = 0
            start = time.time()
            e = self.expectation(cards)
            end = time.time()
            print 'e = %.2f, time: %.3fs, cards =' % (e, end - start),
            for card in cards:
                print card,
            print

            if e > max_e:
                max_e, max_cards = e, cards

        for card in max_cards:
            print card,
        print

        after_all_ends = time.time()
        print 'Total time spent: %.3fs' % (after_all_ends - before_all_starts)

    def hold(self, hand):
        res = []
        # not include the situation that nothing is held, coz it spends too much time.
        for i in range(1, 2**5):
            cur = []
            for j in range(5):
                if 2**j & i >= 1:
                    cur.append(hand[j])
            res.append(cur)
        return res

    def expectation(self, cards):
        num = 5 - len(cards)
        self.choose(cards, self.desk, 5 - len(cards), 0)
        print 'current sum = %d, current num = %d' % (self.cur_sum, self.cur_num)
        return float(self.cur_sum) / self.cur_num
        
    def choose(self, cards, desk, num, index):
        if num == 0:
            self.cur_sum += Judge(Hand(cards)).payoff
            self.cur_num += 1
            return

        for i in range(index, len(desk)):
            cards.append(desk[i])
            self.choose(cards, desk, num - 1, i + 1)
            cards.remove(desk[i])
