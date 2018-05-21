import win32api, win32con, win32gui, win32ui
import threading
import time
import string
import ctypes
import keyboard
import functools

import screencanvas
import grid

def on_press(main_grid, key):
    main_grid.draw_letter_grid(row='h')

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