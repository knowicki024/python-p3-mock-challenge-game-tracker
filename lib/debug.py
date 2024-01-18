#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    g1 = Game("Chess")
    g2 =Game("Basketball")
    g3 = Game("Monopoly")

    p1 = Player("Melissa")
    p2= Player("Hadil")
    p3 = Player("Tyler")

    r1 = Result(p1, g3, 100)
    r2 = Result(p2, g1, 103)
    r3 = Result(p3, g2, 110)

    ipdb.set_trace()
