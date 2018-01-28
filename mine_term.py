import mine_logic, sys, os
from functools import reduce

def main():
    if (len(sys.argv[1:]) != 4):
        print("Usage: py mine_term.py -x [xval] -y [yval]")
    else:
        try:
            _x, _y = int(sys.argv[2]), int(sys.argv[4])
            print(str(_x) + ", " + str(_y))
        except:
            e = sys.exc_info()[0]
            print("Error: %s" %e)
            return
        mine = mine_logic.Minesweeper(_x, _y)
        mine.start_game()
        bomb_num = mine_logic.bomb_num(_x, _y)

        # ------------DANGER ZONE------------------------------
        sys.setrecursionlimit(10000) # could lead to a crash
        # ----------needed for recursive_uncover---------------

        os.system('clear')
        print('Welcome to Python-based Minesweeper.')
        gameOver, improperFormat = False, False
        while not gameOver or mine.uncovered == _x * _y - bomb_num:
            if improperFormat:
                print('Please provide input in a valid format.')
                improperFormat = False
            print_field(mine)
            value = input('Please select a square to uncover (x, y): ')
            value_red = list(filter(isdigit, value))
            if len(value_red) != 2:
                improperFormat = True
            else:
                __x, __y = list(map(int, value_red))
                print(''.join(str(__x) + ' ' + str(__y)))
                if mine.field.field[__x][__y] == -1:
                    gameOver = True
                elif mine.field.field[__x][__y] == 0:
                    recursively_uncover(mine, __x, __y, _x, _y)
                else:
                    mine.uncovered_field[__x][__y] = 1
                    mine.uncovered += 1
            os.system('clear')
    
        print_bombs(mine) if gameOver else print_victory()

def isdigit(i): return i.isdigit()

def recursively_uncover(mine, x, y, width, height):
    mine.uncovered_field[x][y] = 1
    mine.uncovered += 1

    try:
        if x != 0 and not bool(mine.field.field[x-1][y]) and not bool(mine.uncovered_field[x-1][y]):
            recursively_uncover(mine, x-1, y, width, height)
        else: 
            mine.uncovered_field[x-1][y] = 1
            mine.uncovered += 1

        if y != 0 and not bool(mine.field.field[x][y-1]) and not bool(mine.uncovered_field[x][y-1]):
             recursively_uncover(mine, x, y-1, width, height)
        else:
            mine.uncovered_field[x][y-1] = 1
            mine.uncovered += 1

        if x != width - 1 and not bool(mine.field.field[x+1][y]) and not bool(mine.uncovered_field[x+1][y]):
            recursively_uncover(mine, x+1, y, width, height)
        else:
            mine.uncovered_field[x+1][y] = 1
            mine.uncovered += 1

        if y != height - 1 and not bool(mine.field.field[x][y+1]) and not bool(mine.uncovered_field[x][y+1]):
            recursively_uncover(mine, x, y+1, width, height)
        else:
            mine.uncovered_field[x][y+1] = 1
            mine.uncovered += 1

        if x != 0 and y != 0 and not bool(mine.field.field[x-1][y-1]) and not bool(mine.uncovered_field[x-1][y-1]):
                recursively_uncover(mine, x-1, y-1, width, height)
        else:
            mine.uncovered_field[x-1][y-1] = 1
            mine.uncovered += 1

        if x != 0 and y != height - 1 and not bool(mine.field.field[x-1][y+1]) and not bool(mine.uncovered_field[x-1][y+1]):
                recursively_uncover(mine, x-1, y+1, width, height)
        else:
            mine.uncovered_field[x-1][y+1] = 1
            mine.uncovered += 1

        if x != width - 1 and y != 0 and not bool(mine.field.field[x+1][y-1]) and not bool(mine.uncovered_field[x+1][y-1]):
                recursively_uncover(mine, x+1, y-1, width, height)
        else:
            mine.uncovered_field[x+1][y-1] = 1
            mine.uncovered += 1

        if x != width - 1 and y != height - 1 and not bool(mine.field.field[x+1][y+1]) and not bool(mine.uncovered_field[x+1][y+1]):
                recursively_uncover(mine, x+1, y+1, width, height)
        else:
            mine.uncovered_field[x+1][y+1] = 1
            mine.uncovered += 1
    except RecursionLimit as e:
        print('Higher RecursionLimit needed...')
    finally:
        return

def print_bombs(mine):
    for i, _i in enumerate(mine.field.field):
        for j, _j in enumerate(mine.field.field[i]):
            if _j == -1: mine.uncovered_field[i][j] = 1
    print_field(mine)
    print('Sorry, but you\'ve fallen victim to a bomb. RIP in peace.')

def print_victory():
    print('Well done kiddo! Field properly disarmed.')

def print_field(mine):
    sys.stdout.flush()
    for i, _i in enumerate(mine.field.field):
        sys.stdout.write('|')
        for j, _j in enumerate(mine.field.field[i]):
            if not bool(mine.uncovered_field[i][j]):
                sys.stdout.write('__|')
            else:
                sys.stdout.write('  |' if j == 0 else '%2d|' %_j)
        print() #newline

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('\nGoodbye!')
