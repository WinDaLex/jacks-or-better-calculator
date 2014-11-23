from Card import *
from Judge import *

class JudgeTest():

    def run(self):
        print 'Test sort process:'
        judge = Judge([Card('club', 'A'), Card('club', '10'), Card('club', '5')])
        judge.run()
        judge.cards[0].show()
        judge.cards[1].show()
        judge.cards[2].show()


if __name__ == '__main__':
    JudgeTest().run()
