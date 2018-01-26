import sys
import range

class Field:
    def __init__(self, **kwargs):
        if len(kwargs) != 2:
            print("Improper initializer")
        else: 
            try: 
                self._x = kwargs[x]
                self._y = kwargs[y]
            except:
                e = sys.exc_info()[0]
                write_to_page("<p>Error: %s</p>" %e)
            self.field = [[0 for w in range(self._x)] for h in range(self._y)]
            gen_objs()

    def gen_objs(self):
        gen_bombs()
        gen_nums()

    def gen_bombs(self):
        bomb_num = (self.x * self.y) / 5
        # -1 for bombs
        for i in range(bomb_num):             
            self.field[random.randint(0, self._x)][random.randint(0, self._y)] = -1

    def gen_nums(self):
        for x in range(self._x):
            for y in range(self._y):
                if self.field[x][y] != -1:
                    self.field[x][y] = sum_bombs(i, j) 

    def sum_bombs(self, x, y):
        sum = 0
        if x != 0: sum = sum + int(self.field[x - 1][y] == -1)
        if y != 0: sum = sum + int(self.field[x][y - 1] == -1)
        if x != self._x - 1: sum = sum + int(self.field[x + 1][y] == -1)
        if y != self._y - 1: sum = sum + int(self.field[x][y + 1] == -1)
        if x != 0 and y != 0: sum = sum + int(self.field[x - 1][y - 1] == -1)
        if x != 0 and y != self._y: sum = sum + int(self.field[x - 1][y + 1] == -1)
        if x != self._x and y != 0: sum = sum + int(self.field[x + 1][y - 1] == -1)
        if x != self._x and y != self._y: sum = sum + int(self.field[x + 1][y + 1] == -1)
        return sum

class Minesweeper:
    def start_game(*args, **kwargs):
        self._x, self._y = kwargs['x'], kwargs['y']
        uncovered = [2] # format: squares, mines
    
        field = Minesweeper(x=self._x, y=self._y)
    
    def handle_click(e):
        pass
    
