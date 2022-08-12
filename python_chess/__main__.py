#!/usr/bin/env python

from chess import Chess, Human, Robot
from mywindow import Window

players = [Human(1), Robot(2, prediction=2)]
window = Window(build=False, size=[700, 700])
game = Chess(window, players)
game()
game.end()
