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
from src.utils.Player import Player
from src.utils.Pile import Pile
from src.utils.Board import Board


class TestPlayer(TestCase):
    def test_player(self):
        p1 = Player()
        pile = Pile()
        self.assertEqual(pile.pile_index, 0)
        p1.draw(pile)
        self.assertEqual(pile.pile_index, 4)
        p1.hand.use_card(0)
        p1.draw(pile)
        self.assertEqual(pile.pile_index, 5)

        p2 = Player()
        b = Board()
        self.assertRaises(ValueError, p2.play_cards, b)