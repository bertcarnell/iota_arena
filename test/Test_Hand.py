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
from src.utils.Hand import Hand
from src.utils.Pile import Pile
from src.utils.Card import Card


class TestHand(TestCase):
    def test_draw(self):
        h = Hand()
        self.assertEqual(h.get_num_open(), 4)
        p = Pile()
        h.draw(p)
        self.assertEqual(h.get_num_open(), 0)

    def test_num_open(self):
        h = Hand()
        self.assertEqual(h.get_num_open(), 4)

    def test_use_card(self):
        h = Hand()
        p = Pile()
        h.draw(p)
        for i in range(len(h.get_cards())):
            self.assertFalse(h.get_cards()[i].is_null())
        h.use_card(0)
        self.assertTrue(h.get_cards()[0].is_null())

    def test_get_cards(self):
        h = Hand()
        for i in range(len(h.get_cards())):
            self.assertTrue(isinstance(h.get_cards()[i], Card))
            self.assertTrue(h.get_cards()[i].is_null())



