# -*- coding: utf-8 -*-

'''
  reference: http://www.suffecool.net/poker/evaluator.html
'''


ROYAL_FLUSH = 'Royal Flush'
STRAIGHT_FLUSH = 'Straight Flush'
FOUR_OF_A_KIND = 'Four of a Kind'
FULL_HOUSE = 'Full House'
FLUSH = 'Flush'
STRAIGHT = 'Straight'
THREE_OF_A_KIND = 'Three of a Kind'
TWO_PAIR = 'Two Pair'
JACKS_OR_BETTER = 'Jacks or Better'
NOTHING = 'Nothing'

PAYOFF = {ROYAL_FLUSH: 5000, \
          STRAIGHT_FLUSH: 1500, \
          FOUR_OF_A_KIND: 600, \
          FULL_HOUSE: 300, \
          FLUSH: 200, \
          STRAIGHT: 125, \
          THREE_OF_A_KIND: 75, \
          TWO_PAIR: 40, \
          JACKS_OR_BETTER: 10, \
          NOTHING: 0}

PRODUCT_STRAIGHT = (8610, 2310, 15015, 85085, 323323, 1062347, 2800733, 6678671, 14535931, 31367009)


def judge(hand):

    result = NOTHING

    m = hand.dividedByRank()

    maxv1, maxk1 = 0, ''
    maxv2, maxk2 = 0, ''
    for k, v in m.iteritems():
        if v > maxv1:
            maxk2, maxv2 = maxk1, maxv1
            maxk1, maxv1 = k, v
        elif v > maxv2:
            maxk2, maxv2 = k, v

    bo = False

    if maxv1 == 2 and maxv2 == 2:
        result = TWO_PAIR
    elif maxv1 == 2:
        if maxk1 in ['J', 'Q', 'K', 'A']:
            result = JACKS_OR_BETTER
        bo = True
    elif maxv1 == 3 and maxv2 == 2:
        result = FULL_HOUSE
    elif maxv1 == 3:
        result = THREE_OF_A_KIND
    elif maxv1 == 4:
        result = FOUR_OF_A_KIND

    # if a pair or much appear, it's impossible to appear flush or straight
    if bo or result != NOTHING: return result, PAYOFF[result]

    if isFlush(hand):
        if isStraight(hand):
            if isRoyal(hand): result = 'Royal Flush'
            else: result = STRAIGHT_FLUSH
        else: result = FLUSH
    elif isStraight(hand): result = STRAIGHT

    return result, PAYOFF[result]

def isRoyal(hand):
    global PRODUCT_ROYAL_FLUSH
    product = 1
    for i in range(5):
        product *= hand[i].val & 0xff
    return product == 31367009

def isFlush(hand):
    # return hand[0].val & hand[1].val & hand[2].val & hand[3].val & hand[4].val & 0xF000 > 0
    # It is slower than the regular code
    return hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit

def isStraight(hand):
    global PRODUCT_STRAIGHT
    product = 1
    for i in range(5):
        product *= hand[i].val & 0xff
    return product in PRODUCT_STRAIGHT
