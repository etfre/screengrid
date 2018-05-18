import tkinter, win32api, win32con, pywintypes
import sys
import time
import string
import threading

def cli(canvas):
    input()
    canvas.master.destroy()

def add_rectangles(canvas):
    # label = tkinter.Label(text='Text on the screen', font=('Times New Roman','80'), fg='black', bg='white')
    font = ("Purisa", 14)
    t = time.time()
    for i in range(1, 27):
        for j in range(1, 27):
            text = string.ascii_lowercase[j-1] + string.ascii_lowercase[i-1]
            canvas.create_text(i * 58, j * 31, font=font, text=text)
    e = time.time()
    print(e-t)

def init_canvas():
    canvas = tkinter.Canvas()
    canvas.config(width=1920, height=1080)
    canvas.master.overrideredirect(True)
    # canvas.master.geometry("+250+250")
    canvas.master.lift()
    canvas.master.attributes('-alpha', 0.2)
    canvas.master.wm_attributes("-topmost", True)
    canvas.master.wm_attributes("-disabled", True)
    canvas.master.wm_attributes("-transparentcolor", "white")
    canvas.pack()

    canvas.create_line(0, 0, 200, 100)
    canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

    canvas.create_rectangle(50, 25, 150, 75, fill="blue")
    hWindow = pywintypes.HANDLE(int(canvas.master.frame(), 16))
    # # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
    # # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
    return canvas

canvas = init_canvas()
add_rectangles(canvas)

threading.Thread(target=cli, daemon=True, args=(canvas,)).start()

canvas.mainloop()