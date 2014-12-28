from Card import *

PAYOFF = {'Royal Flush': 5000, 'Straight Flush': 1500, \
        'Four of a Kind': 600, 'Full House': 300, 'Flush': 200, \
        'Straight': 125, 'Three of a Kind': 75, 'Two Pair': 40, \
        'Jacks or Better': 10, 'Nothing': 0}

def judge(hand):
    result = compute(hand)
    payoff = PAYOFF[result]
    return result, payoff

def compute(hand):
    m = hand.dividedByRank()
    numOfRank = sorted(m.values(), reverse=True)

    if numOfRank[0] == 4: return 'Four of a Kind'
    if numOfRank[0] == 3 and numOfRank[1] == 2: return 'Full House'
    if numOfRank[0] == 3: return 'Three of a Kind'
    if numOfRank[0] == 2 and numOfRank[1] == 2: return 'Two Pair'
    if numOfRank[0] == 2:
        for i in range(0, 5):
            if hand[i].rank in ['J', 'Q', 'K', 'A']:
                for j in range(i+1, 5):
                    if hand[i].rank == hand[j].rank:
                        return 'Jacks or Better'

    if isFlush(hand):
        if isStraight(hand):
            for i in range(0, 5):
                if hand[i].rank == 'A':
                    return 'Royal Flush'
            return 'Straight Flush'
        else:
            return 'Flush'

    if isStraight(hand): return 'Straight'

    return 'Nothing'

def isFlush(hand):
    return hand.dividedBySuit().values()[0] == 5

def isStraight(hand):
    l = []
    for i in range(0, 5):
        if hand[i].rank == 'A': l.extend([1, 14])
        elif hand[i].rank == '10': l.append(10)
        elif hand[i].rank == 'J': l.append(11)
        elif hand[i].rank == 'Q': l.append(12)
        elif hand[i].rank == 'K': l.append(13)
        else: l.append(int(hand[i].rank))
    l.sort()
    bo = True
    for i in range(2, 5):
        if l[i] != l[i - 1] + 1:
            bo = False

    if bo: return l[0] == l[1] - 1 or len(l) == 6 and l[5] == 14 and l[4] == 13
