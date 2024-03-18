from graphics import Window
from game import Game

def main():
    print("Work in progress....")
    win = Window(1280, 720, "light gray")
    game = Game(6, 20, win)

    win.wait_for_close()


main()
