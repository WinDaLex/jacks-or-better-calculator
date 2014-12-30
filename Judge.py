from Card import *
import time

PAYOFF = {'Royal Flush': 5000, 'Straight Flush': 1500, \
        'Four of a Kind': 600, 'Full House': 300, 'Flush': 200, \
        'Straight': 125, 'Three of a Kind': 75, 'Two Pair': 40, \
        'Jacks or Better': 10, 'Nothing': 0}


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

    if isFlush(hand):
        if isStraight(hand):
            bo = False
            for i in range(5):
                if hand[i].rank == 'A':
                    bo = True
            if bo: result = 'Royal Flush'
            else: result = 'Straight Flush'
        else:
            result = 'Flush'
    end2 = time.time()

    if result == 'Nothing' and isStraight(hand): result = 'Straight'

    end3 = time.time()

    return result, [end1 - start, end2 - end1, end3 - end2]

def isFlush(hand):
    return hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit

def isStraight(hand):
    l = []
    for i in range(5):
        if hand[i].rank == 'A': l.append(1)
        elif hand[i].rank == '10': l.append(10)
        elif hand[i].rank == 'J': l.append(11)
        elif hand[i].rank == 'Q': l.append(12)
        elif hand[i].rank == 'K': l.append(13)
        else: l.append(int(hand[i].rank))
    l.sort()

    for i in range(2, 5):
        if l[i] != l[i - 1] + 1:
            return False

    return l[0] == l[1] - 1 or l[0] == 1 and l[4] == 13
