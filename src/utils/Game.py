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
from random import shuffle, seed
from src.utils.Pile import Pile
from src.utils.Board import Board
from copy import deepcopy


class Game(object):
    """ A game object """

    def __init__(self, players):
        """ Initialize the game with a set of players
        :param Array players: an array of players
        """
        self.num_players = len(players)
        self.players = players
        if self.num_players > 4 or self.num_players < 2:
            raise ValueError("incorrect number of players")
        # start in random order
        shuffle(self.players)
        # create the pile
        self.pile = Pile()
        self.board = Board()

    def play(self):
        """ Play the game
        :return:
        """
        # draw initial cards
        for p in self.players:
            p.draw(self.pile)

        cnt = 0
        # while the pile still has cards and while the number of turns is still small (big turns indicates a problem)
        while self.pile.has_next() and cnt < 100:
            player_index = cnt % self.num_players
            old_board = deepcopy(self.board)
            played_cards, played_locations = self.players[player_index].play_cards(self.board)
            # TODO:  validate the move
            # TODO:  score the play
            self.players[player_index].draw()
            cnt += 1

        # TODO:  return the winning player
