import win32api, win32con, win32gui, win32ui
import threading
import time
import string
import ctypes

import screencanvas

windowText = 'a foo barred'

# New code: Attempt to change the text 1 second later
def customDraw(hWindow):
    global windowText
    time.sleep(1.0)
    windowText = 'Something new'
    win32gui.RedrawWindow(hWindow, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
    # win32gui.CloseWindow(hWindow)

def main():
    canvas = screencanvas.ScreenCanvas()
    letters = string.ascii_lowercase
    xsize = canvas.width // len(letters)
    xremainder = canvas.width % len(letters) 
    ysize = canvas.height // len(letters)
    yremainder = canvas.height % len(letters)
    y = 0
    for i, row_letter in enumerate(letters):
        x = 0
        for j, col_letter in enumerate(letters):
            canvas.add_rectangle(x, y, xsize, ysize, f'{row_letter}{col_letter}')
            x += xsize
            if j < xremainder:
                x += 1
        y += ysize 
        if i < yremainder:
            y += 1
    canvas.render()
    s = time.time()
    while time.time() - s < 10:
        win32gui.PumpWaitingMessages()
    print('dun')

def wndProc(hWnd, message, wParam, lParam):
    if message == win32con.WM_PAINT:
        hdc, paintStruct = win32gui.BeginPaint(hWnd)

        dpiScale = win32ui.GetDeviceCaps(hdc, win32con.LOGPIXELSX) / 60.0
        fontSize = 20

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
        lf = win32gui.LOGFONT()
        lf.lfFaceName = "Times New Roman"
        lf.lfHeight = int(round(dpiScale * fontSize))
        #lf.lfWeight = 150
        # Use nonantialiased to remove the white edges around the text.
        lf.lfQuality = win32con.NONANTIALIASED_QUALITY
        hf = win32gui.CreateFontIndirect(lf)
        win32gui.SelectObject(hdc, hf)

        rect = win32gui.GetClientRect(hWnd)
        _, _, width, height = win32gui.GetClientRect(hWnd)
        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd162498(v=vs.85).aspx
        win32gui.DrawText(
            hdc,
            windowText,
            -1,
            rect,
            win32con.DT_CENTER | win32con.DT_NOCLIP | win32con.DT_SINGLELINE | win32con.DT_VCENTER
        )
        win32gui.EndPaint(hWnd, paintStruct)
        return 0

    elif message == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)
        return 0

    else:
        return win32gui.DefWindowProc(hWnd, message, wParam, lParam)


if __name__ == '__main__':
    main()