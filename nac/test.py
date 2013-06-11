import unittest
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_shuffle(self):
        self.assertEqual(self.game.fields, [[None, None, None],[None, None, None],[None, None, None]])
        self.game._set(0)
        self.assertEqual(self.game.fields, [['X', None, None],[None, None, None],[None, None, None]])
        self.game._set(1)
        self.assertEqual(self.game.fields, [['X', 'O', None],[None, None, None],[None, None, None]])

if __name__ == '__main__':
    unittest.main()