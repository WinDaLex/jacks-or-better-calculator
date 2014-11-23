from Card import *

class CardTest():    

    def run(self):
        print 'Construct Card(spade, A):'
        Card('spade', 'A').show()
        print 'Construct Card(heart, 2):'
        Card('heart', '2').show()
        print 'Construct Card(club, 10):'
        Card('club', '10').show()
        print 'Construct Card(diamand, K):'
        Card('diamand', 'K').show()
        print 'Construct Card(spade, 1): (should be rank error)'
        Card('spade', '1')
        print 'Construct Card(spade, 11): (should be rank error)'
        Card('spade', '11')
        print 'Construct Card(wrong_suit, 1): (should be suit error)'
        Card('wrong_suit', 'K')



if __name__ == '__main__':
    CardTest().run()
