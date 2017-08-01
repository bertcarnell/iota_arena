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
from src.utils.Hand import Hand
from src.utils.Card import Card
import abc


class Player(object):
    """ a player object with a hand """

    def __init__(self):
        """ Initialize the player object """
        self.hand = Hand()

    @abc.abstractmethod
    def play_cards(self, board, pile):
        """ Decide which cards to play, place the cards on the board, return the cards played with locations
        :param Board board: the board of play
        :param Pile pile: the pile for discarding if necessary
        :return: an Array of Cards, an Array of locations (each of x,y) or None, None in the case of a discard and an indicator if this is the last play
        """
        raise ValueError("need to override this method")

    def draw(self, pile):
        """ Draw from a common pile
        :param Pile pile:  The common pile
        """
        self.hand.draw(pile)

    def discard(self, pile, hand_indicies):
        cards = []
        for i in hand_indicies:
            if 0 <= i < 4 and not self.hand.get_cards()[i].is_null():
                cards.append(self.hand.use_card(i))
                self.hand.get_cards()[i] = Card.null_card()
            else:
                raise ValueError("Cannot discard the cards selected from the hand")
        pile.return_cards(cards)
