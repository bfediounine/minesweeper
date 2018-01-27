import sys
import random

def bomb_num(x, y):
    return int(x * y / 5)

class Field:
    def __init__(self, x, y):
        self._y, self._x = x, y
        self.field = [[0 for x in range(self._x)] for y in range(self._y)]
        self.gen_objs()

    def gen_objs(self):
        self.gen_bombs()
        self.gen_nums()

    def gen_bombs(self):
        _bomb_num = bomb_num(self._x, self._y)
        # -1 for bombs
        for i in range(_bomb_num):             
            self.field[random.randint(0, self._x - 1)][random.randint(0, self._y - 1)] = -1

    def gen_nums(self):
        for x in range(self._x):
            for y in range(self._y):
                if self.field[x][y] != -1:
                    self.field[x][y] = self.sum_bombs(x, y) 

    def sum_bombs(self, x, y):
        sum = 0
        if x != 0: sum = sum + int(self.field[x - 1][y] == -1)
        if y != 0: sum = sum + int(self.field[x][y - 1] == -1)
        if x != self._x - 1: sum = sum + int(self.field[x + 1][y] == -1)
        if y != self._y - 1: sum = sum + int(self.field[x][y + 1] == -1)
        if x != 0 and y != 0: sum = sum + int(self.field[x - 1][y - 1] == -1)
        if x != 0 and y != self._y - 1: sum = sum + int(self.field[x - 1][y + 1] == -1)
        if x != self._x - 1 and y != 0: sum = sum + int(self.field[x + 1][y - 1] == -1)
        if x != self._x - 1 and y != self._y - 1: sum = sum + int(self.field[x + 1][y + 1] == -1)
        return sum

class Minesweeper:
    def __init__(self, x, y):
        self._x, self._y = x, y

    def start_game(self):
        self.uncovered = [0, 0] # format: squares, mines
        self.uncovered_field = [[0 for x in range(self._x)] for y in range(self._y)]
        self.field = Field(self._x, self._y)
    
    def handle_click(e):
        pass
    
