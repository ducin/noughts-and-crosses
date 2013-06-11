
class Game():
    '''Game class implements Noughts and Crosses game logic'''

    X = 'X'
    O = 'O'

    combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.fields = [[None, None, None],[None, None, None],[None, None, None]]
        self.turn = self.X
        self.winner = None

    def switch(self):
        self.turn = self.O if self.turn == self.X else self.X

    def set(self, position):
        if (not position in range(9)) or (self.get(position) != None):
            return False
        self.fields[position // 3][position % 3] = self.turn
        self.switch()
        self.checkWinner()
        return True

    def get(self, position):
        return self.fields[position // 3][position % 3]

    def continues(self):
        return self.winner == None

    def checkWinner(self):
        for c in self.combinations:
            if self.get(c[0]) == self.get(c[1]) == self.get(c[2]) and self.get(c[0]) != None:
                self.winner = self.get(c[0])
                break
        if (not None in self.fields[0]) and (not None in self.fields[1]) and (not None in self.fields[2]):
            self.winner = False

    def display(self):
        self.display_advanced()

    def display_simple(self):
        for line in self.fields:
            print line
        print

    def get_element_display(self, position):
        if self.get(position) == None:
            return '(' + str(position) + ')'
        else:
            return ' ' + self.get(position) + ' '

    def display_advanced(self):
        str = '\n'
        tmp_all = []
        for a in range(3):
            tmp_line = []
            for b in range(3):
                tmp_line.append(self.get_element_display(a*3 + b))
            str_line = '|'.join(tmp_line) + '\n'
            tmp_all.append(str_line)
        str += '---+---+---\n'.join(tmp_all)
        print str
