from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, window_color="white"):
        self.__root = Tk()
        self.__root.title("Deduction Derby")
        self.canvas = Canvas(self.__root, bg=window_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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