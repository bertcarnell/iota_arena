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
import numpy as npy
from src.utils.Pile import Pile
from src.utils.Card import Card
from src.utils.Sequence import Sequence


class Board(object):
    """ A class to hold the game board """

    def __init__(self):
        """ Initialize the Board """
        self.m = npy.ndarray(shape=(2 * Pile.get_num_cards(), 2 * Pile.get_num_cards()), dtype=object, order='C')
        for i in range(2 * Pile.num_cards):
            for j in range(2 * Pile.get_num_cards()):
                self.m[i, j] = Card.null_card()
        self.empty = True

    def is_empty(self):
        return self.empty

    def place_card(self, card, location):
        """ Place a card on the board
        :param Card card: a Card
        :param list location: a list of x and y locations
        :return:
        """
        self.m[location[0], location[1]] = card
        self.empty = False

    def place_cards(self, cards, locations):
        """ Place cards on the board

        :param list cards: cards to be placed
        :param list locations: a list of lists of locations for the cards to be placed
        :return:
        """
        if len(cards) != len(locations):
            raise ValueError("cards and locations are not the same length")
        if len(cards) > 4:
            raise ValueError("more than 4 cards are being placed")
        if len(cards) == 0:
            print("passing on the hand")
        if len(cards) > 0 and len(locations[0]) != 2:
            raise ValueError("each location must have an x and y value")
        for i in range(len(cards)):
            self.place_card(cards[i], locations[i])
        # after cards are placed, return score
        base_score = 0
        for i in range(len(cards)):
            base_score += cards[i].get_value()
        # TODO:  Complete scoring algorithm
        return base_score

    def get_board(self):
        return self.m

    def find_adjacent_cards(self, card, x, y):
        if x < 0 or y < 0 or x > 2*Pile.get_num_cards() or y > 2*Pile.get_num_cards():
            raise ValueError("location for card is outside the board")
        if self.empty:
            return [None, None]

        # look horizontally
        horizontal_group = Sequence()
        horizontal_group.add(card)
        for yi in range(y+1, y+4, 1):
            if not self.m[x,yi].is_null():
                horizontal_group.add(self.m[x,yi])
            else:
                # there is a gap, so break
                break
        for yi in range(y-1, y-4, -1):
            if not self.m[x,yi].is_null():
                horizontal_group.add(self.m[x,yi])
            else:
                break

        # look vertically
        vertical_group = Sequence()
        vertical_group.add(card)
        for xi in range(x+1, x+4, 1):
            if not self.m[xi, y].is_null():
                vertical_group.add(self.m[xi, y])
            else:
                break
        for xi in range(x-1, x-4, -1):
            if not self.m[xi, y].is_null():
                vertical_group.add(self.m[xi, y])
            else:
                break

        # if the card is not valid at this location, return none
        if not horizontal_group.is_valid_sequence() or not vertical_group.is_valid_sequence():
            return [None, None]

        vertical_group.sort()
        horizontal_group.sort()

        return [horizontal_group, vertical_group]

    def score_locations(self, cards, locations):
        """ Score the cards that were played this turn.  They must already be on the board
        :param array cards: an array of Cards
        :param array locations: an array of arrays containing x,y coordinates
        :return int: the score
        """
        if len(cards) != len(locations):
            raise ValueError("the length of cards and locations should be the same")
        if len(locations) != 0 and len(locations[0]) != 2:
            raise ValueError("the length of the first locations should be two")
        # find the groups for all the cards that are played
        horizontal_groups = []
        vertical_groups = []
        for i in range(len(cards)):
            horizontal_group, vertical_group = self.find_adjacent_cards(cards[i], locations[i][0], locations[i][1])
            # if a card is next to nothing horizontally or vertically, then it must be the first play alone
            if len(cards) == 1 and horizontal_group.length() == 1 and vertical_group.length() == 1:
                return cards[0].get_value()
            # if a card has no horizontal sequence, then it must have a vertical neighbor
            # don't add single cards
            if horizontal_group.length() > 1:
                horizontal_groups.append(horizontal_group)
            if vertical_group.length() > 1:
                vertical_groups.append(vertical_group)
        # find the unique sequences that are created
        horizontal_groups = set(horizontal_groups)
        vertical_groups = set(vertical_groups)

        score = 0
        for seq in horizontal_groups:
            score += seq.get_sum_scores()
        for seq in vertical_groups:
            score += seq.get_sum_scores()
        if len(cards) == 4:
            score *= 2
        for seq in horizontal_groups:
            if seq.length() == 4:
                score *= 2
        for seq in vertical_groups:
            if seq.length() == 4:
                score *= 2
        return score
