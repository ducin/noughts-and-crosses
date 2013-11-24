# importing module from one directory above
import os
import sys
from nac.game import Game

import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def assertNextMove(self, move):
        self.assertEqual(self.game.continues(), True)
        self.assertEqual(self.game.winner, None)
        self.assertEqual(self.game.turn, move)

    def test_shuffle(self):
        self.assertNextMove('X')
        self.assertEqual(self.game.fields, [None, None, None, None, None, None, None, None, None])
        self.game._set(0)
        self.assertNextMove('O')
        self.assertEqual(self.game.fields, ['X', None, None, None, None, None, None, None, None])
        self.game._set(1)
        self.assertNextMove('X')
        self.assertEqual(self.game.fields, ['X', 'O', None, None, None, None, None, None, None])
        self.game._set(2)
        self.assertNextMove('O')
        self.assertEqual(self.game.fields, ['X', 'O', 'X', None, None, None, None, None, None])
        self.game._set(3)
        self.assertNextMove('X')
        self.assertEqual(self.game.fields, ['X', 'O', 'X', 'O', None, None, None, None, None])
        self.game._set(4)
        self.assertNextMove('O')
        self.assertEqual(self.game.fields, ['X', 'O', 'X', 'O', 'X', None, None, None, None])
        self.game._set(5)
        self.assertNextMove('X')
        self.assertEqual(self.game.fields, ['X', 'O', 'X', 'O', 'X', 'O', None, None, None])
        self.game._set(6)
        self.assertEqual(self.game.fields, ['X', 'O', 'X', 'O', 'X', 'O', 'X', None, None])
        self.assertEqual(self.game.continues(), False)
        self.assertEqual(self.game.winner, 'X')

    def merge_move_seq(self, x, y):
        '''
        Assuming: len(x) == len(y) OR len(x) == len(y) + 1
        '''
        seq = (len(x) + len(y)) * [None]
        seq[::2] = x
        seq[1::2] = y
        return seq

    def test_x_wins(self):
        '''
        X should win this game:
         X | X | X 
        ---+---+---
         O | O |(5)
        ---+---+---
        (6)|(7)|(8)
        '''
        for move in self.merge_move_seq(x=[0,1,2], y=[3,4]):
            self.game._set(move)
        self.assertEqual(self.game.winner, 'X')
        self.assertEqual(self.game.continues(), False)

    def test_y_wins(self):
        '''
        O should win this game:
         O | X | X 
        ---+---+---
        (3)| O | X 
        ---+---+---
        (6)|(7)| O 
        '''
        for move in self.merge_move_seq(x=[1,2,5], y=[0,4,8]):
            self.game._set(move)
        self.assertEqual(self.game.winner, 'O')
        self.assertEqual(self.game.continues(), False)

    def test_noone_wins(self):
        '''
        Noone should win this game:
         O | X | O 
        ---+---+---
         X | O | X 
        ---+---+---
         X | O | X
        '''
        for move in self.merge_move_seq(x=[1,3,5,6,8], y=[0,4,7,2]):
            self.game._set(move)
        self.assertEqual(self.game.winner, None)
        self.assertEqual(self.game.continues(), False)

if __name__ == '__main__':
    unittest.main()
