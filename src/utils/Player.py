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
import abc


class Player(object):
    """ a player object with a hand """

    def __init__(self):
        """ Initialize the player object """
        self.hand = Hand()

    @abc.abstractmethod
    def play_cards(self, board):
        """ Decide which cards to play, place the cards on the board, return the cards played with locations
        :param Board board: the board of play
        :return: an array of cards and an array of 2-length location arrays
        """
        raise ValueError("need to override this method")

    def draw(self, pile):
        """ Draw from a common pile
        :param Pile pile:  The common pile
        """
        self.hand.draw(pile)
