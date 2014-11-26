class Card():
    """A poker card with 4 kinds of suit and 13 kinds of rank, but excluding jokers."""

    suits = ['spade', 'heart', 'club', 'diamand']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        if suit not in self.suits: raise ValueError, 'wrong suit'; return
        if rank not in self.ranks: raise ValueError, 'wrong rank'; return 
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + ' ' + self.rank


class Hand():
    """A hand is five distinct cards which players got."""

    def __init__(self, cards):
        """ cards can be 'suit rank, suit rank, suit rank, suit rank, suit rank' """ 
        self.cards = cards
        if type(cards) == type(''):
            self.cards = []
            for suit_and_rank in cards.split(','):
                suit, rank = suit_and_rank.strip().split(' ')
                self.cards.append(Card(suit, rank))
        if type(self.cards) == type([]):
            if len(self.cards) != 5:
                raise ValueError, 'cards should contain five cards, it is only %d' % len(self.cards)
            for card in self.cards:
                if card.__class__.__name__ != 'Card':
                    raise ValueError, 'cards can only contain Card, %s is not allowed' % type(card)
        else:
            raise ValueError, 'cards should be str or list, cannot be %s' % type(cards)

    def __getitem__(self, ind):
        return self.cards.__getitem__(ind)

    def dividedBySuit(self):
        return self.__dividedBy('suit')

    def dividedByRank(self):
        return self.__dividedBy('rank')

    def __dividedBy(self, attr):
        res = {}
        for card in self.cards:
            attr_val = getattr(card, attr)
            if attr_val not in res: res[attr_val] = 0
            res[attr_val] += 1
        return res
