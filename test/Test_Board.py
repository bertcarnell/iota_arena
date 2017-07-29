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
from src.utils.Board import Board
from src.utils.Pile import Pile
from src.utils.Card import Card


class TestBoard(TestCase):
    def test_board(self):
        a = Board()
        self.assertEqual(a.get_board().shape[0], 2*Pile.get_num_cards())

    def test_is_empy(self):
        b = Board()
        self.assertTrue(b.is_empty())
        b.place_card(Card(1,1,1,False), [5,7])
        self.assertFalse(b.is_empty())

    def test_place_card(self):
        b = Board()
        self.assertTrue(b.is_empty())
        b.place_card(Card(1,1,1,False), [5,7])
        self.assertFalse(b.is_empty())
        self.assertEqual(b.get_board()[5,7], Card(1,1,1,False))

    def test_place_cards(self):
        b = Board()
        self.assertTrue(b.is_empty())
        b.place_cards([Card(1,1,1,False), Card(1,1,2,False)], [[5,7],[3,4]])
        self.assertFalse(b.is_empty())
        self.assertEqual(b.get_board()[5,7], Card(1,1,1,False))
        self.assertEqual(b.get_board()[3,4], Card(1,1,2,False))

        self.assertRaises(ValueError, lambda: b.place_cards([Card(1,1,1,False), Card(1,1,2,False)], [[5,7]]))
        self.assertRaises(ValueError, lambda: b.place_cards([Card.null_card(), Card.null_card(), Card.null_card(), Card.null_card(), Card.null_card()], [[1,1],[2,2],[3,3],[4,4],[5,5]]))
        self.assertRaises(ValueError, lambda: b.place_cards([Card(1,1,1,False), Card(1,1,2,False)], [[5,7,4],[1,2]]))

        b = Board()
        b.place_cards([],[])

    def test_find_adjacent_cards(self):
        b = Board()
        a1 = Card(1,1,1,False)
        a2 = Card(2,2,1,False)
        a3 = Card(2,3,1,False)
        a4 = Card(3,1,1,False)
        a5 = Card(4,1,1,False)
        a7 = Card(2,1,1,False)
        b.place_cards([a1,a2,a3,a4],[[9,10],[10,11],[10,12],[11,10]])
        b.place_card(a5, [12,10])
        hor, ver = b.find_adjacent_cards(a7, 10, 10)
        self.assertEqual(len(hor.get_cards()), 3)
        self.assertEqual(len(ver.get_cards()), 4)

        self.assertRaises(ValueError, lambda: b.find_adjacent_cards(a7, 1000, 1000))
