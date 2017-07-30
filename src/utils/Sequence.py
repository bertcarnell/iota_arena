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


class Sequence(object):

    def __init__(self):
        self.cards = []

    def add(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise NotImplementedError("Sequences are made of Cards only")

    def add_cards(self, cards):
        if isinstance(cards[0], Card):
            for cd in cards:
                self.cards.append(cd)
        else:
            raise NotImplementedError("Sequences are made of Cards only")

    def get_cards(self):
        return self.cards

    def sort(self):
        if len(self.cards) > 1:
            self.cards.sort(key=lambda x: x.sort_order())

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            raise NotImplementedError()
        return self.cards == other.get_cards()

    def __hash__(self):
        if len(self.cards) == 0:
            return hash(0)
        return hash("".join(str(cd) for cd in self.cards))

    def get_sum_scores(self):
        score = 0
        for cd in self.cards:
            score += cd.get_value()
        return score

    def length(self):
        return len(self.cards)

    def is_valid_sequence(self):
        # if the sequence is too long or not a sequence at all, then return False
        if len(self.cards) < 1 or len(self.cards) > 4:
            return False
        # if the sequence contains nulls, then return False
        if any(cd.is_null() for cd in self.cards):
            return False
        # any one card or any two cards in a sequence is valid
        if len(self.cards) == 1 or len(self.cards) == 2:
            return True
        # if the sequence is not all the same value or different values, return False
        bvalue = not self.is_all_same_value() and not self.is_all_different_value()
        bcolor = not self.is_all_same_color() and not self.is_all_different_color()
        bshape = not self.is_all_same_shape() and not self.is_all_different_shape()
        if bvalue or bcolor or bshape:
            return False
        # otherwise return True
        return True

    def is_all_same_value(self):
        # TODO: does not work with wilds
        first = self.cards[0].get_value()
        return all(cd.get_value() == first for cd in self.cards)

    def is_all_same_shape(self):
        # TODO: does not work with wilds
        first = self.cards[0].get_shape()
        return all(cd.get_shape() == first for cd in self.cards)

    def is_all_same_color(self):
        # TODO: does not work with wilds
        first = self.cards[0].get_color()
        return all(cd.get_color() == first for cd in self.cards)

    def is_all_different_value(self):
        # TODO: does not work with two wilds
        return len(set(cd.get_value() for cd in self.cards)) == len(self.cards)

    def is_all_different_color(self):
        # TODO: does not work with two wilds
        return len(set(cd.get_color() for cd in self.cards)) == len(self.cards)

    def is_all_different_shape(self):
        # TODO: does not work with two wilds
        return len(set(cd.get_shape() for cd in self.cards)) == len(self.cards)
