import win32api, win32con, win32gui, win32ui
import threading
import time
import ctypes
import keyboard
import functools

from context import screengrid

def foo():
    main_grid = screengrid.Grid()
    main_grid.draw_letter_grid(click=True)
    time.sleep(5)
    main_grid.font_color = 100, 100, 100

def main():
    threading.Thread(target=foo, daemon=True).start()
    input()

if __name__ == '__main__':
    main()