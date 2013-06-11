
class Game():
    '''Game class implements Noughts and Crosses game logic'''

    X = 'X'
    O = 'O'

    COMBINATIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.fields = [None, None, None, None, None, None, None, None, None]
        self.turn = self.X
        self.winner = None

    def switch(self):
        self.turn = self.O if self.turn == self.X else self.X

    def set(self, position):
        if (not position in range(9)) or (self.get(position) != None):
            return False
        self.fields[position] = self.turn
        self.switch()
        self.check_winner()
        return True

    def get(self, position):
        return self.fields[position]

    def continues(self):
        return self.winner is None

    def check_winner(self):
        for c in self.COMBINATIONS:
            if self.get(c[0]) == self.get(c[1]) == self.get(c[2]) and self.get(c[0]) != None:
                self.winner = self.get(c[0])
                break
        if None not in self.fields:
            self.winner = False

    def display(self):
        fn = lambda pos: '(' + self.fields[pos] + ')' \
                if self.fields[pos] is not None else '(' + str(pos) + ')'
        print '%s|%s|%s\n---+---+---\n%s|%s|%s\n---+---+---\n%s|%s|%s\n' % \
                tuple(fn(pos) for pos in xrange(9))
