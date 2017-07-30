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
from src.utils.Sequence import Sequence
from src.utils.Card import Card


class TestSequence(TestCase):
    def test_add(self):
        s = Sequence()
        s.add(Card.wild_card())
        s.add(Card.wild_card())
        self.assertEqual(len(s.get_cards()), 2)
        self.assertTrue(s.get_cards()[0].is_wild())

        self.assertRaises(NotImplementedError, s.add, "5")

    def test_add_cards(self):
        s = Sequence()
        s.add_cards([Card.null_card(), Card.wild_card()])

        self.assertEqual(len(s.get_cards()), 2)

        self.assertRaises(NotImplementedError, s.add_cards, [1,2,3])

    def test_get_cards(self):
        s = Sequence()
        a = Card(1, 2, 3, False)
        s.add(a)
        self.assertTrue(s.get_cards()[0] == a)

    def test_is_valid_sequence(self):
        # all valid sequences
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    s = Sequence()
                    s.add(Card(i+1, j+1, k+1, False))
                    self.assertTrue(s.is_valid_sequence())
        for i in range(4):
            for j in range(i,4):
                s = Sequence()
                s.add(Card(i+1, 1, 1, False))
                s.add(Card(j+1, 2, 1, False))
                self.assertTrue(s.is_valid_sequence())
        i = [1,1,1,1,2,2,3,4]
        j = [1,2,2,3,3,2,3,4]
        k = [1,3,4,4,4,2,3,4]
        for m in range(len(i)):
            s = Sequence()
            s.add(Card(4, i[m], 4, False))
            s.add(Card(4, j[m], 4, False))
            s.add(Card(4, k[m], 4, False))
            self.assertTrue(s.is_valid_sequence())
        i = [1,1,2,3,4]
        j = [2,1,2,3,4]
        k = [3,1,2,3,4]
        m = [4,1,2,3,4]
        for n in range(len(i)):
            s = Sequence()
            s.add(Card(1, 4, i[n], False))
            s.add(Card(2, 3, j[n], False))
            s.add(Card(3, 2, k[n], False))
            s.add(Card(4, 1, m[n], False))
            self.assertTrue(s.is_valid_sequence())

        # all invalid sequences
        s = Sequence()
        self.assertFalse(s.is_valid_sequence())
        s.add(Card.null_card())
        self.assertFalse(s.is_valid_sequence())
        s = Sequence()
        s.add(Card(1, 2, 3, False))
        s.add(Card(2, 2, 3, False))
        s.add(Card(3, 2, 3, False))
        s.add(Card(4, 2, 3, False))
        s.add(Card(0, 2, 3, False))
        self.assertFalse(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False)])
        self.assertTrue(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 1, False)])
        self.assertTrue(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 1, False), Card(1, 3, 1, False)])
        self.assertTrue(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 1, False), Card(2, 3, 1, False)])
        self.assertFalse(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 1, False), Card(1, 3, 1, False), Card(1, 4, 1, False)])
        self.assertTrue(s.is_valid_sequence())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 1, False), Card(2, 3, 1, False), Card(1, 4, 1, False)])
        self.assertFalse(s.is_valid_sequence())

    def test_is_all_same_value(self):
        s = Sequence()
        s.add(Card(1, 1, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 3, 3, False))
        s.add(Card(1, 4, 3, False))
        self.assertTrue(s.is_all_same_value())
        s = Sequence()
        s.add(Card(1, 1, 3, False))
        s.add(Card(2, 2, 3, False))
        s.add(Card(1, 3, 3, False))
        s.add(Card(1, 4, 3, False))
        self.assertFalse(s.is_all_same_value())

        s = Sequence()
        s.add_cards([Card.null_card(), Card.null_card()])
        self.assertTrue(s.is_all_same_value())

        s = Sequence()
        s.add_cards([Card(1,1,1,False), Card(1,2,2,False), Card(1,3,3,False)])
        self.assertTrue(s.is_all_same_value())

        s = Sequence()
        s.add_cards([Card(1,1,1,False), Card(1,2,2,False), Card(3,3,3,False)])
        self.assertFalse(s.is_all_same_value())

    def test_is_all_same_shape(self):
        s = Sequence()
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        self.assertTrue(s.is_all_same_shape())
        s = Sequence()
        s.add(Card(1, 1, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 1, 3, False))
        s.add(Card(1, 1, 4, False))
        self.assertFalse(s.is_all_same_shape())

        s = Sequence()
        s.add_cards([Card.null_card(), Card.null_card()])
        self.assertTrue(s.is_all_same_shape())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(2, 1, 1, False), Card(3, 1, 1, False)])
        self.assertTrue(s.is_all_same_shape())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 2, False), Card(3, 3, 3, False)])
        self.assertFalse(s.is_all_same_shape())

    def test_is_all_same_color(self):
        s = Sequence()
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 2, 3, False))
        self.assertTrue(s.is_all_same_color())
        s = Sequence()
        s.add(Card(1, 1, 3, False))
        s.add(Card(2, 2, 3, False))
        s.add(Card(1, 1, 3, False))
        s.add(Card(1, 1, 3, False))
        self.assertFalse(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card.null_card(), Card.null_card()])
        self.assertTrue(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(2, 1, 2, False), Card(1, 1, 3, False)])
        self.assertTrue(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 2, 2, False), Card(3, 3, 3, False)])
        self.assertFalse(s.is_all_same_color())

    def test_is_all_different_value(self):
        s = Sequence()
        s.add(Card(1, 1, 3, False))
        s.add(Card(2, 2, 3, False))
        s.add(Card(3, 1, 3, False))
        s.add(Card(4, 1, 3, False))
        self.assertFalse(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 1, 3, False), Card(2, 2, 1, False)])
        self.assertFalse(s.is_all_different_value())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(2, 2, 2, False), Card(4, 3, 3, False)])
        self.assertTrue(s.is_all_different_value())

    def test_is_all_different_color(self):
        s = Sequence()
        s.add(Card(1, 4, 3, False))
        s.add(Card(2, 3, 3, False))
        s.add(Card(1, 2, 3, False))
        s.add(Card(1, 1, 3, False))
        self.assertFalse(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 1, 3, False), Card(2, 2, 1, False)])
        self.assertFalse(s.is_all_different_value())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(2, 2, 2, False), Card(4, 3, 3, False)])
        self.assertTrue(s.is_all_different_value())

    def test_is_all_different_shape(self):
        s = Sequence()
        s.add(Card(1, 1, 2, False))
        s.add(Card(2, 2, 1, False))
        s.add(Card(1, 1, 3, False))
        s.add(Card(1, 1, 4, False))
        self.assertFalse(s.is_all_same_color())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(1, 1, 3, False), Card(2, 2, 1, False)])
        self.assertFalse(s.is_all_different_value())

        s = Sequence()
        s.add_cards([Card(1, 1, 1, False), Card(2, 2, 2, False), Card(4, 3, 3, False)])
        self.assertTrue(s.is_all_different_value())

    def test_sort(self):
        s = Sequence()
        s.add(Card(1, 4, 2, False))
        s.add(Card(1, 2, 2, False))
        s.add(Card(1, 3, 2, False))
        s.add(Card(1, 1, 2, False))
        s.sort()
        self.assertEqual(s.get_cards()[0], Card(1, 1, 2, False))

    def test_eq(self):
        s1 = Sequence()
        s2 = Sequence()
        s1.add(Card(1,1,1,False))
        s1.add(Card(2,2,2,False))
        s2.add(Card(1,1,1,False))
        s2.add(Card(2,2,2,False))
        s3 = Sequence()
        s3.add(Card(3,3,3,False))
        self.assertEqual(s1, s2)
        self.assertFalse(s1 == s3)

        self.assertRaises(NotImplementedError, lambda: s1 == 5)

    def test_sum_scores(self):
        s1 = Sequence()
        s1.add(Card(1, 1, 1, False))
        s1.add(Card(2, 2, 2, False))
        self.assertEqual(s1.get_sum_scores(), 3)

    def test_length(self):
        s1 = Sequence()
        s1.add(Card(1, 1, 1, False))
        s1.add(Card(2, 2, 2, False))
        self.assertEqual(s1.length(), 2)

    def test_hash(self):
        s1 = Sequence()
        hs1 = hash(s1)
        s2 = Sequence()
        s2.add(Card(1, 1, 1, False))
        s2.add(Card(2, 2, 2, False))
        hs2 = hash(s2)
        s3 = Sequence()
        s3.add(Card(1,1,1,False))
        s3.add(Card(2,2,2,False))
        hs3 = hash(s3)
        s4 = Sequence()
        s4.add(Card(3,3,3,False))
        hs4 = hash(s4)

        self.assertEqual(hs2, hs3)
        self.assertFalse(hs1 == hs2)
        self.assertFalse(hs4 == hs2)
