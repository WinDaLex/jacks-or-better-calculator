# -*- coding: utf-8 -*-

import time
from random import Random

from Card import *
from Judge import *


class Game():
    desk = []

    def init(self):
        self.desk = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.desk.append(Card(suit, rank))

        Random().shuffle(self.desk)

    def start(self):
        self.init()
        for i in range(5):
            print self.desk[i],
        print

        judge = Judge(Hand(self.desk[:5]))
        print judge.result, judge.payoff

        return judge.result, judge.payoff


def simulation(number = -1, interval = 1): 
    game = Game() 
    no = 0; total = 0; expectation = 0 
    while (no != number): 
        time.sleep(interval) 
        result, payoff = game.start() 
        total += payoff
        no += 1 
        expectation = float(total) / no 
        print "No. %d\tresult: %s\naward: %d\t total: %d\t E: %f\n" %\
                (no, result, payoff, total, expectation) 
