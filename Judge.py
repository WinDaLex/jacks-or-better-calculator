class Judge():

    PAYOFF = {'Royal Flush': 5000, 'Straight Flush': 1500, \
            'Four of a Kind': 600, 'Full House': 300, 'Flush': 200, \
            'Straight': 125, 'Three of a Kind': 75, 'Two Pair': 40, \
            'Jacks or Better': 10, 'Nothing': 0}

    def __init__(self, hand):
        self.hand = hand
        self.result = self.compute()
        self.payoff = self.PAYOFF[self.result]

    def compute(self):
        m = self.hand.dividedByRank()
        numOfRank = sorted(m.values(), reverse=True)

        if numOfRank[0] == 4: return 'Four of a Kind'
        if numOfRank[0] == 3 and numOfRank[1] == 2: return 'Full House'
        if numOfRank[0] == 3: return 'Three of a Kind'
        if numOfRank[0] == 2 and numOfRank[1] == 2: return 'Two Pair'
        if numOfRank[0] == 2:
            for i in range(0, 5):
                if self.hand[i].rank in ['J', 'Q', 'K', 'A']:
                    for j in range(i+1, 5):
                        if self.hand[i].rank == self.hand[j].rank:
                            return 'Jacks or Better'

        '''
        if self.isFlush() and self.isStraight():
            for i in range(0, 5):
                if self.hand[i].rank == 'A':
                    return 'Royal Flush'
            return 'Straight Flush'

        if self.isFlush(): return 'Flush'
        if self.isStraight(): return 'Straight'
        '''

        if self.isFlush():
            if self.isStraight():
                for i in range(0, 5):
                    if self.hand[i].rank == 'A':
                        return 'Royal Flush'
                return 'Straight Flush'
            else:
                return 'Flush'

        if self.isStraight(): return 'Straight'

        return 'Nothing'

    def isFlush(self):
        return self.hand.dividedBySuit().values()[0] == 5

    def isStraight(self):
        l = []
        for i in range(0, 5):
            if self.hand[i].rank == 'A': l.extend([1, 14])
            elif self.hand[i].rank == '10': l.append(10)
            elif self.hand[i].rank == 'J': l.append(11)
            elif self.hand[i].rank == 'Q': l.append(12)
            elif self.hand[i].rank == 'K': l.append(13)
            else: l.append(int(self.hand[i].rank))
        l.sort()
        bo = True
        for i in range(2, 5):
            if l[i] != l[i - 1] + 1:
                bo = False

        if bo: return l[0] == l[1] - 1 or len(l) == 6 and l[5] == 14 and l[4] == 13
