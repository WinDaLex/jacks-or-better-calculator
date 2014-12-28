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
            e = self.expectation(cards)
            print 'current: ', 'e = ', e, ', cards = ', 
            for card in cards:
                print card,
            print
            if e > max_e:
                max_e, max_cards = e, cards

        for card in max_cards:
            print card


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
        print 'cur_sum = ', self.cur_sum, ', cur_num = ', self.cur_num
        return self.cur_sum / self.cur_num
        
    def choose(self, cards, desk, num, index):
        if num == 0:
            self.cur_sum += Judge(Hand(cards)).payoff
            self.cur_num += 1
            return

        for i in range(index, len(desk)):
            cards.append(desk[i])
            self.choose(cards, desk, num - 1, i + 1)
            cards.remove(desk[i])
