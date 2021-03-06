# Copyright 2017 Robert Carnell
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from unittest import TestCase
from src.utils.Game import Game
from src.utils.Player import Player
from src.player_inventory.OneCardPlayer import OneCardPlayer


class TestGame(TestCase):
    def test_game(self):
        players = [Player(), Player()]
        g = Game(players)

        players = [Player(), Player(), Player(), Player(), Player()]
        try:
            g2 = Game(players)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_play(self):
        players = [OneCardPlayer(), OneCardPlayer()]
        g = Game(players)
        # TODO:  The simulation is taking too long and we need to switch to a sparse matrix (smaller copy and quicker to iterate over)
        #scores = g.play()
        #print(scores)
