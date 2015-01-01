# -*- coding: utf-8 -*-

import time

from Card import *
import Judge


cur_hand = Hand('TS JS QS KS AS')

def solve(hand):

    print 'Hand:',
    for card in hand: print card, 
    print

    before_all_starts = time.time()

    global desk
    desk = []
    for suit in Card.suits:
        for rank in Card.ranks:
            card = Card(suit, rank)
            if card not in hand:
                desk.append(card)

    candidates = hold(hand)

    max_e = 0
    max_held = None
    no = 0
    for i in range(len(candidates)):
        start = time.time()
        e, s, n = expectation(candidates[i])
        end = time.time()
        print '[No.%2d] E = %7d/%6d = %5.2f, spent: %5.3fs, held:' % (i, s, n, e, end - start),
        for card in candidates[i]: print card,
        print
        if e > max_e: max_e, max_held = e, hand

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
    global cur_hand
    for i in range(len(cards)):
        cur_hand[i] = cards[i]
    cur_sum = 0
    cur_num = 0
    choose(0, len(cards))
    return float(cur_sum) / cur_num, cur_sum, cur_num

def choose(index, p):
    global cur_sum
    global cur_num
    global cur_hand
    if p == 5:
        result, payoff = Judge.judge(cur_hand)
        cur_sum += payoff
        cur_num += 1
        return

    for i in range(index, len(desk)):
        cur_hand[p] = desk[i]
        choose(i + 1, p + 1)
