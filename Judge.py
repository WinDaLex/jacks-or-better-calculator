from Card import *
import time

'''
Reference: http://www.suffecool.net/poker/evaluator.html
'''

PAYOFF = {'Royal Flush': 5000, \
          'Straight Flush': 1500, \
          'Four of a Kind': 600, \
          'Full House': 300, \
          'Flush': 200, \
          'Straight': 125, \
          'Three of a Kind': 75, \
          'Two Pair': 40, \
          'Jacks or Better': 10, \
          'Nothing': 0}

PRODUCT_STRAIGHT = (8610, 2310, 15015, 85085, 323323, 1062347, 2800733, 6678671, 14535931, 31367009)

def judge(hand):
    result, time = compute(hand)
    payoff = PAYOFF[result]

    return result, payoff, time

def compute(hand):
    result = 'Nothing'

    start = time.time()

    m = hand.dividedByRank()
    numOfRank = sorted(m.values(), reverse=True)

    if numOfRank[0] == 4: result = 'Four of a Kind'
    elif numOfRank[0] == 3 and numOfRank[1] == 2: result = 'Full House'
    elif numOfRank[0] == 3: result = 'Three of a Kind'
    elif numOfRank[0] == 2 and numOfRank[1] == 2: result = 'Two Pair'
    elif numOfRank[0] == 2:
        for i in range(0, 5):
            if hand[i].rank in ['J', 'Q', 'K', 'A']:
                for j in range(i+1, 5):
                    if hand[i].rank == hand[j].rank:
                        result = 'Jacks or Better'

    end1 = time.time()

    if isFlush(hand) and isRoyal(hand): result = 'Royal Flush'
    elif isFlush(hand) and isStraight(hand): result = 'Straight Flush'
    elif isFlush(hand): result = 'Flush'
    elif isStraight(hand): result = 'Straight'

    end2 = time.time()

    return result, [end1 - start, end2 - end1]

def isRoyal(hand):
    global PRODUCT_ROYAL_FLUSH
    product = 1
    for i in range(5):
        product *= Card.primeOfRank[hand[i].rank]
    return product == 31367009

def isFlush(hand):
    return Card.bitOfSuit[hand[0].suit] & Card.bitOfSuit[hand[1].suit] & Card.bitOfSuit[hand[2].suit] & Card.bitOfSuit[hand[3].suit] & Card.bitOfSuit[hand[4].suit] > 0

def isStraight(hand):
    global PRODUCT_STRAIGHT
    product = 1
    for i in range(5):
        product *= Card.primeOfRank[hand[i].rank]
    return product in PRODUCT_STRAIGHT
