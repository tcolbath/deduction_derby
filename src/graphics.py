from tkinter import Tk, BOTH, Canvas
from PIL import ImageTk, Image
from tkinter.constants import *

class Window:
    def __init__(self, width, height, window_color="white"):
        self.width = width
        self.height = height
        self.window_color = window_color
        self.__root = Tk()
        self.__root.title("Deduction Derby")
        self.canvas = Canvas(self.__root, bg=window_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.images = []


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window Closed.")


    def close(self):
        self.__running = False


    def draw_line(self, line, fill_color="black", width=2):
        line.draw(self.canvas, fill_color, width)


    def draw_image(self, point, file_name):
        x = point.x
        y = point.y
        image = ImageTk.PhotoImage(Image.open(file_name))
        self.images.append(image)
        return self.canvas.create_image(x, y, anchor=SW, image=image)
        
        

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2


    def draw(self, canvas, fill_color="black", lwidth=2):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=lwidth)
        canvas.pack(fill=BOTH, expand=1)
