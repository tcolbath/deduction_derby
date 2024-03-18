from graphics import Window
from game import Game

def main():
    print("Work in progress....")
    # Window Parameters (16:9)
    width = 1280
    height = 720
    win = Window(width, height)

    # Game Parameters
    number_of_horses = 6 # 1 - 6. Default = 6
    spaces = 20 # Tested with 20
    game = Game(number_of_horses, spaces, win)
    
    # Name Your Horses! #color : horse, in order of their rendering. 
    horses = {
        "blue" : "Stormy Symphony",
        "green" : "Whispering Meadow",
        "orange" : "Golden Gallop",
        "purple" : "Mystic Dreamer",
        "red" : "Firestorm",
        "yellow" : "Thunderhoof",
    }
    game.new_game(horses)
    win.wait_for_close()


main()
