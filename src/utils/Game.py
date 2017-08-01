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
from random import shuffle
from src.utils.Pile import Pile
from src.utils.Board import Board
import logging

class Game(object):
    """ A game object """

    def __init__(self, players):
        """ Initialize the game with a set of players
        :param Array players: an array of players
        """
        logging.debug('Initializing the Game object')
        self.num_players = len(players)
        self.players = players
        if self.num_players > 4 or self.num_players < 2:
            msg = 'Incorrect number of players'
            logging.error(msg)
            raise ValueError(msg)
        # start in random order
        shuffle(self.players)
        # create the pile
        self.pile = Pile()
        self.board = Board()
        self.scores = []
        for i in range(self.num_players):
            self.scores.append(0)

    def play(self):
        """ Play the game
        :return:
        """
        # draw initial cards
        logging.debug('Drawing the initial hands')
        for p in self.players:
            p.draw(self.pile)

        cnt = 0
        is_last_play = False
        # while the pile still has cards and while the number of turns is still small (big turns indicates a problem)
        while self.pile.has_next() and cnt < 100:
            # rotate around the players
            player_index = cnt % self.num_players
            logging.debug('Game: Turn # {0}, Player # {1}'.format(cnt, player_index))
            # let the player play the card on the board
            played_cards, played_locations, is_last_play = self.players[player_index].play_cards(self.board, self.pile)
            logging.debug('Game: Cards played {0} at {1}'.format("".join(str(cd) for cd in played_cards), "".join(str(played_locations))))
            if played_cards is not None and played_locations is not None:
                # score the valid cards or identify an invalid move
                score = self.board.score_locations(played_cards, played_locations)
                logging.debug('Game: Move Score {0}'.format(score))
                if score is None:
                    logging.debug('Game: Invalid move by player index {0}'.format(str(player_index)))
                    return None
                self.scores[player_index] += score
                if is_last_play:
                    return self.scores
            self.players[player_index].draw(self.pile)
            cnt += 1
        logging.debug('Game: pile is empty or 100 turns have been reached')
        # after the pile is gone, the players continue to play cards until they are out...
        while not is_last_play:
            # rotate around the players
            player_index = cnt % self.num_players
            # let the player play the card on the board
            played_cards, played_locations, is_last_play = self.players[player_index].play_cards(self.board, self.pile)
            if played_cards is not None and played_locations is not None:
                # score the valid cards or identify an invalid move
                score = self.board.score_locations(played_cards, played_locations)
                if score is None:
                    print('Invalid move by player index {0}'.format(str(player_index)))
                    return None
                self.scores[player_index] += score
            cnt += 1
        return self.scores

        # TODO:  return the winning player
