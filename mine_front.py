import sys
import urwid
import mine_logic

palette = [('bg', '', '', '', '#1F2', '#1FD'),
        ('field', '', '', '', '#DA3', '#2FC'),
        ('font', '', '', '', '#000', '#FEF'),
        ('grid', '', '', '', '#444', '#777'),]

def play_game(*args, **kwargs):
    # print(kwargs)
    try:
        _x, _y = kwargs['x'], kwargs['y']
        print(str(_x) + ", " + str(_y))
    except:
        e = sys.exc_info()[0]
        print("Error: %s" %e)
        return
    mine = mine_logic.Minesweeper(_x, _y)
    mine.start_game()

    # display_field = [[0 for x in range(_x)] for y in range(_y)]
    display_field = list()
    col_width, h_space, v_space = 10, 1, 1

    print(len(display_field))
    for x in range(0, _x):
        for y in range(0, _y):
            try:
                display_field.append(urwid.AttrMap(urwid.Button(('font', str(mine.field.field[x][y])), on_press=handle_click), 'grid'))
            except IndexError as e:
                print(str(e) + '; x=' + str(x) + ', y=' + str(y))
                return

    print(str(type(display_field)) + ";; length: " + str(len(display_field)))
    grid = urwid.GridFlow(cells=display_field, cell_width=5, h_sep=1, v_sep=1, align='center')
    loop = urwid.MainLoop(widget=urwid.Filler(urwid.Padding(urwid.AttrMap(grid, 'bg'), 
        left=int((col_width + 9 * (col_width + h_space)) / 2), right=int((col_width + 9 * (col_width + h_space)) / 2))),
            palette=palette, handle_mouse=True, unhandled_input=exit_on_q)
    loop.screen.set_mouse_tracking(enable=True)
    loop.screen.set_terminal_properties(colors=256) # highcolor
    try:
        loop.run()
    except ValueError as e:
        print("ValueError: " + str(e))

def exit_on_q(e):
    if e in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def handle_click(e):
    value = int(e.get_label())
    if value == -1:
        print('')
        raise urwid.ExitMainLoop()
    elif value == 0:
        pass
    else:
        pass

def draw_field():
    pass

play_game(0, x=10, y=10)
