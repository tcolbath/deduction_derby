from graphics import Window
from game import Game

def main():
    print("Work in progress....")
    win = Window(1280, 720)
    game = Game(2, 20, win)
    game.new_game()

    win.wait_for_close()


main()
