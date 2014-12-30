import time

from Card import *
import Judge
from Game import *

desk = []
cur_sum = 0
cur_num = 0

def init(hand):
    global desk
    global cur_sum
    global cur_num
    desk = []
    for suit in Card.suits:
        for rank in Card.ranks:
            desk.append(Card(suit, rank))
    cur_sum = 0
    cur_num = 0

    for card in hand:
        desk.remove(card)

def solve(hand):
    global cur_sum
    global cur_num

    before_all_starts = time.time()

    init(hand)

    print 'Hand:',
    for card in hand: print card, 
    print

    hands = hold(hand)

    max_e = 0
    max_held = None
    no = 0
    for cards in hands:
        start = time.time()
        e, s, n = expectation(cards)
        end = time.time()
        no += 1
        print '[No.%2d] E = %7d/%6d = %5.2f, spent: %5.3fs, held:' % (no, s, n, e, end - start),
        for card in cards: print card,
        print

        if e > max_e: max_e, max_held = e, cards

    print 'Recommendation: E = %.2f, Hold' % max_e,
    for card in max_held: print card, 
    print

    after_all_ends = time.time()
    print 'Total time spent: %.3fs' % (after_all_ends - before_all_starts)

def hold(hand):
    # not include the situation that nothing is held, coz it spends too much time.
    res = []
    for i in range(1, 2**5):
        cur = []
        for j in range(5):
            if 2**j & i != 0:
                cur.append(hand[j])
        res.append(cur)
    return res

def expectation(cards):
    global cur_sum
    global cur_num
    cur_sum = 0
    cur_num = 0
    choose(cards, 0)
    return float(cur_sum) / cur_num, cur_sum, cur_num

def choose(cards, index):
    global desk
    global cur_sum
    global cur_num
    if len(cards) == 5:
        result, payoff = Judge.judge(Hand(cards))
        cur_sum += payoff
        cur_num += 1
        return

    for i in range(index, len(desk)):
        cards.append(desk[i])
        choose(cards, i + 1)
        cards.pop()
