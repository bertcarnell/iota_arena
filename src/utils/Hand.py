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
from src.utils.Card import Card
import copy


class Hand(object):
    """ A player's hand """
    hand_size = 4

    def __init__(self):
        """ Initialize a Hand
        :returns: A hand object
        """
        self.hand = [Card.null_card(), Card.null_card(), Card.null_card(), Card.null_card()]
        self.num_open = Hand.hand_size

    def draw(self, pile):
        """ Draw a card from a pile into a hand
        :param Pile pile: The pile to draw from
        """
        if pile.has_next() and self.num_open > 0:
            for i in range(Hand.hand_size):
                if self.hand[i].is_null():
                    self.hand[i] = pile.get_next()
                    self.num_open -= 1

    def use_card(self, card_num):
        """ Use a card from the hand
        :param int card_num: the card to use (zero based)
        :return: the card is to be played
        """
        assert 0 <= card_num < Hand.hand_size
        ret_card = copy.deepcopy(self.hand[card_num])
        self.hand[card_num] = Card.null_card()
        self.num_open += 1
        return ret_card

    def get_num_open(self):
        """ Number of places open in a hand
        :return int: the number open
        """
        return self.num_open

    def get_cards(self):
        """ Get the cards in the hand
        :return Array: get an array of cards in the hand
        """
        return self.hand
