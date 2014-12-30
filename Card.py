# -*- coding: utf-8 -*-

class Card():
    """A poker card with 4 kinds of suit and 13 kinds of rank, but excluding jokers."""

    suits = ['S', 'H', 'C', 'D'] # S: spade; H: heart, C: club; D: diamond
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suitsToChar = {'S':'♠', 'H':'♥', 'C':'♣', 'D':'♦'}
    primeOfRank = {'2':2, '3':3, '4':5, '5':7, '6':11, '7':13, '8':17, \
            '9':19, 'T':23, 'J':29, 'Q':31, 'K':37, 'A':41}
    bitOfSuit = {'S':1<<0, 'H':1<<1, 'C':1<<2, 'D':1<<3}

    def __init__(self, suit, rank):
        if suit not in self.suits: raise ValueError, 'invalid suit'; return
        if rank not in self.ranks: raise ValueError, 'invalid rank'; return 
        self.suit = suit
        self.rank = rank
        # val = xxxxxxxx xxxxxxxx CDHSxxxx xxPPPPPP (a 32-bit integer)
        # P = prime number of rank (deuce=2,trey=3,four=5,...,ace=41)
        # CDHS = suit of card (bit turned on based on suit of card)
        self.val = self.bitOfSuit[suit] * 0x1000 + self.primeOfRank[rank]

    def __str__(self):
        return self.suitsToChar[self.suit] + self.rank

    def __eq__(self, obj):
        return self.suit == obj.suit and self.rank == obj.rank

class Hand():
    """A hand is five distinct cards which players got."""

    def __init__(self, cards):
        """ cards can be 'suit rank, suit rank, suit rank, suit rank, suit rank' """ 
        self.cards = cards
        if type(cards) == type(''):
            self.cards = []
            for suit_and_rank in cards.split(' '):
                rank, suit = suit_and_rank.strip()
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

    def __eq__(self, obj):
        for i in range(0, 5):
            if self[i] != obj[i]:
                return False
        return True

