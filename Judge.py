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
    result = 'Nothing'

    start = time.time()

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

    if maxv1 == 4:
        result = 'Four of a Kind'
    elif maxv1 == 3 and maxv2 == 2:
        result = 'Full House'
    elif maxv1 == 3:
        result = 'Three of a Kind'
    elif maxv1 == 2 and maxv2 == 2:
        result = 'Two Pair'
    elif maxv1 == 2:
        if maxk1 in ['J', 'Q', 'K', 'A']:
            result = 'Jacks or Better'
        bo = True

    end1 = time.time()

    # if a pair or much appear, it's impossible to appear flush or straight
    if bo or result != 'Nothing': return result, PAYOFF[result], [end1 - start, 0]

    if isFlush(hand) and isRoyal(hand): result = 'Royal Flush'
    elif isFlush(hand) and isStraight(hand): result = 'Straight Flush'
    elif isFlush(hand): result = 'Flush'
    elif isStraight(hand): result = 'Straight'

    end2 = time.time()

    return result, PAYOFF[result], [end1 - start, end2 - end1]

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
