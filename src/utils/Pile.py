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
from src.utils.Card import Card


class Pile(object):
    """ A pile of cards """
    # there are 64 cards and 2 wilds
    num_cards = 66

    def __init__(self):
        """ Initialize a Pile object """
        # start with the wild cards
        self.pile = [Card.wild_card(), Card.wild_card()]
        for i in range(Card.num_values):
            for j in range(Card.num_colors):
                for k in range(Card.num_shapes):
                    self.pile.append(Card(i + 1, j + 1, k + 1, False))
        assert len(self.pile) == Pile.num_cards
        shuffle(self.pile)

    def get_next(self):
        """ Get the next card from the pile
        :return Card: the next card on the pile
        """
        if self.has_next():
            return self.pile.pop(0)
        else:
            return Card.null_card()

    def has_next(self):
        """ Does the pile have another card?
        :return bool: does the pile have another card?
        """
        return len(self.pile) > 0

    @classmethod
    def get_num_cards(cls):
        return cls.num_cards

    def size(self):
        return len(self.pile)

    def return_cards(self, cards):
        for cd in cards:
            self.pile.append(cd)
