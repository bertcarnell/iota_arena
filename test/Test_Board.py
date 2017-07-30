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
        # test normal operation
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

        # test looking off the board
        self.assertRaises(ValueError, lambda: b.find_adjacent_cards(a7, 1000, 1000))

        # test an empty board
        empty_board = Board()
        self.assertTrue(empty_board.is_empty())
        n1, n2 = empty_board.find_adjacent_cards(a7, 10, 10)
        self.assertTrue(n1 is None)
        self.assertTrue(n2 is None)

        # test invalid sequence
        b = Board()
        b.place_cards([a1, a2, a7], [[10,9],[10,11],[10,12]])
        hor, ver = b.find_adjacent_cards(a5, 10, 10)
        self.assertTrue(hor is None)
        self.assertTrue(ver is None)

        # test corners
        b = Board()
        b.place_cards([a1,a2,a7], [[0,0],[0,1],[1,0]])
        hor, ver = b.find_adjacent_cards(a1, 0, 0)
        self.assertTrue(hor is not None)
        self.assertTrue(ver is not None)

        b = Board()
        b.place_cards([a1,a2,a7], [[b.max_x-1,0],[b.max_x-1,1],[b.max_x-2,0]])
        hor, ver = b.find_adjacent_cards(a1, b.max_x-1, 0)
        self.assertTrue(hor is not None)
        self.assertTrue(ver is not None)

        b = Board()
        b.place_cards([a1,a2,a7], [[0,b.max_y-1],[0,b.max_y-2],[1,b.max_y-1]])
        hor, ver = b.find_adjacent_cards(a1, 0, b.max_y-1)
        self.assertTrue(hor is not None)
        self.assertTrue(ver is not None)

        b = Board()
        b.place_cards([a1,a2,a7], [[b.max_x-1,b.max_y-1],[b.max_x-2,b.max_y-1],[b.max_x-1,b.max_y-2]])
        hor, ver = b.find_adjacent_cards(a1, b.max_x-1, b.max_y-1)
        self.assertTrue(hor is not None)
        self.assertTrue(ver is not None)


    def test_score_locations(self):
        # test normal operation
        b = Board()
        a1 = Card(1,1,1,False)
        a2 = Card(2,2,1,False)
        a3 = Card(2,3,1,False)
        a4 = Card(3,1,1,False)
        a5 = Card(4,1,1,False)
        a7 = Card(2,1,1,False)
        # 1
        # 2 2 2
        # 3
        # 4
        # pre-existing on the board
        b.place_cards([a1,a2,a3,a4],[[9,10],[10,11],[10,12],[11,10]])
        b.place_card(a5, [12,10])
        # card played this turn
        b.place_card(a7, [10, 10])
        # score the cards played
        score = b.score_locations([a7], [[10, 10]])
        self.assertEqual(score, (10+6)*2)

        # test errors
        self.assertRaises(ValueError, lambda: b.score_locations([a7],[[1,1],[2,2]]))
        self.assertRaises(ValueError, lambda: b.score_locations([a7],[[1,1,1]]))

        b = Board()
        #   1
        # 2 2 2 2
        #   3
        #   4
        b.place_cards([a1,a2,a3,a4],[[9,10],[10,11],[10,12],[11,10]])
        b.place_card(a5, [12,10])
        b.place_card(Card(2,4,1,False), [10,9])
        # this turn
        b.place_card(a7, [10,10])
        score = b.score_locations([a7], [[10, 10]])
        self.assertEqual(score, (10+8)*2*2)

        b = Board()
        #   1
        # 2 2 2 2
        #   3
        #   4
        b.place_cards([a1, a4, a5],[[9,10],[11,10],[12,10]])
        # this turn
        b.place_cards([Card(2,4,1,False),a7,a2,a3], [[10, 9],[10,10],[10,11],[10,12]])
        score = b.score_locations([Card(2,4,1,False),a7,a2,a3], [[10, 9],[10,10],[10,11],[10,12]])
        self.assertEqual(score, (10+8)*2*2*2)

        b = Board()
        b.place_card(a1, [10,10])
        score = b.score_locations([a1], [[10,10]])
        self.assertEqual(score, 1)
