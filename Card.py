class Card():

    mapperSuit = {'spade': 0, 'heart': 1, 'club': 2, 'diamand': 3}
    mapperRank = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
            '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12}
    # suit: 'spade', 'heart', 'club', 'diamand'
    # rank: 'A', '2', '3', '4', '5', '6', '7', 8', '9', '10', 'J', 'Q', 'K'
    def __init__(self, suit, rank):
        if suit not in self.mapperSuit: print 'ERROR'; return
        if rank not in self.mapperRank: print 'ERROR'; return
        self.suit = suit
        self.rank = rank
        self.value = self.mapperSuit[self.suit] * 13 + \
                self.mapperRank[self.rank]
        self.show()

    def show(self):
        print self.suit, self.rank, self.value
