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
from src.utils.Player import Player
from src.utils.Pile import Pile
from copy import deepcopy


class OneCardPlayer(Player):
    """ A player that only plays one card at a time """
    def play_cards(self, board, pile):
        """ Overridden method, see parent class for details """
        is_last_play = False
        # if the board is empty, then play the first card in the middle
        if board.is_empty():
            # find highest score card in hand
            first = self.hand.get_cards()[0].get_value()
            maxi = 0
            for i in range(len(self.hand.get_cards())):
                if self.hand.get_cards()[i].get_value() > first:
                    maxi = i
            temp_card = self.hand.use_card(maxi)
            board.place_card(temp_card, [Pile.get_num_cards(),Pile.get_num_cards()])
            return [temp_card], [[Pile.get_num_cards(), Pile.get_num_cards()]], is_last_play

        # for each card in the hand
        # for each location in the board
        # find the location with the highest score
        b = board.get_board()
        nrows = b.shape[0]
        ncols = b.shape[1]
        max_score = 0
        max_x = -1
        max_y = -1
        max_card = -1
        for cd in range(len(self.hand.get_cards())):
            for x in range(nrows):
                for y in range(ncols):
                    if b[x,y].is_null():
                        if y == 0 and x == 0:
                            if b[x+1,y].is_null() and b[x,y+1].is_null():
                                continue
                        elif y == 0 and x < nrows - 1:
                            if b[x-1,y].is_null() and b[x+1,y].is_null() and b[x,y+1].is_null():
                                continue
                        elif y == 0 and x == nrows - 1:
                            if b[x-1,y].is_null() and b[x,y+1].is_null():
                                continue
                        elif x == 0 and y < ncols - 1:
                            if b[x,y-1].is_null() and b[x,y+1].is_null() and b[x+1,y].is_null():
                                continue
                        elif x == 0 and y == ncols - 1:
                            if b[x,y-1].is_null() and b[x+1,y].is_null():
                                continue
                        elif x == nrows - 1 and y == ncols - 1:
                            if b[x-1,y].is_null() and b[x,y-1].is_null():
                                continue
                        elif x == nrows - 1:
                            if b[x-1,y].is_null() and b[x,y-1].is_null() and b[x,y+1].is_null():
                                continue
                        elif y == ncols - 1:
                            if b[x-1,y].is_null() and b[x+1,y].is_null() and b[x,y-1].is_null():
                                continue
                        else:
                            if b[x-1,y].is_null() and b[x+1,y].is_null() and b[x,y+1].is_null() and b[x, y-1].is_null():
                                continue
                        board_copy = deepcopy(board)
                        board_copy.place_card(self.hand.get_cards()[cd], [x,y])
                        current_score = board_copy.score_locations([self.hand.get_cards()[cd]], [[x,y]])
                        if current_score is None:
                            continue
                        if current_score > max_score:
                            max_score = current_score
                            max_x = x
                            max_y = y
                            max_card = cd
                    else:
                        continue

        # if none of the cards can be played in a valid situation, then no score would have been produced
        if max_score == 0:
            to_discard = []
            for i in range(4):
                if self.hand.get_cards()[i].is_null():
                    continue
                else:
                    to_discard.append(self.hand.get_cards()[i])
            self.discard(pile, to_discard)
            return None, None, False

        temp_card = self.hand.use_card(max_card)
        board.place_card(temp_card, [max_x, max_y])

        # if there are no cards left in the hand and none left in the pile, then this is the last turn
        if self.hand.get_num_open() == 4 and not pile.has_next():
            is_last_play = True

        return [temp_card], [[max_x, max_y]], is_last_play

