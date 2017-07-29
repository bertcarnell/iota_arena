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


class Card(object):
    """A class for the iota card"""
    values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'wild': 0}
    shapes = {'square': 1, 'plus': 2, 'circle': 3, 'triangle': 4, 'wild': 0}
    colors = {'red': 1, 'yellow': 2, 'green': 3, 'blue': 4, 'wild': 0}
    num_values = 4
    num_colors = 4
    num_shapes = 4

    def __init__(self, value, color, shape, isWild):
        """ Initialize the Card

        :param int value: the card value
        :param int color: the card color
        :param int shape: the card shape
        :param bool isWild: is this a wild card?
        """
        self.value = value
        self.color = color
        self.shape = shape
        self.isWild = isWild

    @staticmethod
    def null_card():
        """ Create a null Card

        :returns Card: a null Card
        """
        return Card(0,0,0,False)

    def __str__(self):
        """ Create a string representation of the card

        :returns string: a string for the Card
        """
        return '<%s, %s, %s, %s>' % (self.get_value_str(), self.get_color_str(), self.get_shape_str(), self.get_wild_str())

    def __repr__(self):
        return self.__str__()

    def is_null(self):
        """ Is the Card null?

        :returns bool: is the card null?
        """
        if self.value == 0 and self.isWild == False:
            return True
        else:
            return False

    @staticmethod
    def wild_card():
        """ Create a Card representing a Wild Card

        :returns Card: a wild card
        """
        return Card(0, 0, 0, True)

    def is_wild(self):
        return self.isWild

    def get_value(self):
        """ Get the card value
        :return int: card value
        """
        return self.value

    def get_color(self):
        """ Get the card color
        :return int: card color
        """
        return self.color

    def get_shape(self):
        """ Get the card shape
        :return int: the card shape
        """
        return self.shape

    def get_value_str(self):
        """ Get the card value as a string
        :return string: the card value
        """
        for key, val in Card.values.items():
            if val == self.value:
                return key

    def get_color_str(self):
        """ Get the card color as a string
        :return string: the card color
        """
        for key, val in Card.colors.items():
            if val == self.color:
                return key

    def get_shape_str(self):
        """ Get the card shape as a string
        :return string: the card shape
        """
        for key, val in Card.shapes.items():
            if val == self.shape:
                return key

    def get_wild_str(self):
        if self.isWild:
            return 'wild'
        else:
            return 'not wild'

    def sort_order(self):
        return 125*self.value + 25*self.color + 5*self.shape + self.isWild

    def __eq__(self, other):
        if isinstance(other, Card):
            if self.sort_order() == other.sort_order():
                return True
            else:
                return False
        raise NotImplementedError()

