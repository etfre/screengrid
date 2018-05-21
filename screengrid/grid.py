import string
import screencanvas

class Grid:

    def __init__(self):
        self.canvas = screencanvas.ScreenCanvas()

    def draw_letter_grid(self, row=None):
        self.canvas.reset()
        letters = string.ascii_lowercase
        xsize = self.canvas.width // len(letters)
        xremainder = self.canvas.width % len(letters) 
        ysize = self.canvas.height // len(letters)
        yremainder = self.canvas.height % len(letters)
        y = 0
        for i, row_letter in enumerate(letters):
            x = 0
            recheight = ysize
            if i < yremainder:
                recheight += 1
            if row is None or row == row_letter:
                for j, col_letter in enumerate(letters):
                    recwidth = xsize
                    if j < xremainder:
                        recwidth += 1
                    self.canvas.add_rectangle(x, y, recwidth, recheight, f'{row_letter}{col_letter}')
                    x += recwidth
            y += recheight
        self.canvas.render()