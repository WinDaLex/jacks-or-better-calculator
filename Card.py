class Card():
    """A poker card with 4 kinds of suit and 13 kinds of rank, but excluding jokers."""

    suits = ['spade', 'heart', 'club', 'diamand']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        if suit not in self.suits: print 'SUIT ERROR'; return
        if rank not in self.ranks: print 'RANK ERROR'; return
        self.suit = suit
        self.rank = rank

    def show(self):
        print self.suit, self.rank
