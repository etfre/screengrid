import win32api, win32con, win32gui, win32ui
import threading
import time
import string
import ctypes
import keyboard
import functools

import screencanvas
import grid
import mouse

done = False

LETTERS = set(string.ascii_lowercase)

def on_press(main_grid, key):
    global done
    if key.event_type == 'down':
        return
    if key.name in LETTERS:
        if len(main_grid.selection) == 1:
            x, y = main_grid.centers[f'{main_grid.selection}{key.name}']
            mouse.move(x, y)
            main_grid.empty()
        else:
            main_grid.draw_letter_grid(row=key.name)
            main_grid.selection += key.name
    elif key.name == 'backspace':
        main_grid.draw_letter_grid()
    elif key.name == 'esc':
        main_grid.empty()

def main():
    main_grid = grid.Grid()
    main_grid.draw_letter_grid()
    hook = keyboard.hook(functools.partial(on_press, main_grid), suppress=True)
    s = time.time()
    while time.time() - s < 10:
        win32gui.PumpWaitingMessages()
    keyboard.unhook_all()
    print('dun')

if __name__ == '__main__':
    main()