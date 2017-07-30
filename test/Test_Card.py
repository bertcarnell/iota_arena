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
from src.utils.Card import Card


class TestCard(TestCase):
    def test_card(self):
        a = Card(Card.values['one'], Card.colors['blue'], Card.shapes['square'], False)
        self.assertEqual(a.value, 1)
        self.assertEqual(a.shape, 1)
        self.assertEqual(a.color, 4)
        self.assertEqual(a.get_value(), 1)
        self.assertEqual(a.get_shape(), 1)
        self.assertEqual(a.get_color(), 4)
        self.assertEqual(a.get_value_str(), 'one')
        self.assertEqual(a.get_shape_str(), 'square')
        self.assertEqual(a.get_color_str(), 'blue')
        self.assertEqual(a.get_wild_str(), 'not wild')
        self.assertFalse(a.isWild)
        self.assertFalse(a.is_wild())
        b = Card.null_card()
        self.assertEqual(b.get_value(), 0)
        self.assertEqual(b.get_shape(), 0)
        self.assertEqual(b.get_color(), 0)
        self.assertFalse(b.isWild)
        self.assertFalse(b.is_wild())
        d = Card.wild_card()
        self.assertEqual(d.get_value(), 0)
        self.assertEqual(d.get_shape(), 0)
        self.assertEqual(d.get_color(), 0)
        self.assertTrue(d.isWild)
        self.assertTrue(d.is_wild())
        self.assertEqual(d.get_wild_str(), 'wild')

    def test_null_card(self):
        a = Card.null_card()
        self.assertEqual(a.get_value(), Card.values['wild'])
        self.assertEqual(a.get_shape(), Card.shapes['wild'])
        self.assertEqual(a.get_color(), Card.colors['wild'])
        self.assertFalse(a.is_wild())

    def test_wild_card(self):
        a = Card.wild_card()
        self.assertEqual(a.get_value(), Card.values['wild'])
        self.assertEqual(a.get_shape(), Card.shapes['wild'])
        self.assertEqual(a.get_color(), Card.colors['wild'])
        self.assertTrue(a.is_wild())

    def test_str(self):
        a = Card(Card.values['one'], Card.colors['blue'], Card.shapes['square'], False)
        self.assertEqual(str(a), "<one, blue, square, not wild>")

    def test_repr(self):
        a = Card(Card.values['one'], Card.colors['blue'], Card.shapes['square'], False)
        self.assertEqual(repr(a), "<one, blue, square, not wild>")

    def test_sort_order(self):
        a = Card(1, 1, 1, False)
        self.assertEqual(a.sort_order(), 1*125+1*25+1*5+0)

    def test_eq(self):
        a = Card(1, 1, 1, False)
        b = Card(1, 1, 1, False)
        self.assertEqual(a, a)
        self.assertEqual(b, b)
        self.assertTrue(a == a)
        self.assertTrue(b == b)

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for m in [False, True]:
                        if i == 1 and j == 1 and k == 1 and not m:
                            self.assertTrue(a == Card(i, j, k, m))
                            continue
                        self.assertFalse(a == Card(i, j, k, m))
        self.assertRaises(NotImplementedError, a.__eq__, 5)

    def test_ne(self):
        a = Card(1, 1, 1, False)
        b = Card(1, 2, 1, False)
        self.assertTrue(a != b)
        self.assertFalse(b != b)

        self.assertRaises(NotImplementedError, a.__ne__, 5)



