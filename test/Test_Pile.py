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
from unittest import TestCase
from random import shuffle, seed
from src.utils.Pile import Pile
from src.utils.Card import Card


class TestPile(TestCase):
    def test_pile(self):
        p = Pile()
        self.assertEqual(p.size(), Pile.get_num_cards())
        self.assertTrue(p.has_next())
        self.assertEqual(type(p.get_next()), type(Card.null_card()))
        self.assertEqual(p.size(), Pile.get_num_cards() - 1)
        self.assertTrue(p.has_next())
        self.assertTrue(p.get_next().get_value() < 5)
        self.assertEqual(p.size(), Pile.get_num_cards() - 2)
        # set the seed so that the shuffle is done the same way
        seed(1976)
        p1 = Pile()
        c1 = p1.get_next()
        self.assertEqual(c1.get_value(), 3)
        self.assertEqual(c1.get_color_str(), "blue")
        self.assertEqual(c1.get_shape_str(), "circle")
        p2 = Pile()
        for i in range(Pile.get_num_cards()):
            self.assertTrue(p2.has_next())
            c2 = p2.get_next()
        self.assertTrue(not p2.has_next())
        self.assertEqual(p2.get_next(), Card.null_card())

    def test_return_cards(self):
        p = Pile()
        c1 = p.get_next()
        c2 = p.get_next()
        c3 = p.get_next()
        c4 = p.get_next()
        self.assertEqual(p.size(), Pile.get_num_cards() - 4)
        p.return_cards([c1, c2])
        self.assertEqual(p.size(), Pile.get_num_cards() - 2)
        c5 = p.get_next()
        self.assertFalse(c5 == c2)
        self.assertFalse(c5 == c1)
